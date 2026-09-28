from src.document_loader.document_loader import load_pdfs
from src.text_splitter.splitter import TextSplitter
from src.embedding.embedder import Embedder
from src.vector_store.vector_store import VectorStore
from src.retriever import Retriever

data_path = r"..\data"
documents = load_pdfs(data_path)
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

queries = [
    "补码为什么可以实现减法？",
    "存储器有哪些主要类型？",
    "CPU的主要组成部分有哪些？",
    "指令系统包括哪些内容？",
    "系统总线的作用是什么？"
]


for query in queries:

    print("================")
    print("问题:", query)

    results = retriever.retrieve(
        query,
        k=3
    )

    for doc, score in results:
        print("----------------")
        print("score:", score)
        print(doc.text[:100])
        print(doc.metadata)


