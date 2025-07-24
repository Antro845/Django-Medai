import json
from django.core.management.base import BaseCommand
from decouple import config
from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Load .env manually from project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, '.env'))

mongo_uri = config("MONGODB_URI")

class Command(BaseCommand):
    help = 'Upload sample medicines to MongoDB'

    def handle(self, *args, **kwargs):
        try:
            client = MongoClient(mongo_uri)
            db = client["Medai"]
            collection = db["medicines"]
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"MongoDB connection failed: {e}"))
            return

        # Sample data
        medicines = [
            {
                "name": "Paracetamol",
                "description": "Used for fever and mild pain.",
                "symptoms": ["fever", "headache", "body pain"]
            },
            {
                "name": "Ibuprofen",
                "description": "Used to reduce fever and treat pain or inflammation.",
                "symptoms": ["fever", "inflammation", "muscle pain"]
            },
            {
                "name": "Amoxicillin",
                "description": "Antibiotic used for bacterial infections.",
                "symptoms": ["infection", "sore throat", "tooth infection"]
            },
            {
                "name": "Gabapentin",
                "description": "Used to treat pain from damaged nerves (postherpetic neuralgia) following shingles in adults.",
                "symptoms": ["nerve pain", "zoster", "postherpetic pain"]
            },
            {
                "name": "Homeopathic Cold Relief",
                "description": "Homeopathic medicine made from a combination of ingredients traditionally used to relieve symptoms associated with cough and cold: dry cough, cough with expectoration, chest congestion, fever, aches, and pains.",
                "symptoms": ["dry cough", "wet cough", "chest congestion", "fever", "aches"]
            },
              
            {
                "name": "Cetirizine",
                "description": "Used to relieve allergy symptoms such as runny nose, sneezing, and itchy or watery eyes.",
                "symptoms": ["allergy", "runny nose", "sneezing", "itchy eyes"]
            },
            {
                "name": "Metformin",
                "description": "Used to control high blood sugar in people with type 2 diabetes.",
                "symptoms": ["type 2 diabetes", "high blood sugar", "insulin resistance"]
            },
            {
                "name": "Loperamide",
                "description": "Used to treat sudden diarrhea. It works by slowing down the movement of the gut.",
                "symptoms": ["diarrhea", "stomach cramps", "loose stool"]
            },
            {
                "name": "Loratadine",
                "description": "An antihistamine that relieves allergy symptoms without drowsiness.",
                "symptoms": ["sneezing", "runny nose", "itchy throat", "hives"]
            },
            {
                "name": "Ranitidine",
                "description": "Used to treat and prevent ulcers in the stomach and intestines and gastroesophageal reflux disease (GERD).",
                "symptoms": ["acid reflux", "GERD", "heartburn", "stomach ulcer"]
            },
            {
                "name": "Omeprazole",
                "description": "Used to treat certain stomach and esophagus problems (such as acid reflux, ulcers).",
                "symptoms": ["acid reflux", "ulcer", "heartburn", "indigestion"]
            },
            {
                "name": "Azithromycin",
                "description": "An antibiotic used to treat various types of infections caused by bacteria.",
                "symptoms": ["bacterial infection", "chest infection", "throat infection", "skin infection"]
            },
            {
                "name": "Salbutamol",
                "description": "Used to relieve symptoms of asthma and chronic obstructive pulmonary disease (COPD).",
                "symptoms": ["asthma", "wheezing", "shortness of breath", "COPD"]
            },
            {
                "name": "Hydroxyzine",
                "description": "Used to treat anxiety, nausea, allergies, skin rash, hives, and itching.",
                "symptoms": ["anxiety", "itching", "hives", "nausea", "rash"]
            }
                   ]

        inserted_count = 0
        for med in medicines:
            if not collection.find_one({"name": med["name"], "description": med["description"]}):
                collection.insert_one(med)
                inserted_count += 1
            else:
                self.stdout.write(f"Skipped (duplicate): {med['name']}")

        self.stdout.write(self.style.SUCCESS(f"{inserted_count} new medicines uploaded successfully!"))
# Build JSON structure
   