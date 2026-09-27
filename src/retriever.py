

class Retriever:

    def __init__(
        self,
        embedder,
        vector_store
    ):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, query, k=3):
        query_vector = self.embedder.embed_query(query)

        results = self.vector_store.search(
            query_vector,
            k=k
        )

        return results