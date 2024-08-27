from flask import Flask, request, jsonify, send_from_directory
from main import scrap_idealista

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/scrap', methods=['POST'])
def scrap():
    url = request.json.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    try:
        scraped_data = scrap_idealista(url)
        return jsonify(scraped_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)