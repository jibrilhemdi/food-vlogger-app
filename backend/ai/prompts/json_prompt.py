def build_json_prompt(extracted_text: str) -> str:
    return f"""
ROLE:
You are a strict JSON generator.

TASK:
Convert the structured content below into EXACTLY one valid JSON object.

ABSOLUTE RULES:
- Output JSON ONLY.
- No explanation.
- No extra text.
- Output must start with {{ and end with }}.
- Stop immediately after JSON.

JSON SCHEMA:
{{
  "suggestions": [
    {{
      "dish_name": "",
      "reasoning": "",
      "estimated_likes": "",
      "estimated_followers_gained": "",
      "estimated_viewers": "",
      "hashtags": []
    }}
  ]
}}

FIELD RULES:
- Use values exactly as provided.
- Split hashtags into a list.
- Remove duplicates.
- Max 10 hashtags.

CONTENT:
<<<
{extracted_text}
>>>

FINAL OUTPUT:
JSON only.
"""