from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-small-zh")

    def embed(self,document):
        vector = self.model.encode(
            document.text
        )

        return vector