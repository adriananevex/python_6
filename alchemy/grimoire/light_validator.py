def validate_ingredients(ingredients: str) -> str:
    allowed = ["earth", "air", "fire", "water"]

    for item in allowed:
        if item.lower() in ingredients.lower():
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"