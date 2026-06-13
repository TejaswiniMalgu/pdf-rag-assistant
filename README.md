# 📚 PDF RAG Assistant

A Retrieval-Augmented Generation (RAG) application that lets you chat with any PDF document. Built with LangChain, Mistral AI, HuggingFace embeddings, and ChromaDB (local) / FAISS (cloud) — with both a CLI interface and a Streamlit web UI.

Live here : https://pdf-rag-assistant.streamlit.app/

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-🦜-green)
![Mistral AI](https://img.shields.io/badge/Mistral%20AI-mistral--small--2506-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)

---

## 🖼️ Output

![App Screenshot 1](https://github.com/user-attachments/assets/dfe0f0cf-c546-4a6e-afa8-caba04ced1d1)
![App Screenshot 2](https://github.com/user-attachments/assets/1369e6b6-27e0-4789-bc1a-aaf14f319925)

---

## ✨ Features

- 📄 Upload any PDF and ask questions from it
- 🔍 Semantic search using HuggingFace `all-MiniLM-L6-v2` embeddings (free, no API key needed)
- 🧠 Answers powered by Mistral AI (`mistral-small-2506`)
- 💾 ChromaDB locally / FAISS on Streamlit Cloud — controlled by one environment variable
- 🖥️ Two ways to use: CLI or Streamlit web app
- 🎯 MMR (Maximal Marginal Relevance) retrieval for diverse, high-quality context

---

## 📁 Project Structure

```
pdf-rag-assistant/
├── document loaders/       # Place your PDF files here (for CLI usage)
├── app.py                  # Streamlit web UI (auto-switches vector store)
├── create_database.py      # Loads PDF, creates ChromaDB vector store (CLI)
├── main.py                 # CLI chatbot
├── requirements.txt        # Python dependencies
├── runtime.txt             # Pins Python 3.11 for Streamlit Cloud
└── .gitignore
```

> `chroma_db/`, `faiss_index/` and `venv/` are created locally and are git-ignored.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11
- A [Mistral AI API key](https://console.mistral.ai/)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/TejaswiniMalgu/pdf-rag-assistant.git
cd pdf-rag-assistant

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
```

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

---

## 🖥️ Usage

### Option A — Streamlit Web UI *(Recommended)*

```bash
streamlit run app.py
```

1. Upload a PDF using the file uploader
2. Click **"Create Vector Database"**
3. Type your question and get answers instantly

---

### Option B — CLI

**Step 1:** Edit the file path in `create_database.py` to point to your PDF, then build the vector store:

```bash
python create_database.py
```

**Step 2:** Start the chatbot:

```bash
python main.py
```

- Type your questions at the prompt
- Enter `0` to exit

---

## ☁️ Deploying to Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Add the following under **App Settings → Secrets**:

```toml
MISTRAL_API_KEY = "your_mistral_api_key_here"
USE_FAISS = "true"
```

4. Deploy — done!

---

## 🔀 Dual Vector Store — ChromaDB vs FAISS

This app uses a single environment variable `USE_FAISS` to switch vector stores automatically:

| Environment | `USE_FAISS` | Vector Store | Persists |
|---|---|---|---|
| Local | not set / `false` | ChromaDB (`chroma_db/`) | ✅ Yes |
| Streamlit Cloud | `true` (set in Secrets) | FAISS (`faiss_index/`) | ✅ Yes |

> ChromaDB has a `protobuf`/`grpc` dependency conflict on Streamlit Cloud's shared environment. FAISS is used there instead — same retrieval quality, zero cloud headaches. Locally, ChromaDB works perfectly and persists between sessions.

---

## 📝 Notes

- The HuggingFace embedding model (~90MB) downloads automatically on first run
- Embeddings are completely **free** via HuggingFace — no API key needed
- Only the Mistral AI key is required
- `chroma_db/` (local) and `faiss_index/` (cloud) both persist your vector store between sessions

---

## 🔮 Future Improvements

- [ ] Support for multiple PDF uploads
- [ ] Chat history and memory
- [ ] Source highlighting (show which page the answer came from)
- [ ] Docker support

---

## 🤝 Acknowledgements

- [LangChain](https://www.langchain.com/)
- [Mistral AI](https://mistral.ai/)
- [HuggingFace Sentence Transformers](https://huggingface.co/sentence-transformers)
- [ChromaDB](https://www.trychroma.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
