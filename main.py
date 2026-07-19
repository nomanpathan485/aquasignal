from src.embedding_service import calculate_similarity


pairs = [
    ("No water coming", "पानी नहीं आ रहा"),
    ("No water coming", "Paani nahi aa raha"),
    ("No water coming", "Water supply has stopped"),
    ("No water coming", "Water smells bad"),
]

for text1, text2 in pairs:
    score = calculate_similarity(text1, text2)

    print(f"\nText 1: {text1}")
    print(f"Text 2: {text2}")
    print(f"Similarity: {score:.4f}")