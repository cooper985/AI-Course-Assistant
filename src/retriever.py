from embedding.embedder import Embedder


class Retriever:

    def __init__(
        self,
        embedder,
        vector_store
    ):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, query):
        query_vector = self.embedder.embed_query(query)

        document = self.vector_store.search(query_vector)

        return document