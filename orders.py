import csv

# read the csv file
with open('orders.csv', 'r') as file:
    reader = csv.DictReader(file)

    # initialize dictionaries to store data
    monthly_revenue = {}
    product_revenue = {}
    customer_revenue = {}

    # iterate through each row in the csv file
    for row in reader:
        order_id = row['order_id']
        customer_id = row['customer_id']
        order_date = row['order_date']
        product_id = row['product_id']
        product_name = row['product_name']
        product_price = float(row['product_price'])
        quantity = int(row['quantity'])

        # Compute monthly revenue
        month = order_date[0:7]
        if month in monthly_revenue:
            monthly_revenue[month] += product_price * quantity
        else:
            monthly_revenue[month] = product_price * quantity

        # Compute product revenue
        if product_name in product_revenue:
            product_revenue[product_name] += product_price * quantity
        else:
            product_revenue[product_name] = product_price * quantity

        # Compute customer revenue
        if customer_id in customer_revenue:
            customer_revenue[customer_id] += product_price * quantity
        else:
            customer_revenue[customer_id] = product_price * quantity

    # Sort the dictionary by value in descending order
    top_customers = sorted(customer_revenue.items(), key=lambda x: x[1], reverse=True)[:10]

    # Print the results
    print("Monthly Revenue: ")
    for month, revenue in monthly_revenue.items():
        print(f"{month}: {revenue}")

    print("\nProduct Revenue: ")
    for product, revenue in product_revenue.items():
        print(f"{product}: {revenue}")

    print("\nCustomer Revenue: ")
    for customer, revenue in customer_revenue.items():
        print(f"{customer}: {revenue}")

    print("\nTop 10 Customers by Revenue: ")
    for i, (customer, revenue) in enumerate(top_customers):
        print(f"{i+1}. {customer} - {revenue}")