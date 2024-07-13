
import pandas as pd
import scipy.stats as stats

# Load the cleaned data
data = pd.read_csv('cleaned_data.csv')

# Example: Perform a t-test
group1 = data[data['Frequency'] == 33.33]['Fatigue_Life']
group2 = data[data['Frequency'] == 50.00]['Fatigue_Life']

t_stat, p_val = stats.ttest_ind(group1, group2)
print(f"T-statistic: {t_stat}, P-value: {p_val}")
