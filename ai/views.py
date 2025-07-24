import heapq
import os
import re
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from dotenv import load_dotenv
from pymongo import MongoClient
import requests
from medai.scripts.fetch_medicines import fetch_and_insert
load_dotenv()
# Get URI from .env
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client["Medai"]
users_collection = db["Users"]
GOOGLE_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
@csrf_exempt
def signin_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if users_collection.find_one({"username": username}):
            messages.error(request, "Username already exists.")
            return render(request, 'signin.html')

        users_collection.insert_one({
            "username": username,
            "password": password
        })

       
        messages.success(request, "Sign up successful! Welcome, " + username)

        
        request.session['username'] = username

        return redirect('index')

    return render(request, 'signin.html')


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = users_collection.find_one({
            "username": username,
            "password": password
        })

        if user:
            request.session['username'] = username
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()  # Clears all session data
    return redirect('index')


def index(request):
    username = request.session.get('username', 'Guest')  # Fallback if not logged in
    return render(request, 'index.html', {'username': username})

medicines = db["medicines"]


@csrf_exempt
def prompt_query(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '').lower()
        matched_medicines = []
        hospitals = []

        # Location-related keywords
        location_keywords = [
            'nearby', 'hospital in', 'clinic in', 'hospital near', 'emergency in',
            'hospitals', 'hospital', 'hospitals near', 'clinic near', 'clinics near',
            'clinic in', 'clinics in', 'hospital nearby', 'hospitals nearby'
        ]

        # If user is asking for hospitals
        if any(word in prompt for word in location_keywords):
            # Try to extract location from prompt
            location_match = re.search(r'in ([\w\s]+)', prompt)
            if location_match:
                location = location_match.group(1).strip()
            else:
                location = "Tirunelveli"  # default fallback

            # Geocode the location to lat/lng
            geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={GOOGLE_API_KEY}"
            geocode_data = requests.get(geocode_url).json()

            if geocode_data.get("status") == "OK":
                lat = geocode_data["results"][0]["geometry"]["location"]["lat"]
                lng = geocode_data["results"][0]["geometry"]["location"]["lng"]

                # Extract specialty if present
                specialty_match = re.search(r'(heart|eye|cancer|cardiac|orthopedic|neuro|mental|skin|dental)', prompt)
                specialty = specialty_match.group(1) if specialty_match else ""

                # Build Places API URL
                places_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius=5000&type=hospital"
                if specialty:
                    places_url += f"&keyword={specialty}"
                places_url += f"&key={GOOGLE_API_KEY}"

                # Fetch nearby hospital data
                places_data = requests.get(places_url).json()

                if places_data.get("status") == "OK":
                    for place in places_data.get("results", []):
                        lat = place["geometry"]["location"]["lat"]
                        lng = place["geometry"]["location"]["lng"]
                        hospitals.append({
                            "type": "hospital",
                            "name": place.get("name", "Unknown"),
                            "address": place.get("vicinity", "N/A"),
                            "rating": place.get("rating", "N/A"),
                            "map_link": f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
                        })
                else:
                    hospitals.append({
                        "type": "hospital",
                        "name": "No hospitals found",
                        "address": "Invalid location or no results.",
                        "rating": "N/A",
                        "map_link": "#"
                    })

                return render(request, 'index.html', {
                    'prompt_response': hospitals,
                    'username': request.session.get('username', 'Guest')
                })

        # Else handle symptom → medicine match
        prompt_words = set(re.findall(r'\w+', prompt.lower()))
        all_docs = db["medicines"].find()

        for doc in all_docs:
            doc_symptoms = doc.get("symptoms", [])
            symptom_words = set(s.lower() for s in doc_symptoms if isinstance(s, str))
            match_count = len(prompt_words.intersection(symptom_words))
            if match_count > 0:
                heapq.heappush(matched_medicines, (-match_count, str(doc.get("_id")), doc))

        matched_medicines.sort(key=lambda x: x[0], reverse=True)
        top_meds = [summarize_medicine_data(doc) for _, _, doc in matched_medicines[:3]]

        return render(request, 'index.html', {
            'prompt_response': top_meds,
            'username': request.session.get('username', 'Guest')
        })

    # Default fallback GET
    return render(request, 'index.html', {
        'prompt_response': [],
        'username': request.session.get('username', 'Guest')
    })

    


    
def summarize_medicine_data(doc):
    raw_desc = doc.get("description", "")
    name = doc.get("name", "Unknown")

    if isinstance(raw_desc, list):
        raw_desc = raw_desc[0] if raw_desc else ""

    raw_desc = str(raw_desc)

    summary_match = re.search(r"(used (to|for) [^.]+?\.)", raw_desc, re.IGNORECASE)
    if summary_match:
        summary = summary_match.group(1).strip()
    elif raw_desc:
        summary = raw_desc.split('.')[0].strip() + '.'
    else:
        summary = "No brief description available."

    symptoms = doc.get("symptoms", [])
    clean_symptoms = list(set([s.lower() for s in symptoms if isinstance(s, str)]))[:5]

    return {
        "type": "medicine",
        "name": name,
        "description": summary,
        "symptoms": clean_symptoms
    }



def nearby_hospitals(request):
    if request.method == "GET":
        return render(request, "index.html")

    if request.method == "POST":
        location = request.POST.get("location")
        if not location:
            return JsonResponse({"error": "Location not provided"}, status=400)

        
        geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={GOOGLE_API_KEY}"
        geocode_data = requests.get(geocode_url).json()

        if geocode_data["status"] != "OK":
            return JsonResponse({"error": "Invalid location"}, status=400)

        latlng = geocode_data["results"][0]["geometry"]["location"]
        latitude, longitude = latlng["lat"], latlng["lng"]

        
        places_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            "location": f"{latitude},{longitude}",
            "radius": 5000,  # in meters
            "type": "hospital",
            "key": GOOGLE_API_KEY,
        }

        response = requests.get(places_url, params=params)
        data = response.json()

        hospitals = []
        for result in data.get("results", []):
            hospitals.append({
                "name": result.get("name"),
                "address": result.get("vicinity"),
                "rating": result.get("rating"),
                "location": result["geometry"]["location"]
            })

        return JsonResponse({"hospitals": hospitals})