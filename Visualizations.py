import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(data_file):
    # Load data
    df = pd.read_csv(data_file)
    
    # 1. Initial exploration
    print("=== Dataset Overview ===")
    print(f"Shape: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nData Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # 2. Statistical summary
    print("\n=== Statistical Summary ===")
    print(df.describe(include='all'))
    
    # 3. Visual exploration
    plt.figure(figsize=(12, 6))
    
    # Numeric variables distribution
    numeric_cols = df.select_dtypes(include=np.number).columns
    if len(numeric_cols) > 0:
        print("\n=== Numeric Variables Distribution ===")
        df[numeric_cols].hist(bins=20, figsize=(12, 8))
        plt.tight_layout()
        plt.show()
    
    # Categorical variables
    cat_cols = df.select_dtypes(include='object').columns
    if len(cat_cols) > 0:
        print("\n=== Categorical Variables Distribution ===")
        for col in cat_cols:
            plt.figure(figsize=(8, 4))
            sns.countplot(data=df, x=col)
            plt.title(f"Distribution of {col}")
            plt.xticks(rotation=45)
            plt.show()
    
    # Correlation matrix for numeric variables
    if len(numeric_cols) > 1:
        print("\n=== Correlation Matrix ===")
        plt.figure(figsize=(10, 8))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Matrix")
        plt.show()
    
    # Identify potential outliers
    if len(numeric_cols) > 0:
        print("\n=== Boxplots for Outlier Detection ===")
        for col in numeric_cols:
            plt.figure(figsize=(8, 4))
            sns.boxplot(data=df, y=col)
            plt.title(f"Boxplot of {col}")
            plt.show()

# Example usage
data_file = "scraped_data.csv"  # Or your dataset
perform_eda(data_file)