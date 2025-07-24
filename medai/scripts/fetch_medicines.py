import re
import requests
from pymongo import MongoClient
from decouple import config
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = config("MONGODB_URI")
OPENFDA_KEY = config("OPENFDA_API_KEY", default="")

client = MongoClient(MONGODB_URI)
db = client["Medai"]
medicines = db["medicines"]
STOP_WORDS = [
    "and", "or", "the", "a", "of", "to", "in", "for", "on", "with", "is",
    "by", "an", "as", "at", "that", "this", "from", "are", "was", "be"
]

def fetch_and_insert(indication, limit=10):
    import requests
    url = f"https://api.fda.gov/drug/label.json?search=indications_and_usage:{indication}&limit={limit}"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json().get("results", [])
    inserted_docs = []

    for item in data:
        openfda = item.get("openfda", {})
        
        # Try multiple fields for medicine name
        name = (
            openfda.get("brand_name", [None])[0] or
            openfda.get("generic_name", [None])[0] or
            openfda.get("substance_name", [None])[0] or
            "Unknown"
        )

        # Clean symptoms (optional: from indication or adverse effects)
        indications_raw = item.get("indications_and_usage", "")

# Ensure it's a string before passing to re.findall
        # Inside fetch_and_insert or wherever you're extracting symptoms
        known_symptoms = {
            "fever", "pain", "headache", "nausea", "cough", "vomiting", "diarrhea",
            "dizziness", "sore throat", "inflammation", "muscle pain", "body pain",
            "fatigue", "cold", "congestion", "chills", "rash", "itching", "anxiety",
            "depression", "insomnia", "weakness"
        }

# After extracting words from text
        possible_words = re.findall(r"\b[a-z]{4,}\b", indications_raw.lower())
        symptoms = list(set([word for word in possible_words if word in known_symptoms]))



        doc = {
            "name": name,
            "description": item.get("indications_and_usage", ""),
            "symptoms": symptoms
        }

        # Insert into DB
        medicines.insert_one(doc)
        inserted_docs.append(doc)

    return inserted_docs
