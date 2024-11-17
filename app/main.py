from fastapi import FastAPI, File, UploadFile, Form
from typing import List
from .document_handler import extract_text_from_pdfs
from .chat import handle_query

app = FastAPI()

# Global knowledge base to store PDF content
knowledge_base = []

@app.post("/upload-pdfs/")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    # Extract and store content from PDFs for the knowledge base
    for file in files:
        content = await extract_text_from_pdfs(file)
        knowledge_base.append(content)
    return {"message": "PDFs uploaded successfully"}

@app.post("/ask-query/")
async def ask_query(prompt: str = Form(...)):
    # Use the knowledge base for answering the prompt
    response = handle_query(prompt, knowledge_base)
    return {"response": response}
