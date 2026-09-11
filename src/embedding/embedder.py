from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-small-zh")

    def embed(self,text):
        vector = self.model.encode(text)

        return vector