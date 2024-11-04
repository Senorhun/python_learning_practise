from datetime import datetime, timedelta

def find_palindromic_dates(year):
    start_date = datetime(year, 1, 1, 0, 0, 0)
    end_date = datetime(year, 12, 31, 23, 59, 59)
    
    palindromic_dates = []

    current_time = start_date
    while current_time <= end_date:
        formatted_time = current_time.strftime("%Y%m%d%H%M%S")
        
        if formatted_time == formatted_time[::-1]:
            palindromic_dates.append(current_time)
        
        current_time += timedelta(seconds=1)
    
    return palindromic_dates

year = 2022
palindromic_dates = find_palindromic_dates(year)
for date in palindromic_dates:
    print(date.strftime("%Y.%m.%d %H:%M:%S"))
