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

if __name__ == '__main__':
    pdf_path = 'nota.pdf'
    text = extract_text_from_pdf(pdf_path)
    extracted_data = extract_information(text)
    print(json.dumps(extracted_data, indent=4))
