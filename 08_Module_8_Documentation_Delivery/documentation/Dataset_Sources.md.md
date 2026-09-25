# EduVision – Dataset Sources

## 1. Overview

EduVision uses higher-education ranking and performance data to analyze university performance, research impact, student characteristics, and country-level education performance.

The datasets collected during the project were prepared and transformed before being used for KPI engineering and Tableau dashboard development.

---

## 2. Primary Data Sources

### 2.1 QS World University Rankings

The QS World University Rankings dataset was used as one of the primary sources for university ranking and performance information.

The dataset provides information related to university rankings and academic performance indicators.

Important fields used in the project include:

- University Name
- Country
- Rank
- Academic Reputation
- Citations per Faculty
- Faculty-to-Student Ratio
- International Student Ratio
- Overall Score

The QS dataset supports university-level ranking, academic reputation, research-related analysis, and student-related analysis.

---

### 2.2 Times Higher Education World University Rankings

The Times Higher Education World University Rankings dataset was used as another primary source for university performance analysis.

Important indicators include:

- University Name
- Country
- Overall Performance
- Research Environment
- Research Quality
- Students-to-Staff Ratio
- International Students
- Other available ranking indicators

The THE dataset supports research, student, and overall university performance analysis.

---

## 3. Supporting Education Data

Supporting education data was considered during the project to provide additional educational context where applicable.

Only datasets that were relevant to the EduVision analysis and compatible with the project data structure were considered for integration.

---

## 4. Data Collection Process

The data collection process included:

1. Identifying relevant university ranking datasets.
2. Downloading the QS World University Rankings dataset.
3. Downloading the Times Higher Education World University Rankings dataset.
4. Reviewing available fields and indicators.
5. Checking dataset structure and completeness.
6. Preparing the datasets for integration.

---

## 5. Data Integration

The ranking datasets were reviewed and transformed into a common analytical structure.

The integration process included:

- Standardizing university names.
- Standardizing country names.
- Aligning common indicators.
- Handling ranking information.
- Combining relevant university performance information.
- Preparing the integrated dataset for cleaning and KPI engineering.

---

## 6. Data Preparation

The collected datasets were prepared using Python and data-analysis libraries.

The preparation process included:

- Duplicate identification.
- Missing-value review.
- Data-type conversion.
- University-name standardization.
- Country-name standardization.
- Ranking-field processing.
- Metric normalization where required.

---

## 7. Data Quality Considerations

During preparation, the following areas were reviewed:

- Duplicate university records.
- Missing ranking values.
- Inconsistent university names.
- Country-name variations.
- Ranking ranges.
- Differences between ranking sources.
- Availability of individual performance indicators.

Missing values were reviewed carefully because the absence of a ranking or metric may represent unavailable source information rather than an incorrect record.

---

## 8. Dataset Usage in EduVision

The prepared datasets were used for:

- University ranking analysis.
- Academic reputation analysis.
- Research impact analysis.
- Research productivity analysis.
- Student analytics.
- Country comparison.
- KPI engineering.
- Tableau dashboard development.

---

## 9. Source References

### QS World University Rankings

Source: QS World University Rankings

### Times Higher Education World University Rankings

Source: Times Higher Education World University Rankings

The exact dataset files used in the project are maintained within the corresponding project modules.