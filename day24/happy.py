# # import pandas as pd

# # # Load the CSV file
# # file_path = r'F:\111\resources\happiest.csv'
# # df = pd.read_csv(file_path)

# # # Show original shape
# # print("Original shape:", df.shape)

# # # Replace string 'None' with actual NaN for processing
# # df.replace('None', pd.NA, inplace=True)

# # # Convert columns to numeric if needed (ignoring errors for non-convertible values)
# # df['HappiestCountriesWorldHappinessReportRankings2024'] = pd.to_numeric(df['HappiestCountriesWorldHappinessReportRankings2024'], errors='coerce')
# # df['HappiestCountriesWorldHappinessReportScore2024'] = pd.to_numeric(df['HappiestCountriesWorldHappinessReportScore2024'], errors='coerce')

# # # Remove rows where any of the two columns have 0 or are missing (NaN)
# # df_cleaned = df[
# #     (df['HappiestCountriesWorldHappinessReportRankings2024'] != 0) &
# #     (df['HappiestCountriesWorldHappinessReportScore2024'] != 0) &
# #     (df['HappiestCountriesWorldHappinessReportRankings2024'].notna()) &
# #     (df['HappiestCountriesWorldHappinessReportScore2024'].notna())
# # ]

# # # Show cleaned shape
# # print("Cleaned shape:", df_cleaned.shape)

# # # Save cleaned data back to CSV (optional)
# # df_cleaned.to_csv(r'F:\111\resources\happiest_cleaned.csv', index=False)
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load the cleaned CSV
# file_path = r'F:\111\resources\happiest_cleaned.csv'
# df = pd.read_csv(file_path)

# # Sort by happiness score (descending for happiest, ascending for unhappiest)
# top_10 = df.sort_values(by='HappiestCountriesWorldHappinessReportScore2024', ascending=False).head(10)
# bottom_10 = df.sort_values(by='HappiestCountriesWorldHappinessReportScore2024', ascending=True).head(10)

# # Set seaborn style
# sns.set(style='whitegrid')

# # Plot Top 10 Happiest Countries
# plt.figure(figsize=(10, 6))
# sns.barplot(data=top_10, x='HappiestCountriesWorldHappinessReportScore2024', y='country', palette='Greens_r')
# plt.title('Top 10 Happiest Countries (2024)', fontsize=16)
# plt.xlabel('Happiness Score')
# plt.ylabel('Country')
# plt.tight_layout()
# plt.show()

# # Plot Bottom 10 Unhappiest Countries
# plt.figure(figsize=(10, 6))
# sns.barplot(data=bottom_10, x='HappiestCountriesWorldHappinessReportScore2024', y='country', palette='Reds')
# plt.title('Bottom 10 Unhappiest Countries (2024)', fontsize=16)
# plt.xlabel('Happiness Score')
# plt.ylabel('Country')
# plt.tight_layout()
# plt.show()
import pandas as pd
import pycountry
import pycountry_convert as pc

# Load data
file_path = r'F:\111\resources\happiest_cleaned.csv'
df = pd.read_csv(file_path)

# Helper function to map country to continent
def get_continent(country_name):
    try:
        country = pycountry.countries.lookup(country_name)
        country_alpha2 = country.alpha_2
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        return pc.convert_continent_code_to_continent_name(continent_code)
    except:
        return 'Unknown'

# Create 'Continent' column
df['Continent'] = df['country'].apply(get_continent)
import seaborn as sns
import matplotlib.pyplot as plt

# Drop unknowns if needed
df = df[df['Continent'] != 'Unknown']

# Group by continent
continent_scores = df.groupby('Continent')['HappiestCountriesWorldHappinessReportScore2024'].mean().sort_values(ascending=False)

# Bar plot
plt.figure(figsize=(10,6))
sns.barplot(x=continent_scores.values, y=continent_scores.index, palette='viridis')
plt.title('Average Happiness Score by Continent (2024)', fontsize=16)
plt.xlabel('Average Happiness Score')
plt.ylabel('Continent')
plt.tight_layout()
plt.show()
