import json as JSON
import os as OS

ARTICLES_FILE = 'articles.json'
ARTICLES_FOLDER = 'articles'
DB_FOLDER = 'chroma_storage'
DATA_FOLDER = 'data'
INDONESIA_ACT_URL = 'https://ojk.go.id/waspada-investasi/id/regulasi/Documents/UU_20_Tahun_2008_Usaha_Mikro_Kecil_dan_Menengah.pdf'

# load articles data from file_name (.json)
def load_articles(file_name) -> list:
    result = []
    if OS.path.exists(file_name):
        with open(file_name, 'r') as file:
            try:
                result = JSON.load(file)
            except JSON.JSONDecodeError:
                print("File exist but is not valid JSON. Returning empty object")
    else:
        with open(file_name, 'w') as file:
            JSON.dump('[{}]', file)
        print(f"File '{file_name}' did not exist and was created.")
        OS.mkdir('articles')
        print("'articles' directory was created")

    return result

# save articles data to file_name (.json)
def save_articles(file_name, data):
    try:
        with open(file_name, 'w') as file:
            JSON.dump(data, file, indent=4)
            print(f"Data succesfully saved to '{file_name}'.")
    except Exception as e:
        print(f"Error: trying to save articles data [{e}]")

# save articles content to individual files
def save_article_content(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
    except IOError as e:
        print(f"An IOError occurred: {e.strerror}")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"Content succesfully written to '{file_name}'.")

# load article body text from file
def load_article_content(file_name):
    result = ''
    try:
        with open(file_name, 'r') as file:
            result = file.read()
    except Exception as e:
        print(f"An unexpected error occured while reading content file '{file_name}': {e}")
        
    return result