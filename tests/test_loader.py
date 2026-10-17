import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.document_loader.document_loader import load_pdf

data_path = Path(__file__).resolve().parents[1] / "data"
pdf_paths = sorted(p for p in data_path.rglob("*") if p.is_file() and p.suffix.lower() == ".pdf")
if not pdf_paths:
    raise FileNotFoundError(f"没有找到 PDF 文件：{data_path}")
documents = load_pdf(pdf_paths[0])
assert documents, f"PDF 没有可提取的文字：{pdf_paths[0]}"


print(len(documents))


for doc in documents:

    print("----------------")

    print(doc.text[:100])

    print(doc.metadata)
