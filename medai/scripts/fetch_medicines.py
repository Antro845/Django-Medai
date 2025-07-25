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
    "depression", "insomnia", "weakness", "thyroid", "hyperthyroidism"
}

def fetch_and_insert(data):
    inserted_docs = []

    for item in data:
        name = item.get("name", "Unknown")
        indications = item.get("indications_and_usage", "")
        description = item.get("description", "")

        full_text = f"{indications} {description}".lower()

        possible_words = re.findall(r"\b[a-z]{4,}\b", full_text)
        symptoms = list(set([word for word in possible_words if word in known_symptoms]))

        doc = {
            "name": name,
            "description": indications,
            "symptoms": symptoms
        }

        if not medicines.find_one({"name": name, "symptoms": symptoms}):
            medicines.insert_one(doc)
            inserted_docs.append(doc)

    return inserted_docs