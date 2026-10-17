import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

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


results = retriever.retrieve(
    "补码为什么可以实现减法"
)


assert len(results) == 2
assert results[0][0] is doc1
for doc, score in results:
    print(doc.text)
    print(doc.metadata)
    print("score:", score)
