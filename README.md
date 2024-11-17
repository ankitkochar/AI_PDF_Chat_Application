# AI PDF Chat Application

This is a small AI chat application allowing users to upload multiple PDFs and query information from them.
The project includes a FastAPI backend and a Streamlit frontend.

### Setup and Run

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Run the FastAPI server:

   ```
   uvicorn app.main:app --reload
   ```

3. Launch the Streamlit interface:

   ```
   streamlit run streamlit_ui/streamlit_app.py
   ```

### Project Structure
- `app/`: Backend code for handling PDFs, queries, and LLM responses.
- `streamlit_ui/`: Streamlit-based frontend for user interaction.
- `tests/`: Contains unit tests for various modules.
#   A I _ P D F _ C h a t _ A p p l i c a t i o n  
 #   p r o j e c t - r o o t  
 