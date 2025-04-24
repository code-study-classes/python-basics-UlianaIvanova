def sum_even_digits(number):
    number = abs(number)
    total = 0
    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            total += digit
        number = number // 10
    return total

def count_vowel_triplets(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    text = text.lower()
    i = 0
    while i < len(text) - 2:
        if (text[i] in vowels and 
            text[i+1] in vowels and 
            text[i+2] in vowels):
            count += 1
            i += 2  
        else:
            i += 1
    return count

def find_fibonacci_index(number):
    if number < 1:
        return -1
    if number == 1:
        return 1
    a, b = 1, 1
    index = 2
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1

def remove_duplicates(string):
    if not string:
        return ""
    result = string[0]
    for char in string[1:]:
        if char != result[-1]:
            result += char
    return result