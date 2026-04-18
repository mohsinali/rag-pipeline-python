# 🧠 RAG Pipeline in Python (Chunking + Embedding + Qdrant)

A production-style implementation of a **Retrieval-Augmented Generation (RAG) pipeline** using Python.
This project demonstrates how to process raw text, split it into meaningful chunks, generate embeddings, and store them in a vector database for semantic search.

---

## 🚀 Features

* ✂️ Multiple chunking strategies

  * Paragraph-based
  * Sentence-based
  * Fixed-size with overlap
* 🔢 Embedding generation using OpenAI
* 🧱 Vector storage using Qdrant
* 🔍 Semantic search capability
* ⚙️ Clean, modular, production-ready structure

---

## 🏗️ Architecture

```
Raw Text
   ↓
Chunking
   ↓
Embedding (OpenAI)
   ↓
Vector Database (Qdrant)
   ↓
Semantic Search
```

---

## 📁 Project Structure

```
rag_pipeline/
│── config.py
│── chunker.py
│── embedder.py
│── vector_store.py
│── pipeline.py
│── data/
│    └── sample.txt
```

---

## ⚙️ Setup

### 1. Clone the repository

```
git clone https://github.com/<your-username>/rag-pipeline-python.git
cd rag-pipeline-python
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
```

---

## ▶️ Running the Pipeline

```
python pipeline.py
```

This will:

1. Load text from `data/sample.txt`
2. Split into chunks
3. Generate embeddings
4. Store vectors in Qdrant

---

## 🔍 Running a Search Query

You can add a simple query function:

```
search("How does the system detect suspicious activity?")
```

---

## 🧠 Key Concepts

### Chunking

Splitting large text into smaller pieces improves retrieval accuracy and context relevance.

### Overlap

Chunks overlap slightly to preserve context across boundaries.

### Embeddings

Text is converted into high-dimensional vectors for semantic similarity search.

### Vector Database

Qdrant stores embeddings and enables fast nearest-neighbor search.

---

## 🧪 Example Use Cases

* Semantic search
* Question answering systems
* AI chatbots with memory
* Document retrieval systems

---

## 🔮 Future Improvements

* Hybrid search (keyword + vector)
* Reranking layer
* LLM-based answer generation
* Streaming ingestion pipeline
* Metadata filtering

---

## 🛠️ Tech Stack

* Python
* OpenAI Embeddings API
* Qdrant Vector Database

---

## 📌 Notes

* `recreate_collection()` is used for development (resets data).
* For production, switch to `create_collection()` and persistent storage.
* Batch embedding is recommended for large datasets.

---

## 🤝 Contributing

Feel free to fork this repository and experiment with:

* Different chunking strategies
* Alternative embedding models
* Other vector databases

---

## 📄 License

MIT License

---

## ⭐ Acknowledgment

This project is part of a hands-on journey to understand **RAG systems** and modern AI application architecture.
