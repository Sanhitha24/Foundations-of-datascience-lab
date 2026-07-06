import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Automobile_data.csv")
print("\nNumeric Attributes")
numeric = df.select_dtypes(include=['int64', 'float64']).columns
print(numeric)

print("\nNominal Attributes")
nominal = ['make', 'fuel-type', 'body-style', 'drive-wheels']
print(nominal)

print("\nBinary Attributes")
binary = ['aspiration', 'two-or-three']
print(binary)