from pydantic import BaseModel
from typing import List, Literal

PersonaType = Literal[
    "fine_dining",
    "healthy_fit",
    "cozy_home",
    "street_viral"
]

class FoodRequest(BaseModel):
    ingredients: str
    persona: PersonaType

class DishSuggestion(BaseModel):
    dish_name: str
    reasoning: str
    estimated_likes: str
    estimated_followers_gained: str
    estimated_viewers: str
    hashtags: List[str]

class FoodResponse(BaseModel):
    suggestions: List[DishSuggestion]
