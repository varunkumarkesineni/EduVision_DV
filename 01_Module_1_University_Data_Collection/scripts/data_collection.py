import pandas as pd
from pathlib import Path

# University Data Collection

# Get the project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Define data folders
RAW_DIR = BASE_DIR / "Data" / "Raw Data"
PROCESSED_DIR = BASE_DIR / "Data" / "Processed Data"

# Create processed data folder
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Define mentor-provided datasets
QS_FILE = RAW_DIR / "2026_QS_World University_Rankings.csv"
THE_FILE = RAW_DIR / "THE World University Rankings 2026.xlsx"

# Check the dataset files
print("=" * 70)
print("MODULE 1: UNIVERSITY DATA COLLECTION")
print("=" * 70)

if not QS_FILE.exists():
    print("QS dataset not found:")
    print(QS_FILE)
    raise SystemExit

if not THE_FILE.exists():
    print("THE dataset not found:")
    print(THE_FILE)
    raise SystemExit

print("\nBoth mentor-provided datasets were found.")

# Load QS dataset
print("\nLoading QS World University Rankings...")
qs = pd.read_csv(QS_FILE)

print("QS rows:", len(qs))
print("QS columns:", len(qs.columns))

# Load THE dataset
print("\nLoading THE World University Rankings...")
the = pd.read_excel(THE_FILE)

print("THE rows:", len(the))
print("THE columns:", len(the.columns))

# Rename QS columns
qs = qs.rename(columns={
    "Name": "university_name",
    "Country/Territory": "country",
    "Rank": "rank",
    "Overall SCORE": "score"
})

# Rename THE columns
the = the.rename(columns={
    "Name": "university_name",
    "Country": "country",
    "Rank": "rank",
    "Overall Score": "score"
})

# Select common QS fields
qs_data = qs[
    [
        "university_name",
        "country",
        "rank",
        "score"
    ]
].copy()

# Select common THE fields
the_data = the[
    [
        "university_name",
        "country",
        "rank",
        "score"
    ]
].copy()

# Add ranking year
qs_data["year"] = 2026
the_data["year"] = 2026

# Add ranking source
qs_data["ranking_source"] = "QS"
the_data["ranking_source"] = "THE"

# Remove extra spaces from text fields
for dataframe in [qs_data, the_data]:

    dataframe["university_name"] = (
        dataframe["university_name"]
        .astype("string")
        .str.strip()
    )

    dataframe["country"] = (
        dataframe["country"]
        .astype("string")
        .str.strip()
    )

# Define the common structure
common_columns = [
    "university_name",
    "country",
    "year",
    "ranking_source",
    "rank",
    "score"
]

# Arrange both datasets using the same structure
qs_data = qs_data[common_columns]
the_data = the_data[common_columns]

# Combine QS and THE
university_raw_data = pd.concat(
    [qs_data, the_data],
    ignore_index=True
)

# Remove exact duplicate records
university_raw_data = university_raw_data.drop_duplicates()

# Check the combined dataset
print("\nCombined dataset")
print("Rows:", len(university_raw_data))
print("Columns:", len(university_raw_data.columns))

# Check duplicate records
duplicate_count = university_raw_data.duplicated().sum()

print("\nDuplicate rows:", duplicate_count)

# Check missing values
print("\nMissing values:")

missing_values = university_raw_data.isna().sum()

print(missing_values)

# Calculate completeness using required fields
required_columns = [
    "university_name",
    "country",
    "year",
    "ranking_source",
    "rank",
    "score"
]

total_cells = (
    len(university_raw_data) *
    len(required_columns)
)

missing_cells = (
    university_raw_data[required_columns]
    .isna()
    .sum()
    .sum()
)

completeness = (
    1 - (missing_cells / total_cells)
) * 100

print("\nDataset completeness:", round(completeness, 2), "%")

# Check source distribution
print("\nRecords by ranking source:")

print(
    university_raw_data["ranking_source"]
    .value_counts()
)

# Save the raw integrated dataset
output_file = (
    PROCESSED_DIR /
    "university_raw_data.csv"
)

university_raw_data.to_csv(
    output_file,
    index=False
)

print("\nOutput file created:")
print(output_file)

# Final Module 1 status
print("\nModule 1 completed successfully.")

if completeness >= 95:
    print("Completeness requirement: PASSED")
else:
    print("Completeness requirement: NOT PASSED")

if duplicate_count == 0:
    print("Duplicate requirement: PASSED")
else:
    print("Duplicate requirement: CHECK REQUIRED")