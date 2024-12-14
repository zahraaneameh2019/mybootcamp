from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

# Sample data
sentiment_data = {
    "2024-09-23": {
        "negative": 52,
        "neutral": 1209,
        "positive": 39
    },
    "2024-10-01": {
        "negative": 28,
        "neutral": 651,
        "positive": 21
    },
    "2024-10-11": {
        "negative": 28,
        "neutral": 651,
        "positive": 21
    },
    "2024-10-16": {
        "negative": 32,
        "neutral": 744,
        "positive": 24
    }
}

positive_articles = [
    {"title": "Positive News 1", "date": "2024-10-16"},
    {"title": "Positive News 2", "date": "2024-10-15"},
]

negative_articles = [
    {"title": "Negative News 1", "date": "2024-10-14"},
    {"title": "Negative News 2", "date": "2024-10-13"},
]

@app.route('/')
def index():
    return send_from_directory('static', 'AnalysisDashboard.html')

@app.route('/sentiment_trends', methods=['GET'])
def get_sentiment_trends():
    return jsonify(sentiment_data)

@app.route('/most_positive_articles', methods=['GET'])
def get_most_positive_articles():
    return jsonify(positive_articles)

@app.route('/most_negative_articles', methods=['GET'])
def get_most_negative_articles():
    return jsonify(negative_articles)

@app.route('/articles_by_sentiment/<sentiment>', methods=['GET'])
def articles_by_sentiment(sentiment):
    if sentiment == 'positive':
        return jsonify(positive_articles)
    elif sentiment == 'negative':
        return jsonify(negative_articles)
    else:
        return jsonify({"error": "Invalid sentiment type"}), 400

if _name_ == '_main_':
    app.run(debug=True)