import pandas as pd
import unittest
import pandas as pd
from Revenue import *

class TestOrderProcessing(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'order_id': [1, 2, 3, 4, 5],
            'customer_id': [101, 102, 103, 101, 102],
            'order_date': ['2022-01-01', '2022-01-15', '2022-02-01', '2022-03-01', '2022-03-15'],
            'product_id': [1, 2, 3, 4, 5],
            'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
            'product_price': [10.0, 15.0, 10.0, 5.0, 15.0],
            'quantity': [2, 1, 3, 4, 2]
            })
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])
        self.df['revenue'] = self.df['product_price'] * self.df['quantity']


    def test_monthly_revenue(self):
        # Compute expected results
        expected_revenue = pd.Series([35.0,30.0,50.0], name='revenue', index=pd.date_range('2022-01-31', '2022-03-31', freq='M'))
        # Compute actual results
        actual_revenue =CalcRevenueByMonth(self.df)   # self.df.groupby(pd.Grouper(key='order_date', freq='M'))['revenue'].sum()
        # Compare expected and actual results
        self.assertTrue(expected_revenue.equals(actual_revenue))

    def test_product_revenue(self):
        # Compute expected results
        expected_revenue = pd.Series([50.0, 45.0, 20.0], name='revenue', index=['Product A', 'Product B', 'Product C'])

        # Compute actual results
        actual_revenue = CalcRevenuePerProduct(self.df)
        print(actual_revenue)
        # Compare expected and actual results
        self.assertTrue(expected_revenue.equals(actual_revenue))

    def test_customer_revenue(self):
        # Compute expected results
        expected_revenue = pd.Series([40.0,45.0,30.0], name='revenue', index=[101, 102, 103])

        # Compute actual results
        #self.df['revenue'] = self.df['product_price'] * self.df['quantity']
        actual_revenue = CalcRevenueByCustomer(self.df) #self.df.groupby('customer_id')['revenue'].sum()
        print(actual_revenue)
        # Compare expected and actual results
        self.assertTrue(expected_revenue.equals(actual_revenue))

    def test_top_customers(self):
        # Compute expected results
        expected_top_customers = pd.Series([40.0,45.0,30.0], name='revenue', index=[101,102,103]).nlargest(3)
        print(expected_top_customers)
        # Compute actual results
        actual_top_customers = CalcTopTENCust(self.df)
        print(actual_top_customers)
        # Compare expected and actual results
        self.assertTrue(expected_top_customers.equals(actual_top_customers))

if __name__ == '__main__':
    unittest.main()
