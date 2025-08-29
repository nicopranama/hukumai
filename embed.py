import utils as Utils
import os as OS
from tqdm import tqdm
import requests
import fitz
from chromadb.utils import embedding_functions
import chromadb
from dotenv import load_dotenv

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

def embed_text_in_chromadb(text, document_name, document_description, persist_directory=Utils.DB_FOLDER):
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
        load_dotenv(),
        api_key = OS.getenv("OPENAI_API_KEY"),
        model_name = "text-embedding-ada-002"
    )
    documents = split_text_into_sections(text, 1000)

    ids = [str(hash(d)) for d in documents]

    metadata = {
        "name": document_name,
        "description": document_description
    }
    metadatas = [metadata] * len(documents)

    client = chromadb.PersistentClient(path=persist_directory)
    collection_name = 'collection_1'
    collection = client.get_or_create_collection(name=collection_name, embedding_function=openai_ef)

    count = collection.count()
    print(f"Collection already contains {count} documents")
    ids = [str(i) for i in range(count, count + len(documents))]

    for i in tqdm(
        range(0, len(documents), 100), desc="Adding documents", unit_scale=100
    ):
        collection.add(
            ids=ids[i:i+100],
            documents=documents[i:i+100],
            metadatas=metadatas[i:i+100]
        )
    
    new_count = collection.count()
    print(f"Added {new_count - count} documents")

if __name__ == "__main__":
    document_name = "UU No.20 Tahun 2008 - UMKM"
    document_description = "Undang-Undang tentang Usaha Mikro, Kecil, dan Menengah di Indonesia"
    text = pdf_to_text(Utils.INDONESIA_ACT_URL)
    embed_text_in_chromadb(text, document_name, document_description)
