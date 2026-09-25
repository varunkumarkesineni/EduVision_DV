# EduVision – Education Analytics Methodology

## 1. Overview

EduVision follows a structured data analytics methodology to transform higher-education ranking data into an interactive Tableau dashboard suite.

The methodology covers data collection, cleaning, transformation, KPI engineering, dashboard development, integration, testing, and final delivery.

---

## 2. Project Objective

The objective of EduVision is to analyze higher-education performance using university ranking and performance indicators.

The project provides analytical insights into:

- University rankings
- Academic reputation
- Research impact
- Research productivity
- International students
- Faculty-to-student ratio
- Country-level education performance

---

## 3. Data Collection

The project begins with the collection of higher-education ranking datasets.

Primary sources include:

- QS World University Rankings
- Times Higher Education World University Rankings

The collected datasets are reviewed to identify relevant university, ranking, research, academic, and student indicators.

---

## 4. Data Cleaning

The collected data is cleaned and prepared using Python-based data-processing techniques.

The cleaning process includes:

- Removing duplicate records.
- Standardizing university names.
- Standardizing country names.
- Reviewing missing values.
- Converting fields to appropriate data types.
- Processing ranking information.
- Preparing consistent analytical fields.

---

## 5. Data Transformation

After cleaning, the datasets are transformed into a common structure.

The transformation process includes:

- Aligning common fields.
- Normalizing relevant metrics.
- Processing ranking values.
- Creating analytical fields.
- Preparing data for KPI engineering.
- Preparing Tableau-ready datasets.

---

## 6. Data Integration

QS and THE university ranking information is integrated where relevant.

The integration process is designed to maintain a consistent university-level analytical structure while preserving ranking-source information.

This allows EduVision to perform broader university performance analysis.

---

## 7. KPI Engineering

The project develops six major KPIs:

1. Global Ranking Score
2. Research Impact Score
3. Faculty-to-Student Ratio
4. International Student Percentage
5. Academic Reputation Score
6. Research Productivity Index

The KPI calculations follow the logic implemented during Module 3.

The resulting KPI dataset is prepared for Tableau dashboard development.

---

## 8. Dashboard Planning

The dashboard structure is planned around four main analytical areas:

### University Overview

Focuses on university ranking and overall performance.

### Research Analytics

Focuses on research impact and research productivity.

### Student Analytics

Focuses on international students, student diversity, and faculty-to-student ratio.

### Country Comparison

Focuses on country-level education performance and benchmarking.

---

## 9. Dashboard Development

Tableau is used to transform the prepared KPI dataset into interactive visualizations.

The dashboards use different visualization types to represent:

- Rankings
- Distributions
- Comparisons
- Relationships
- Geographic patterns
- Performance benchmarks

---

## 10. Dashboard Integration

The individual dashboards are integrated into the EduVision dashboard suite.

Navigation controls allow users to move between dashboard sections.

Interactive filters and dashboard actions allow users to explore selected universities, countries, and ranking-score ranges.

---

## 11. Testing and Validation

Testing is performed before final delivery.

The validation process includes:

- KPI validation
- Ranking validation
- Visualization testing
- Filter testing
- Navigation testing
- Dashboard action testing
- Educational metric validation
- Cross-dashboard consistency checks

Testing documentation is maintained under Module 7.

---

## 12. Analytical Approach

The EduVision analytical approach follows a structured progression:

```
Raw University Data
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Data Integration
        ↓
KPI Engineering
        ↓
Exploratory Analysis
        ↓
Dashboard Development
        ↓
Interactive Dashboard
        ↓
Testing & Validation
        ↓
Final Delivery
```