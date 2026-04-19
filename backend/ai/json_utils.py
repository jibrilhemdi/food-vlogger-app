import json
def extract_json(text: str) -> dict:
    """
    Extracts the first complete JSON object by balancing braces.
    Ignores anything before or after.
    """
    text = text.strip()

    start = text.find("{")
    if start == -1:
        raise ValueError("No JSON object found in model output")

    brace_count = 0
    end = None

    for i, char in enumerate(text[start:], start=start):
        if char == "{":
            brace_count += 1
        elif char == "}":
            brace_count -= 1
            if brace_count == 0:
                end = i + 1
                break

    if end is None:
        raise ValueError("Incomplete JSON object")

    json_str = text[start:end]

    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON extracted: {e}")