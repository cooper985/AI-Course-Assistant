from src.document import Document
from src.embedding.embedder import Embedder


doc = Document(
    "补码可以实现减法",
    {
        "source":"test.pdf",
        "page":1
    }
)


embedder = Embedder()


vector = embedder.embed(doc)


print(vector)

print(len(vector))