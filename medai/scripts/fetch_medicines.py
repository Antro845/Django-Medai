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
    "depression", "insomnia", "weakness", "thyroid", "hyperthyroidism", "dry cough", "wet cough",
    "irritability", "sweating", "insomnia", "blisters", "skin rash", "joint pain",
    "swelling", "convulsions", "seizures", "loss of consciousness", "loss of awareness",
    "epilepsy", "autoimmune flare", "organ swelling", "stomach acidity", "acid reflux",
    "chest discomfort", "indigestion", "ear infection", "earache", "ear discharge",
    "hearing difficulty", "pus discharge", "itchy rash", "fatigue", "burning sensation",
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
    "facial twitching", "gut inflammation", "sun sensitivity", "ulcers", "mood instability",
    "involuntary movements", "cattaract"
}


def fetch_and_insert(data):
    inserted_docs = []

    for item in data:
        name = item.get("name", "Unknown")
        indications = item.get("indications_and_usage", "")
        description = item.get("description", "")

        full_text = f"{indications} {description}".lower()

        # ✅ Match full known symptoms
        symptoms = [symptom for symptom in known_symptoms if symptom in full_text]

        doc = {
            "name": name,
            "description": indications,
            "symptoms": symptoms
        }

        if not medicines.find_one({"name": name, "symptoms": symptoms}):
            medicines.insert_one(doc)
            inserted_docs.append(doc)

    return inserted_docs
