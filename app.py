import streamlit as st
from dotenv import load_dotenv
import tempfile
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Set USE_FAISS=true in Streamlit Cloud secrets, leave unset for local
USE_FAISS = os.environ.get("USE_FAISS", "false").lower() == "true"

if USE_FAISS:
    from langchain_community.vectorstores import FAISS
else:
    from langchain_community.vectorstores import Chroma

st.set_page_config(page_title="RAG Assistant")
st.title("📚 RAG Assistant")
st.write("Upload a PDF and ask questions from the document")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    st.success("PDF uploaded successfully!")

    if st.button("Create Vector Database"):
        with st.spinner("Processing document... (first run downloads the model, may take a minute)"):

            loader = PyPDFLoader(file_path)
            docs = loader.load()

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            chunks = splitter.split_documents(docs)

            embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

            if USE_FAISS:
                vectorstore = FAISS.from_documents(chunks, embeddings)
                vectorstore.save_local("faiss_index")
            else:
                vectorstore = Chroma.from_documents(
                    documents=chunks,
                    embedding=embeddings,
                    persist_directory="chroma_db"
                )

        st.success("Vector database created!")

STORE_EXISTS = (
    os.path.exists("faiss_index") if USE_FAISS else os.path.exists("chroma_db")
)

if STORE_EXISTS:
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    if USE_FAISS:
        vectorstore = FAISS.load_local(
            "faiss_index",
            embeddings,
            allow_dangerous_deserialization=True
        )
    else:
        vectorstore = Chroma(
            persist_directory="chroma_db",
            embedding_function=embeddings
        )

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4, "fetch_k": 10, "lambda_mult": 0.5}
    )

    llm = ChatMistralAI(model="mistral-small-2506")

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
        ),
        (
            "human",
            """Context:
{context}

Question:
{question}
"""
        )
    ])

    st.divider()
    st.subheader("Ask Questions From the Book")

    query = st.text_input("Enter your question")

    if query:
        docs = retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in docs])
        final_prompt = prompt.invoke({"context": context, "question": query})
        response = llm.invoke(final_prompt)

        st.write("### AI Answer")
        st.write(response.content)