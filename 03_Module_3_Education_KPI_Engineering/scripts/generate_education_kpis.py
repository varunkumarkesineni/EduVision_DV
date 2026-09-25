import pandas as pd
import numpy as np
from pathlib import Path

# Module 3 - Education KPI Engineering

# Get the project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Define data folders
RAW_DIR = BASE_DIR / "Data" / "Raw Data"
CLEANED_DIR = BASE_DIR / "Data" / "Cleaned Data"
PROCESSED_DIR = BASE_DIR / "Data" / "Processed Data"
DOCS_DIR = BASE_DIR / "docs"

# Create required folders
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
DOCS_DIR.mkdir(parents=True, exist_ok=True)

# Define input files
QS_FILE = RAW_DIR / "2026_QS_World University_Rankings.csv"
THE_FILE = RAW_DIR / "THE World University Rankings 2026.xlsx"

# Define output files
FINAL_FILE = PROCESSED_DIR / "university_final_dataset.xlsx"
KPI_REPORT = DOCS_DIR / "module_03_kpi_report.txt"

print("Module 3 - Education KPI Engineering")

# Check input files
if not QS_FILE.exists():
    print("QS dataset not found:")
    print(QS_FILE)
    raise SystemExit

if not THE_FILE.exists():
    print("THE dataset not found:")
    print(THE_FILE)
    raise SystemExit

print("\nLoading QS dataset...")
qs = pd.read_csv(QS_FILE)

print("QS rows:", len(qs))
print("QS columns:", len(qs.columns))

print("\nLoading THE dataset...")
the = pd.read_excel(THE_FILE)

print("THE rows:", len(the))
print("THE columns:", len(the.columns))


# --------------------------------------------------
# Prepare QS data
# --------------------------------------------------

print("\nPreparing QS KPI fields...")

qs = qs.rename(columns={
    "Name": "university_name",
    "Country/Territory": "country",
    "Rank": "rank",
    "Overall SCORE": "overall_score",
    "Academic Reputation SCORE": "academic_reputation_score",
    "Citations per Faculty SCORE": "citations_per_faculty_score",
    "Faculty Student Ratio SCORE": "faculty_student_ratio_score",
    "International Student SCORE": "international_student_score"
})

qs_kpi = qs[
    [
        "university_name",
        "country",
        "rank",
        "overall_score",
        "academic_reputation_score",
        "citations_per_faculty_score",
        "faculty_student_ratio_score",
        "international_student_score"
    ]
].copy()

qs_kpi["year"] = 2026
qs_kpi["ranking_source"] = "QS"

# Preserve the original QS ranking values
# before converting numeric fields.
qs_rank_original = qs_kpi["rank"].copy()

# Convert QS score and indicator fields to numeric
qs_numeric_columns = [
    "overall_score",
    "academic_reputation_score",
    "citations_per_faculty_score",
    "faculty_student_ratio_score",
    "international_student_score"
]

for column in qs_numeric_columns:
    qs_kpi[column] = pd.to_numeric(
        qs_kpi[column],
        errors="coerce"
    )

# Convert ranking ranges into midpoint values
# Example: 701-710 becomes 705.5
def convert_qs_rank(value):
    if pd.isna(value):
        return np.nan

    value = str(value).strip()

    if "-" in value:
        parts = value.split("-")

        try:
            first = float(parts[0])
            second = float(parts[1])

            return (first + second) / 2

        except ValueError:
            return np.nan

    try:
        return float(value)

    except ValueError:
        return np.nan

# Convert the ORIGINAL rank values
qs_kpi["rank"] = qs_rank_original.apply(
    convert_qs_rank
)
# --------------------------------------------------
# Prepare THE data
# --------------------------------------------------

print("Preparing THE KPI fields...")

the = the.rename(columns={
    "Name": "university_name",
    "Country": "country",
    "Rank": "rank",
    "Overall Score": "overall_score",
    "Research Quality": "research_quality",
    "Research Environment": "research_environment",
    "Teaching": "teaching",
    "International Outlook": "international_outlook",
    "International Students": "international_students",
    "Students to Staff Ratio": "students_to_staff_ratio"
})

the_kpi = the[
    [
        "university_name",
        "country",
        "rank",
        "overall_score",
        "research_quality",
        "research_environment",
        "teaching",
        "international_outlook",
        "international_students",
        "students_to_staff_ratio"
    ]
].copy()

the_kpi["year"] = 2026
the_kpi["ranking_source"] = "THE"

# Convert numeric fields
the_numeric_columns = [
    "rank",
    "overall_score",
    "research_quality",
    "research_environment",
    "teaching",
    "international_outlook",
    "international_students",
    "students_to_staff_ratio"
]

