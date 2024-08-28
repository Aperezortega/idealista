# Idealista Scraper

## Overview

This is a simple Python program that scrapes real estate listings from the Idealista website, the leading real estate ads platform in Spain. While Idealista offers a paid API service, this tool provides a free alternative for extracting similar data.

## Features

- **Scraping Functionality**: Extracts information such as title, price, image URL, features, and location from the Idealista listings.
- **Flask API**: Provides an endpoint to perform scraping operations via HTTP requests.
- **Database Integration**: (Commented out in this version) Option to save or update scraped data in a database using SQLAlchemy.

## How It Works

### Scraping Process

1. **URL Request**: The scraper takes a URL from Idealista and sends an HTTP request using a custom user-agent to mimic a real browser.
2. **HTML Parsing**: The received HTML content is parsed using BeautifulSoup to extract relevant details from the listings.
3. **Data Extraction**: The scraper collects data such as the title, price, image URL, features, and location of each ad.
4. **API Response**: The scraped data is returned as a JSON response.

### Flask API

- **Endpoint**: `/scrap`
- **Method**: `POST`
- **Input**: JSON object with a `url` key, which should contain the Idealista search URL.
- **Output**: JSON object with the scraped data or an error message if the scraping fails.

## Setup Instructions

### Prerequisites

- Python 3.x
- Required Python libraries: Flask, BeautifulSoup4, requests, SQLAlchemy (if using database functionality)

### Installation

1. **Clone the repository**:
   git clone https://github.com/yourusername/idealista-scraper.git
   cd idealista-scraper
   pip install -r requirements.txt

### Code Structure

- **app.py**: The main Flask application file, contains the API endpoint.
- **main.py**: Contains the core scraping logic using BeautifulSoup
- **database.py**: Sets up the SQLAlchemy engine and session.
- **models.py**: Defines the database models for storing ads.
- **index.html**: root URL

### Customization:

- **Max Pages/Ads**: Variables to limit the number of ads/pages to scrape
- **Database Integration**: for the demo,  the database insertion code is commented, uncomment to enable database storage

### Disclaimer 
This tool is intended for educational purposes only. Please respect the terms of service of Idealista and avoid overloading their servers with too many requests.

