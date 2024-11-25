
# AI PDF Chat Application

This is an **AI-powered chat application** that allows users to upload PDF files and interact with the content using a conversational interface. The application is built using **FastAPI** for the backend and **Streamlit** for the frontend.

---

## Features

- Upload multiple PDFs as a knowledge base.
- Use AI to query and retrieve answers from uploaded PDFs.
- Intuitive web-based interface built with Streamlit.
- Fast and scalable backend API using FastAPI.

---

## Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
- **AI Integration:** Open-source LLMs for natural language processing.
- **Deployment:** Uvicorn for serving the FastAPI backend.

---

## Prerequisites

1. **Python 3.8 or higher** installed on your machine.
2. [Git](https://git-scm.com/) installed for version control.
3. **Virtual Environment (optional but recommended)** for managing dependencies.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AI_PDF_Chat_Application.git
   cd AI_PDF_Chat_Application
   ```

2. Create and activate a virtual environment:
   - **Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

1. **Start the Backend (FastAPI):**
   Open a terminal and run:
   ```bash
   uvicorn app.main:app --reload
   ```
   - The backend will be available at `http://127.0.0.1:8000`.
   - You can access the API documentation at `http://127.0.0.1:8000/docs`.

2. **Start the Frontend (Streamlit):**
   Open a second terminal and run:
   ```bash
   streamlit run streamlit_ui/streamlit_app.py
   ```
   - The frontend will open in your browser at `http://localhost:8501`.

---

## How to Use

1. **Upload PDFs:**
   - On the Streamlit interface, upload one or more PDF files.

2. **Ask Questions:**
   - Type your questions in the input box. The AI will process the query and return answers based on the content of the uploaded PDFs.

3. **View Responses:**
   - Answers will be displayed in the Streamlit interface.

---

## Troubleshooting

- If `git` or `Python` is not recognized, ensure they are properly installed and added to your system's PATH.
- Restart the backend (`uvicorn`) and frontend (`streamlit`) if you encounter errors.

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [OpenAI](https://openai.com/) and open-source AI models
