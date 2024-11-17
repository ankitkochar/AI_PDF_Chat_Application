from ..document_handler import extract_text_from_pdfs
from fastapi import UploadFile
import pytest

@pytest.mark.asyncio
async def test_extract_text_from_pdfs():
    with open("sample.pdf", "rb") as f:
        pdf_file = UploadFile(filename="sample.pdf", file=f)
        pdf_text = await extract_text_from_pdfs(pdf_file)
        assert len(pdf_text) > 0
