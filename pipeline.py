from chunker import Chunker
from embedder import Embedder
from vector_store import VectorStore
from openai import OpenAI

def load_text(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()

def run_pipeline():
    text = load_text("data/sample.txt")

    # Step 1: Chunking
    chunker = Chunker(chunk_size=200, overlap=40)

    # Try different strategies
    chunks = chunker.chunk_fixed(text)
    # chunks = chunker.chunk_by_paragraph(text)

#     print(f"Total chunks: {len(chunks)}")

    # Step 2: Embedding
    embedder = Embedder()
    embeddings = embedder.embed(chunks)

    # Step 3: Store in Qdrant
    vector_store = VectorStore()

    vector_store.create_collection(
        vector_size=len(embeddings[0])
    )

    vector_store.insert(chunks, embeddings)

    print("✅ Pipeline completed successfully!")

def search(query: str):
    embedder = Embedder()
    vector_store = VectorStore()

    query_vector = embedder.embed([query])[0]

    results = vector_store.client.query_points(
        collection_name=vector_store.collection_name,
        query=query_vector,
        limit=3
    )

    client_ai = OpenAI()
    context = "\n".join([r.payload["text"] for r in results.points])
    prompt = f"""
    Answer based on the context:

    Context:
    {context}

    Query:
    {query}
    """

    response = client_ai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    # run_pipeline()
    search("What triggers a suspicious activity alert?")