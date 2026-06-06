from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain
from dotenv import load_dotenv
import streamlit as st
import tempfile



load_dotenv()

st.title("Edu Buddy")
st.write("Upload notes & ask a question")

upload_notes = st.file_uploader(
    "Upload notes",
    type = ["pdf"]
)
if upload_notes:
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp_file:
        tmp_file.write(upload_notes.read())
        pdf_path = tmp_file.name

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Store vectors
    db = FAISS.from_documents(chunks, embeddings)

    # LLM
    llm = ChatGroq(
        model="llama-3.1-8b-instant"
    )

    # Prompt
    prompt = ChatPromptTemplate.from_template("""
    Answer the question in detail based only on the provided context.

    Context:
    {context}

    Question:
    {input}
    """)

    # Create chains
    document_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    retrieval_chain = create_retrieval_chain(
        db.as_retriever(),
        document_chain
    )

# st.success("PDF processed successfully!")

    # Question Input
question = st.text_input(
        "Ask a Question:"
    )

if st.button("Get Answer"):

    if question:

        with st.spinner("Generating answer..."):

            response = retrieval_chain.invoke(
                {"input": question}
            )

        st.subheader("Answer")
        st.write(response["answer"])

    else:
        st.warning("Please enter a question.")
