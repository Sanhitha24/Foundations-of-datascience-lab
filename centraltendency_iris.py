from sklearn.datasets import load_iris
import pandas as pd

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Check for null values
print("\nNull Values in Each Column:")
print(df.isnull().sum())

# Mean
print("\nMean:")
print(df.mean())

print("\nMedian:")
print(df.median())

print("\nMode:")
print(df.mode().iloc[0])