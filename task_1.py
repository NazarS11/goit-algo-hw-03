from datetime import datetime as dtdt

def get_days_from_today(date):
    #приведення поточної дати до типу datetime "тільки дата"
    current_date = dtdt.now().date()
    #приведення заданої дати до типу datetime "тільки дата"
    formated_date = dtdt.strptime(date, "%Y-%m-%d").date()
    delta = formated_date - current_date
    print (delta.days)
    #повернення різниці дат в форматі "тільки день"
    return delta.days

get_days_from_today("2024-01-05")
