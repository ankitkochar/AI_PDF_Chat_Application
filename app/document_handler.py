import pypdf
from fastapi import UploadFile

async def extract_text_from_pdfs(file: UploadFile) -> str:
    pdf_text = ""
    pdf_reader = pypdf.PdfReader(file.file)
    for page in pdf_reader.pages:
        pdf_text += page.extract_text() or ""
    print(pdf_text)
    return pdf_text
