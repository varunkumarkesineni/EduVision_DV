# EduVision – KPI Definitions

## 1. Overview

Key Performance Indicators (KPIs) are used in EduVision to summarize important aspects of university and higher-education performance.

The KPIs are engineered from the prepared university ranking datasets and are used throughout the Tableau dashboard suite.

---

## 2. Global Ranking Score

### Definition

Global Ranking Score represents the normalized university ranking performance used within the EduVision analytical dataset.

### Purpose

It provides a standardized measure for comparing university ranking performance.

### Source

Ranking-related information from the prepared university ranking datasets.

### Calculation / Method

The Global Ranking Score follows the KPI engineering logic implemented during Module 3.

### Interpretation

A higher score represents stronger performance according to the project's normalized ranking measure.

### Dashboard Usage

Used in:

- University Overview
- Research Analytics
- Student Analytics
- Country Comparison

---

## 3. Research Impact Score

### Definition

Research Impact Score represents the research-related performance of a university based on the available research indicators.

### Purpose

It is used to compare the research influence and research performance of universities.

### Source Fields

Research-related indicators from the QS and THE datasets, including available research performance measures.

### Calculation / Method

The Research Impact Score follows the KPI engineering logic implemented during Module 3.

### Interpretation

Higher values indicate stronger research impact within the EduVision analytical framework.

### Dashboard Usage

Used mainly in:

- Research Analytics
- University Overview
- Country Comparison

---

## 4. Faculty-to-Student Ratio

### Definition

Faculty-to-Student Ratio represents the relationship between faculty/staff and students within the university dataset.

### Purpose

It provides an indicator for analyzing the student-to-faculty environment of universities.

### Source Fields

Faculty/student-related indicators available in the QS and THE datasets.

### Calculation / Method

The metric follows the data transformation and KPI logic implemented during Module 3.

### Interpretation

The value is used to compare faculty and student conditions across universities.

### Dashboard Usage

Used mainly in:

- Student Analytics
- University Overview

---

## 5. International Student Percentage

### Definition

International Student Percentage represents the proportion or score related to international students in the university dataset.

### Purpose

It is used to analyze international student participation and student diversity.

### Source Fields

International student indicators from the prepared ranking datasets.

### Calculation / Method

The metric follows the KPI engineering logic implemented during Module 3.

### Interpretation

Higher values indicate greater international student representation according to the project metric.

### Dashboard Usage

Used mainly in:

- Student Analytics
- University Overview
- Country Comparison

---

## 6. Academic Reputation Score

### Definition

Academic Reputation Score represents the academic reputation indicator available in the university ranking data.

### Purpose

It is used to analyze academic reputation and compare universities based on academic perception.

### Source Field

QS Academic Reputation indicator.

### Calculation / Method

The score is represented according to the prepared dataset and KPI engineering process.

### Interpretation

Higher values indicate stronger academic reputation within the ranking dataset.

### Dashboard Usage

Used mainly in:

- University Overview
- Country Comparison

---

## 7. Research Productivity Index

### Definition

Research Productivity Index represents the research productivity measure developed for the EduVision project.

### Purpose

It is used to compare university research productivity.

### Source Fields

Research-related indicators from the prepared university ranking datasets.

### Calculation / Method

The Research Productivity Index follows the KPI engineering logic implemented during Module 3.

### Interpretation

Higher values represent stronger research productivity within the EduVision analytical framework.

### Dashboard Usage

Used mainly in:

- Research Analytics
- University Overview
- Country Comparison

---

## 8. KPI Usage Across Dashboards

| KPI | University Overview | Research Analytics | Student Analytics | Country Comparison |
|---|---|---|---|---|
| Global Ranking Score | Yes | Yes | Yes | Yes |
| Research Impact Score | Yes | Yes | No | Yes |
| Faculty-to-Student Ratio | Yes | No | Yes | No |
| International Student Percentage | Yes | No | Yes | Yes |
| Academic Reputation Score | Yes | No | No | Yes |
| Research Productivity Index | Yes | Yes | No | Yes |

---

## 9. KPI Validation

The KPIs were reviewed during Module 7 Testing and Validation.

Validation focused on:

- Source fields.
- Calculation logic.
- Data availability.
- Tableau representation.
- Consistency across dashboards.

---

## 10. Conclusion

The KPI framework provides the analytical foundation for EduVision and enables consistent university, research, student, and country-level performance analysis.