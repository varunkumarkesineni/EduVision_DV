# Module 7 – Testing and Validation

## EduVision – Higher Education Performance Dashboard

---

# 1. Module Overview

Module 7 focuses on testing and validation of the EduVision higher-education analytics solution.

The purpose of this module is to ensure that the prepared data, engineered KPIs, ranking calculations, Tableau visualizations, filters, navigation, and dashboard interactions operate correctly before final project delivery.

---

# 2. Module Objectives

The objectives of Module 7 are:

- Validate KPI calculations.
- Verify ranking calculations.
- Test dashboard interactions.
- Validate educational metrics.
- Check dashboard filters.
- Verify navigation.
- Review dashboard actions.
- Check consistency across dashboards.
- Document testing activities and observations.
- Prepare the solution for final delivery.

---

# 3. Testing Areas

The validation process covers the following areas:

1. Data Validation
2. KPI Validation
3. Ranking Validation
4. Visualization Testing
5. Filter Testing
6. Navigation Testing
7. Dashboard Action Testing
8. Educational Metric Validation
9. Cross-Dashboard Consistency
10. Final QA Review

---

# 4. Data Validation

The final project dataset was reviewed before dashboard validation.

The validation focused on:

- University records.
- University names.
- Country names.
- Ranking information.
- Numeric KPI fields.
- Missing values.
- Duplicate records.
- Data types.
- Tableau compatibility.

The purpose of this step was to ensure that the dataset used by Tableau was structured correctly for dashboard analysis.

---

# 5. KPI Validation

The project defines six major education KPIs:

1. Global Ranking Score
2. Research Impact Score
3. Faculty-to-Student Ratio
4. International Student Percentage
5. Academic Reputation Score
6. Research Productivity Index

Each KPI was reviewed against the project's KPI engineering process and prepared data.

The validation ensures that:

- Required fields are available.
- Calculations follow the defined project logic.
- KPI values can be represented correctly in Tableau.
- KPI cards and related visualizations use the appropriate measures.

---

# 6. Ranking Validation

Ranking calculations were reviewed as part of the validation process.

The following areas were checked:

- Ranking values.
- Top university identification.
- Ranking source.
- Ranking-related filtering.
- Ranking representation in Tableau.

Because EduVision combines university ranking information from multiple sources, ranking-source handling was also reviewed during validation.

---

# 7. Dashboard Validation

The main EduVision dashboards were reviewed individually.

## 7.1 EduVision Home

Validation areas:

- KPI cards.
- Top university display.
- Dashboard navigation.
- Overall layout.
- Links to analytical dashboards.

## 7.2 University Overview

Validation areas:

- Global ranking analysis.
- Academic reputation.
- University distribution.
- Overall score analysis.
- University ranking analysis.
- Institutional comparison.
- KPI cards.

## 7.3 Research Analytics

Validation areas:

- Research impact.
- Research productivity.
- Research comparisons.
- Research-related distributions.
- KPI cards.
- Interactive analysis.

## 7.4 Student Analytics

Validation areas:

- International students.
- Faculty-to-student ratio.
- Student diversity.
- Student distribution.
- Student comparisons.
- KPI cards.

## 7.5 Country Comparison

Validation areas:

- Country performance.
- Country-level comparisons.
- Overall score.
- Research impact.
- Country filtering.
- Country-level KPI analysis.

---

# 8. Filter Validation

The main filters used by the project were reviewed.

### Country

Used for country-level filtering and comparison.

### University Name

Used for university-level analysis and selection.

### Global Ranking Score Range

Used to filter universities according to their global ranking score.

The validation checked whether filter selections correctly affected the relevant dashboard views.

---

# 9. Navigation Validation

Navigation controls were tested across the dashboard suite.

The intended navigation structure is:

```text
Home
  ↓
University Overview
  ↓
Research Analytics
  ↓
Student Analytics
  ↓
Country Comparison