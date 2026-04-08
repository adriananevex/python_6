from elements import create_fire, create_water
from .elements import create_earth, create_air


def healing_potion() -> str:
    earth = create_earth()
    air = create_air()
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion() -> str:
    fire = create_fire()
    water = create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'"


def invisibility_potion():
    air_result = create_air()
    water_result = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion():
    fire = create_fire()
    water = create_water()
    earth = create_earth()
    air = create_air()

    return (
        f"Wisdom potion brewed with all elements: "
        f"{fire}, {water}, {earth}, {air}"
    )
