import pandas as pd

def CalcRevenueByMonth(df):
    """
    Compute the total revenue generated by the online store for each month and returns the value
    """
    revenue_by_month = df.groupby(pd.Grouper(key='order_date', freq='M'))['revenue'].sum()
    return revenue_by_month

def CalcRevenuePerProduct(df):
    """
    This method computes the total revenue generated by each product and returns the result
    Input Type: dataframe
    return Type: Series
    """
    revenue_by_product = df.groupby('product_name')['revenue'].sum()
    return revenue_by_product

def CalcRevenueByCustomer(df):
    """
    This method used to Compute the total revenue generated by each customer and return the result
    Input Type: Pandas DataFrame
    Return Type: Series
    """
    revenue_by_customer = df.groupby('customer_id')['revenue'].sum()
    return revenue_by_customer

def CalcTopTENCust(df):
    """
    This method used to Identify the top 10 customers by revenue generated from each customer and return the result
    InputType: Pandas Series
    returnType: Series
    """
    revenue_by_customer = CalcRevenueByCustomer(df)
    top_10_customers = revenue_by_customer.sort_values(ascending=False).head(10)
    return top_10_customers

if __name__ == '__main__':
    # Read the data from the CSV file
    orders_df = pd.read_csv('orders.csv')
    # Convert order_date column to datetime format
    orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])
    #Calculating the revenue generated from each order
    orders_df['revenue'] = orders_df['product_price'] * orders_df['quantity']
    #Printing the results
    print("Revenue By Month:\n", CalcRevenueByMonth(orders_df))
    print("\nRevenue By Product:\n",CalcRevenuePerProduct(orders_df))
    print("\nRevenue per Customer:\n",CalcRevenueByCustomer(orders_df))
    print("\nTop 10 Customers:\n", CalcTopTENCust(orders_df))


