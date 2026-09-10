from src.text_splitter.splitter import TextSplitter


text = """
Transformer is a deep learning model.
It uses self attention mechanism.
Self attention allows tokens to interact with each other.
"""


splitter = TextSplitter(
    chunk_size=50,
    overlap=10
)


chunks = splitter.split_text(text)


for i, chunk in enumerate(chunks):
    print("----------------")
    print(f"Chunk {i}")
    print(chunk)