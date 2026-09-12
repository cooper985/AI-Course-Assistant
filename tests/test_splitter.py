from src.document import Document
from src.text_splitter.splitter import TextSplitter


doc = Document(
    text="这是一个测试文本。" * 200,
    metadata={
        "source":"test.pdf",
        "page":1
    }
)


splitter = TextSplitter(
    chunk_size=100,
    overlap=20
)


chunks = splitter.split(doc)


print("chunk数量:",len(chunks))


for i, chunk in enumerate(chunks):

    print("----------------")

    print("Chunk",i)

    print(chunk.text[:50])

    print(chunk.metadata)