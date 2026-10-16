from urllib.parse import urlsplit

def normalize_url(url: str) -> str:
   parsed_url = urlsplit(url)
   normal_path = f"{parsed_url.netloc}{parsed_url.path}"
   normal_path = normal_path.rstrip("/")
   return normal_path.lower()


