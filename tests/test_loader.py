from src.document_loader.document_loader import load_pdf
documents = load_pdf(r"..\data\test.pdf")


print(len(documents))


for doc in documents:

    print("----------------")

    print(doc.text[:100])

    print(doc.metadata)