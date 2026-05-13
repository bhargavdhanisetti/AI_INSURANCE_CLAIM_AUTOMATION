# ==========================================
# W4 - Unit Testing
# ==========================================

from main import extract_entities

def test_empty_text():

    result = extract_entities("")

    assert result == {
        "diagnosis": [],
        "amount": []
    }

def test_icd_extraction():

    text = "Patient diagnosed with E11"

    result = extract_entities(text)

    assert result["diagnosis"] == ["E11"]

print("All Tests Passed ✅")