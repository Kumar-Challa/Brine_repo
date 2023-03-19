# Brine Task 

# 1.The code in 'Revenue.py' gives the following
    Revenue By Month:
    order_date
    2022-01-31     50
    2022-02-28    250
    2022-03-31     70
    2022-04-30    180
    2022-05-31    140
    2022-06-30    110
    Freq: M, Name: revenue, dtype: int64

    Revenue By Product:
    product_name
    Product A    280
    Product B    160
    Product C    360
    Name: revenue, dtype: int64

    evenue per Customer:
    customer_id
    C1    100
    C2    160
    C3    180
    C4    360
    Name: revenue, dtype: int64

# 2.The output of Testcases.py
    customer_id
    101    40.0
    102    45.0
    103    30.0
    Name: revenue, dtype: float64
    ..product_name
    Product A    50.0
    Product B    45.0
    Product C    20.0
    Name: revenue, dtype: float64
    102    45.0
    101    40.0
    103    30.0
    Name: revenue, dtype: float64
    customer_id
    102    45.0
    101    40.0
    103    30.0
    Name: revenue, dtype: float64
    .
    ----------------------------------------------------------------------
    Ran 4 tests in 0.023s

    OK

#   To create docker images use the following commands
    docker build --tag test:v1 -f Dockerfile_test .
    docker build --tag python_task:v1 .