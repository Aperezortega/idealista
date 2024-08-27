import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from models import Ad

BASE_URL = 'https://www.idealista.com'


Base.metadata.create_all(bind=engine)

def fetch_page_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://www.google.com/'
    }
    
 
    session = requests.Session()
    session.headers.update(headers)
    
 
    print(f"Realizando solicitud HTTP a la URL: {url}")
    response = session.get(url)
    

    if response.status_code != 200:
        print(f"Error: No se pudo obtener la página. Código de estado: {response.status_code}")
        return None
    print("Solicitud HTTP exitosa.")
    
    return response.content

def fetch_ad_details(url):
    page_content = fetch_page_content(url)
    if not page_content:
        return None

    soup = BeautifulSoup(page_content, 'html.parser')
    
    picture = soup.find('picture')
    img_url = picture.find('img')['src'] if picture and picture.find('img') else "N/A"
    features = soup.find('div', class_='details-property-feature-one')
    features_list = [li.get_text(strip=True) for li in features.find_all('li')] if features else []
    features_text = " | ".join(features_list) if features_list else "N/A"
    header_map = soup.find('div', id='headerMap')
    location_list = [li.get_text(strip=True) for li in header_map.find_all('li')] if header_map else []
    location_text = " | ".join(location_list) if location_list else "N/A"
    
    return {
        'img_url': img_url,
        'features': features_text,
        'location': location_text
    }

def scrape_idealista():
    base_url = 'https://www.idealista.com/venta-viviendas/malaga-malaga/con-precio-hasta_100000,precio-desde_80000'
    query_params = '?ordenado-por=fecha-publicacion-desc'
    
    count = 0
    max_pages = 5

    session = SessionLocal()

    for page in range(1, max_pages + 1):
        if page == 1:
            url = f"{base_url}{query_params}"
        else:
            url = f"{base_url}/pagina-{page}.htm{query_params}"

      
        page_content = fetch_page_content(url)
        if not page_content:
            continue
        
        print(f"Parseando el contenido HTML de la página {page}...")
        soup = BeautifulSoup(page_content, 'html.parser')
        
        print("Buscando anuncios...")
        ads = soup.find_all('div', class_='item-info-container')
        if not ads:
            print(f"No se encontraron anuncios en la página {page}.")
            continue
        print(f"Se encontraron {len(ads)} anuncios en la página {page}.")
        
        for ad in ads:
            title = ad.find('a', class_='item-link')
            href = BASE_URL + ad.find('a', class_='item-link')['href']
            price = ad.find('span', class_='item-price')
            title_text = title.get_text(strip=True) if title else "N/A"
            price_text = price.get_text(strip=True) if price else "N/A"

            ad_details = fetch_ad_details(href)
            if ad_details:
                img_url = ad_details['img_url']
                features_text = ad_details['features']
                location_text = ad_details['location']
            else:
                img_url = "N/A"
                features_text = "N/A"
                location_text = "N/A"

            print(f"Anuncio {count + 1}:")
            print(f"Título: {title_text}")
            print(f"Enlace: {href}")
            print(f"Precio: {price_text}")
            print(f"URL de la imagen: {img_url}")
            print(f"Características: {features_text}")
            print(f"Ubicación: {location_text}\n")

            try:
                existing_ad = session.query(Ad).filter_by(href=href).one()
                print(f"El anuncio con href {href} ya existe en la base de datos.")
            except NoResultFound:
                ad_record = Ad(
                    title=title_text,
                    href=href,
                    price=price_text,
                    img_url=img_url,
                    features=features_text,
                    location=location_text
                )
                session.add(ad_record)
                session.commit()

            count += 1

    session.close()

scrape_idealista()