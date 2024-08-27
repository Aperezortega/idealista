import requests
from bs4 import BeautifulSoup
BASE_URL = 'https://www.idealista.com'

def fetch_page_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://www.google.com/'
    }
    
    # Usar una sesión de requests
    session = requests.Session()
    session.headers.update(headers)
    
    # Realizar la solicitud HTTP a la URL
    print(f"Realizando solicitud HTTP a la URL: {url}")
    response = session.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code != 200:
        print(f"Error: No se pudo obtener la página. Código de estado: {response.status_code}")
        return None
    print("Solicitud HTTP exitosa.")
    
    return response.content

def get_max_pages(soup):
    # Buscar el contenedor de paginación
    pagination = soup.find('div', class_='pagination')
    if not pagination:
        print("No se encontró el contenedor de paginación.")
        return 1  # Si no se encuentra el contenedor de paginación, asumir que solo hay una página
    
    # Buscar todos los elementos 'li' dentro del contenedor de paginación
    pages = pagination.find_all('li')
    if not pages:
        print("No se encontraron elementos de página.")
        return 1  # Si no se encuentran elementos de página, asumir que solo hay una página
    
    # Extraer los números de página de los enlaces
    page_numbers = []
    for page in pages:
        link = page.find('a')
        if link and link.get_text().isdigit():
            page_numbers.append(int(link.get_text()))
    
    if not page_numbers:
        print("No se encontraron números de página.")
        return 1  # Si no se encuentran números de página, asumir que solo hay una página
    
    max_page = max(page_numbers)
    print(f"Número máximo de páginas encontrado: {max_page}")
    return max_page

def scrape_idealista():
    base_url = 'https://www.idealista.com/venta-viviendas/malaga-malaga/con-precio-hasta_100000,precio-desde_80000'
    query_params = '?ordenado-por=fecha-publicacion-desc'
    url = f"{base_url}{query_params}"
    # Obtener el contenido de la primera página
    page_content = fetch_page_content(url)
    if not page_content:
        return
    
    # Parsear el contenido HTML de la primera página
    print("Parseando el contenido HTML de la primera página...")
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Obtener el número máximo de páginas
    max_pages = get_max_pages(soup)
    print(f"Número máximo de páginas: {max_pages}")
    
    count = 0

    for page in range(1, max_pages + 1):
        if page == 1:
            url = f"{base_url}{query_params}"
        else:
            url = f"{base_url}/pagina-{page}.htm{query_params}"
        
        # Obtener el contenido de la página actual
        page_content = fetch_page_content(url)
        if not page_content:
            continue
        
        # Parsear el contenido HTML
        print(f"Parseando el contenido HTML de la página {page}...")
        soup = BeautifulSoup(page_content, 'html.parser')
        
        # Buscar los anuncios
        print("Buscando anuncios...")
        ads = soup.find_all('div', class_='item-info-container')
        
        # Verificar si se encontraron anuncios
        if not ads:
            print(f"No se encontraron anuncios en la página {page}.")
            continue
        print(f"Se encontraron {len(ads)} anuncios en la página {page}.")
        
        for ad in ads:
            title = ad.find('a', class_='item-link')
            href = BASE_URL + ad.find('a', class_='item-link')['href']
            price = ad.find('span', class_='item-price')
            
            # Verificar si los elementos existen antes de obtener el texto
            title_text = title.get_text(strip=True) if title else "N/A"
            price_text = price.get_text(strip=True) if price else "N/A"
            details = fetch_ad_details(href)
            
            print(f"Anuncio {count + 1}:")
            print(f"Título: {title_text}")
            print(f"Enlace: {href}")
            print(f"Precio: {price_text}")
            print(f"Imagen: {details['img_url']}")
            print(f"Características: {details['features']}")
            print(f"Ubicación: {details['location']}")
            count += 1
            
def fetch_ad_details(url):
    # Convertir la URL relativa en una URL absoluta
    
    # Obtener el contenido de la página del anuncio
    page_content = fetch_page_content(url)
    if not page_content:
        return None

    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Extraer la URL de la imagen
    picture = soup.find('picture')
    img_url = picture.find('img')['src'] if picture and picture.find('img') else "N/A"
    
    # Extraer las características
    features = soup.find('div', class_='details-property-feature-one')
    features_list = [li.get_text(strip=True) for li in features.find_all('li')] if features else []
    features_text = " | ".join(features_list) if features_list else "N/A"
    
    # Extraer la ubicación
    header_map = soup.find('div', id='headerMap')
    location_list = [li.get_text(strip=True) for li in header_map.find_all('li')] if header_map else []
    location_text = " | ".join(location_list) if location_list else "N/A"
    
    return {
        'img_url': img_url,
        'features': features_text,
        'location': location_text
    }
    
# Ejecutar la función
scrape_idealista()