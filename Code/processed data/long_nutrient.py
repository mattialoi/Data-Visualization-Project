import pandas as pd

# If reading from a CSV file:
df = pd.read_csv('nutrients.csv')


# First, melt the data to long format
df_long = df.melt(
    id_vars=['Entity', 'Code', 'Year'],
    var_name='Nutrient',
    value_name='Tonnes'
)

# Then pivot to have years as columns and nutrients as rows
df_pivot = df_long.pivot_table(
    index=['Entity', 'Code', 'Nutrient'],
    columns='Year',
    values='Tonnes'
).reset_index()

# Sort the years in ascending order
df_pivot = df_pivot.reindex(sorted(df_pivot.columns, key=lambda x: x if isinstance(x, int) else 0), axis=1)

# Reorder columns to have Entity, Code, Nutrient first
cols = ['Entity', 'Code', 'Nutrient'] + [col for col in df_pivot.columns if col not in ['Entity', 'Code', 'Nutrient']]
df_pivot = df_pivot[cols]

print(df_pivot.head())
print(f"\nShape: {df_pivot.shape}")
print(f"Years: {sorted(df['Year'].unique())}")

# Save to CSV
df_pivot.to_csv('nutrients_long_format.csv', index=False)
print("\nSaved to 'nutrients_long_format.csv'")

# Save to Excel
df_pivot.to_excel('nutrients_long_format.xlsx', index=False)
print("Saved to 'nutrients_long_format.xlsx'")