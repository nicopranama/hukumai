## English Version

### Project Overview

This project is an AI-powered legal assistant for SMEs (Small and Medium Enterprises) in Indonesia.
It combines:

* Retrieval-Augmented Generation (RAG)
* ChromaDB as a vector database
* OpenAI Embeddings (`text-embedding-3-small`)
* LangChain Agent for orchestrating the query-answering pipeline

With this setup, the assistant can process Indonesian legal documents (e.g., Law No.20/2008 on SMEs) and answer user questions in natural language.

---

### Features

* Chat memory support: the system can remember previous conversations during a session, making the dialogue more natural.
* Document extensibility: you can add new legal documents, and the assistant will automatically include them in future answers.
* Context-aware responses: answers are always based on the retrieved legal text, not just generic AI output.
* Flexible question handling: even if the user’s question is unclear, the LangChain Agent can reformulate it.
* Interactive interface: simple and easy-to-use front end powered by Streamlit.
* SME-oriented: designed to answer practical legal questions specifically for small and medium enterprises in Indonesia.

---

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nicopranama/umkm-legal-assistant.git
   cd umkm-legal-assistant
   ```
2. Create and activate virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Create `.env` file and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

---

### How to Run

Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

### Program Flow

```
User Question
     │
     ▼
LangChain Agent
     │
     ├─► Reformulate Question (if unclear)
     ├─► Query ChromaDB → Retrieve Relevant Documents
     ├─► Combine Context + Question
     ├─► LLM Generates Answer
     ▼
Answer Returned to User
```

* Input: Natural language question from user
* Process:

  1. LangChain Agent receives question
  2. Searches embeddings in ChromaDB
  3. Collects top relevant document chunks
  4. Sends combined context + question to LLM
  5. LLM generates context-aware answer
* Output: Short, accurate legal answer

---

### Example Question

```
Are SMEs with annual revenue below 500 million IDR required to pay income tax?
```

---

## Versi Bahasa Indonesia

### Gambaran Proyek

Proyek ini adalah Asisten Hukum berbasis AI untuk UMKM di Indonesia.
Menggunakan kombinasi:

* Retrieval-Augmented Generation (RAG)
* ChromaDB sebagai vector database
* OpenAI Embeddings (`text-embedding-3-small`)
* LangChain Agent untuk mengatur alur query dan jawaban

Dengan setup ini, asisten dapat memproses dokumen hukum Indonesia (misalnya UU No.20/2008 tentang UMKM) dan menjawab pertanyaan pengguna dengan bahasa alami.

---

### Fitur

* Ekstraksi dan pemotongan teks dari dokumen PDF hukum
* Membuat embedding dengan OpenAI
* Menyimpan dan query embedding dengan ChromaDB
* LangChain Agent mengatur alur kerja:

  * Reformulasi pertanyaan (jika perlu)
  * Query ChromaDB untuk konteks relevan
  * Gabungkan konteks + pertanyaan ke LLM
  * Mengembalikan jawaban singkat ke pengguna
* Antarmuka dengan Streamlit

---

### Instalasi

1. Clone repositori:

   ```bash
   git clone https://github.com/nicopranama/umkm-legal-assistant.git
   cd umkm-legal-assistant
   ```
2. Buat dan aktifkan virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```
3. Install dependensi:

   ```bash
   pip install -r requirements.txt
   ```
4. Buat file `.env` dan tambahkan API key OpenAI:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

---

### Cara Menjalankan

Jalankan aplikasi Streamlit:

   ```bash
   streamlit run app.py
   ```

---

### Flow Program

```
Pertanyaan User
     │
     ▼
LangChain Agent
     │
     ├─► Reformulasi Pertanyaan (jika kurang jelas)
     ├─► Query ke ChromaDB → Ambil Dokumen Relevan
     ├─► Gabungkan Konteks + Pertanyaan
     ├─► LLM Membuat Jawaban
     ▼
Jawaban Diterima User
```

* Input: Pertanyaan hukum dari pengguna
* Proses:

  1. Pertanyaan diterima oleh LangChain Agent
  2. Cari embedding relevan di ChromaDB
  3. Ambil potongan dokumen yang sesuai
  4. Kirim pertanyaan + konteks ke LLM
  5. LLM menghasilkan jawaban berbasis dokumen
* Output: Jawaban hukum singkat dan akurat

---

### Contoh Pertanyaan

```
Apakah UMKM dengan omzet di bawah 500 juta per tahun wajib membayar pajak penghasilan?
```

---
