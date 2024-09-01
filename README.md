[![English](https://img.shields.io/badge/language-English-blue)](#ENGLISH) 
[![Español](https://img.shields.io/badge/idioma-Español-red)](#ESPAÑOL)
___

# ENGLISH

## Overview

This is a simple Python program that scrapes real estate listings from the Idealista website, the leading real estate ads platform in Spain. While Idealista offers a paid API service, this tool provides a free alternative for extracting similar data.

## Features

- **Scraping Functionality**: Extracts information such as title, price, image URL, features, and location from the Idealista listings.
- **Flask API**: Provides an endpoint to perform scraping operations via HTTP requests.
- **Database Integration**: (Commented out in this version) Option to save or update scraped data in a database using SQLAlchemy.
- **PDF Upload and Extraction**: Allows users to upload a "nota simple" in PDF format to extract property characteristics and automatically search for similar listings on Idealista.

## How It Works

### Scraping Process

1. **URL Request**: The scraper takes a URL from Idealista and sends an HTTP request using a custom user-agent to mimic a real browser.
2. **HTML Parsing**: The received HTML content is parsed using BeautifulSoup to extract relevant details from the listings.
3. **Data Extraction**: The scraper collects data such as the title, price, image URL, features, and location of each ad.
4. **API Response**: The scraped data is returned as a JSON response.

### PDF Upload and Extraction

1. **PDF Upload**: Users can upload a "nota simple" PDF file via the `/upload` endpoint.
2. **Text Extraction**: The uploaded PDF is processed to extract text content.
3. **Data Extraction**: Relevant property characteristics such as municipality and built area are extracted from the text.
4. **Idealista Search**: The extracted characteristics are used to construct a search URL for Idealista, and similar listings are scraped and returned as a JSON response.

### Flask API

- **Endpoint**: `/scrap`
- **Method**: `POST`
- **Input**: JSON object with a `url` key, which should contain the Idealista search URL.
- **Output**: JSON object with the scraped data or an error message if the scraping fails.
- **PDF Upload Endpoint**: `/upload`
  - **Method**: `POST`
  - **Input**: Form data with a `pdfFile` key, which should contain the "nota simple" PDF file.
  - **Output**: JSON object with the extracted property characteristics and similar listings from Idealista.
## Setup Instructions

### Prerequisites

- Python 3.x
- Required Python libraries: Flask, BeautifulSoup4, requests, SQLAlchemy (if using database functionality)

### Installation

1. **Clone the repository**:
   - git clone https://github.com/Aperezortega/idealista.git
   - cd idealista
   - pip install -r requirements.txt

### Code Structure

- **app.py**: The main Flask application file, contains the API endpoint.
- **main.py**: Contains the core scraping logic using BeautifulSoup
- **database.py**: Sets up the SQLAlchemy engine and session.
- **models.py**: Defines the database models for storing ads.
- **index.html**: root URL

### Customization:

- **Max Pages/Ads**: Variables to limit the number of ads/pages to scrape
- **Database Integration**: for the demo,  the database insertion code is commented, uncomment to enable database storage
___
### Disclaimer 
This tool is intended for educational purposes only. Please respect the terms of service of Idealista and avoid overloading their servers with too many requests.

___

# ESPAÑOL

## Descripción General

Este es un programa simple en Python que extrae listados de bienes raíces del sitio web Idealista, la plataforma líder de anuncios inmobiliarios en España. Aunque Idealista ofrece un servicio API de pago, esta herramienta proporciona una alternativa gratuita para extraer datos similares.

## Características

- **Funcionalidad de Scraping**: Extrae información como título, precio, URL de la imagen, características y ubicación de los listados de Idealista.
- **API de Flask**: Proporciona un endpoint para realizar operaciones de scraping a través de solicitudes HTTP.
- **Integración con Base de Datos**: (Comentado en esta versión) Opción para guardar o actualizar los datos extraídos en una base de datos usando SQLAlchemy.
- **Carga y Extracción de PDF**: Permite a los usuarios cargar una "nota simple" en formato PDF para extraer las características de la propiedad y buscar automáticamente listados similares en Idealista.

## Cómo Funciona

### Proceso de Scraping

1. **Solicitud de URL**: El scraper toma una URL de Idealista y envía una solicitud HTTP usando un user-agent personalizado para imitar un navegador real.
2. **Análisis HTML**: El contenido HTML recibido se analiza usando BeautifulSoup para extraer detalles relevantes de los listados.
3. **Extracción de Datos**: El scraper recopila datos como el título, precio, URL de la imagen, características y ubicación de cada anuncio.
4. **Respuesta de la API**: Los datos extraídos se devuelven como una respuesta JSON.

### Carga y Extracción de PDF

1. **Carga de PDF**: Los usuarios pueden cargar un archivo PDF de "nota simple" a través del endpoint `/upload`.
2. **Extracción de Texto**: El PDF cargado se procesa para extraer el contenido de texto.
3. **Extracción de Datos**: Se extraen características relevantes de la propiedad, como el municipio y el área construida, del texto.
4. **Búsqueda en Idealista**: Las características extraídas se utilizan para construir una URL de búsqueda para Idealista, y se extraen listados similares que se devuelven como una respuesta JSON.

### API de Flask

- **Endpoint**: `/scrap`
- **Método**: `POST`
- **Entrada**: Objeto JSON con una clave `url`, que debe contener la URL de búsqueda de Idealista.
- **Salida**: Objeto JSON con los datos extraídos o un mensaje de error si el scraping falla.
- **Endpoint de Carga de PDF**: `/upload`
  - **Método**: `POST`
  - **Entrada**: Datos de formulario con una clave `pdfFile`, que debe contener el archivo PDF de "nota simple".
  - **Salida**: Objeto JSON con las características de la propiedad extraídas y listados similares de Idealista.

## Instrucciones de Configuración

### Requisitos Previos

- Python 3.x
- Bibliotecas de Python requeridas: Flask, BeautifulSoup4, requests, SQLAlchemy (si se utiliza la funcionalidad de base de datos)

### Instalación

1. **Clonar el repositorio**:
   - git clone https://github.com/Aperezortega/idealista.git
   - cd idealista
   - pip install -r requirements.txt

### Estructura del Código

- **app.py**: El archivo principal de la aplicación Flask, contiene el endpoint de la API.
- **main.py**: Contiene la lógica principal de scraping usando BeautifulSoup.
- **database.py**: Configura el motor y la sesión de SQLAlchemy.
- **models.py**: Define los modelos de base de datos para almacenar anuncios.
- **index.html**: URL raíz.

### Personalización:

- **Máximo de Páginas/Anuncios**: Variables para limitar el número de anuncios/páginas a extraer.
- **Integración con Base de Datos**: Para la demostración, el código de inserción en la base de datos está comentado, descomentar para habilitar el almacenamiento en la base de datos.

___
### Disclaimer
Esta herramienta está destinada únicamente para fines educativos. Por favor, respete los términos de servicio de Idealista y evite sobrecargar sus servidores con demasiadas solicitudes.