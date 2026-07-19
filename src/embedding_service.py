from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


model = SentenceTransformer(
    "anuragwagh0/hinglish-minilm"
)


def generate_embedding(text: str):
    return model.encode(text)


def calculate_similarity(text1: str, text2: str) -> float:
    embedding1 = generate_embedding(text1)
    embedding2 = generate_embedding(text2)

    similarity = cos_sim(embedding1, embedding2)

    return float(similarity.item())