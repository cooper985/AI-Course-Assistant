from src.retriever import Retriever
from src.embedding.embedder import Embedder
from src.vector_store.vector_store import VectorStore
from src.document import Document


store = VectorStore()


doc1 = Document(
    text="补码可以实现减法",
    metadata={
        "page":10
    }
)

doc2 = Document(
    text="原码表示数字",
    metadata={
        "page":11
    }
)


embedder = Embedder()


vector1 = embedder.embed_document(doc1)
vector2 = embedder.embed_document(doc2)


store.add(
    doc1,
    vector1
)

store.add(
    doc2,
    vector2
)


retriever = Retriever(
    embedder,
    store
)


result = retriever.retrieve(
    "补码为什么可以实现减法"
)


print(result.text)
print(result.metadata)