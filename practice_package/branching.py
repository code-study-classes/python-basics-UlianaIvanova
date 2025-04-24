def is_weekend(day):
    return day in (6, 7)

def get_discount(amount):
    if amount >= 5000:
        return round(amount * 0.10, 2)
    elif amount >= 1000:
        return round(amount * 0.05, 2)
    return 0.0

def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    if n < 10:
        digits = "однозначное"
    elif n < 100:
        digits = "двузначное"
    else:
        digits = "трехзначное"
    return f"{parity} {digits} число"

def convert_to_meters(unit, length):
    multipliers = {
        1: 0.1,    
        2: 1000,    
        3: 1,       
        4: 0.001,
        5: 0.01     
    }
    return length * multipliers.get(unit, 0)

def describe_age(age):
    units = ["", "один", "два", "три", "четыре", "пять", 
             "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать",
             "четырнадцать", "пятнадцать", "шестнадцать", 
             "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят",
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    
    if age % 100 in range(10, 20):
        word = "лет"
    else:
        last_digit = age % 10
        word = "год" if last_digit == 1 else "года" if last_digit in (2,3,4) else "лет"
    
    if age == 100:
        return "сто лет"
    elif age < 10:
        return f"{units[age]} {word}"
    elif age < 20:
        return f"{teens[age-10]} {word}"
    else:
        ten, unit = divmod(age, 10)
        return f"{tens[ten]} {units[unit]} {word}".replace("  ", " ").strip()