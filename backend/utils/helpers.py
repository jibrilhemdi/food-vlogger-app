from pathlib import Path
from utils.personas import PERSONAS
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

def load_trends(csv_path: str = "data/food_trends.csv", limit: int = 5) -> list:
    """
    Loads top-ranked food trends from CSV.
    Returns structured trend context for AI.
    """

    full_path = BASE_DIR / csv_path

    df = pd.read_csv(full_path)
    df = df.sort_values(by="rank").head(limit)

    trends = []
    for _, row in df.iterrows():
        trends.append({
            "name": row["trend_name"],
            "hashtag": row["instagram_hashtag"],
            "rank": int(row["rank"])
        })

    return trends

def get_persona_context(persona_key: str) -> str:
    persona = PERSONAS.get(persona_key)

    return f"""
    Persona Label: {persona['label']}
    Content Style: {persona['style']}
    Tone: {persona['tone']}
    Focus: {persona['focus']}
    """
