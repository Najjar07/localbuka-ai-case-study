# LocalBuka – AI Restaurant Recommendation Assistant

## Overview

LocalBuka is a prototype restaurant discovery and recommendation assistant focused on restaurants and food in Kano State, Nigeria.

## Features

- Cuisine preference matching
- Exact and partial meal matching
- Budget matching
- Distance-based filtering
- Restaurant rating consideration
- Spicy-food preference
- Explainable recommendations
- Free-text command-line conversational assistant

## Project Structure

```text
localbuka-ai-case-study/
├── data/
│   └── restaurants.json
├── src/
│   ├── recommender.py
│   ├── test_recommender.py
│   └── chat_assistant.py
├── README.md
├── REFLECTION.md
└── requirements.txt
```

## Requirements

Python 3.9+ is recommended. The current prototype uses only Python's standard library and does not require a paid LLM API.

## How to Run

From the project root:

```bash
python src/test_recommender.py
python src/chat_assistant.py
```

### Example

```text
You: I need something spicy and cheap near me
```

Type `exit` to close the assistant.

## Recommendation Approach

The system scores restaurants using cuisine, preferred meals, budget, distance, rating, and spicy-food preference. Exact meal combinations receive a stronger match than partial matches. Results are sorted by score and accompanied by explanations.

## Conversational Assistant

The assistant accepts free-text requests, extracts supported preferences using lightweight keyword/rule matching, and passes them to the same recommendation engine.

## Testing

The system was tested with different user profiles, including:

- Hausa/Northern Nigerian food preferences with Tuwo Shinkafa + Miyan Kuka
- Budget, spicy Beef Suya preference
- International-food preference with Grilled Chicken

## Production Considerations

Possible failures include misunderstood free-text requests and outdated restaurant information. Mitigations include better NLP, clarification questions, verified and regularly refreshed data, and monitoring recommendation quality.

The current prototype does not use a paid LLM. If an LLM is added later, costs can be controlled through smaller models, short prompts, caching, limited conversation history, selective LLM use, and token/spending monitoring.

## Current Limitations

- Case-study dataset rather than live production data
- Distance values are dataset values, not real-time GPS/road distances
- Limited keyword-based natural-language understanding
- No live availability or ordering integration
- No learned personalization

## Future Improvements

- Real GPS distance calculation
- Road distance and travel time
- Live restaurant/menu data
- Database/API backend
- Stronger natural-language understanding
- User-history personalization
- Machine-learning or hybrid recommendations
- Web/mobile interface

## License

Created as an AI Engineer internship case-study prototype.