def validate_ingredientes(ingredients: str) -> str:
  valid_elements = ["fire", "water", "earth", "air"]

  for element in valid_elements:
    if element in ingredients:
      return f"{ingredients} - VALID"

  return f"{ingredients} - INVALID"
