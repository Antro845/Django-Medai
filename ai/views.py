import heapq
import os
import re
from bson import ObjectId
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from dotenv import load_dotenv
from pymongo import MongoClient
import requests
from datetime import datetime
from medai.scripts.fetch_medicines import fetch_and_insert

# Load env variables
load_dotenv()

# MongoDB setup
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client["Medai"]
users_collection = db["Users"]
medicines = db["medicines"]
history_collection = db["prompt_history"]
GOOGLE_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")


@csrf_exempt
def signin_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if users_collection.find_one({"username": username}):
            messages.error(request, "Username already exists.")
            return render(request, "signin.html")

        users_collection.insert_one({"username": username, "password": password})
        request.session["username"] = username
        messages.success(request, "Sign up successful! Welcome, " + username)
        return redirect("index")

    return render(request, "signin.html")


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = users_collection.find_one({"username": username, "password": password})

        if user:
            request.session["username"] = username
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def logout_view(request):
    request.session.flush()
    return redirect("index")


@csrf_exempt
def prompt_query(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt", "").lower()
        username = request.session.get("username", None)

        matched_medicines = []
        hospitals = []
        all_medicines = list(medicines.find({}, {"_id": 0}))

        location_keywords = [
            "nearby",
            "hospital in",
            "clinic in",
            "hospital near",
            "emergency in",
            "hospitals",
            "hospital",
            "hospitals near",
            "clinic near",
            "clinics near",
            "clinic in",
            "clinics in",
            "hospital nearby",
            "hospitals nearby",
        ]

        if any(keyword in prompt for keyword in location_keywords):
            location_match = re.search(r"in ([\w\s]+)", prompt)
            location = (
                location_match.group(1).strip() if location_match else "Tirunelveli"
            )

            geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={GOOGLE_API_KEY}"
            geocode_data = requests.get(geocode_url).json()

            if geocode_data.get("status") == "OK":
                lat = geocode_data["results"][0]["geometry"]["location"]["lat"]
                lng = geocode_data["results"][0]["geometry"]["location"]["lng"]

                specialty_match = re.search(
                    r"(heart|eye|cancer|cardiac|orthopedic|neuro|mental|skin|dental)",
                    prompt,
                )
                specialty = specialty_match.group(1) if specialty_match else ""

                places_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=5000&type=hospital"
                if specialty:
                    places_url += f"&keyword={specialty}"
                places_url += f"&key={GOOGLE_API_KEY}"

                places_data = requests.get(places_url).json()

                if places_data.get("status") == "OK":
                    for place in places_data.get("results", []):
                        hospitals.append(
                            {
                                "type": "hospital",
                                "name": place.get("name", "Unknown"),
                                "address": place.get("vicinity", "N/A"),
                                "rating": place.get("rating", "N/A"),
                                "map_link": f"https://www.google.com/maps/search/?api=1&query={place['geometry']['location']['lat']},{place['geometry']['location']['lng']}",
                            }
                        )

                else:
                    hospitals.append(
                        {
                            "type": "hospital",
                            "name": "No hospitals found",
                            "address": "Invalid location or no results.",
                            "rating": "N/A",
                            "map_link": "#",
                        }
                    )

                # Save to history if user is logged in
                if username and username != "Guest":
                    history_collection.insert_one(
                        {
                            "user": request.user.username,
                            "prompt": prompt,
                            "type": "hospital",
                            "result": hospitals,  # Store result list here
                            "timestamp": datetime.now(),
                            "map_link": f"https://www.google.com/maps/search/?api=1&query={place['geometry']['location']['lat']},{place['geometry']['location']['lng']}",
                        }
                    )

                return render(
                    request,
                    "index.html",
                    {
                        "username": username or "Guest",
                        "prompt_response": hospitals,
                        "medicines": all_medicines,
                    },
                )

        # Not hospital → match medicine
        prompt_words = set(re.findall(r"\w+", prompt.lower()))
        all_docs = db["medicines"].find()

        for doc in all_docs:
            doc_symptoms = doc.get("symptoms", [])
            symptom_words = set(s.lower() for s in doc_symptoms if isinstance(s, str))
            match_count = sum(
                any(word in symptom for symptom in symptom_words)
                for word in prompt_words
            )

            if match_count > 0:
                heapq.heappush(
                    matched_medicines, (-match_count, str(doc.get("_id")), doc)
                )

        top_meds = [
            summarize_medicine_data(doc)
            for _, _, doc in heapq.nsmallest(3, matched_medicines)
        ]

        if username and username != "Guest":
            history_collection.insert_one(
                {
                    "user_id": username,
                    "prompt": prompt,
                    "result": top_meds[0] if top_meds else {},
                    "timestamp": datetime.now(),
                }
            )

        return render(
            request,
            "index.html",
            {
                "username": username or "Guest",
                "prompt_response": top_meds,
                "medicines": all_medicines,
            },
        )

    return redirect("index")


def summarize_medicine_data(doc):
    raw_desc = doc.get("description", "")
    name = doc.get("name", "Unknown")

    if isinstance(raw_desc, list):
        raw_desc = raw_desc[0] if raw_desc else ""

    summary_match = re.search(r"(used (to|for) [^.]+?\.)", str(raw_desc), re.IGNORECASE)
    summary = (
        summary_match.group(1).strip()
        if summary_match
        else str(raw_desc).split(".")[0].strip() + "."
    )

    symptoms = doc.get("symptoms", [])
    clean_symptoms = list(set([s.lower() for s in symptoms if isinstance(s, str)]))[:5]

    return {
        "type": "medicine",
        "name": name,
        "description": summary,
        "symptoms": clean_symptoms,
        "advantages": doc.get("advantages", []),
        "disadvantages": doc.get("disadvantages", []),
        "first_aid": doc.get("first_aid", "N/A"),
        "foods_to_eat": doc.get("foods_to_eat", []),
        "foods_to_avoid": doc.get("foods_to_avoid", []),
        "natural_remedies": doc.get("natural_remedies", []),
    }


def user_history(request):
    username = request.session.get("username")
    history = list(history_collection.find({"user_id": username}).sort("timestamp", -1))
    return render(request, "index.html", {"history": history})


def index(request):
    username = request.session.get("username", "Guest")
    user_id = username  # Assuming user_id is stored as username

    selected_prompt = None
    response_for_selected_prompt = None

    # Load all medicines
    all_medicines = list(medicines.find({}, {"_id": 0}))

    # Load history for current user
    user_history = list(
        history_collection.find({"user_id": user_id}).sort("timestamp", -1)
    )

    # Convert ObjectId to string for frontend usage
    for entry in user_history:
        entry["id"] = str(entry["_id"])

    # If a prompt_id is selected from history
    prompt_id = request.GET.get("prompt_id")
    if prompt_id:
        try:
            selected_prompt = history_collection.find_one(
                {"_id": ObjectId(prompt_id), "user_id": user_id}
            )
            if selected_prompt:
                result_data = selected_prompt.get("result", {})

                if result_data.get("type") == "medicine":
                    response_for_selected_prompt = {
                        "type": "medicine",
                        "name": result_data.get("name", ""),
                        "description": result_data.get("description", ""),
                        "symptoms": result_data.get("symptoms", []),
                        "advantages": result_data.get("advantages", []),
                        "disadvantages": result_data.get("disadvantages", []),
                        "first_aid": result_data.get("first_aid", "N/A"),
                        "foods_to_eat": result_data.get("foods_to_eat", []),
                        "foods_to_avoid": result_data.get("foods_to_avoid", []),
                        "natural_remedies": result_data.get("natural_remedies", []),
                    }

                elif (
                    isinstance(result_data, list)
                    and result_data
                    and result_data[0].get("type") == "hospital"
                ):
                    response_for_selected_prompt = {
                        "type": "hospital",
                        "hospitals": result_data,  # Pass the full list to the template
                    }

                else:
                    response_for_selected_prompt = (
                        result_data  # fallback if type not recognized
                    )

        except Exception as e:
            print("Invalid prompt_id:", e)

    return render(
        request,
        "index.html",
        {
            "username": username,
            "prompt_response": response_for_selected_prompt,
            "medicines": all_medicines,
            "user_history": user_history,
            "selected_prompt_id": prompt_id,
        },
    )


@csrf_exempt
def delete_history(request):
    if request.method == "POST":
        prompt_id = request.POST.get("prompt_id")
        username = request.session.get("username")

        if prompt_id and username:
            try:
                history_collection.delete_one(
                    {"_id": ObjectId(prompt_id), "user_id": username}
                )
            except Exception as e:
                print("Delete failed:", e)

        return redirect("index")

    return HttpResponseBadRequest("Invalid request")
