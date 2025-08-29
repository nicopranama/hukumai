import utils as Utils
import os as OS
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_core.chat_history import BaseChatMessageHistory

class NewsChat:
    store = {}
    session_id = ''
    rag_chain = None

    def __init__(self, article_id: str):
        load_dotenv()
        open_api_key = OS.getenv("OPENAI_API_KEY")
        embeddings = OpenAIEmbeddings(openai_api_key=open_api_key)
        self.session_id = article_id

        llm = ChatOpenAI(openai_api_key=open_api_key, model='gpt-4o')
        db = Chroma(persisy_directory=Utils.DB_FOLDER, embedding_function=embeddings, collection_name='collection_1')
        retriever = db.as_retriever()

        

