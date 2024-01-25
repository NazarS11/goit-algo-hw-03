from datetime import datetime as dtdt

def get_days_from_today(date):
    current_date = dtdt.now().date()
    formated_date = dtdt.strptime(date, "%Y-%m-%d").date()
    delta = formated_date - current_date
    print (delta.days)
    return delta.days

get_days_from_today("2024-01-05")
