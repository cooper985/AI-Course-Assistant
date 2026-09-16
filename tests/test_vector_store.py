from src.vector_store.vector_store import VectorStore
from src.document import Document


store = VectorStore()


doc0 = Document(
    text="补码可以实现减法",
    metadata={
        "source":"test.pdf",
        "page":10
    }
)


doc1 = Document(
    text="原码表示方法",
    metadata={
        "source":"test.pdf",
        "page":11
    }
)


store.add(
    doc0,
    [1,0,0]
)


store.add(
    doc1,
    [0,1,0]
)


query = [0.9,0.1,0]


result = store.search(query)


print(result.text)
print(result.metadata)