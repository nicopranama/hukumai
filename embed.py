import utils as Utils
import os as OS
from tqdm import tqdm
import requests
import fitz
from chromadb.utils import embedding_functions
import chromadb

def pdf_to_text(url):
    try:
        response = requests.get(url)
        pdf_data = response.content
        document = fitz.open(stream=pdf_data, filetype="pdf")

        text = ""
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()
        return text
    except Exception as e:
        print(f"An error occured: {e}")
        return ""
    
def split_text_into_sections(text, min_chars_per_section):
    paragraphs = text.split('\n')
    sections = []
    current_section = ""
    current_length = 0

    for paragraph in paragraphs:
        paragraph_length = len(paragraph)

        if current_length + paragraph_length + 2 <= min_chars_per_section:
            current_length += paragraph + '\n\n'
            current_length += paragraph_length + 2
        else:
            if current_section:
                sections.append(current_section.strip())
            current_section = paragraph + '\n\n'
            current_length = paragraph_length + 2

    if current_section:
        sections.append(current_section.strip())
    
    return sections