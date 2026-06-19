<div align="center">

# 📊 Triliant Data — Business Performance Analytics

### End-to-end data analysis project tracking revenue, KPIs, and client performance for a Bangladesh-based data services firm

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=flat-square&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Excel](https://img.shields.io/badge/Excel-Dashboard-217346?style=flat-square&logo=microsoftexcel&logoColor=white)](https://www.microsoft.com/excel)
[![Power BI](https://img.shields.io/badge/Power%20BI-Ready-F2C811?style=flat-square&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](#license)

</div>

<br>

<p align="center">
  <img src="assets/0.png" alt="Triliant Data Business Performance Dashboard" width="100%">
</p>

<br>

## 🧭 Overview

This project simulates a real-world analyst workflow at **[Triliant Data](https://triliantdata.com)**, a Bangladesh-based data and technology services company operating out of **Dhaka** and **Chittagong**. It covers the full pipeline from raw data to executive-ready dashboard:

```
Data Generation  →  Cleaning & EDA  →  KPI Modeling  →  Visualization  →  Reporting
```

The dataset tracks **8 real Triliant Data clients** across **4 core service lines** over a **12-month period** (Mar 2025 – Feb 2026), measuring revenue, client satisfaction, operational efficiency, and lead conversion — the exact metrics a Data & Business Analyst is responsible for reporting on.

> Built by **Md. Abul Bashar Nirob** — Data & Business Analyst | [LinkedIn](https://linkedin.com/in/mdashar202) · [GitHub](https://github.com/ABnirob)

<br>

## 🎯 Key Results

| Metric | Result |
|---|---|
| 💰 Total Revenue Tracked | **BDT 208.3M** across 12 months |
| 📈 Revenue Growth | **+175%** from first to last month |
| ⏱️ Reporting Time Reduction | **−50%** (18 hrs → 9 hrs per report) |
| ⭐ Client Satisfaction | **+1.1 points** improvement (3.6 → 4.7 / 5.0) |
| 🎯 KPI Achievement | Up from **64% → 94%** by final quarter |
| 🤝 Active Clients | **6 of 8** clients currently active |

<br>

## 🗂️ Repository Structure

```
triliant-data-analytics/
│
├── README.md
│
├── assets/
│   └── dashboard-preview.png          # Full dashboard, rendered (this README's hero image)
│
├── data/
│   └── Triliant_Data_Analytics.xlsx   # Source workbook — 6 sheets, 130+ live formulas
│
├── analysis/
│   └── triliant_data_analysis.py      # Python EDA + dashboard generation script
│
└── powerbi/
    ├── PowerQuery_RawData.m           # Paste into Power BI to load the full dataset instantly
    ├── HOW_TO_BUILD_PBIX.md           # Step-by-step .pbix build guide
    └── DAX_Measures_Guide.html        # 15+ ready-to-use DAX measures + visual specs
```

<br>

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| **Data Wrangling** | Python, Pandas, NumPy |
| **Statistical Analysis** | Correlation matrices, pivot tables, trend analysis |
| **Visualization** | Matplotlib (custom dark-theme dashboard), Excel native charts |
| **Spreadsheet Layer** | Excel (openpyxl) — formulas, conditional formatting, pivot summaries |
| **BI Layer** | Power BI (DAX measures, relationships, RLS-ready) |

<br>

## 📐 Dataset Schema

`Raw Data` sheet — 96 records (8 clients × 12 months), 14 columns:

| Column | Type | Description |
|---|---|---|
| `Month` | string | Reporting month (Mar-25 → Feb-26) |
| `Client` | string | Client company name |
| `Industry` | string | Client's industry vertical |
| `Service Type` | string | Custom Software Dev / AI & ML / Data Analytics / Digital Transformation |
| `Revenue (BDT)` | numeric | Monthly revenue in Bangladeshi Taka |
| `Project Status` | string | Active / Completed / On Hold |
| `Report Time (hrs)` | numeric | Hours spent producing client reports |
| `Satisfaction (1–5)` | numeric | Client satisfaction score |
| `KPI Achievement (%)` | numeric | % of agreed KPIs met that month |
| `New Leads` | numeric | Leads generated |
| `Conversions` | numeric | Leads converted to engagements |
| `Region` | string | Dhaka / Chittagong |
| `Team Size` | numeric | Analysts assigned |
| `On-Time` | string | Whether deliverable was on-time |

<br>

## 👥 Client Portfolio

| Client | Industry | Service | Region |
|---|---|---|---|
| Adila Apparels | Garments | Custom Software Dev | Dhaka |
| Chai Break | F&B | AI & ML Solutions | Dhaka |
| Fair Farm BD | AgriTech | Data Analytics | Dhaka |
| Infinabel | E-commerce | Digital Transformation | Dhaka |
| Nodi Bangla | Media | Custom Software Dev | Chittagong |
| Robust Developments | Real Estate | Data Analytics | Dhaka |
| Monoara Jahur | Manufacturing | AI & ML Solutions | Dhaka |
| TechnoVate BD | IT Services | Digital Transformation | Chittagong |

<br>

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/ABnirob/triliant-data-analytics.git
cd triliant-data-analytics
```

### 2. Install dependencies
```bash
pip install pandas numpy matplotlib openpyxl
```

### 3. Run the analysis
```bash
python analysis/triliant_data_analysis.py
```
This regenerates the full EDA report (console output) and renders the dashboard PNG.

### 4. Explore the Excel workbook
Open `data/Triliant_Data_Analytics.xlsx` — six sheets:
- **Raw Data** — full transactional dataset (filterable)
- **KPI Summary** — monthly rollups with live formulas
- **Service Analysis** — revenue & performance by service line
- **Client Tracker** — per-client summary with status indicators
- **Charts** — native Excel visualizations
- **README** — in-workbook documentation

### 5. Build the Power BI dashboard (.pbix)
1. Open Power BI Desktop → **Home → Transform Data → New Blank Query → Advanced Editor**
2. Paste in the contents of `powerbi/PowerQuery_RawData.m` → **Done → Close & Apply**
   (loads the full 96-row dataset instantly, fully typed, no external file needed)
3. Paste the DAX measures from `powerbi/DAX_Measures_Guide.html` into **New Measure**
4. Build the visuals listed in `powerbi/HOW_TO_BUILD_PBIX.md` (exact chart type + fields per page)
5. **File → Save As → Triliant_Data.pbix**

<br>

## 📊 Dashboard Highlights

- **KPI summary cards** — revenue, satisfaction, time saved, growth at a glance
- **Monthly revenue trend** with month-over-month growth annotations
- **Service mix donut chart** across all 4 offering lines
- **Operational efficiency view** — reporting time vs. satisfaction (dual-axis)
- **KPI achievement trendline** — 64% → 94% over 12 months
- **Regional breakdown** — Dhaka vs. Chittagong revenue split
- **Client revenue ranking** — full client comparison, color-coded by region
- **Lead generation & conversion funnel**
- **Full client portfolio tracker** with live status indicators

<br>

## 📌 Notes on the Data

This dataset is **synthetically generated** for portfolio purposes, modeled on Triliant Data's real published client roster and service offerings (sourced from [triliantdata.com](https://triliantdata.com)). Revenue figures, satisfaction scores, and KPI percentages are illustrative and do not represent actual company financials.

<br>

## 📬 Contact

**Md. Abul Bashar Nirob**
Data & Business Analyst · Dhaka, Bangladesh

📧 abnirob40@gmail.com · 🔗 [LinkedIn](https://linkedin.com/in/mdashar202) · 💻 [GitHub](https://github.com/ABnirob)

<br>

## 📄 License

This project is licensed under the MIT License — feel free to fork, adapt, and build on it.

<br>

<div align="center">

⭐ If this project helped you understand end-to-end analyst workflows, consider giving it a star!

</div>
