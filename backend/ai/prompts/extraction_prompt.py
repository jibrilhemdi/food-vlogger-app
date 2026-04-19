def build_extraction_prompt(idea_text: str) -> str:
    return f"""
ROLE:
You are a data extraction assistant.

TASK:
Extract clean structured information from the content below.

RULES:
- Do NOT output JSON.
- Do NOT explain anything.
- Do NOT repeat content.
- Remove duplicated ideas and sentences.
- Normalize wording but do NOT invent data.

OUTPUT FORMAT (PLAIN TEXT):
Dish name:
<dish name>

Reasoning:
<one clean paragraph>

Estimated likes:
<range or empty>

Estimated followers gained:
<range or empty>

Estimated viewers:
<range or empty>

Hashtags:
#tag1 #tag2 #tag3 ...

CONTENT:
<<<
{idea_text}
>>>

FINAL OUTPUT:
Structured text only. Stop.
"""