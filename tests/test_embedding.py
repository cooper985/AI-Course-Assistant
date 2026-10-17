import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.document import Document

from src.embedding.embedder import Embedder


doc = Document(
    "补码可以实现减法",
    {
        "source":"test.pdf",
        "page":1
    }
)


embedder = Embedder()


vector = embedder.embed_document(doc)


print(vector)

print(len(vector))
