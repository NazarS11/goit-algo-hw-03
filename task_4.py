from datetime import datetime as dtdt
from datetime import timedelta as td

def get_upcoming_birthdays(list):
    today = dtdt.now().date()
    congrat_list = []   #empty list for future result list
    for user in users:
# birthday string parse to datetime
        birthday_date = dtdt.strptime(user["birthday"], "%Y.%m.%d").date() 
# convert birth date into latest birthday date
        latest_birth_date = dtdt(today.year, birthday_date.month, birthday_date.day).date()
# check if latest birthday date meets condition
        if today < latest_birth_date and (latest_birth_date - today).days < 8:
# adding to the resulting list and correcting if the day of congratulations falls on a saturday  
            if latest_birth_date.weekday() == 6:
                congrat_list.append({'name':user['name'],'congratulation_date':(latest_birth_date + td(days=1)).strftime("%Y.%m.%d")})
# adding to the resulting list and correcting if the day of congratulations falls on a sunday
            elif latest_birth_date.weekday() == 5:
                congrat_list.append({'name':user['name'],'congratulation_date':(latest_birth_date + td(days=2)).strftime("%Y.%m.%d")})
# adding to the resulting list if the birthday falls on a working day
            else:
                congrat_list.append({'name':user['name'],'congratulation_date':latest_birth_date.strftime("%Y.%m.%d")})
    print(congrat_list)
    return congrat_list

users = [
    {"name": "John Lenon", "birthday": "1994.01.24"},
    {"name": "John Doe", "birthday": "1985.01.26"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Bill Murphy", "birthday": "1994.01.28"},
    {"name": "Jimm Carrey", "birthday": "1994.02.01"}
]
get_upcoming_birthdays(users)