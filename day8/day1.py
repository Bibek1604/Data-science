import pandas as pd
import matplotlib as plt

# Load your DataFrame
df = pd.read_csv('data.csv')

# Finding duplicates
findingduplicates = df[df.duplicated()]  # Fix: add parentheses to call duplicated()
findingduplicates.to_csv('duplicates.csv', index=False)

# Cleaning the missing data by dropping duplicates
cleaning = df.drop_duplicates()  # Drops duplicate rows
cleaning.to_csv('cleaned.csv', index=False)

# Finding missing values
missing = df.isnull()  # Check for missing values
column = df.columns[df.isnull().any()].to_list()  # Get columns with missing values
rows = df[df.isnull().any(axis=1)]  # Get rows with any missing values

# Print the columns with missing values
print("Columns with missing values:", column)

# Print the rows with missing values
print("Rows with missing values:")
print(rows)

# Saving the rows with missing values to a CSV file
rows.to_csv("rows_missing.csv", index=False)

# Saving the columns with missing values to a CSV file (Convert list to DataFrame for saving)
column_df = pd.DataFrame(column, columns=['Columns with Missing Values'])
column_df.to_csv("columns_missing.csv", index=False)



df_cleaned=df.dropna()
df_cleaned=df_cleaned.drop_duplicates() 
df_cleaned.to_csv("cleaned datas.csv",index=False)
print("data has been cleansded")

import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
df_original = pd.read_csv("data.csv")
df_cleaned = pd.read_csv("cleaned datas.csv")

# Subplot layout: 2 rows, 2 columns
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('🧹 Data Cleaning Summary Dashboard', fontsize=16)

plt.figure(figsize=(6, 4))
plt.bar(['Original Data', 'Cleaned Data'], [len(df_original), len(df_cleaned)], color=['salmon', 'mediumseagreen'])
plt.title('📊 Number of Rows: Original vs Cleaned')
plt.ylabel('Total Rows')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
