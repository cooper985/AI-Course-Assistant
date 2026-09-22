from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-small-zh")

    def embed_document(self,document):
        vector = self.model.encode(
            document.text
        )

        return vector

    def embed_query(self, query):
        vector = self.model.encode(
            query
        )

        return vector