work_hours = [('Abby',1000),('Billy',500),('Cassie',800)]

def employee_check(work_hours):
    current_max = 0
    current_name = ''
    for name,hours in work_hours:
        if hours > current_max:
            current_max = hours
            current_name = name
        else:
            pass
    return(current_name,current_max)

results = employee_check(work_hours)

name,hours = results

hours_statement = f"{name} is the Employee of the Month and worked for a total of {hours} hours!"
print(hours_statement)
