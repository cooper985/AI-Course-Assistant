class Document:

    def __init__(self,text,metadata=None):
        self.text = text
        self.metadata = metadata or {}