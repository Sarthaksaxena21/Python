import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def clean_numeric(val):
    if pd.isna(val): return np.nan
    s = str(val).strip().replace('(', '').replace(')', '').replace('*', '')
    try: return float(s)
    except: return np.nan

def load_and_clean(filepath):
    df = pd.read_csv(filepath)
    cols_to_fix = [
        'Women (age 15-49) who are literate4 (%)',
        'Total Fertility Rate (number of children per woman)',
        'Women (age 15-49)  who have ever used the internet (%)',
        'Women age 20-24 years married before age 18 years (%)',
        'Institutional births (in the 5 years before the survey) (%)'
    ]
    for col in cols_to_fix:
        df[col] = df[col].apply(clean_numeric)
    return df

if __name__ == "__main__":
    df = load_and_clean('data/datafile.csv')
    plot_df = df[(df['States/UTs'] != 'India') & (df['Area'] == 'Total')]
    
    # 1. Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(plot_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.savefig('heatmap.png')
    
    # Add other plotting functions here...
    print("Analysis complete. Graphs saved as PNG files.")
