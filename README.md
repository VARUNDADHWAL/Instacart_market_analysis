# Instacart Market Basket Analysis

An end-to-end data analysis project using real Instacart grocery order data to uncover customer behaviour, reorder patterns, and peak shopping trends.

---

## Tools Used

| Tool | Purpose |
|---|---|
| PostgreSQL | Database storage and schema setup |
| Python (pandas) | Data cleaning and feature engineering |
| SQL | Business analysis queries |
| Power BI | Dashboard and visualisation |

---

## Dataset

Source: [Instacart Market Basket Analysis — Kaggle](https://www.kaggle.com/competitions/instacart-market-basket-analysis/data)

Download the following files and place them inside the `data/` folder:

- `orders.csv`
- `products.csv`
- `aisles.csv`
- `departments.csv`
- `order_products__prior.csv`

> The `data/` folder is excluded from this repository via `.gitignore` due to file size.

---

## Project Structure

```
instacart-market-analysis/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── data/                          # Raw CSVs (not pushed to GitHub)
│
├── database/
│   ├── generate_schema.py         # Auto-reads CSVs and generates SQL
│   └── schema.sql                 # Output from generate_schema.py
│
├── notebooks/
│   ├── 01_eda_cleaning.ipynb      # Exploratory analysis and data cleaning
│   ├── 02_feature_engineering.ipynb
│   └── 03_analysis_summary.ipynb
│
├── sql/
│   ├── reorder_rate_by_aisle.sql
│   ├── peak_order_hours.sql
│   └── top_products_per_dept.sql
│
└── dashboard/
    ├── instacart_dashboard.pbix
    └── screenshots/
```

---

## How to Run This Project

### Step 1 — Set up the database

1. Download the dataset from Kaggle and place CSVs in `data/`
2. Run the schema generator:
   ```
   python database/generate_schema.py
   ```
3. Copy the terminal output and paste it into PostgreSQL query editor (pgAdmin)
4. Run the SQL — tables are created and data is loaded automatically

### Step 2 — Run the notebooks

Open notebooks in order:
```
notebooks/01_eda_cleaning.ipynb
notebooks/02_feature_engineering.ipynb
notebooks/03_analysis_summary.ipynb
```

### Step 3 — Explore SQL analysis

Each file in `sql/` answers one business question. Run them directly in pgAdmin after data is loaded.

### Step 4 — View the dashboard

Open `dashboard/instacart_dashboard.pbix` in Power BI Desktop.

Screenshots are available in `dashboard/screenshots/` if you don't have Power BI installed.

---

## Key Findings

> *(Fill this in once your analysis is complete)*

- **Peak ordering time:** Sunday and Monday mornings see the highest order volume
- **Most reordered aisle:** Fresh fruits and fresh vegetables have reorder rates above 60%
- **Average basket size:** X items per order
- **Top department:** Produce accounts for X% of all items ordered

---

## Dashboard Preview

> *(Add a screenshot here once your Power BI dashboard is ready)*

![Dashboard Preview](dashboard/screenshots/dashboard_overview.png)

---

## Setup

Install Python dependencies:

```
pip install pandas sqlalchemy psycopg2-binary jupyter
```

Or using the requirements file:

```
pip install -r requirements.txt
```

---

## Author

**Varun Dadhwal**
[LinkedIn](https://linkedin.com/in/varundadhwal) · [GitHub](https://github.com/VARUNDADHWAL) · [Kaggle](https://www.kaggle.com/varundadwal)# Instacart_market_analysis
