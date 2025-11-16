# Energy Dashboard

This project fetches energy generation and weather data from APIs, transforms the data, stores it in SQLite, and visualizes it in a Streamlit dashboard.

---

## Features

- Fetch daily **generation** and **weather** data from Elexon API.
- Transform and clean the data:
  - Consolidates generation per day across all fuel types.
  - Normalizes date columns for easy merging.
- Store data in **SQLite** for efficient querying.
- Interactive **Streamlit dashboard**:
  - Line chart of total generation (GW) and temperature (°C) over time.
  - Dual y-axis (left: temperature, right: total generation).
  - Monthly x-axis with easy-to-read layout.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/energy-dashboard.git
cd energy-dashboard
```

2. Create a Python environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```
pip install -r requirements.txt
```
---

## Configuration

All API endpoints and settings are in config/settings.yaml.

---

## Usage

1. Fetch, transform and store data:
python extract_load.py

2. Run the streamlit dashboard: 
streamlit run dashboard.py

3. Open URL shown by Streamlit in your browser

---

## Project Structure

energy-dashboard/
├── config/
│   └── settings.yaml       # API endpoints and settings
├── data/
│   └── energy.db           # SQLite database
├── extract_load.py         # Fetch and transform data, load into SQLite
├── transforms.py           # Functions to normalize and transform raw API data
├── dashboard.py            # Streamlit dashboard script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

---

## Notes

- Dates in all datasets are normalized (time removed) to simplify merging.
- Total generation is stored in GW for consistency.
- The dashboard dynamically adapts its y-axis starting from 0 for clarity.
