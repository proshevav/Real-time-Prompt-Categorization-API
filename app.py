from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

#category defaults
CATEGORY_DEFAULTS = {
    "Coding": {"temperature": 0.2, "reasoning_effort": "high", "verbosity": "balanced", "web": "optional"},
    "Debugging": {"temperature": 0.1, "reasoning_effort": "high", "verbosity": "verbose", "web": "optional"},
    "Creative_Writing": {"temperature": 0.7, "reasoning_effort": "medium", "verbosity": "high", "web": "optional"},
    "Factual_QA": {"temperature": 0.3, "reasoning_effort": "medium", "verbosity": "low", "web": "optional"},
    "Summarization": {"temperature": 0.3, "reasoning_effort": "medium", "verbosity": "low", "web": "optional"},
    "Translation": {"temperature": 0.5, "reasoning_effort": "medium", "verbosity": "balanced", "web": "optional"},
    "Data_Analysis": {"temperature": 0.2, "reasoning_effort": "high", "verbosity": "balanced", "web": "optional"},
    "Planning_Itinerary": {"temperature": 0.6, "reasoning_effort": "medium", "verbosity": "balanced", "web": "optional"},
    "Sensitive_Medical_Legal": {"temperature": 0.3, "reasoning_effort": "high", "verbosity": "low", "web": "required"},
    "ChitChat": {"temperature": 0.8, "reasoning_effort": "low", "verbosity": "high", "web": "optional"},
}

#load zero-shot classification model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

#function to map categories to LLM settings
def map_to_settings(categories):
    settings = {"temperature": 0.5, "reasoning_effort": "medium", "verbosity": "balanced", "web": "optional"}
    for category in categories:
        category_settings = CATEGORY_DEFAULTS.get(category, {})
        for key, value in category_settings.items():
            if key in settings:
                if key == "temperature":
                    settings[key] = (settings[key] + value) / 2
                else:
                    settings[key] = value
    return settings

@app.route('/classify', methods=['POST'])
def classify_prompt():
    try:
        prompt = request.json.get('prompt')

        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        candidate_labels = list(CATEGORY_DEFAULTS.keys())
        classification = classifier(prompt, candidate_labels)

        #filter categories with confidence greater than 0.5
        categories = [{"name": category, "confidence": confidence}
                      for category, confidence in zip(classification["labels"], classification["scores"]) if
                      confidence > 0.5]

        selected_categories = [category["name"] for category in categories]
        settings = map_to_settings(selected_categories)

        return jsonify({
            "categories": categories,
            "settings": settings
        })

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
