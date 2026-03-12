import difflib

def calculate_exact_match(prediction: str, reference: str) -> float:
    return 1.0 if prediction.strip().lower() == reference.strip().lower() else 0.0

def calculate_similarity(prediction: str, reference: str) -> float:
    """Returns a score between 0 and 1 based on sequence matching."""
    return difflib.SequenceMatcher(None, prediction, reference).ratio()
