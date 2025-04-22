from flask import Flask, request, jsonify
from flask_cors import CORS
from collections import Counter
import re

app = Flask(__name__)
CORS(app)  # ✅ разрешить все источники

@app.route('/count', methods=['POST'])
def count_words():
    text = request.json.get("text", "")
    
    # Удаляем все знаки пунктуации и лишние символы
    cleaned_text = re.sub(r'[^\w\s]', '', text)  

    words = cleaned_text.lower().split()  
    freq = Counter(words)
    return jsonify(freq)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)