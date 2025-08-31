import streamlit as ST
import agent as Agent
import utils as Utils
import embed
import os as OS

def create_chat(id: str):
    chat = ST.container()

    # Initialize chat history
    if "messages" not in ST.session_state:
        ST.session_state.messages = []

    for message in ST.session_state.messages:
        if message["id"] == id:
            chat.chat_message(message['role']).write(message['content'])
    
    ST.session_state.newschat = Agent.NewsChat(id)

    if prompt := ST.chat_input(placeholder = "Tanyakan saya tentang regulasi UMKM di Indonesia", key = id):
        chat.chat_message("user").write(prompt)
        with ST.spinner("Mencari jawaban..."):
            assistant_response = ST.session_state.newschat.ask(prompt)
            chat.chat_message("assistant").write(f"{assistant_response}")

            ST.session_state.messages.append({"id": id, "role": "user", "content": prompt})
            ST.session_state.messages.append({"id": id, "role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    if not OS.path.exists(Utils.DB_FOLDER):
        document_name = "UU No.20 Tahun 2008 - UMKM"
        document_description = "Undang-Undang tentang Usaha Mikro, Kecil, dan Menengah di Indonesia"
        text = embed.pdf_to_text(Utils.INDONESIA_ACT_URL)
        embed.embed_text_in_chromadb(text, document_name, document_description)
    
    create_chat("chat1")