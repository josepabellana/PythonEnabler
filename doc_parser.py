import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

import requests
from bs4 import BeautifulSoup

def scrape_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extracting all text from a webpage. Customize it as needed.
        text = ' '.join(p.text for p in soup.find_all('p'))
        return text
    else:
        return ""