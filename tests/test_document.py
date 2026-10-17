import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


from src.document import Document


doc = Document(
    "补码可以实现减法",
    {
        "source":"计算机组成原理.pdf",
        "page":25
    }
)


print(doc.text)

print(doc.metadata)
