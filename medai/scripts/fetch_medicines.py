import re
from pymongo import MongoClient
from decouple import config
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = config("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client["Medai"]
medicines = db["medicines"]

known_symptoms = {
    "fever", "pain", "headache", "nausea", "cough", "vomiting", "diarrhea",
    "dizziness", "sore throat", "inflammation", "muscle pain", "body pain",
    "fatigue", "cold", "congestion", "chills", "rash", "itching", "anxiety",
    "depression", "insomnia", "weakness", "thyroid", "dry cough", "wet cough",
    "irritability", "sweating", "blisters", "skin rash", "joint pain",
    "swelling", "convulsions", "seizures", "loss of consciousness", "loss of awareness",
    "epilepsy", "autoimmune flare", "organ swelling", "stomach acidity", "acid reflux",
    "chest discomfort", "indigestion", "ear infection", "earache", "ear discharge",
    "hearing difficulty", "pus discharge", "itchy rash", "burning sensation",
    "stomach irritation", "bloating", "fullness after eating", "high blood sugar",
    "frequent urination", "blurred vision", "tingling", "wound healing delay",
    "joint swelling", "gut inflammation", "skin plaques", "memory loss", "confusion",
    "loss of memory", "difficulty concentrating", "behavioral issues", "communication delay",
    "social withdrawal", "learning disability", "low immunity", "persistent infections",
    "immune flare", "neurological symptoms", "vision problems", "eye redness",
    "swollen glands", "internal bleeding", "low platelet count", "severe headache",
    "muscle spasms", "neck stiffness", "muscle cramps", "back pain", "tooth pain",
    "bleeding gums", "high cholesterol", "high blood pressure", "stroke", "tremors",
    "paralysis", "numbness", "slurred speech", "unconsciousness", "sensitivity to light",
    "facial twitching", "sun sensitivity", "ulcers", "mood instability",
    "involuntary movements", "cataract"
}


def fetch_and_insert(data):
    inserted_docs = []

    for item in data:
        name = item.get("name", "Unknown")
        advantages = item.get("advantages", [])
        disadvantages = item.get("disadvantages", [])
        first_aid = item.get("first_aid", "")
        foods_to_eat = item.get("foods_to_eat", [])
        foods_to_avoid = item.get("foods_to_avoid", [])
        natural_remedies = item.get("natural_remedies", [])

        combined_text = " ".join(advantages + disadvantages + [first_aid] + foods_to_eat + foods_to_avoid + natural_remedies).lower()

        symptoms = [symptom for symptom in known_symptoms if symptom in combined_text]

        doc = {
            "name": name,
            "advantages": advantages,
            "disadvantages": disadvantages,
            "first_aid": first_aid,
            "foods_to_eat": foods_to_eat,
            "foods_to_avoid": foods_to_avoid,
            "natural_remedies": natural_remedies,
            "symptoms": symptoms
        }

        if not medicines.find_one({"name": name}):
            medicines.insert_one(doc)
            inserted_docs.append(doc)

    return inserted_docs