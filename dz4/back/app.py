from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from collections import Counter
import re

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "OPTIONS"], "allow_headers": "*"}})
CORS(app, supports_credentials=True)

@app.route('/count', methods=['POST', 'OPTIONS'])
def count_words():
    if request.method == 'OPTIONS':
        # Ответ на preflight-запрос
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        return response

    text = request.json.get("text", "")
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    words = cleaned_text.lower().split()
    freq = Counter(words)
    return jsonify(freq)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)