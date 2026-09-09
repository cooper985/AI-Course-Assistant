from document_loader import load_pdf


pdf_path = "../data/test.pdf"

text = load_pdf(pdf_path)


print(text)