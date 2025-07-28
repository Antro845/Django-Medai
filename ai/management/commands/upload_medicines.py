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
                "symptoms": ["fever", "cold", "headache", "toothache", "body pain"]
            },
            
            {
                "name": "Amoxicillin",
                "description": "Antibiotic used for bacterial infections.",
                "symptoms": ["infection", "tooth ache", "sore throat", "tooth infection"]
            },
            {
                "name": "Gabapentin",
                "description": "Used to treat pain from damaged nerves (postherpetic neuralgia) following shingles in adults.",
                "symptoms": ["nerve pain", "zoster", "postherpetic pain"]
            },
            {
                "name": "Homeopathic Cold Relief",
                "description": "Homeopathic medicine made from a combination of ingredients traditionally used to relieve symptoms associated with cough and cold: dry cough, cough with expectoration, chest congestion, fever, aches, and pains.",
                "symptoms": ["dry cough", "wet cough", "cough", "chest congestion", "fever", "aches"]
            },
              
            {
                "name": "Cetirizine",
                "description": "Used to relieve allergy symptoms such as runny nose, sneezing, and itchy or watery eyes.",
                "symptoms": ["allergy", "cold", "runny nose", "sneezing", "itchy eyes"]
            },
            {
                "name": "Dextromethorphan",
                "description": "A cough suppressant used to treat dry cough by affecting the signals in the brain that trigger cough reflex.",
                "symptoms": ["dry cough", "cough", "irritating cough", "throat irritation"]
            },
            {
                "name": "Guaifenesin",
                "description": "An expectorant used to thin mucus in the airways, making it easier to cough up phlegm.",
                "symptoms": ["wet cough", "cough", "chest congestion", "phlegm"]
            },
            {
                "name": "Hyoscine Butylbromide",
                "description": "Used to relieve abdominal cramps, stomach pain, and menstrual cramps by relaxing the muscles of the gastrointestinal tract.",
                "symptoms": ["stomach cramps", "cramps", "abdominal pain", "menstrual cramps"]
            },
            {
                "name": "Ibuprofen",
                "description": "A nonsteroidal anti-inflammatory drug (NSAID) used to reduce inflammation and relieve pain, including menstrual and muscle cramps.",
                "symptoms": ["muscle cramps", "toothache", "cramps", "menstrual pain", "fever", "body ache"]
            },
            {
                "name": "Loperamide",
                "description": "Used to treat sudden diarrhea. It works by slowing down the movement of the gut.",
                "symptoms": ["diarrhea", "stomach cramps", "cramps", "loose stool"]
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
            },
            {
                "name": "Ferrous Sulfate",
                "description": "An iron supplement used to treat or prevent low blood levels of iron (e.g., for anemia or during pregnancy).",
                "symptoms": ["fatigue", "pale skin", "shortness of breath", "dizziness", "anemia"]
            },
            {
                "name": "Ondansetron",
                "description": "An antiemetic used to prevent nausea and vomiting caused by surgery, chemotherapy, or stomach upset.",
                "symptoms": ["nausea", "vomiting", "motion sickness", "gastroenteritis", "chemotherapy-induced nausea"]
            },
            {
                "name": "Diclofenac",
                "description": "A nonsteroidal anti-inflammatory drug (NSAID) used to relieve pain and reduce inflammation in conditions such as low back pain, arthritis, and muscle injuries.",
                "symptoms": ["low back pain", "inflammation", "muscle stiffness", "joint pain", "swelling"]
            },
            {
                "name": "Methotrexate",
                "description": "A disease-modifying antirheumatic drug (DMARD) used to treat rheumatoid arthritis by reducing joint inflammation and slowing disease progression.",
                "symptoms": ["joint pain", "joint stiffness", "swelling", "arthritis", "fatigue"]
            },
            {
                "name": "Metformin",
                "description": "An oral antidiabetic drug used to control high blood sugar in people with type 2 diabetes by improving insulin sensitivity and reducing glucose production in the liver.",
                "symptoms": ["high blood sugar", "frequent urination", "increased thirst", "type 2 diabetes", "fatigue"]
            },
            {
                "name": "Rabies Vaccine (Post-Exposure Prophylaxis)",
                "description": "A series of rabies vaccines given after suspected exposure to prevent the rabies virus from causing illness.",
                "symptoms": ["animal bite", "fever", "tingling at bite site", "hydrophobia", "rabies exposure"]
            },
            {
                "name": "Erythropoietin (EPO)",
                "description": "A synthetic hormone used to treat anemia caused by chronic kidney failure by stimulating red blood cell production.",
                "symptoms": ["fatigue", "anemia", "chronic kidney disease", "weakness", "shortness of breath"]
            },
            {
                "name": "Aspirin",
                "description": "An antiplatelet agent used to reduce the risk of blood clots, often given immediately after an ischemic stroke to prevent further strokes.",
                "symptoms": ["sudden weakness", "numbness", "slurred speech", "ischemic stroke", "dizziness"]
            },
            {
                "name": "Isoniazid (INH)",
                "description": "A first-line antitubercular antibiotic used to treat and prevent active and latent tuberculosis by inhibiting the synthesis of mycolic acids in the bacterial cell wall.",
                "symptoms": ["persistent cough", "fever", "night sweats", "weight loss", "tuberculosis"]
            },
            {
                "name": "Amlodipine",
                "description": "A calcium channel blocker used to lower high blood pressure by relaxing blood vessels, making it easier for the heart to pump blood.",
                "symptoms": ["high blood pressure", "headache", "chest pain", "dizziness", "shortness of breath"]
            },
            {
                "name": "Hydrocortisone",
                "description": "A topical corticosteroid used to treat inflammation and itching caused by various skin conditions such as eczema, dermatitis, and allergic reactions.",
                "symptoms": ["skin inflammation", "itching", "redness", "eczema", "rashes"]
            },
            {
                "name": "Clotrimazole",
                "description": "An antifungal cream used to treat fungal skin infections such as ringworm, athlete’s foot, and candidiasis.",
                "symptoms": ["itching", "red patches", "fungal infection", "skin peeling", "ringworm"]
            },
            {
                "name": "Calamine Lotion",
                "description": "A soothing topical lotion used to relieve itching and skin irritation caused by allergies, insect bites, or rashes.",
                "symptoms": ["itching", "skin irritation", "insect bites", "chickenpox rash", "rashes", "allergic reaction"]
            },
            {
                "name": "Isotretinoin",
                "description": "An oral retinoid used to treat severe acne by reducing sebum production and preventing clogged pores.",
                "symptoms": ["severe acne", "oily skin", "skin inflammation", "nodular acne", "cystic acne"]
            },
            {
                "name": "Acyclovir",
                "description": "An antiviral medication used to reduce the severity and duration of chickenpox by slowing the growth and spread of the varicella-zoster virus.",
                "symptoms": ["itchy rash", "blisters", "fever", "fatigue", "chickenpox"]
            },
            {
                "name": "Artemether-Lumefantrine",
                "description": "A combination antimalarial medication used to treat uncomplicated Plasmodium falciparum malaria by killing the parasites in the blood.",
                "symptoms": ["high fever", "chills", "sweating", "headache", "malaria"]
            },
            {
                "name": "Chloroquine",
                "description": "An antimalarial drug used to treat and prevent malaria caused by sensitive strains of Plasmodium vivax and Plasmodium ovale.",
                "symptoms": ["fever", "chills", "fatigue", "malaria", "body aches"]
            },
            {
                "name": "Quinine",
                "description": "Used in the treatment of severe or complicated malaria, especially when caused by chloroquine-resistant strains.",
                "symptoms": ["severe malaria", "high fever", "muscle cramps", "headache", "chills"]
            },
            {
                "name": "Clove Oil (Eugenol)",
                "description": "A natural analgesic and antiseptic used topically to numb and relieve toothache temporarily.",
                "symptoms": ["toothache", "gum irritation", "sensitivity", "tooth pain"]
            },
            {
                "name": "Hydrocortisone",
                "description": "A topical corticosteroid used to reduce inflammation, redness, and itching caused by conditions such as eczema, dermatitis, and allergic skin reactions.",
                "symptoms": ["itching", "redness", "eczema", "inflammation", "skin allergy"]
            },
            {
                "name": "Clotrimazole",
                "description": "An antifungal cream used to treat fungal skin infections such as ringworm, athlete’s foot, and candidiasis.",
                "symptoms": ["fungal infection", "itching", "scaly skin", "ringworm", "rash"]
            },
            {
                "name": "Isotretinoin",
                "description": "A powerful oral retinoid used to treat severe nodular acne by reducing oil gland size and controlling sebum production.",
                "symptoms": ["severe acne", "oily skin", "nodules", "cystic acne", "skin inflammation"]
            },
            {
                "name": "Permethrin",
                "description": "A topical cream used to treat scabies and lice by paralyzing and killing the parasites and their eggs.",
                "symptoms": ["scabies", "intense itching", "mites", "skin rash", "nighttime itching"]
            },
            {
                "name": "Salicylic Acid",
                "description": "A keratolytic agent used to treat psoriasis, warts, acne, and dandruff by softening and removing the outer layer of skin.",
                "symptoms": ["acne", "psoriasis", "rough skin", "scaly patches", "blackheads"]
            },
            {
                "name": "Mupirocin",
                "description": "A topical antibiotic used to treat localized skin infections like impetigo and infected cuts by stopping bacterial growth.",
                "symptoms": ["impetigo", "infected wounds", "skin irritation", "bacterial skin infection", "crusty sores"]
            },
            {
                "name": "Cephalexin",
                "description": "An oral antibiotic commonly prescribed for bacterial skin infections such as cellulitis, folliculitis, and boils.",
                "symptoms": ["cellulitis", "boils", "folliculitis", "swollen skin", "painful red skin"]
            },
            {
                "name": "Clindamycin",
                "description": "An antibiotic used for treating bacterial skin infections, especially those caused by resistant bacteria like MRSA.",
                "symptoms": ["MRSA infection", "boils", "infected acne", "skin swelling", "pus"]
            },
            {
                "name": "Mannitol",
                "description": "An osmotic diuretic used to reduce intracranial pressure and brain swelling after traumatic brain injury by drawing excess fluid out of brain tissue.",
                "symptoms": ["brain swelling", "increased intracranial pressure", "head trauma", "confusion", "loss of consciousness"]
            },
            {
                "name": "Phenytoin",
                "description": "An antiepileptic drug used to prevent seizures that can occur following a traumatic brain injury.",
                "symptoms": ["post-traumatic seizures", "brain injury", "head trauma", "convulsions"]
            },
            {
                "name": "Dexmedetomidine",
                "description": "A sedative used in ICU settings to help manage agitation, pain, and blood pressure in patients with severe brain injury.",
                "symptoms": ["agitation", "pain", "hypertension", "brain trauma", "confusion"]
            },
            {
                "name": "Donepezil",
                "description": "A cholinesterase inhibitor used to improve memory and cognitive function in patients with memory loss due to conditions like Alzheimer's disease.",
                "symptoms": ["memory loss", "amnesia", "confusion", "difficulty concentrating", "mild cognitive impairment"]
            },
            {
                "name": "Memantine",
                "description": "An NMDA receptor antagonist used to manage moderate to severe memory loss in neurodegenerative conditions by protecting brain cells from damage.",
                "symptoms": ["amnesia", "Alzheimer’s disease", "confusion", "disorientation", "cognitive decline"]
            },
            {
                "name": "Vitamin B12",
                "description": "A vital nutrient used to treat memory impairment caused by vitamin B12 deficiency, which can lead to reversible amnesia.",
                "symptoms": ["memory loss", "numbness", "tingling", "fatigue", "vitamin B12 deficiency"]
            },
            {
                "name": "Piracetam",
                "description": "A nootropic agent used in some cases to improve memory, focus, and cognitive function, particularly in age-related memory decline.",
                "symptoms": ["amnesia", "cognitive dysfunction", "poor memory", "learning difficulties"]
            },
            {
                "name": "Risperidone",
                "description": "An atypical antipsychotic approved to treat irritability, aggression, and self-injurious behavior in children and adolescents with autism spectrum disorder (ASD).",
                "symptoms": ["irritability", "aggression", "self-injury", "autism spectrum disorder", "mood swings"]
            },
            {
                "name": "Aripiprazole",
                "description": "An antipsychotic used to treat irritability and emotional disturbances in children with autism, helping reduce aggression and repetitive behaviors.",
                "symptoms": ["autism", "irritability", "repetitive behavior", "aggression", "emotional outbursts"]
            },
            {
                "name": "Methylphenidate",
                "description": "A stimulant used to manage attention deficit and hyperactivity symptoms often present in children with autism and co-occurring ADHD.",
                "symptoms": ["inattention", "hyperactivity", "impulsivity", "autism", "ADHD"]
            },
            {
                "name": "Melatonin",
                "description": "A natural supplement often used to help regulate sleep patterns in children with autism who experience insomnia or irregular sleep-wake cycles.",
                "symptoms": ["sleep disturbances", "autism", "insomnia", "restlessness", "night awakenings"]
            },
            {
                "name": "Cisplatin",
                "description": "A chemotherapy drug used to treat various types of cancer by interfering with the DNA of cancer cells, preventing their replication and growth.",
                "symptoms": ["cancer", "tumor growth", "pain", "fatigue", "advanced cancer"]
            },
            {
                "name": "Paclitaxel",
                "description": "A chemotherapy agent that inhibits cell division, used to treat breast, ovarian, and lung cancers.",
                "symptoms": ["breast cancer", "ovarian cancer", "tumors", "fatigue", "cancer-related pain"]
            },
            {
                "name": "Imatinib",
                "description": "A targeted therapy used to treat chronic myeloid leukemia (CML) and gastrointestinal stromal tumors (GIST) by blocking cancer-specific proteins.",
                "symptoms": ["chronic myeloid leukemia", "GIST", "abnormal white blood cells", "tumor growth"]
            },
            {
                "name": "Tamoxifen",
                "description": "A hormone therapy drug used to treat and prevent hormone receptor-positive breast cancer by blocking estrogen receptors.",
                "symptoms": ["breast cancer", "hormonal imbalance", "tumor growth", "recurrence prevention"]
            },
            {
                "name": "Bevacizumab",
                "description": "A monoclonal antibody that inhibits angiogenesis (blood vessel formation), used in the treatment of colorectal, lung, and kidney cancers.",
                "symptoms": ["advanced cancer", "tumor progression", "blood vessel growth", "colorectal cancer"]
            },
            {
                "name": "Amlodipine",
                "description": "A calcium channel blocker used to relax and widen blood vessels, making it easier for the heart to pump and lowering blood pressure.",
                "symptoms": ["high blood pressure", "chest pain", "dizziness", "fatigue", "shortness of breath"]
            },
            {
                "name": "Losartan",
                "description": "An angiotensin II receptor blocker (ARB) that helps lower blood pressure by relaxing blood vessels and reducing resistance.",
                "symptoms": ["hypertension", "heart strain", "kidney protection", "high blood pressure"]
            },
            {
                "name": "Lisinopril",
                "description": "An ACE inhibitor used to treat high blood pressure and heart failure by blocking the formation of a substance that narrows blood vessels.",
                "symptoms": ["high blood pressure", "heart failure", "chronic hypertension", "kidney disease"]
            },
            {
                "name": "Hydrochlorothiazide",
                "description": "A thiazide diuretic that helps lower blood pressure by removing excess salt and water from the body.",
                "symptoms": ["fluid retention", "high blood pressure", "swelling", "hypertension"]
            },
            {
                "name": "Metoprolol",
                "description": "A beta-blocker that slows the heart rate and reduces the heart's workload, used in the management of high blood pressure and angina.",
                "symptoms": ["hypertension", "chest pain", "rapid heartbeat", "high blood pressure"]
            },
            {
                "name": "Phenytoin",
                "description": "An antiepileptic drug used to prevent and control seizures by stabilizing electrical activity in the brain.",
                "symptoms": ["seizures", "convulsions", "fits", "epilepsy", "loss of consciousness"]
            },
            {
                "name": "Sodium Valproate",
                "description": "An anticonvulsant medication used to treat various types of seizures and epilepsy by increasing brain levels of GABA.",
                "symptoms": ["generalized seizures", "absence seizures", "epilepsy", "fits", "bipolar disorder"]
            },
            {
                "name": "Carbamazepine",
                "description": "An antiepileptic drug used to treat focal and tonic-clonic seizures by reducing nerve impulses that cause seizures.",
                "symptoms": ["partial seizures", "epilepsy", "nerve pain", "fits", "trigeminal neuralgia"]
            },
            {
                "name": "Levetiracetam",
                "description": "A broad-spectrum antiepileptic drug used to control partial and generalized seizures, especially in children and adults.",
                "symptoms": ["seizures", "epilepsy", "convulsions", "fits", "neurological disorder"]
            },
            {
                "name": "Clobazam",
                "description": "A benzodiazepine used as an adjunctive treatment in epilepsy to reduce the frequency of seizures.",
                "symptoms": ["epilepsy", "seizures", "anxiety", "fits", "convulsions"]
            },
            {
                "name": "Tetanus Toxoid Vaccine (TT)",
                "description": "A vaccine used to prevent tetanus by stimulating the body to produce immunity against the tetanus toxin.",
                "symptoms": ["muscle stiffness", "jaw lock (lockjaw)", "muscle spasms", "tetanus", "difficulty swallowing"]
            },
            {
                "name": "Tetanus Immune Globulin (TIG)",
                "description": "A preparation of antibodies used to provide immediate passive immunity after exposure to the tetanus bacteria.",
                "symptoms": ["tetanus exposure", "wound contamination", "muscle spasms", "lockjaw", "tetanus infection"]
            },
            {
                "name": "Diazepam",
                "description": "A benzodiazepine used to control severe muscle spasms and seizures associated with tetanus.",
                "symptoms": ["muscle spasms", "tetanus", "seizures", "rigidity", "anxiety"]
            },
            {
                "name": "Metronidazole",
                "description": "An antibiotic used to kill Clostridium tetani bacteria at the wound site, helping to control infection.",
                "symptoms": ["tetanus infection", "wound infection", "bacterial contamination", "inflammation"]
            },
            {
                "name": "Atorvastatin",
                "description": "A statin medication used to lower bad cholesterol (LDL) and triglycerides while increasing good cholesterol (HDL), reducing the risk of heart attack and stroke.",
                "symptoms": ["high cholesterol", "atherosclerosis", "heart disease risk", "high LDL", "low HDL"]
            },
            {
                "name": "Rosuvastatin",
                "description": "A potent statin that lowers LDL cholesterol and reduces the risk of cardiovascular events in high-risk individuals.",
                "symptoms": ["high LDL", "high cholesterol", "heart disease risk", "stroke prevention", "plaque buildup"]
            },
            {
                "name": "Fenofibrate",
                "description": "A lipid-lowering agent primarily used to reduce triglyceride levels and increase HDL cholesterol.",
                "symptoms": ["high triglycerides", "low HDL", "metabolic syndrome", "cholesterol imbalance"]
            },
            {
                "name": "Ezetimibe",
                "description": "A cholesterol absorption inhibitor that reduces blood cholesterol by limiting absorption from the intestine.",
                "symptoms": ["high LDL", "dietary cholesterol", "hypercholesterolemia", "cholesterol imbalance"]
            },
            {
                "name": "Omega-3 Fatty Acids",
                "description": "Natural supplements that help reduce high triglyceride levels and support heart health.",
                "symptoms": ["high triglycerides", "cholesterol imbalance", "heart disease prevention", "inflammation"]
            },
            {
                "name": "Oral Rehydration Salts (ORS)",
                "description": "Used to prevent and treat dehydration caused by high fever, vomiting, or low platelet count in dengue patients.",
                "symptoms": ["dehydration", "fatigue", "vomiting", "dengue fever", "fluid loss"]
            },
            {
                "name": "Papaya Leaf Extract",
                "description": "A natural remedy believed to help increase platelet count in patients with dengue fever, though scientific evidence is limited.",
                "symptoms": ["low platelet count", "fatigue", "dengue symptoms", "bleeding tendency"]
            },
            {
                "name": "IV Fluids",
                "description": "Intravenous fluids are administered in moderate to severe cases to maintain hydration and prevent shock.",
                "symptoms": ["low blood pressure", "dengue hemorrhagic fever", "shock", "severe dehydration"]
            },
            {
                "name": "Phenylephrine Eye Drops",
                "description": "Used to dilate the pupil before cataract surgery or eye examination; helps provide access to the lens for surgical removal.",
                "symptoms": ["blurry vision", "cloudy lens", "cataract", "light sensitivity", "vision loss"]
            },
            {
                "name": "Tropicamide Eye Drops",
                "description": "Used to dilate the pupil and relax eye muscles before cataract surgery or eye examination.",
                "symptoms": ["blurred vision", "cataract diagnosis", "pupil dilation", "eye discomfort"]
            },
            {
                "name": "Prednisolone Acetate Eye Drops",
                "description": "A corticosteroid used after cataract surgery to reduce inflammation and promote healing.",
                "symptoms": ["post-surgical inflammation", "eye pain", "redness", "swelling", "cataract surgery recovery"]
            },
            {
                "name": "Moxifloxacin Eye Drops",
                "description": "An antibiotic used after cataract surgery to prevent eye infections.",
                "symptoms": ["infection prevention", "eye redness", "postoperative care", "cataract surgery"]
            },
            {
                "name": "Paracetamol (Acetaminophen)",
                "description": "An over-the-counter pain reliever and fever reducer commonly used to relieve mild to moderate ear pain caused by infection or inflammation.",
                "symptoms": ["earache", "fever", "ear infection", "throbbing pain", "inflammation"]
            },
            {
                "name": "Ofloxacin Ear Drops",
                "description": "An antibiotic ear drop used to treat bacterial outer and middle ear infections.",
                "symptoms": ["ear discharge", "itching", "pain", "bacterial ear infection", "swelling"]
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
   