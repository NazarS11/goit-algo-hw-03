from datetime import datetime as dtdt

def get_days_from_today(date):
    try:
# converting the current date to the "date only" datetime type
        current_date = dtdt.now().date()
# converting the specified date to the datetime type "date only"
        formated_date = dtdt.strptime(date, "%Y-%m-%d").date()
        delta = formated_date - current_date
        print (delta.days)
# returning the date difference in the "day only" format
        return delta.days
# date variable error exception
    except ValueError:
        print(f"Not valid format for \"{date}\" variable, please try again with the following format \"yyyy-mm-dd\"")

get_days_from_today("2024.01.05")
