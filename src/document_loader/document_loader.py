import pdfplumber
from pathlib import Path
from src.document import Document


def load_pdf(file_path):

    documents = []

    with pdfplumber.open(file_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            page_text = page.extract_text()
            if page_text:
                doc = Document(
                    text=page_text,
                    metadata={
                        "source": str(file_path),
                        "page": page_num + 1
                    }
                )

                documents.append(doc)
    return documents


def load_pdfs(directory):

    documents = []

    directory = Path(directory)
    if not directory.is_dir():
        raise NotADirectoryError(f"PDF 目录不存在或不是目录：{directory}")

    for file_path in sorted(directory.rglob("*")):
        if file_path.is_file() and file_path.suffix.lower() == ".pdf":
            documents.extend(load_pdf(file_path))

    return documents
