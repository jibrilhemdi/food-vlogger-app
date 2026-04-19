def build_prompt(ingredients: str, persona_context: str, trends: list) -> str:
    trends_text = "\n".join(
        [f"- {t['name']} ({t['hashtag']}, rank {t['rank']})" for t in trends]
    )

    return f"""
SYSTEM RULES (STRICT):
- Output MUST be valid JSON only.
- Do NOT explain the JSON.
- Do NOT repeat instructions or placeholders.
- Output must start with {{ and end with }}.

You are generating ACTUAL VALUES, not templates.

REQUIRED FORMAT (DO NOT COPY TEXT BELOW VERBATIM):
The response must be a JSON object with this shape:
- suggestions: list of objects
- each object contains:
  - dish_name: real, canonical food name
  - reasoning: 2–3 sentences of explanation
  - estimated_likes: realistic range string
  - estimated_followers_gained: realistic range string

CONTENT RULES:
- Dish names must be real foods.
- Reasoning MUST explicitly explain:
  1. why the dish fits the available ingredients
  2. why it fits the creator persona as Instagram content
  3. optionally how a trend can be used
- Avoid generic cooking descriptions.
- Write like a content strategist advising a creator.

ENGAGEMENT CONSTRAINTS:
- Assume a small Instagram account (0–10k followers).
- Likes: usually between 500 and 15,000.
- Followers gained: usually between 5 and 300.
- Always use ranges (e.g. "1.2k–4k", "20–60").

INPUT:
Ingredients: {ingredients}

Persona:
{persona_context}

Instagram Trends:
{trends_text}

TASK:
Generate 2–3 COMPLETE suggestions with REAL VALUES.

FINAL OUTPUT:
JSON only. No placeholders. No instructions.
"""