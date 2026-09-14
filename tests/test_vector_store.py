from src.vector_store.vector_store import VectorStore


store = VectorStore()


store.add(
    "document0",
    [1,0,0]
)


store.add(
    "document1",
    [0,1,0]
)


query = [0.9,0.1,0]


index = store.search(query)


print("最相似index:")
print(index)