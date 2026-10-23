from urllib.parse import urlsplit
from bs4 import BeautifulSoup, Tag

def normalize_url(url: str) -> str:
   parsed_url = urlsplit(url)
   normal_path = f"{parsed_url.netloc}{parsed_url.path}"
   normal_path = normal_path.rstrip("/")
   return normal_path.lower()

def get_heading_from_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    h_tag = None

    if not soup.h1:
        h_tag = soup.h2
    else:
        h_tag = soup.h1
        
    return h_tag.get_text(strip=True) if isinstance(h_tag, Tag) else ""

def get_first_paragraph_from_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    p_tag = ""

    if not soup.find("main"):
        p_tag = soup.p
    else: 
        p_tag = soup.find("main").find("p").text

    return p_tag