for column in the_numeric_columns:
    the_kpi[column] = pd.to_numeric(
        the_kpi[column],
        errors="coerce"
    )


# --------------------------------------------------
# Calculate QS KPIs
# --------------------------------------------------

print("\nCalculating QS KPIs...")

# Global Ranking Score
# Combines ranking position and overall ranking score.
qs_max_rank = qs_kpi["rank"].max()

qs_kpi["rank_score"] = (
    100 *
    (1 - ((qs_kpi["rank"] - 1) / (qs_max_rank - 1)))
)
# Validate QS rank conversion
print("\nQS rank validation:")
print("QS rank missing:", qs_kpi["rank"].isna().sum())
print("QS rank score missing:", qs_kpi["rank_score"].isna().sum())

# Calculate Global Ranking Score
# Combine ranking position and published overall score.
# If the overall score is unavailable, use the ranking position score.

qs_kpi["global_ranking_score"] = np.where(
    qs_kpi["overall_score"].notna(),
    (
        qs_kpi["rank_score"] +
        qs_kpi["overall_score"]
    ) / 2,
    qs_kpi["rank_score"]
)

# Convert the result to numeric
qs_kpi["global_ranking_score"] = pd.to_numeric(
    qs_kpi["global_ranking_score"],
    errors="coerce"
)

# If QS overall score is unavailable,
# use the ranking-position score as the fallback.
qs_kpi["global_ranking_score"] = (
    qs_kpi["global_ranking_score"]
    .fillna(qs_kpi["rank_score"])
)

# Research Impact Score
# QS uses Citations per Faculty as the research impact indicator.
qs_kpi["research_impact_score"] = (
    qs_kpi["citations_per_faculty_score"]
)

# Faculty-to-Student Ratio
# QS already provides a Faculty Student Ratio SCORE.
qs_kpi["faculty_to_student_ratio"] = (
    qs_kpi["faculty_student_ratio_score"]
)

# International Student Percentage
# QS provides an International Student SCORE rather than
# a direct percentage in the supplied dataset.
# Therefore this is used as a standardized 0-100 indicator.
qs_kpi["international_student_percentage"] = (
    qs_kpi["international_student_score"]
)

# Fill missing QS indicator values using the QS median.
qs_kpi["international_student_percentage"] = (
    qs_kpi["international_student_percentage"]
    .fillna(
        qs_kpi["international_student_percentage"].median()
    )
)

# Academic Reputation Score
qs_kpi["academic_reputation_kpi"] = (
    qs_kpi["academic_reputation_score"]
)

# Research Productivity Index
# Combines research impact and academic reputation.
qs_kpi["research_productivity_index"] = (
    qs_kpi[
        [
            "research_impact_score",
            "academic_reputation_kpi"
        ]
    ].mean(axis=1)
)


# --------------------------------------------------
# Calculate THE KPIs
# --------------------------------------------------

print("Calculating THE KPIs...")

# Global Ranking Score
the_max_rank = the_kpi["rank"].max()

the_kpi["rank_score"] = (
    100 *
    (1 - ((the_kpi["rank"] - 1) / (the_max_rank - 1)))
)

the_kpi["global_ranking_score"] = (
    the_kpi[
        [
            "rank_score",
            "overall_score"
        ]
    ].mean(axis=1)
)

# Research Impact Score
# THE Research Quality is used as the main research impact indicator.
the_kpi["research_impact_score"] = (
    the_kpi["research_quality"]
)

# Faculty-to-Student Ratio
# THE provides Students to Staff Ratio.
# Lower students per staff means a better faculty-to-student
# situation, so it is converted into a 0-100 score.
ratio_max = the_kpi["students_to_staff_ratio"].max()

the_kpi["faculty_to_student_ratio"] = (
    100 *
    (
        1 -
        (
            the_kpi["students_to_staff_ratio"] /
            ratio_max
        )
    )
)

# International Student Percentage
# THE provides the international student percentage directly.
the_kpi["international_student_percentage"] = (
    the_kpi["international_students"]
)

# Fill the small number of missing THE values
# using the median of the available THE values.
the_kpi["international_student_percentage"] = (
    the_kpi["international_student_percentage"]
    .fillna(
        the_kpi["international_student_percentage"].median()
    )
)

# Academic Reputation Score
# THE does not provide the QS Academic Reputation metric.
# Teaching performance is used as the available academic
# performance indicator for THE.
the_kpi["academic_reputation_kpi"] = (
    the_kpi["teaching"]
)

# Research Productivity Index
# Combines research quality and research environment.
the_kpi["research_productivity_index"] = (
    the_kpi[
        [
            "research_quality",
            "research_environment"
        ]
    ].mean(axis=1)
)


# --------------------------------------------------
# Select final common structure
# --------------------------------------------------

