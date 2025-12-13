import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Filter and Prepare Fertilizer Data ---
df_fert = pd.read_csv('fertilizers.csv')

# Filter for China, Agricultural Use, and Nitrogen
df_nitrogen = df_fert[
    (df_fert['Area'] == 'China') &
    (df_fert['Element'] == 'Agricultural Use') &
    (df_fert['Item'] == 'Nutrient nitrogen N (total)')
].copy()

# Select and rename columns
df_nitrogen = df_nitrogen[['Year', 'Value']].rename(columns={'Value': 'Nitrogen Use (t)'})

# --- 2. Filter and Prepare Crop Yield Data ---
df_agri = pd.read_csv('analyzed_agricultural_data.csv')

# Filter for China, mainland, Yield, and Wheat
df_yield = df_agri[
    (df_agri['Area'].isin(['China, mainland', 'China'])) & # Aligning areas
    (df_agri['Element'] == 'Yield') &
    (df_agri['Item'] == 'Wheat')
].copy()

# Select and rename columns
df_yield = df_yield[['Year', 'Value']].rename(columns={'Value': 'Wheat Yield (kg/ha)'})

# --- 3. Merge DataFrames ---
df_merged = pd.merge(df_nitrogen, df_yield, on='Year', how='inner')

# Ensure 'Year' is integer and sort
df_merged['Year'] = df_merged['Year'].astype(int)
df_merged.sort_values(by='Year', inplace=True)

# --- 4. Visualization (Dual-Axis Line Chart) ---

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Nitrogen Use on the primary Y-axis (ax1)
color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('Nitrogen Use (Metric Tonnes)', color=color)
line1 = ax1.plot(df_merged['Year'], df_merged['Nitrogen Use (t)'], color=color, label='Nitrogen Use')
ax1.tick_params(axis='y', labelcolor=color)
ax1.ticklabel_format(style='plain', axis='y') # Prevent scientific notation

# Create a secondary Y-axis (ax2) for Wheat Yield
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Wheat Yield (kg/ha)', color=color)
line2 = ax2.plot(df_merged['Year'], df_merged['Wheat Yield (kg/ha)'], color=color, label='Wheat Yield')
ax2.tick_params(axis='y', labelcolor=color)

# Combine legends
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

# Title and Grid
plt.title('Nitrogen Fertilizer Use vs. Wheat Yield in China (1961-2022)')
ax1.grid(True, linestyle='--', alpha=0.6)

# Save the plot
plt.savefig('china_nitrogen_yield_dual_axis.png')
plt.close()