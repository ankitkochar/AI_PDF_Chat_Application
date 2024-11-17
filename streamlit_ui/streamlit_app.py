import streamlit as st
import requests

st.title("AI PDF Chat Application")

# File uploader for PDF files
uploaded_files = st.file_uploader("Upload PDF Files", accept_multiple_files=True)

# Upload PDFs when files are selected
if uploaded_files:
    files = [("files", file) for file in uploaded_files]
    response = requests.post("http://localhost:8000/upload-pdfs/", files=files)
    st.success(response.json().get("message"))

# Text input for queries
query = st.text_input("Ask a question about the PDFs")
if query:
    response = requests.post("http://localhost:8000/ask-query/", data={"prompt": query})
    st.write(response.json().get("response"))
