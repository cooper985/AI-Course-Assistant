from src.document_loader.document_loader import load_pdf
from src.text_splitter.splitter import TextSplitter
from src.embedding.embedder import Embedder
from src.vector_store.vector_store import VectorStore
from src.retriever import Retriever

pdf_path = r"..\data\test.pdf"
documents = load_pdf(pdf_path)
print("Document数量：")
print(len(documents))


splitter = TextSplitter(
    chunk_size=500,
    overlap=50
)
chunks = []
for doc in documents:
    chunks.extend(
        splitter.split(doc)
    )
print("Chunk数量")
print(len(chunks))


embedder = Embedder()
store = VectorStore()

for chunk in chunks:
    vector  = embedder.embed_document(chunk)
    store.add(
        chunk,
        vector
    )

retriever = Retriever(
    embedder,
    store
)

query = "补码为什么可以实现减法？"


result = retriever.retrieve(query)


print("检索结果:")
print(result.text)

print("来源:")
print(result.metadata)


