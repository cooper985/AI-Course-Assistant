from src.document import Document


class TextSplitter:
    def __init__(
        self,
        chunk_size = 500,
        overlap = 50
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap


    def split(self, document):
        chunks = []

        text = document.text

        start = 0

        while start < len(text):
            end = start + self.chunk_size

            chunk_text = text[start:end]

            chunk_document = Document(
                text=chunk_text,
                metadata=document.metadata.copy()
            )

            chunks.append(chunk_document)

            start = end - self.overlap

        return chunks