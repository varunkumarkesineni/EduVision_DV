# EduVision – Dashboard Testing Report

## 1. Document Information

| Item | Details |
|---|---|
| Project | EduVision – Higher Education Performance Dashboard |
| Module | Module 7 – Testing & Validation |
| Report | Dashboard Testing Report |
| Dashboard Tool | Tableau |
| Data Preparation | Python, Pandas, NumPy |
| Purpose | Validate dashboard functionality, calculations, and interactions |

---

# 2. Introduction

The EduVision project provides an interactive dashboard suite for analyzing higher-education performance using university ranking and performance data.

This testing report documents the validation performed on the EduVision Tableau dashboards before final project delivery.

The testing focuses on data accuracy, KPI calculations, ranking-related values, visualizations, filters, navigation, dashboard actions, and educational performance metrics.

---

# 3. Testing Objectives

The main objectives of dashboard testing are:

1. Verify that dashboards load correctly.
2. Validate KPI values.
3. Verify ranking-related calculations.
4. Confirm that visualizations represent the underlying data correctly.
5. Test dashboard filters.
6. Test navigation between dashboards.
7. Test dashboard actions.
8. Verify educational metrics.
9. Check consistency across dashboards.
10. Identify and address dashboard issues before delivery.

---

# 4. Dashboards Tested

The following dashboards were included in the testing process:

### 4.1 EduVision Home

Testing areas:

- KPI cards
- Top university display
- Navigation controls
- Dashboard layout
- Links to analytical dashboards

### 4.2 University Overview

Testing areas:

- Global ranking KPI
- Research impact KPI
- Overall score KPI
- University distribution
- Academic reputation analysis
- University ranking analysis
- Overall score analysis
- Institutional comparison

### 4.3 Research Analytics

Testing areas:

- Research productivity KPI
- Research impact KPI
- Research productivity analysis
- Research impact analysis
- Research comparison visualizations
- Research-related filters and interactions

### 4.4 Student Analytics

Testing areas:

- International student KPI
- Faculty-to-student ratio KPI
- Student-related visualizations
- International student analysis
- Student diversity analysis
- Student comparison views

### 4.5 Country Comparison

Testing areas:

- Country-level KPI cards
- Country comparison visualizations
- Country performance analysis
- Country filtering
- Country-level research and overall score comparison

---

# 5. Testing Methodology

The dashboard testing process followed a structured validation approach.

## Step 1 – Data Validation

The final prepared dataset was reviewed to ensure that the required fields were available for dashboard analysis.

## Step 2 – KPI Validation

Calculated KPIs were checked against the project's KPI engineering logic and prepared dataset.

## Step 3 – Visualization Validation

Each dashboard visualization was checked to confirm that:

- It loads correctly.
- The correct fields are used.
- Aggregations are appropriate.
- Labels and titles are understandable.
- The displayed values respond correctly to filters.

## Step 4 – Interaction Testing

Interactive dashboard elements were tested, including:

- Country filters
- University filters
- Global Ranking Score Range
- Dashboard navigation
- Dashboard actions

## Step 5 – Cross-Dashboard Validation

Relevant values were compared across dashboards to identify inconsistencies.

## Step 6 – Final Review

A final usability and functionality review was performed before preparing the project for documentation and delivery.

---

# 6. KPI Testing

The following project KPIs were validated:

| KPI | Validation Focus |
|---|---|
| Global Ranking Score | Correct calculation and Tableau representation |
| Research Impact Score | Correct calculation and representation |
| Faculty-to-Student Ratio | Correct metric representation |
| International Student Percentage | Correct metric representation |
| Academic Reputation Score | Correct source value and representation |
| Research Productivity Index | Correct calculation and representation |

The KPI validation process ensures that the dashboard displays values derived from the prepared project data and KPI logic.

---

# 7. Ranking Testing

Ranking-related functionality was reviewed to verify:

