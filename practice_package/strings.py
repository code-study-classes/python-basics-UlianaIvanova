import os

def extract_file_name(full_file_name):
    base = os.path.basename(full_file_name)
    return os.path.splitext(base)[0]

def encrypt_sentence(sentence):
    even_chars = []
    odd_chars = []
    for i, char in enumerate(sentence):
        if i % 2 == 1:  
            even_chars.append(char)
        else:
            odd_chars.append(char)
    return ''.join(even_chars + odd_chars[::-1])

def check_brackets(expression):
    stack = []
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                return i
            stack.pop()
    return -1 if stack else 0

def reverse_domain(domain):
    parts = domain.split('.')
    return '.'.join(reversed(parts))

def count_vowel_groups(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    in_vowel_group = False
    for char in word.lower():
        if char in vowels:
            if not in_vowel_group:
                count += 1
                in_vowel_group = True
        else:
            in_vowel_group = False
    return count