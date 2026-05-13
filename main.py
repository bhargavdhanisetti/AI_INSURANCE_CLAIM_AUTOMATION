# ==========================================
# W3 - FastAPI NLP API
# ==========================================

from fastapi import FastAPI
import re

app = FastAPI()

# ==========================================
# Entity Extraction Function
# ==========================================

def extract_entities(text):

    diagnosis = re.findall(r'\b[A-Z][0-9]{2}(?:\.[0-9]+)?\b', text)

    amount = re.findall(r'\d+', text)

    return {
        "diagnosis": diagnosis,
        "amount": amount
    }

# ==========================================
# API Endpoint
# ==========================================

@app.post("/extract-entities")

def extract(text: str):

    result = extract_entities(text)

    return result

# ==========================================
# Run Command
# ==========================================

#python -m uvicorn main:app --reload