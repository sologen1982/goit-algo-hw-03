from datetime import datetime


def get_days_from_today(date):
    
    date_now = datetime.today()
    
    try:
        current_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(f'{date} is wrong input, enter date in format JJJJ-MM-DD')
    else:
        difference = date_now.toordinal() - current_date.toordinal()
                
        return (difference)

result = get_days_from_today("2024-02-01")

print(f'Difference between dates is {result} days')

