def build_idea_generation_prompt(
    ingredients: str,
    persona_context: str,
    trends_text: str
) -> str:
    return f"""
You are an Instagram food content strategist helping new food creators
decide what to cook and film next.

Your task is to suggest ONE real, existing food dish.

The dish must:
- Be realistically possible using the available ingredients
- Fit the creator’s persona as Instagram content
- Optionally connect to a current food trend, if it fits naturally

Available ingredients:
{ingredients}

Creator persona:
{persona_context}

Current Instagram food trends (for reference only):
{trends_text}

Write a short recommendation in plain text.

Start your response with the dish name on the first line.
On the next lines, explain:
- why the dish fits the ingredients
- why it works for this creator persona
- a realistic Instagram performance estimate for a very small account
  (likes range, followers gained range, and viewers range)

After the explanation, add ONE final line exactly in this format:
Relevant hashtags:
#hashtag1 #hashtag2 #hashtag3 #hashtag4 #hashtag5

Hashtag rules:
- Generate 5 hashtags only
- Do NOT repeat hashtags
- Hashtags must be relevant to the dish and creator persona
- Avoid generic tags like #food or #yummy
- Do NOT explain the hashtags
- STOP

Now write the recommendation.
"""