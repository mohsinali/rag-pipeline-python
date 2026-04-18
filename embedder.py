from openai import OpenAI
from config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

class Embedder:
    def __init__(self, model: str = settings.EMBEDDING_MODEL):
        self.model = model

    def embed(self, texts):
        print("I am called")
        response = client.embeddings.create(
            model=self.model,
            input=texts
        )

        return [item.embedding for item in response.data]
    
# embedder = Embedder()   # create object

# texts = ["Hello world", "This is a test"]

# embeddings = embedder.embed(texts)   # call method
# print(embeddings)
    