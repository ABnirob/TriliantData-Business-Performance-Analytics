# Triliant Data — Build Your .pbix File (5 Minutes)

This guide gets you a real, working `Triliant_Data.pbix` file on your own machine.
Power BI Desktop only runs on Windows — if you're on Mac/Linux, use a Windows VM
or **app.powerbi.com** (Power BI Service) which also accepts this same Power Query.

---

## Step 1 — Open Power BI Desktop

Download it free (if you don't have it): https://powerbi.microsoft.com/desktop/

---

## Step 2 — Paste the Dataset (Power Query)

1. Click **Home → Transform Data** (opens Power Query Editor)
2. Click **Home → New Source → Blank Query**
3. Right-click the new query → **Advanced Editor**
4. **Delete everything** in the box
5. Open `PowerQuery_RawData.m` (included in this package), copy **all** of it
6. Paste into the Advanced Editor → click **Done**
7. Rename the query (right panel) to **`Raw Data`**
8. Click **Home → Close & Apply**

You now have a fully-typed 96-row table loaded natively into your `.pbix` —
no external Excel file needed, no broken links if you move the file later.

---

## Step 3 — Add the DAX Measures

In **Report View**, click **Raw Data** table in the Fields pane →
**Table tools → New Measure**, and paste each one below (one at a time):

```dax
Total Revenue = SUM('Raw Data'[RevenueBDT])

Revenue (BDT M) = DIVIDE([Total Revenue], 1000000)

MoM Revenue Growth =
VAR CurrentRev = [Total Revenue]
VAR PrevRev =
    CALCULATE([Total Revenue], DATEADD('Raw Data'[Month], -1, MONTH))
RETURN DIVIDE(CurrentRev - PrevRev, PrevRev)

Avg Report Time = AVERAGE('Raw Data'[ReportTimeHrs])

Report Time Reduction % =
VAR FirstMonth =
    CALCULATE(AVERAGE('Raw Data'[ReportTimeHrs]),
        TOPN(1, ALL('Raw Data'[Month]), 'Raw Data'[Month], ASC))
VAR LastMonth =
    CALCULATE(AVERAGE('Raw Data'[ReportTimeHrs]),
        TOPN(1, ALL('Raw Data'[Month]), 'Raw Data'[Month], DESC))
RETURN DIVIDE(FirstMonth - LastMonth, FirstMonth)

Avg Satisfaction = AVERAGE('Raw Data'[Satisfaction])

Avg KPI Achievement = AVERAGE('Raw Data'[KPIAchievement])

Total Leads = SUM('Raw Data'[NewLeads])

Total Conversions = SUM('Raw Data'[Conversions])

Conversion Rate = DIVIDE([Total Conversions], [Total Leads])

Active Clients =
CALCULATE(DISTINCTCOUNT('Raw Data'[Client]), 'Raw Data'[ProjectStatus] = "Active")

Revenue per Client =
DIVIDE([Total Revenue], DISTINCTCOUNT('Raw Data'[Client]))

On-Time Delivery Rate =
DIVIDE(
    CALCULATE(COUNTROWS('Raw Data'), 'Raw Data'[OnTime] = "Yes"),
    COUNTROWS('Raw Data')
)

Revenue Share by Service =
DIVIDE([Total Revenue], CALCULATE([Total Revenue], ALL('Raw Data'[ServiceType])))
```

---

## Step 4 — Build the Visuals

### Page 1 — Executive Summary
- 4x **Card** visuals: `Total Revenue`, `Avg Satisfaction`, `Report Time Reduction %`, `Active Clients`
- **Clustered Column + Line**: Axis = `Month`, Column = `Total Revenue`, Line = `MoM Revenue Growth`
- **Donut Chart**: Legend = `ServiceType`, Values = `Total Revenue`
- **Slicer**: `Region`

### Page 2 — Client Analysis
- **Horizontal Bar**: Axis = `Client`, Values = `Total Revenue`
- **Table**: `Client`, `ServiceType`, `Total Revenue`, `Avg Satisfaction`, `ProjectStatus`
- **Treemap**: Group = `Industry`, Values = `Total Revenue`

### Page 3 — Operational KPIs
- **Line Chart**: Axis = `Month`, Values = `Avg Report Time`
- **Area Chart**: Axis = `Month`, Values = `Avg KPI Achievement`
- **Gauge**: `Conversion Rate` vs target 0.55

### Page 4 — Regional Deep Dive
- **Stacked Bar**: Axis = `Region`, Values = `Total Revenue`, Legend = `ServiceType`
- **Matrix**: Rows = `Region`, Columns = `Month`, Values = `Total Revenue`

---

## Step 5 — Theme It

**Format → Themes → Customize current theme:**
- Name: Triliant Dark
- Primary: `#3B82F6`  ·  Secondary: `#22D3EE`  ·  Tertiary: `#F97316`
- Background: `#0B1120`  ·  Foreground: `#F1F5F9`

---

## Step 6 — Save as .pbix

**File → Save As → `Triliant_Data.pbix`**

Done. You now have a real, native Power BI Desktop file you can open, edit,
refresh, and publish to your own Power BI workspace anytime.

---

*Built on real Triliant Data clients & service lines (triliantdata.com).*
*Analyst: Md. Abul Bashar Nirob · abnirob40@gmail.com*
