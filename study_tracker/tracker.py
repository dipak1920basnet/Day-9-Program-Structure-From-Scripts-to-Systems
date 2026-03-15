def add_study_hours(study_hours:dict, day:str, hours):
    
    try:
        study_hours[day] += hours 
    except KeyError:
        study_hours[day] = 0
    return study_hours
    

def calculate_total_hours(study_hours:dict):
    
    total = 0
    for value in study_hours.values():
        total += value

    return total

def average(total, length):
    averages = total/length
    print(averages)

def build_dict(dicts, days_list):
    for i in days_list:
        dicts[i] = 0
    return dicts
