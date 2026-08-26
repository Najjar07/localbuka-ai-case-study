from recommender import recommend_restaurants


def parse_user_message(message):
    """
    Convert a user's natural-language message
    into preferences understood by the recommender.
    """

    message = message.lower()

    user = {
        "preferred_cuisine": None,
        "preferred_dishes": [],
        "budget": None,
        "spicy": None,
        "max_distance_km": 6
    }

    # Cuisine
    if "hausa" in message or "northern" in message:
        user["preferred_cuisine"] = "Hausa"

    elif "international" in message or "western" in message:
        user["preferred_cuisine"] = "International"

    # Dishes
    dishes = [
        "tuwo shinkafa",
        "tuwo masara",
        "miyan kuka",
        "miyan taushe",
        "suya",
        "jollof rice",
        "fried rice",
        "grilled chicken",
        "masa",
        "kilishi",
        "danwake"
    ]

    for dish in dishes:
        if dish in message:
            user["preferred_dishes"].append(dish.title())

    # Budget
    if (
        "cheap" in message
        or "affordable" in message
        or "cheaply" in message
    ):
        user["budget"] = "budget"

    elif "expensive" in message or "premium" in message:
        user["budget"] = "premium"

    # Spicy preference
    if "spicy" in message or "pepper" in message:
        user["spicy"] = True

    return user


def chat():
    print("\nLocalBuka Assistant")
    print("=" * 40)
    print("Tell me what you want to eat.")
    print("Type 'exit' to quit.\n")

    while True:
        message = input("You: ")

        if message.lower() == "exit":
            print("LocalBuka: Goodbye!")
            break

        user = parse_user_message(message)

        recommendations = recommend_restaurants(user)

        print("\nLocalBuka:")

        if not recommendations:
            print("Sorry, I couldn't find a suitable restaurant.")
            continue

        print("Here are my top recommendations:\n")

        for index, restaurant in enumerate(recommendations, start=1):
            print(f"{index}. {restaurant['name']}")
            print(f"   Area: {restaurant['area']}")
            print(f"   Score: {restaurant['score']}")
            print(f"   Rating: {restaurant['rating']}")
            print(
                f"   Meals: {', '.join(restaurant['popular_meals'])}"
            )

            if restaurant["reasons"]:
                print("   Why:")
                for reason in restaurant["reasons"]:
                    print(f"   ✓ {reason}")

            print()


if __name__ == "__main__":
    chat()