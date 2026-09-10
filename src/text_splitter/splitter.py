class TextSplitter:
    def __init__(
        self,
        chunk_size = 500,
        overlap = 50
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap


    def split_text(self, text):
        chunks = []
        start = 0
        while start < len(text):
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start = end - self.overlap

        return chunks