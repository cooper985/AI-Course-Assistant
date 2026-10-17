import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.document_loader.document_loader import load_pdf
from src.text_splitter.splitter import TextSplitter
from src.embedding.embedder import Embedder

# PDF路径
data_path = Path(__file__).resolve().parents[1] / "data"
pdf_paths = sorted(p for p in data_path.rglob("*") if p.is_file() and p.suffix.lower() == ".pdf")
if not pdf_paths:
    raise FileNotFoundError(f"没有找到 PDF 文件：{data_path}")
pdf_path = pdf_paths[0]


# 1. 加载PDF
documents = load_pdf(pdf_path)
assert documents, f"PDF 没有可提取的文字：{pdf_path}"


print("Documents数量:")
print(len(documents))

#2.初始化文本切分器
splitter = TextSplitter(
    chunk_size=500,
    overlap=50
)

#保存所有chunk
all_chunks = []

#3.对每个Document进行切分
for doc in documents:
    chunk = splitter.split(doc)
    all_chunks.extend(chunk)

print("\nChunk数量:")
print(len(all_chunks))

# 4. 查看第一个chunk
first_chunk = all_chunks[0]

print("\n第一个Chunk:")
print(first_chunk.text[:200])


print("\nMetadata:")
print(first_chunk.metadata)


embedder = Embedder()
vectors = []
for i, chunk in enumerate(all_chunks):
    vector = embedder.embed_document(chunk)
    vectors.append(vector)
    print(f"第{i}个chunk完成，向量维度:{len(vector)}")

print("\n总向量数量:")
print(len(vectors))
