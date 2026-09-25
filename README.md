# EduVision — Higher Education Performance Analytics Dashboard

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458.svg)](https://pandas.pydata.org/)
[![Tableau](https://img.shields.io/badge/Tableau-Dashboard-E97627.svg)](https://www.tableau.com/)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)]()

> An end-to-end higher-education analytics platform that transforms global university ranking data into actionable insights using Python, Pandas, NumPy, and Tableau.

---

## Table of Contents

- [Overview](#overview)
- [Objectives](#objectives)
- [Architecture](#architecture)
- [Dashboard Suite](#dashboard-suite)
- [Key Performance Indicators](#key-performance-indicators)
- [Analytical Capabilities](#analytical-capabilities)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Project Workflow](#project-workflow)
- [Data Sources](#data-sources)
- [Business Questions Answered](#business-questions-answered)
- [Quality & Validation](#quality--validation)
- [Getting Started](#getting-started)
- [Future Enhancements](#future-enhancements)
- [Documentation](#documentation)

---

## Overview

**EduVision** is an end-to-end data analytics and business intelligence project designed to analyze and visualize global higher-education performance.

The project integrates university ranking and performance data from major global ranking sources, prepares and transforms the data using Python, engineers analytical KPIs, and presents the results through an interactive Tableau dashboard suite.

The platform enables users to explore:

- University performance and global rankings
- Academic reputation and research impact
- Research productivity
- International student representation
- Faculty-to-student metrics
- Country-level education performance and comparisons
- Global education trends

**Lifecycle:** Data Collection → Data Cleaning → KPI Engineering → Dashboard Planning → Dashboard Development → Integration → Testing → Documentation & Delivery

---

## Objectives

1. Collect higher-education ranking and performance data
2. Integrate datasets from multiple ranking sources
3. Clean and standardize university and country information
4. Engineer meaningful education analytics KPIs
5. Build an optimized dataset for Tableau
6. Develop interactive dashboards for different analytical perspectives
7. Enable university- and country-level comparisons
8. Provide actionable insights through data visualization
9. Validate dashboard calculations and interactions
10. Deliver a professional, documented, portfolio-ready analytics solution

---

## Architecture

```
Ranking Datasets (QS, THE, supporting data)
            │
            ▼
    Data Collection (Python)
            │
            ▼
Data Cleaning & Transformation (Python / Pandas / NumPy)
            │
            ▼
    KPI Engineering
    (Ranking Score, Research Impact, Research Productivity, Student Metrics)
            │
            ▼
    Tableau-Ready Dataset
            │
            ▼
EduVision Dashboard Suite
(University Overview · Research Analytics · Student Analytics · Country Comparison)
            │
            ▼
    Testing & Validation
            │
            ▼
    Documentation & Delivery (GitHub / Tableau)
```

---

## Dashboard Suite

EduVision consists of four primary analytical dashboards supported by a central navigation/home experience.

### 1. University Overview
Provides a high-level view of global university performance.

| | |
|---|---|
| **Key Analysis** | Top university rankings · Global distribution · Academic reputation · Score distribution · Country-level performance · Institutional comparison |
| **Main Visualizations** | Global University Distribution Map · Top University Rankings · Academic Reputation Heatmap · Overall Score Analysis & Distribution · Institutional Comparison |

### 2. Research Analytics
Focuses on research performance and institutional research strength.

| | |
|---|---|
| **Key Analysis** | Research impact & productivity · Performance distribution · Impact by country · Research-vs-overall performance relationship |
| **Main Visualizations** | Research Impact Analysis & Distribution · Research Productivity Treemap · Research Impact vs Global Ranking · Research Impact by Country |

### 3. Student Analytics
Analyzes student-related university performance indicators.

| | |
|---|---|
| **Key Analysis** | International student percentage · Faculty-to-student ratio · Student diversity & performance · Country-level representation |
| **Main Visualizations** | International Students vs Overall Score · Faculty-to-Student Ratio · Student Performance Highlight Table · International Student Distribution by Country |

### 4. Country Comparison
Provides country-level benchmarking of higher-education performance.

| | |
|---|---|
| **Key Analysis** | University distribution by country · Country performance comparison · Research impact · Geographic education performance |
| **Main Visualizations** | University Count by Country · Country Performance Map · Country Overall Score Comparison · Country Overall Score vs Research Impact |

---

## Key Performance Indicators

| KPI | Purpose |
|---|---|
| Global Ranking Score | Measures university ranking performance |
| Research Impact Score | Measures research-related impact |
| Research Productivity Index | Represents research productivity |
| Faculty-to-Student Ratio | Measures faculty/student relationship |
| International Student Percentage | Measures international student representation |
| Academic Reputation Score | Measures academic reputation |
| Overall Score | Provides an overall university performance measure |

KPI calculations are implemented using the project datasets and transformation logic developed in Module 3.

---

## Analytical Capabilities

- **University-Level Analysis** — individual ranking position, academic reputation, research performance, student indicators, and overall performance
- **Country-Level Analysis** — cross-country comparison of university counts, overall performance, research strength, and education benchmarks
- **Comparative Analysis** — side-by-side comparison across universities, countries, ranking metrics, research indicators, and student indicators

### Dashboard Interactivity
The Tableau dashboards support country/university/ranking filters, cross-dashboard navigation, interactive selections, dashboard actions, and geographic exploration — allowing users to move between analytical areas without leaving the EduVision environment.

---

## Technology Stack

| Category | Tools |
|---|---|
| Programming & Data Processing | Python, Pandas, NumPy |
| Data Visualization & BI | Tableau |
| Development Environment | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |
| Data Formats | CSV, Excel, Tableau Workbook |

---

## Project Structure

```
EduVision_DV/
│
├── README.md
│
├── 01_Module_1_University_Data_Collection/
│   ├── README.md
│   ├── data/
│   │   └── university_raw_data.csv
│   └── scripts/
│       └── data_collection.py
│
├── 02_Module_2_Data_Cleaning_Transformation/
│   ├── README.md
│   ├── data/
│   │   └── university_cleaned.csv
│   └── notebooks/
│       └── education_cleaning.ipynb
│
├── 03_Module_3_Education_KPI_Engineering/
│   ├── README.md
│   ├── data/
│   │   └── university_final_dataset.xlsx
│   └── scripts/
│       └── generate_education_kpis.py
│
├── 04_Module_4_Dashboard_Planning_Prototyping/
│   ├── README.md
│   ├── planning/
│   │   └── dashboard_storyboard.pdf
│   └── prototype/
│       └── eduvision_prototype.twbx
│
├── 05_Module_5_Dashboard_Development/
│   ├── README.md
│   ├── tableau/
│   │   └── eduvision_dashboard_v1.twbx
│   └── screenshots/
│
├── 06_Module_6_Dashboard_Integration/
│   ├── README.md
│   ├── tableau/
│   │   └── EduVision_DV.twbx
│   └── screenshots/
│
├── 07_Module_7_Testing_Validation/
│   ├── README.md
│   ├── testing/
│   │   └── QA_Checklist.md
│   └── reports/
│       ├── Dashboard_Testing_Report.md
│       └── Module_7_Testing_and_Validation.md
│
└── 08_Module_8_Documentation_Delivery/
    ├── README.md
    ├── documentation/
    │   ├── Dataset_Sources.md
    │   ├── KPI_Definitions.md
    │   ├── Dashboard_Guide.md
    │   └── Education_Analytics_Methodology.md
    └── deployment/
        └── Module_8_Documentation_and_Delivery.md
```

---

## Project Workflow

| Phase | Description | Output |
|---|---|---|
| **1. Data Collection** | Ranking datasets collected and organized into a common analytical structure | `university_raw_data.csv` |
| **2. Data Cleaning & Transformation** | Duplicate removal, university/country standardization, ranking-metric normalization, missing-value handling, restructuring | `university_cleaned.csv` |
| **3. KPI Engineering** | Standardized measures generated for ranking, research, academic reputation, students, and overall performance | `university_final_dataset.xlsx` |
| **4. Dashboard Planning** | Layouts, filters, navigation, and interactions defined for four dashboard areas | Storyboard + prototype |
| **5. Dashboard Development** | Dashboards implemented in Tableau with interactive filtering and comparison views | `eduvision_dashboard_v1.twbx` |
| **6. Dashboard Integration** | Individual dashboards unified into a single navigable EduVision experience (Home → University Overview → Research Analytics → Student Analytics → Country Comparison) | `EduVision_DV.twbx` |
| **7. Testing & Validation** | KPI/ranking calculations, interactions, filters, navigation, and visualizations reviewed | QA & testing reports |
| **8. Documentation & Delivery** | Final repository organized with data, scripts, notebooks, workbooks, screenshots, and documentation | Complete project package |

---

## Data Sources

The project primarily uses global university ranking and higher-education performance datasets, including:

- QS World University Rankings
- Times Higher Education (THE) World University Rankings
- Supporting education datasets used where applicable

Detailed source information is documented in [`Dataset_Sources.md`](08_Module_8_Documentation_Delivery/documentation/Dataset_Sources.md).

### Data Processing Pipeline

```
Raw Data → Load → Inspect → Clean → Standardize Fields →
Handle Missing Values → Transform Metrics → Engineer KPIs →
Export Tableau Dataset
```

---

## Business Questions Answered

<details>
<summary><b>University Performance</b></summary>

- Which universities perform strongly globally?
- How does academic reputation vary?
- How are overall scores distributed?
- How do universities compare with each other?
</details>

<details>
<summary><b>Research</b></summary>

- Which institutions demonstrate strong research performance?
- How does research impact relate to overall performance?
- Which countries demonstrate stronger research performance?
- How does research productivity vary?
</details>

<details>
<summary><b>Students</b></summary>

- How does international student representation vary?
- What is the relationship between student indicators and university performance?
- How do faculty-to-student indicators differ?
- Which countries have higher international student representation?
</details>

<details>
<summary><b>Countries</b></summary>

- Which countries have stronger university performance?
- How many universities are represented per country?
- How does country performance compare against the overall benchmark?
- What relationship exists between country-level overall performance and research impact?
</details>

---

## Quality & Validation

| Layer | Checks |
|---|---|
| **Data Validation** | Duplicate checking, missing-value inspection, field/university/country consistency, metric validation |
| **KPI Validation** | Calculation review, source-field verification, aggregation checks, dashboard value verification |
| **Dashboard Validation** | Filter testing, navigation testing, dashboard action testing, visualization review, KPI display verification |

---

## Getting Started

**1. Clone the repository**
```bash
git clone <repository-url>
cd EduVision_DV
```

**2. Explore the data processing modules**
```
01_Module_1_University_Data_Collection
02_Module_2_Data_Cleaning_Transformation
03_Module_3_Education_KPI_Engineering
```

**3. Open the Tableau workbooks**

Available under:
```
05_Module_5_Dashboard_Development/tableau/
06_Module_6_Dashboard_Integration/tableau/
```

**4. Explore the final dashboard**

Open `EduVision_DV.twbx` from the Module 6 Tableau directory.

### Recommended Environment
- Python 3.x
- Pandas, NumPy
- Jupyter Notebook
- Tableau Desktop
- Git

---

## Key Deliverables

- **Data** — Raw dataset, cleaned dataset, final KPI dataset
- **Python** — Data collection script, KPI generation script
- **Jupyter** — Data cleaning and transformation notebook
- **Tableau** — Prototype, development, and final integrated workbooks
- **Documentation** — Dataset sources, KPI definitions, dashboard guide, methodology, testing, and delivery docs

---

## Skills Demonstrated

`Python` `Pandas` `NumPy` `Data Cleaning` `Data Transformation` `EDA` `KPI Engineering` `Data Visualization` `Tableau` `Dashboard Development` `Dashboard Integration` `Data Storytelling` `Business Intelligence` `Git` `GitHub` `Documentation` `Data Validation`

---

## Future Enhancements

- Automated data refresh pipelines
- Additional ranking sources
- Historical ranking trend analysis
- Advanced statistical & predictive performance models
- Machine learning-based ranking analysis
- Cloud-based data pipelines
- Advanced geographic analytics
- University recommendation capabilities

---

## Documentation

Detailed documentation is available under [`08_Module_8_Documentation_Delivery/documentation/`](08_Module_8_Documentation_Delivery/documentation/):

- `Dataset_Sources.md`
- `KPI_Definitions.md`
- `Dashboard_Guide.md`
- `Education_Analytics_Methodology.md`

Testing documentation: [`07_Module_7_Testing_Validation/`](07_Module_7_Testing_Validation/)

---

## Project Status

| | |
|---|---|
| **Implementation** | Complete |
| **Modules** | 8 |
| **Dashboard Suite** | University Overview · Research Analytics · Student Analytics · Country Comparison |
| **Primary BI Tool** | Tableau |
| **Data Processing** | Python / Pandas / NumPy |
| **Repository** | GitHub |
| **Documentation** | Completed |

---

<p align="center">
Built with <b>Python</b> • <b>Pandas</b> • <b>NumPy</b> • <b>Tableau</b> • <b>Git</b> • <b>GitHub</b>
</p>
