import json
from pathlib import Path


# Path to restaurant dataset
DATA_PATH = Path(__file__).parent.parent / "data" / "restaurants.json"


def load_restaurants():
    """Load restaurant data from JSON."""
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def calculate_score(restaurant, user):
    """Calculate how well a restaurant matches user preferences."""

    score = 0

    # 1. Cuisine match — 20 points
    preferred_cuisine = user.get("preferred_cuisine")

    if preferred_cuisine:
        cuisines = restaurant.get("cuisine", [])

        if preferred_cuisine.lower() in [
            cuisine.lower() for cuisine in cuisines
        ]:
            score += 20

    # 2. Meal match — 30 points
    preferred_dishes = user.get("preferred_dishes", [])
    restaurant_meals = restaurant.get("popular_meals", [])

    for preferred_dish in preferred_dishes:
        preferred_dish = preferred_dish.lower().strip()

        for meal in restaurant_meals:
            meal_lower = meal.lower().strip()

            # Exact meal combination
            if preferred_dish == meal_lower:
                score += 30
                break

            # Partial meal match
            elif preferred_dish in meal_lower:
                score += 15
                break

    # 3. Budget match — 15 points
    preferred_budget = user.get("budget")

    if preferred_budget:
        if restaurant.get("price_range") == preferred_budget:
            score += 15

    # 4. Distance match — 15 points
    max_distance = user.get("max_distance_km")

    if max_distance is not None:
        distance = restaurant.get("distance_km", 999)

        if distance <= max_distance:
            score += 15

        elif distance <= max_distance + 3:
            score += 8

    # 5. Rating — 10 points
    rating = restaurant.get("rating", 0)

    if rating >= 4.5:
        score += 10

    elif rating >= 4.0:
        score += 7

    elif rating >= 3.5:
        score += 4

    # 6. Spicy food preference — 10 points
    wants_spicy = user.get("spicy")

    if wants_spicy is not None:

        spicy_keywords = [
            "suya",
            "kilishi",
            "pepper",
            "yaji"
        ]

        has_spicy_food = any(
            any(keyword in meal.lower() for keyword in spicy_keywords)
            for meal in restaurant_meals
        )

        if wants_spicy == has_spicy_food:
            score += 10

    return score

def generate_reasons(restaurant, user):
    """Explain why a restaurant was recommended."""

    reasons = []

    # Cuisine
    preferred_cuisine = user.get("preferred_cuisine")

    if preferred_cuisine:
        cuisines = restaurant.get("cuisine", [])

        if preferred_cuisine.lower() in [
            cuisine.lower() for cuisine in cuisines
        ]:
            reasons.append(
                f"Matches your {preferred_cuisine} cuisine preference"
            )

    # Meal
    preferred_dishes = user.get("preferred_dishes", [])
    restaurant_meals = restaurant.get("popular_meals", [])

    for preferred_dish in preferred_dishes:
        preferred_dish_lower = preferred_dish.lower()

        for meal in restaurant_meals:
            if preferred_dish_lower == meal.lower():
                reasons.append(
                    f"Offers your preferred meal: {meal}"
                )
                break

            elif preferred_dish_lower in meal.lower():
                reasons.append(
                    f"Offers a meal matching your preference: {meal}"
                )
                break

    # Budget
    preferred_budget = user.get("budget")

    if preferred_budget == restaurant.get("price_range"):
        reasons.append("Matches your budget preference")

    # Distance
    max_distance = user.get("max_distance_km")
    distance = restaurant.get("distance_km")

    if max_distance is not None and distance is not None:
        if distance <= max_distance:
            reasons.append(
                f"Within your preferred distance ({distance} km)"
            )

    # Rating
    rating = restaurant.get("rating", 0)

    if rating >= 4.0:
        reasons.append(
            f"Highly rated ({rating}/5)"
        )

    # Spicy
    if user.get("spicy") is True and restaurant.get("spicy") is True:
        reasons.append("Suitable for your spicy-food preference")

    return reasons

def recommend_restaurants(user, limit=5):
    """Return the highest-ranked restaurants."""

    restaurants = load_restaurants()

    scored_restaurants = []

    for restaurant in restaurants:

        score = calculate_score(restaurant, user)

        reasons = generate_reasons(restaurant, user)

        scored_restaurants.append({
            "name": restaurant["name"],
            "area": restaurant["area"],
            "score": score,
            "rating": restaurant["rating"],
            "popular_meals": restaurant["popular_meals"],
            "reasons": reasons
        })

    # Highest score first
    scored_restaurants.sort(
        key=lambda restaurant: restaurant["score"],
        reverse=True
    )

    return scored_restaurants[:limit]