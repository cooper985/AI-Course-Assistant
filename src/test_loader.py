from document_loader import load_pdf

# 测试1：正常PDF
pdf_path = "../data/test.pdf"

text = load_pdf(pdf_path)

if text:
    print("PDF读取成功")
    print(text[:500])
else:
    print("PDF读取失败")

# 测试2：错误路径
wrong_path = "../data/not_exist.pdf"

text = load_pdf(wrong_path)

if text is None:
    print("错误处理正常")
else:
    print("错误处理失败")