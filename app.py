from flask import Flask, request, jsonify, send_from_directory
from main import scrap_idealista
from pdf import extract_text_from_pdf, extract_information
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/nota.html')
def nota():
    return send_from_directory('.', 'nota.html')

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

@app.route('/upload', methods=['POST'])
def upload():
    if 'pdfFile' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['pdfFile']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and file.filename.endswith('.pdf'):
        try:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            
            
            text = extract_text_from_pdf(file_path)
            extracted_data = extract_information(text)
            print("Información extraída del PDF:")
            for key, value in extracted_data.items():
                print(f"{key}: {value}")
            
            
            municipio = extracted_data.get('municipio', 'No encontrado')
            superficie_construida = extracted_data.get('superficie_construida', '0')
            
           
            try:
                superficie_construida = superficie_construida.replace(' m2', '')
                if ',' in superficie_construida:
                    superficie_construida = float(superficie_construida.replace(',', '.'))
                else:
                    superficie_construida = float(superficie_construida)
                
               
                superficie_construida = round(superficie_construida)
                
                
                superficie_construida = round(superficie_construida / 20) * 20
                superficie_min = max(0, superficie_construida - 20)
                superficie_max = superficie_construida + 20
            except ValueError:
                print("Error al convertir la superficie construida a entero.")
                superficie_min = 0
                superficie_max = 0
            
            municipio_url = municipio.lower().replace(' ', '-')
            url = (f"https://www.idealista.com/venta-viviendas/{municipio_url}-balears-illes/"
                   f"con-metros-cuadrados-mas-de_{superficie_min},"
                   f"metros-cuadrados-menos-de_{superficie_max}/")
            print(f"URL de búsqueda en Idealista: {url}")
            scraped_data = scrap_idealista(url)
            response_data = {
                "municipio": municipio,
                "superficie_construida": superficie_construida,
                "extracted_data": extracted_data,
                "scraped_data": scraped_data
            }
            print("Response Data:", response_data)
            return jsonify(response_data), 200
        
        except Exception as e:
            return jsonify({"error": f"Failed to process file: {str(e)}"}), 500
    else:
        return jsonify({"error": "Invalid file type, only PDF is allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True)