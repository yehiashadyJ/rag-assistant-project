Backend terminal paste and run:
 1.source .venv/bin/activate
 2.PYTHONPATH=backend uvicorn app.main:app --reload

Frontend terminal paste and run: 
 1.source .venv/bin/activate
 2.export API_BASE_URL="http://127.0.0.1:8000"
 3.streamlit run frontend/app.py