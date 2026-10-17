import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.document_loader.document_loader import load_pdfs


data_path = Path(__file__).resolve().parents[1] / "data"


documents = load_pdfs(data_path)
assert documents, f"没有读取到 PDF 文字：{data_path}"


print("Document数量:")
print(len(documents))


print(documents[0].metadata)
