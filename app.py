from flask import Flask, request, jsonify
from main import scrap_idealista

app = Flask(__name__)

@app.route('/scrap', methods=['GET'])
def scrap():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    try:
        scrap_idealista(url)
        return jsonify({"message": "Scraping completed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)