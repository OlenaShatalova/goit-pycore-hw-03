import re

# Варіант не зовсім по флоу вимог до д.з., але враховує випадки, коли "+"
# може випадково бути всередині номера телефона, або більше 1 разу
def normalize_phone(phone_number: str) -> str:
    digits = re.sub(r'[^\d]', "", phone_number)
    if digits.startswith("380"):
        normalized = digits
    elif digits.startswith("0"):
        normalized = "38" + digits
    else:
        normalized = digits
    return "+" + normalized

# print(normalize_phone("++0-1-2345_6789"))

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 456+7",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
