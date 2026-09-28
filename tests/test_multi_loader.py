from src.document_loader.document_loader import load_pdfs


data_path = r"..\data"


documents = load_pdfs(data_path)


print("Document数量:")
print(len(documents))


print(documents[0].metadata)