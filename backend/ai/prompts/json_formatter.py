def build_json_formatter_prompt(idea_text: str) -> str:
    return f"""
ROLE:
You are a strict JSON conversion engine.

TASK:
Convert the content provided into ONE valid JSON object that follows the exact schema below.

ABSOLUTE RULES (NO EXCEPTIONS):
- Output JSON ONLY.
- No explanations.
- No markdown.
- No comments.
- No extra text before or after JSON.
- Do NOT invent, remove, or rephrase information beyond light grammar cleanup.
- If data is vague, infer the most reasonable meaning.
- All keys and values MUST use double quotes.
- Output MUST start with {{ and end with }}.

JSON SCHEMA (MUST MATCH EXACTLY):
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

CONVERSION INSTRUCTIONS:
- Each dish = one object in "suggestions".
- Merge all explanation text into "reasoning".
- Keep engagement numbers or ranges EXACTLY as written.
- Extract hashtags ONLY from the line starting with "Relevant hashtags:".
- Split hashtags into a list.
- Each hashtag MUST include the leading "#".
- Maximum 10 hashtags per dish.
- If a field is missing, use an empty string "" or empty list [].

CONTENT TO CONVERT:
<<<
{idea_text}
>>>

FINAL CHECK BEFORE OUTPUT:
- Valid JSON
- Schema matches exactly
- No trailing commas
- One single JSON object

OUTPUT:
"""


# def build_json_formatter_prompt(idea_text: str) -> str:
#     return f"""
# You are a formatting assistant.

# Your ONLY task is to convert the content below into VALID JSON.

# RULES (STRICT):
# - Output JSON only.
# - Do NOT add new information.
# - Do NOT remove information.
# - Do NOT explain anything.
# - Do NOT include markdown or extra text.
# - If something is unclear, make the best reasonable interpretation.
# - Output must start with {{ and end with }}.

# REQUIRED JSON STRUCTURE:
# {{
#   "suggestions": [
#     {{
#       "dish_name": "",
#       "reasoning": "",
#       "estimated_likes": "",
#       "estimated_followers_gained": "",
#       "estimated_viewers": "",
#       "hashtags": []
#     }}
#   ]
# }}

# CONVERSION RULES:
# - Each dish becomes one object in the "suggestions" array.
# - Combine explanation text into the "reasoning" field.
# - Preserve engagement ranges exactly as written.
# - Use clean, readable sentences.
# - Ensure all strings use DOUBLE QUOTES.
# - Extract hashtags from the line starting with "Relevant hashtags:".
# - Split hashtags into a list of strings.
# - Each hashtag must include the leading "#".
# - Do NOT include more than 10 hashtags.

# CONTENT TO CONVERT:
# <<<
# {idea_text}
# >>>

# FINAL OUTPUT:
# Return ONLY ONE valid JSON object.
# """