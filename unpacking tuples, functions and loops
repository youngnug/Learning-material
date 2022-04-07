#unpacking tuples
stock_prices = [('APPL',200), ('GOOG',400), ('MSFT',100)]
print(stock_prices)

for items in stock_prices:
    print(items)

for ticker,price in stock_prices:
    print(ticker)
#who works the most hours function  
work_hours = [('Abby',100), ('Billy',400), ('Cassie', 800)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours>current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return(employee_of_month,current_max)
print(employee_check(work_hours))
#or
result = employee_check(work_hours)
print(result)
#or unpack
employee,hours = employee_check(work_hours)
print(employee)
print(hours)
