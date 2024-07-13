
import pandas as pd

# Load the data from the Excel file
file_path = 'MECH.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataset
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Clean the data (if needed)
# Example: Fill missing values or drop unnecessary columns
data = data.dropna()

# Save the cleaned data to a new file
data.to_csv('cleaned_data.csv', index=False)