- University ranking values.
- Top university identification.
- Ranking source handling.
- Ranking-related filtering.
- Consistency of ranking information across relevant dashboards.

Special attention was given to ranking-source handling because the project integrates ranking information from multiple higher-education ranking sources.

---

# 8. Visualization Testing

Each visualization was checked for:

- Correct chart type.
- Correct dimensions.
- Correct measures.
- Appropriate aggregation.
- Correct labels.
- Readable titles.
- Proper filtering behavior.
- Correct display after interaction.

The testing covered the visualization areas used in the:

- University Overview
- Research Analytics
- Student Analytics
- Country Comparison

dashboards.

---

# 9. Filter Testing

The dashboard filter functionality was tested using the main project filters.

### Country Filter

Expected behavior:

Selecting a country should update the relevant dashboard analysis to reflect the selected country.

### University Name Filter

Expected behavior:

Selecting a university should allow the relevant university-level analysis to be isolated.

### Global Ranking Score Range

Expected behavior:

Selecting a score range should filter universities according to the selected score range.

### Filter Reset

Expected behavior:

Clearing filters should return the dashboard to its expected overall state.

---

# 10. Navigation Testing

The dashboard navigation structure was tested to ensure that users can move between the main sections of EduVision.

The navigation destinations include:

- Home
- University Overview
- Research Analytics
- Student Analytics
- Country Comparison

Each navigation control was checked to ensure that it opens the intended dashboard.

---

# 11. Dashboard Action Testing

Dashboard actions were reviewed to ensure that selections made by the user produce the expected changes in connected views.

The following areas were tested:

- University selection.
- Country selection.
- Filter actions.
- Clearing selections.
- Connected dashboard views.

The testing also helps identify unintended filtering effects, such as a KPI displaying only a subset of records when a dashboard action remains active.

---

# 12. Educational Metric Validation

Educational performance metrics were reviewed to ensure that the dashboard represents the intended analytical areas.

The main areas include:

- Academic Reputation
- Research Impact
- Research Productivity
- International Students
- Faculty-to-Student Ratio
- Overall University Performance

These metrics form the core analytical components of the EduVision dashboard suite.

---

# 13. Cross-Dashboard Validation

Cross-dashboard validation was performed to check whether common metrics remain consistent when displayed in different dashboard sections.

The following were reviewed:

- Overall Score
- Global Ranking Score
- Research Impact Score
- Research Productivity Index
- International Student Percentage
- Faculty-to-Student Ratio

This validation helps maintain consistency throughout the EduVision dashboard suite.

---

# 14. Issues and Resolution

During dashboard development and validation, issues were reviewed and corrected where required.

Examples of validation areas included:

### Top University Display

The Top University KPI was reviewed to ensure that multiple ranking-source records did not result in multiple university names being displayed simultaneously.

The ranking source filter was used to ensure that the KPI represents the intended ranking source.

### Dashboard Filter Behavior

Dashboard actions were reviewed to ensure that unintended selections did not cause KPI cards or other dashboard components to display only a limited subset of records.

### Ranking Field Handling

Ranking-related fields were reviewed to ensure that ranking information and score fields were not incorrectly treated as interchangeable.

---

# 15. Final Testing Status

The EduVision dashboard suite was reviewed across the required testing areas:

- Data validation
- KPI validation
- Ranking validation
- Visualization testing
- Filter testing
- Navigation testing
- Dashboard action testing
- Educational metric validation
- Cross-dashboard consistency
- Final usability review

The testing activities provide the validation required before proceeding to the final documentation and delivery stage.

---

# 16. Conclusion

Dashboard testing is an important stage of the EduVision project because it ensures that the final Tableau dashboards are reliable, interactive, and aligned with the prepared education analytics data.

The testing process covered the major functional and analytical components of the project and prepared the dashboard suite for final documentation and delivery.

---

## Next Step

The project proceeds to:

**Module 8 – Documentation and Delivery**