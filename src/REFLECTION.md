LocalBuka — Written Reflection

1. Overall Approach

I built LocalBuka as a lightweight restaurant recommendation and conversational assistant prototype focused on restaurants and food in Kano State, Nigeria.

The recommendation component uses transparent rule-based scoring. It considers cuisine, preferred meals, budget, distance, restaurant rating, and spicy-food preference. Restaurants are scored and ranked according to how well they match the user's preferences.

I chose this approach because the case-study dataset is small and does not provide enough historical user-interaction data to justify training a machine-learning recommendation model. The rule-based approach is also easy to understand, test, debug, and explain.

I added exact meal-combination matching so a complete preference such as "Tuwo Shinkafa + Miyan Kuka" receives a stronger match than a partial match.

I also added an explanation layer so recommendations include reasons rather than only a numerical score.

For Part 2, I built a command-line conversational assistant. It accepts free-text requests such as "I need something spicy and cheap near me", extracts supported preferences using lightweight keyword/rule matching, and sends them to the recommendation engine.

2. What I Would Build With More Time

I would replace the case-study dataset with a continuously updated database containing verified restaurant information, menus, prices, opening hours, locations, and availability.

I would collect user interactions such as searches, clicks, saved restaurants, ratings, and orders. With enough data, this could support a machine-learning or hybrid recommendation system.

I would improve natural-language understanding so users could express the same intent in many ways without relying on predefined keywords, and I would add clarification questions for ambiguous requests.

The distance feature could be upgraded from dataset values to real GPS-based distance calculation and eventually road distance and estimated travel time.

At production scale, I would use a backend API and database and add monitoring, caching, logging, and personalization.

3. One Real AI Risk and Mitigation

A major risk is providing incorrect or outdated restaurant information. Menus, prices, ratings, locations, opening hours, and availability can change.

A production system should use verified data sources, regularly refresh information, record update times, and avoid presenting uncertain information as fact.

If an LLM were introduced, I would constrain it to retrieve restaurant information from trusted backend data rather than allowing it to invent restaurant names, dishes, prices, or availability.

4. Debugging Experience

During development, I encountered a Python SyntaxError: 'return' outside function error after modifying the meal-matching logic.

I traced the problem to incorrect indentation, which caused Python to interpret return score as being outside the calculate_score() function.

I replaced the affected function with a clean, correctly indented implementation and reran the tests. The system then successfully produced the expected recommendations.

I also tested different user profiles to verify that rankings changed according to user preferences. This reinforced the importance of reading the exact error message, identifying the affected code structure, making a focused correction, and rerunning the relevant tests.