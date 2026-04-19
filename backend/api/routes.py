import html
from fastapi import APIRouter, HTTPException

from schemas.request_response import FoodRequest, FoodResponse
from ai.model import run_local_ai
from ai.json_utils import extract_json
from utils.helpers import load_trends, get_persona_context

# Prompt A & B
from ai.prompts.idea_generation import build_idea_generation_prompt
from ai.prompts.json_formatter import build_json_formatter_prompt
from ai.prompts.extraction_prompt import build_extraction_prompt
from ai.prompts.json_prompt import build_json_prompt


router = APIRouter()


# -------------------------
# Helper functions
# -------------------------
def clean_idea_text(text: str) -> str:
    # Remove internal thinking tokens
    text = text.replace("</think>", "").strip()

    # Decode HTML entities (&amp; → &)
    text = html.unescape(text)

    return text

def clean_hashtags(hashtags):
    seen = set()
    cleaned = []

    for tag in hashtags:
        tag = tag.strip()
        if not tag.startswith("#"):
            continue
        key = tag.lower()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(tag)

    return cleaned[:5]

# -------------------------
# API route
# -------------------------
@router.post("/generate", response_model=FoodResponse)
def generate_food_ideas(request: FoodRequest):
    # -------------------------
    # Prepare context
    # -------------------------
    trends = load_trends(limit=5)
    persona_context = get_persona_context(request.persona)

    trends_text = "\n".join(
        [f"- {t['name']} ({t['hashtag']}, rank {t['rank']})" for t in trends]
    )

    # -------------------------
    # Prompt A: Idea generation
    # -------------------------
    prompt_a = build_idea_generation_prompt(
        ingredients=request.ingredients,
        persona_context=persona_context,
        trends_text=trends_text
    )

    idea_text = run_local_ai(prompt_a)
    idea_text = clean_idea_text(idea_text)

    print("\n--- PROMPT A OUTPUT ---\n", idea_text)

    if not idea_text.strip():
        raise HTTPException(
            status_code=500,
            detail="Prompt A returned no complete dish ideas"
        )

    # -------------------------
    # Prompt B: JSON formatting (with retry)
    # -------------------------
    last_error = None

    for _ in range(2):  # retry once
        # Step 1: extract structured text
        # prompt_b1 = build_extraction_prompt(idea_text)
        # extracted_text = run_local_ai(prompt_b1)

        # # Step 2: convert to strict JSON
        # prompt_b2 = build_json_prompt(extracted_text)
        # json_text = run_local_ai(prompt_b2)

        # parsed = extract_json(json_text)
        # json_text = run_local_ai(parsed)

        prompt_b = build_json_formatter_prompt(idea_text)
        json_text = run_local_ai(prompt_b)

        print("\n--- PROMPT B OUTPUT ---\n", json_text)

        try:
            parsed = extract_json(json_text)
            parsed["suggestions"][0]["hashtags"] = clean_hashtags(
                parsed["suggestions"][0].get("hashtags", [])
            )
            return FoodResponse(**parsed)
        except Exception as e:
            last_error = e
            continue

    raise HTTPException(
        status_code=500,
        detail=f"Invalid AI output after formatting: {str(last_error)}"
    )