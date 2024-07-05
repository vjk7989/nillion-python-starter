import pandas as pd
import numpy as np

# Try importing nada from nada_dsl, if fails print available attributes
try:
    from nada_dsl import nada
except ImportError as e:
    import nada_dsl
    print("ImportError:", e)
    print("Available attributes in nada_dsl:", dir(nada_dsl))
    nada = None  # Handle the case where nada is not available

# Define Sample Sales Data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Product': np.random.choice(['Product A', 'Product B', 'Product C'], size=100),
    'Sales_Amount': np.random.randint(100, 1000, size=100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], size=100)
}
sales_data = pd.DataFrame(data)

if nada:
    # Clean and Prepare Data
    @nada
    def clean_sales_data(df):
        df['Sales_Amount'] = df['Sales_Amount'].fillna(df['Sales_Amount'].mean())
        df['Date'] = pd.to_datetime(df['Date'])
        return df

    cleaned_sales_data = clean_sales_data(sales_data)
else:
    # Fallback to manual cleaning if nada is not available
    cleaned_sales_data = sales_data.copy()
    cleaned_sales_data['Sales_Amount'] = cleaned_sales_data['Sales_Amount'].fillna(cleaned_sales_data['Sales_Amount'].mean())
    cleaned_sales_data['Date'] = pd.to_datetime(cleaned_sales_data['Date'])

print("Cleaned Sales Data:")
print(cleaned_sales_data.head())

# Analyze Sales Trend Over Time
if nada:
    @nada
    def sales_trend_over_time(df):
        sales_trend = df.groupby('Date')['Sales_Amount'].sum().reset_index()
        return sales_trend

    sales_trend = sales_trend_over_time(cleaned_sales_data)
else:
    sales_trend = cleaned_sales_data.groupby('Date')['Sales_Amount'].sum().reset_index()

print("Sales Trend Over Time:")
print(sales_trend.head())

# Analyze Sales by Product
if nada:
    @nada
    def sales_by_product(df):
        sales_product = df.groupby('Product')['Sales_Amount'].sum().reset_index()
        return sales_product

    sales_product = sales_by_product(cleaned_sales_data)
else:
    sales_product = cleaned_sales_data.groupby('Product')['Sales_Amount'].sum().reset_index()

print("Sales by Product:")
print(sales_product)

# Analyze Sales by Region
if nada:
    @nada
    def sales_by_region(df):
        sales_region = df.groupby('Region')['Sales_Amount'].sum().reset_index()
        return sales_region

    sales_region = sales_by_region(cleaned_sales_data)
else:
    sales_region = cleaned_sales_data.groupby('Region')['Sales_Amount'].sum().reset_index()

print("Sales by Region:")
print(sales_region)
