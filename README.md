# 📚 PDF RAG Assistant

A Retrieval-Augmented Generation (RAG) application that lets you chat with any PDF document. Built with LangChain, Mistral AI, HuggingFace embeddings, and ChromaDB — with both a CLI interface and a Streamlit web UI.

Live here: https://pdf-rag-assistant.streamlit.app/

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
- 💾 Persistent vector store using ChromaDB
- 🖥️ Two ways to use: CLI or Streamlit web app
- 🎯 MMR (Maximal Marginal Relevance) retrieval for diverse, high-quality context

---

## 📁 Project Structure

```
pdf-rag-assistant/
├── document loaders/       # Place your PDF files here (for CLI usage)
├── app.py                  # Streamlit web UI
├── create_database.py      # Loads PDF, creates ChromaDB vector store
├── main.py                 # CLI chatbot
├── requirements.txt        # Python dependencies
├── runtime.txt             # Pins Python 3.11 for Streamlit Cloud
└── .gitignore
```

> `chroma_db/` and `venv/` are created locally and are git-ignored.

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
3. Add your `MISTRAL_API_KEY` under **App Settings → Secrets**
4. Deploy — the `runtime.txt` file pins **Python 3.11** automatically

> ⚠️ **Note:** Streamlit Cloud defaults to Python 3.14 which breaks ChromaDB's `protobuf` dependency. The included `runtime.txt` (set to `python-3.11`) fixes this — no code changes needed.

---

## 📝 Notes

- The HuggingFace embedding model (~90MB) downloads automatically on first run
- The `chroma_db/` folder is created locally and persists your vector store between sessions
- Embeddings are completely **free** via HuggingFace — no API key needed
- Only the Mistral AI key is required

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
