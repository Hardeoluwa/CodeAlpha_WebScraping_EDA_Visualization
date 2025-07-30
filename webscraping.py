import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(data_file):
    # Load data
    df = pd.read_csv(data_file)
    
    # Set style
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # 1. Line Chart (for trends over time)
    if 'date' in df.columns:  # Adjust column name
        plt.figure(figsize=(12, 6))
        df.plot(x='date', y='value', kind='line')  # Adjust column names
        plt.title("Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    # 2. Bar Chart (for categorical comparisons)
    categorical_var = df.select_dtypes(include='object').columns[0] if len(df.select_dtypes(include='object').columns) > 0 else None
    numeric_var = df.select_dtypes(include=np.number).columns[0] if len(df.select_dtypes(include=np.number).columns) > 0 else None
    
    if categorical_var and numeric_var:
        plt.figure(figsize=(12, 6))
        sns.barplot(data=df, x=categorical_var, y=numeric_var)
        plt.title(f"{numeric_var} by {categorical_var}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    # 3. Scatter Plot (for relationships)
    numeric_cols = df.select_dtypes(include=np.number).columns
    if len(numeric_cols) >= 2:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=numeric_cols[0], y=numeric_cols[1], hue=categorical_var if categorical_var else None)
        plt.title(f"Relationship between {numeric_cols[0]} and {numeric_cols[1]}")
        plt.tight_layout()
        plt.show()
    
    # 4. Pie Chart (for proportions)
    if categorical_var:
        plt.figure(figsize=(8, 8))
        df[categorical_var].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title(f"Proportion of {categorical_var}")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()
    
    # 5. Advanced: Pairplot for multivariate analysis
    if len(numeric_cols) > 1:
        sns.pairplot(df[numeric_cols])
        plt.suptitle("Pairwise Relationships", y=1.02)
        plt.tight_layout()
        plt.show()

# Example usage
data_file = "scraped_data.csv"  # Or your dataset
create_visualizations(data_file)