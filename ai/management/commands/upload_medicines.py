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
                "symptoms": ["fever", "cold", "headache", "body pain"]
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
                "symptoms": ["allergy", "cold", "runny nose", "sneezing", "itchy eyes"]
            },
            {
                "name": "Dextromethorphan",
                "description": "A cough suppressant used to treat dry cough by affecting the signals in the brain that trigger cough reflex.",
                "symptoms": ["dry cough", "irritating cough", "throat irritation"]
            },
            {
                "name": "Guaifenesin",
                "description": "An expectorant used to thin mucus in the airways, making it easier to cough up phlegm.",
                "symptoms": ["wet cough", "chest congestion", "phlegm"]
            },
            {
                "name": "Hyoscine Butylbromide",
                "description": "Used to relieve abdominal cramps, stomach pain, and menstrual cramps by relaxing the muscles of the gastrointestinal tract.",
                "symptoms": ["stomach cramps", "abdominal pain", "menstrual cramps"]
            },
            {
                "name": "Ibuprofen",
                "description": "A nonsteroidal anti-inflammatory drug (NSAID) used to reduce inflammation and relieve pain, including menstrual and muscle cramps.",
                "symptoms": ["muscle cramps", "menstrual pain", "fever", "body ache"]
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
            },
            {
                "name": "Levothyroxine",
                "description": "Synthetic form of the thyroid hormone T4; used to treat hypothyroidism by normalizing hormone levels.",
                "symptoms": ["fatigue", "hypothyroidism", "weight gain", "cold intolerance", "constipation", "dry skin"]
            },
            {
                "name": "Liothyronine",
                "description": "Synthetic form of the T3 hormone; sometimes used in combination with Levothyroxine for better symptom control in hypothyroidism.",
                "symptoms": ["depression", "hypothyroidism", "low energy", "brain fog", "slow heart rate"]
            },
            {
                "name": "Armour Thyroid",
                "description": "Natural desiccated thyroid (NDT) from pig thyroid glands; contains both T3 and T4 hormones.",
                "symptoms": ["sluggishness", "thyroid", "memory issues", "hoarseness", "weight gain"]
            },
            {
                "name": "Methimazole",
                "description": "Antithyroid medication used to treat hyperthyroidism by inhibiting the production of thyroid hormones.",
                "symptoms": ["tremors", "hyperthyroidism", "heat intolerance", "rapid heartbeat", "weight loss"]
            },
            {
                "name": "Propylthiouracil (PTU)",
                "description": "Used to treat hyperthyroidism; blocks thyroid hormone production and conversion of T4 to T3.",
                "symptoms": ["irritability", "hyperthyroidism", "insomnia", "sweating", "diarrhea"]
            },
            {
                "name": "Beta-blockers (e.g., Propranolol)",
                "description": "Not a direct thyroid treatment, but helps manage symptoms of hyperthyroidism like palpitations and anxiety.",
                "symptoms": ["palpitations", "thyroid", "hyperthyroidism", "shaking", "anxiety", "high blood pressure"]
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
   