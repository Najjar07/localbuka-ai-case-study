from recommender import recommend_restaurants


user = {
    "preferred_cuisine": "International",
    "budget": "premium",
    "preferred_dishes": ["Grilled Chicken"],
    "spicy": False,
    "max_distance_km": 8
}


recommendations = recommend_restaurants(user)


print("\nLocalBuka Recommendations")
print("=" * 40)

for index, restaurant in enumerate(recommendations, start=1):
    print(f"\n{index}. {restaurant['name']}")
    print(f"   Area: {restaurant['area']}")
    print(f"   Score: {restaurant['score']}")
    print(f"   Rating: {restaurant['rating']}")
    print(f"   Meals: {', '.join(restaurant['popular_meals'])}")

    print("   Why recommended:")

    for reason in restaurant["reasons"]:
        print(f"   ✓ {reason}")