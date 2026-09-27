import numpy as np
class VectorStore:

    def __init__(self):
        self.vectors = []
        self.documents = []
    def add(self, document, vector):
        self.documents.append(document)
        self.vectors.append(vector)

    def cosine_similarity(self, vector1, vector2):
        vector1 = np.array(vector1)
        vector2 = np.array(vector2)
        similarity =(
            np.dot(vector1, vector2)
            /
            (
                np.linalg.norm(vector1)
                *
                np.linalg.norm(vector2)
            )
        )
        return similarity

    def search(self, query_vector, k=3):
        results = []
        for i, vector in enumerate(self.vectors):
            score = self.cosine_similarity(
                query_vector,
                vector
            )
            results.append(
                (
                    self.documents[i],
                    score
                )
            )

        results.sort(
            key = lambda x: x[1],
            reverse = True
        )

        return results[:k]