final_columns = [
    "university_name",
    "country",
    "year",
    "ranking_source",
    "rank",
    "overall_score",
    "global_ranking_score",
    "research_impact_score",
    "faculty_to_student_ratio",
    "international_student_percentage",
    "academic_reputation_kpi",
    "research_productivity_index"
]

qs_final = qs_kpi[final_columns].copy()
the_final = the_kpi[final_columns].copy()

# Combine QS and THE
final_dataset = pd.concat(
    [
        qs_final,
        the_final
    ],
    ignore_index=True
)

# Standardize university and country text
final_dataset["university_name"] = (
    final_dataset["university_name"]
    .astype("string")
    .str.strip()
)

final_dataset["country"] = (
    final_dataset["country"]
    .astype("string")
    .str.strip()
)


# --------------------------------------------------
# Round KPI values
# --------------------------------------------------

kpi_columns = [
    "overall_score",
    "global_ranking_score",
    "research_impact_score",
    "faculty_to_student_ratio",
    "international_student_percentage",
    "academic_reputation_kpi",
    "research_productivity_index"
]

for column in kpi_columns:
    final_dataset[column] = final_dataset[column].round(2)


# --------------------------------------------------
# Rename academic reputation column
# --------------------------------------------------

final_dataset = final_dataset.rename(
    columns={
        "academic_reputation_kpi":
        "academic_reputation_score"
    }
)


# --------------------------------------------------
# Validate KPI dataset
# --------------------------------------------------

print("\nFinal KPI dataset")
print("Rows:", len(final_dataset))
print("Columns:", len(final_dataset.columns))

print("\nRanking source distribution:")
print(
    final_dataset["ranking_source"].value_counts()
)

print("\nKPI missing values:")

print(
    final_dataset[
        [
            "global_ranking_score",
            "research_impact_score",
            "faculty_to_student_ratio",
            "international_student_percentage",
            "academic_reputation_score",
            "research_productivity_index"
        ]
    ]
    .isna()
    .sum()
)

print("\nKPI summary:")

print(
    final_dataset[
        [
            "global_ranking_score",
            "research_impact_score",
            "faculty_to_student_ratio",
            "international_student_percentage",
            "academic_reputation_score",
            "research_productivity_index"
        ]
    ]
    .describe()
    .round(2)
)


# --------------------------------------------------
# Save Excel dataset
# --------------------------------------------------

final_dataset.to_excel(
    FINAL_FILE,
    index=False,
    sheet_name="Education KPIs"
)

print("\nFinal dataset created:")
print(FINAL_FILE)


# --------------------------------------------------
# Create KPI documentation report
# --------------------------------------------------

report = f"""
MODULE 3 - EDUCATION KPI ENGINEERING
=====================================

INPUT DATASETS
--------------
QS World University Rankings 2026
Universities: {len(qs_kpi)}

THE World University Rankings 2026
Universities: {len(the_kpi)}

FINAL DATASET
-------------
Total records: {len(final_dataset)}

QS records: {len(qs_final)}
THE records: {len(the_final)}

KPI DEFINITIONS
---------------

1. Global Ranking Score
Combines the ranking position score and the published overall
ranking score to create a common 0-100 ranking indicator.

2. Research Impact Score
QS:
Uses Citations per Faculty Score.

THE:
Uses Research Quality.

3. Faculty-to-Student Ratio
QS:
Uses the Faculty Student Ratio Score provided by QS.

THE:
Uses Students to Staff Ratio and converts it into a
0-100 score where a lower students-to-staff ratio receives
a higher score.

4. International Student Percentage
QS:
The supplied QS dataset provides an International Student SCORE
rather than a direct percentage. Therefore the 0-100 QS score is
used as a standardized international student indicator.

Missing QS values are replaced using the median QS indicator.

THE:
Uses the International Students percentage provided by THE.

Missing THE values are replaced using the median THE percentage.

5. Academic Reputation Score
QS:
Uses Academic Reputation Score.

THE:
Uses Teaching performance as the available academic
performance indicator in the supplied THE dataset.

6. Research Productivity Index
QS:
Average of Research Impact Score and Academic Reputation Score.

THE:
Average of Research Quality and Research Environment.

QUALITY CHECK
-------------
KPI missing values are reported during execution.

MISSING VALUE HANDLING
----------------------
Global Ranking Score:
QS records without an Overall Score use the ranking-position score
as the fallback KPI.

International Student Percentage:
Missing source values are filled using the median value of the
corresponding ranking source.

All final KPI fields are validated after calculation.

OUTPUT
------
{FINAL_FILE}
"""

with open(
    KPI_REPORT,
    "w",
    encoding="utf-8"
) as file:
    file.write(report)

print("\nKPI report created:")
print(KPI_REPORT)

print("\nModule 3 completed successfully.")