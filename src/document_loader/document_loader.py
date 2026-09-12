import pdfplumber
from src.document import Document


def load_pdf(file_path):

    documents = []

    try:
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    doc = Document(
                        text=page_text,
                        metadata={
                            "source": file_path,
                            "page": page_num + 1
                        }
                    )

                    documents.append(doc)
    except Exception as e:
        print(f"读取PDF失败: {e}")
        return None
    return documents
