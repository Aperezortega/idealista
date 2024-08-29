import pdfplumber
import re
import json

def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text

def extract_information(text):
    # Definir patrones de regex para extraer la información necesaria
    patterns = {
        'municipio': r'Municipio:\s*(.*?)\s*Finca',
        'calle': r'Vía Publica:\s*(.*)',
        'numero': r'Número:\s*(.*)',
        'codigo_postal': r'Código Postal:\s*(.*)',
        'superficie_construida': r'Superficie Construida:\s*(.*)',
        'superficie_terreno': r'Superficie del terreno:\s*(.*)',
    }

    extracted_data = {}
    for key, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            extracted_data[key] = matches if key == 'caracteristicas' else matches[0].strip()

    return extracted_data

def extract_information_from_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    extracted_data = extract_information(text)
    return json.dumps(extracted_data, ensure_ascii=False, indent=4)

# Ejemplo de uso
pdf_path = 'nota.pdf'
json_data = extract_information_from_pdf(pdf_path)
print(json_data)