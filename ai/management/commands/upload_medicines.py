from django.core.management.base import BaseCommand
from decouple import config
from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Load .env manually from project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))

mongo_uri = config("MONGODB_URI")


class Command(BaseCommand):
    help = "Upload sample medicines to MongoDB"

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
        "name": "Dexamethasone 1",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 2",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 3",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 4",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 5",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 6",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 7",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 8",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 9",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 10",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 11",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 12",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 13",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 14",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 15",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 16",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 17",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 18",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 19",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 20",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 21",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 22",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 23",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 24",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 25",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 26",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 27",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 28",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 29",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 30",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 31",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 32",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 33",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 34",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 35",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 36",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 37",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 38",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 39",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 40",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 41",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 42",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 43",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 44",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 45",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 46",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 47",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 48",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 49",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 50",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 51",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 52",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 53",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 54",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 55",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 56",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 57",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 58",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 59",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 60",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 61",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 62",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 63",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 64",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 65",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 66",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 67",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 68",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 69",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 70",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 71",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 72",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 73",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 74",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 75",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 76",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 77",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 78",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 79",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 80",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 81",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 82",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 83",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 84",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 85",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 86",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 87",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 88",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 89",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 90",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 91",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 92",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 93",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 94",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 95",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 96",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    },
    {
        "name": "Dexamethasone 97",
        "advantages": [
            "Reduces inflammation",
            "Treats allergic reactions",
            "Manages autoimmune diseases"
        ],
        "disadvantages": [
            "May raise blood sugar",
            "Possible mood changes",
            "Increased infection risk"
        ],
        "first_aid": "Take as prescribed, avoid abrupt withdrawal",
        "foods_to_eat": [
            "Whole grains",
            "Lean meats",
            "Leafy greens"
        ],
        "foods_to_avoid": [
            "High sugar foods",
            "Alcohol",
            "Fried snacks"
        ],
        "natural_remedies": [
            "Turmeric",
            "Ginger",
            "Licorice root"
        ],
        "description": "Dexamethasone is a corticosteroid used to treat inflammation, allergic conditions, and certain cancers. It suppresses the immune response.",
        "symptoms": [
            "inflammation",
            "allergic reactions",
            "autoimmune disorders"
        ]
    },
    {
        "name": "Mupirocin 98",
        "advantages": [
            "Topical use with minimal systemic absorption",
            "Effective against skin infections",
            "Broad-spectrum antibiotic"
        ],
        "disadvantages": [
            "May cause skin irritation",
            "Resistance can develop with overuse",
            "Burning sensation possible"
        ],
        "first_aid": "Clean affected area before applying",
        "foods_to_eat": [
            "Vitamin C-rich foods",
            "High-protein diet"
        ],
        "foods_to_avoid": [
            "Processed sugar",
            "Greasy food"
        ],
        "natural_remedies": [
            "Tea tree oil",
            "Aloe vera",
            "Honey"
        ],
        "description": "Mupirocin is an antibiotic cream used to treat skin infections like impetigo. It works by stopping the growth of certain bacteria.",
        "symptoms": [
            "skin infections",
            "impetigo",
            "minor wounds"
        ]
    },
    {
        "name": "Escitalopram 99",
        "advantages": [
            "Improves mood and energy",
            "Reduces anxiety",
            "Fewer side effects than other SSRIs"
        ],
        "disadvantages": [
            "Drowsiness",
            "Sexual dysfunction",
            "Possible weight gain"
        ],
        "first_aid": "Take at same time daily, do not stop abruptly",
        "foods_to_eat": [
            "Omega-3 fatty acids",
            "Whole grains",
            "Berries"
        ],
        "foods_to_avoid": [
            "Alcohol",
            "Caffeine",
            "Refined sugar"
        ],
        "natural_remedies": [
            "Meditation",
            "Chamomile tea",
            "Exercise"
        ],
        "description": "Escitalopram is an antidepressant used to treat depression and generalized anxiety disorder. It restores the balance of serotonin in the brain.",
        "symptoms": [
            "depression",
            "anxiety",
            "panic disorder"
        ]
    },
    {
        "name": "Rosuvastatin 100",
        "advantages": [
            "Well-tolerated",
            "Effective for lowering cholesterol",
            "Reduces risk of heart attack"
        ],
        "disadvantages": [
            "May cause headache",
            "Can affect liver function",
            "Muscle pain possible"
        ],
        "first_aid": "Take with water, monitor for muscle weakness",
        "foods_to_eat": [
            "Oats",
            "Boiled vegetables",
            "Brown rice"
        ],
        "foods_to_avoid": [
            "Grapefruit",
            "Red meat",
            "Fried foods"
        ],
        "natural_remedies": [
            "Garlic",
            "Omega-3 rich foods",
            "Green tea"
        ],
        "description": "Rosuvastatin is used to lower bad cholesterol and fats and raise good cholesterol in the blood. It helps prevent heart disease and stroke.",
        "symptoms": [
            "high cholesterol",
            "heart disease",
            "stroke risk"
        ]
    }
                ]

        for medicine in medicines:
            collection.delete_many({"name": medicine["name"]})

        # Insert medicines
        try:
            collection.insert_many(medicines)
            self.stdout.write(self.style.SUCCESS("Medicines uploaded successfully."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error inserting medicines: {e}"))
