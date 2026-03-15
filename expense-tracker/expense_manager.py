def add_expense(expese_data:dict, key:str, value:float):
    try:
        expese_data[key] += value
    except KeyError:
        expese_data[key] = value
    return expese_data

def total_expense(expense_data:dict):
    total = 0
    for value in expense_data.values():
        total += value
    return total

def average_expense(total, length):
    return total/length

