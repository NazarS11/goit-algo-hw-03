import re

def normalize_phone(phone_number):
    pattern = r"[^0-9]"
    replacement = ""
# substitute all symbols except numbers with "", take last 10 charaters and add +380 at the beginning 
    return ('+380' + (re.sub(pattern, replacement, phone_number))[-9:])

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)