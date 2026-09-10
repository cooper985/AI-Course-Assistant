from src.document_loader.document_loader import load_pdf
from src.text_splitter.splitter import TextSplitter


# PDF路径
pdf_path = r"..\data\test.pdf"


# 1. 加载PDF
text = load_pdf(pdf_path)


print("PDF文本长度:")
print(len(text))


# 2. 创建文本切分器
splitter = TextSplitter(
    chunk_size=500,
    overlap=50
)


# 3. 文本切分
chunks = splitter.split_text(text)


# 4. 查看结果
print("----------------")
print("Chunk数量:")
print(len(chunks))


for i, chunk in enumerate(chunks[:3]):

    print("----------------")
    print(f"Chunk {i}")

    print(chunk)