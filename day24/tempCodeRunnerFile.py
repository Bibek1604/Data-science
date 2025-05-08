import pandas as pd

# Load the CSV file
file_path = r'F:\111\resources\happiest.csv'
df = pd.read_csv(file_path)

# Show original shape
print("Original shape:", df.shape)

# Replace string 'None' with actual NaN for processing
df.replace('None', pd.NA, inplace=True)

# Convert columns to numeric if needed (ignoring errors for non-convertible values)
df['HappiestCountriesWorldHappinessReportRankings2024'] = pd.to_numeric(df['HappiestCountriesWorldHappinessReportRankings2024'], errors='coerce')
df['HappiestCountriesWorldHappinessReportScore2024'] = pd.to_numeric(df['HappiestCountriesWorldHappinessReportScore2024'], errors='coerce')

# Remove rows where any of the two columns have 0 or are missing (NaN)
df_cleaned = df[
    (df['HappiestCountriesWorldHappinessReportRankings2024'] != 0) &
    (df['HappiestCountriesWorldHappinessReportScore2024'] != 0) &
    (df['HappiestCountriesWorldHappinessReportRankings2024'].notna()) &
    (df['HappiestCountriesWorldHappinessReportScore2024'].notna())
]

# Show cleaned shape
print("Cleaned shape:", df_cleaned.shape)

# Save cleaned data back to CSV (optional)
df_cleaned.to_csv(r'F:\111\resources\happiest_cleaned.csv', index=False)
