# EduBuddy
# Edu Buddy - PDF Question Answering Chatbot

## Overview

Edu Buddy is an AI-powered PDF Question Answering application built using Streamlit, LangChain, Groq LLM, Hugging Face Embeddings, and FAISS Vector Database.

The application allows users to upload PDF notes and ask questions related to the uploaded content. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from the document and generate accurate answers based on the document context.

---

## Features

* Upload PDF notes
* Extract and process PDF content
* Split documents into manageable chunks
* Generate embeddings using Hugging Face models
* Store embeddings in FAISS Vector Database
* Retrieve relevant context for user queries
* Generate answers using Groq's Llama 3.1 model
* Simple and interactive Streamlit interface

---

## Tech Stack

* Python
* Streamlit
* LangChain
* Groq API
* Hugging Face Embeddings
* FAISS
* PyPDF
* Sentence Transformers

---

## Project Workflow

1. User uploads a PDF document.
2. PDF content is extracted using PyPDFLoader.
3. Text is split into smaller chunks using RecursiveCharacterTextSplitter.
4. Hugging Face Embeddings convert text chunks into vector representations.
5. FAISS stores the vectors for efficient similarity search.
6. User asks a question.
7. Relevant document chunks are retrieved from FAISS.
8. Retrieved context and user question are sent to the Groq LLM.
9. The generated answer is displayed in the Streamlit application.

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd Edu-Buddy
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from Groq.

---

## Run the Application

```bash
streamlit run app.py
```

---

## Example Usage

1. Upload your PDF notes.
2. Enter a question such as:

```
What is software testing?
```

3. Click **Get Answer**.
4. Receive an answer generated from the uploaded document.

---

## Folder Structure

```text
Edu-Buddy/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── uploaded_pdfs/
```

---

## Future Enhancements

* Chat history support
* Multiple PDF uploads
* PDF summarization
* Topic-wise question generation
* Voice-based interaction
* Export answers to PDF
* Advanced retrieval techniques

## Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embedding Models
* Large Language Models (LLMs)
* Semantic Search
* Streamlit Application Development
* LangChain Framework

## Author -: Tanish Bhatia

Aspiring AI/ML Engineer | Python Developer | Generative AI Enthusiast
