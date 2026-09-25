# Module 7 – Testing & Validation

## Overview

Module 7 focuses on testing and validating the EduVision – Higher Education Performance Dashboard to ensure that the prepared datasets, calculated KPIs, dashboard visualizations, filters, navigation, and interactive features work correctly.

The objective of this module is to identify and resolve errors before the final project delivery.

---

## Objectives

The main objectives of Module 7 are:

- Validate KPI calculations.
- Verify ranking calculations.
- Test dashboard interactions.
- Validate educational performance metrics.
- Check filters and dashboard controls.
- Verify dashboard navigation.
- Check data consistency across dashboards.
- Identify and document issues.
- Ensure the final dashboards are suitable for project delivery.

---

## Testing Scope

Testing is performed across the following areas:

1. Data Validation
2. KPI Validation
3. Ranking Validation
4. Dashboard Visualization Testing
5. Filter Testing
6. Navigation Testing
7. Dashboard Action Testing
8. Educational Metric Validation
9. Cross-Dashboard Consistency
10. Final Usability Review

---

## Testing Workflow

The testing process follows these steps:

1. Verify the final dataset.
2. Validate calculated KPIs.
3. Verify ranking-related calculations.
4. Check dashboard visualizations.
5. Test filters and controls.
6. Test navigation between dashboards.
7. Test dashboard actions.
8. Compare values across dashboards.
9. Record identified issues.
10. Perform final validation before delivery.

---

## Main Dashboards Tested

The following EduVision dashboards are included in the testing process:

- EduVision Home
- University Overview
- Research Analytics
- Student Analytics
- Country Comparison

---

## Key Validation Areas

### KPI Validation

The following KPIs are checked:

- Global Ranking Score
- Research Impact Score
- Faculty-to-Student Ratio
- International Student Percentage
- Academic Reputation Score
- Research Productivity Index

The KPI values displayed in Tableau are checked against the prepared project dataset and KPI-generation logic.

---

### Ranking Validation

Ranking-related calculations are reviewed to ensure:

- University rankings are represented correctly.
- Ranking values are consistent with the source data.
- Ranking-related filters work correctly.
- Top universities are displayed correctly.
- Ranking source information is handled consistently.

---

### Dashboard Interaction Testing

Interactive elements are tested to verify:

- Filters respond correctly.
- University selections update relevant views.
- Country selections work correctly.
- Navigation buttons open the intended dashboards.
- Dashboard actions do not produce unexpected results.
- Charts update according to selected filters.

---

## Testing Documentation

The following documents are maintained as part of Module 7:

### QA Checklist

`testing/QA_Checklist.md`

Contains the checklist used to verify data, KPIs, dashboards, filters, navigation, and interactions.

### Dashboard Testing Report

`reports/Dashboard_Testing_Report.md`

Contains the detailed testing approach, test cases, observations, and validation status.

### Module 7 Testing and Validation Report

`reports/Module_7_Testing_and_Validation.md`

Contains the overall testing and validation summary for the milestone.

---

## Repository Structure

```text
07_Module_7_Testing_Validation/
│
├── README.md
│
├── testing/
│   └── QA_Checklist.md
│
└── reports/
    ├── Dashboard_Testing_Report.md
    └── Module_7_Testing_and_Validation.md