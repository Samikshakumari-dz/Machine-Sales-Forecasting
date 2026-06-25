# Machine-Sales-Forecasting
AI-powered Machine Sales Forecasting System using Python, Streamlit, Random Forest, and XGBoost for demand forecasting and inventory optimization.

---

## Project Overview
This project provides a Streamlit dashboard for machine sales forecasting and inventory recommendations.

---

## Requirements
- Python 3.10+ (tested with Python 3.12)

---

## Setup Instructions (from scratch)
1. **Clone the repo**
   ```bash
   git clone <https://github.com/Samikshakumari-dz/Machine-Sales-Forecasting>
   cd Machine-Sales-Forecasting
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## Run the Project (Streamlit)
Example (fresh clone):
```bash
git clone https://github.com/Samikshakumari-dz/Machine-Sales-Forecasting
cd Machine-Sales-Forecasting

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
```

If port **8501** is already in use, use another port:
```bash
streamlit run app.py --server.port 8502 --server.address 127.0.0.1
```

After starting, open in your browser:
- http://127.0.0.1:8501 (or the port you selected)

---

## Environment Variables
This project does **not** require any environment variables.


---

## Database Setup
No database is used by this project.

---

## Repository Checklist
This repository includes everything required to run locally:
- ✅ `app.py` (application source code)
- ✅ `requirements.txt` (Python dependencies)
- ✅ `README.md` (setup + run instructions)

---

## Notes / Testing
- The app is UI-only and generates example tables/graphs inside the dashboard.
- If any dependency installation fails (e.g., `xgboost` wheels), retry `pip install -r requirements.txt`.
