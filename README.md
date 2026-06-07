📚 PDF RAG Assistant
A Retrieval-Augmented Generation (RAG) application that lets you chat with any PDF document. Built with LangChain, Mistral AI, HuggingFace embeddings, and ChromaDB — with both a CLI interface and a Streamlit web UI.

✨ Features

📄 Upload any PDF and ask questions from it
🔍 Semantic search using HuggingFace all-MiniLM-L6-v2 embeddings (free, no API key needed)
🧠 Answers powered by Mistral AI (mistral-small-2506)
💾 Persistent vector store using ChromaDB
🖥️ Two ways to use: CLI or Streamlit web app
🎯 MMR (Maximal Marginal Relevance) retrieval for diverse, high-quality context


🖥️ Usage
Option A — Streamlit Web UI (Recommended)
bashstreamlit run app.py

Upload a PDF using the file uploader
Click "Create Vector Database"
Type your question and get answers instantly


Option B — CLI
Step 1: Build the vector database from your PDF:
bashpython create_database.py

Edit the file path inside create_database.py to point to your PDF.

Step 2: Start the chatbot:
bashpython main.py

Type your questions at the prompt
Enter 0 to exit


📝 Notes

The HuggingFace embedding model (~90MB) downloads automatically on first run
The chroma_db/ folder is created locally and persists your vector store between sessions
embeddings are fully free via HuggingFace


🔮 Future Improvements

 Support for multiple PDF uploads
 Chat history and memory
 Source highlighting (show which page the answer came from)
 Docker support


🤝 Acknowledgements

LangChain
Mistral AI
HuggingFace Sentence Transformers
ChromaDB

output:
<img width="1901" height="852" alt="Screenshot 2026-06-07 205158" src="https://github.com/user-attachments/assets/dfe0f0cf-c546-4a6e-afa8-caba04ced1d1" />
<img width="1897" height="702" alt="Screenshot 2026-06-07 205224" src="https://github.com/user-attachments/assets/1369e6b6-27e0-4789-bc1a-aaf14f319925" />

