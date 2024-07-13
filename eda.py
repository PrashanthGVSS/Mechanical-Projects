
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
data = pd.read_csv('cleaned_data.csv')

# Summary statistics
print(data.describe())

# Pairplot to see the relationships between variables
sns.pairplot(data)
plt.savefig('pairplot.png')
plt.show()

# Correlation matrix
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.savefig('correlation_matrix.png')
plt.show()
