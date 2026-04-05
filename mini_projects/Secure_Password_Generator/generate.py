import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
wired = "il1Lo0O"
chars = ''

variants = input("Сколько паролей вам нужно сгенерировать? ")
len_password = input("Какой длины должен быть пароль? ")
need_numbers = input("Нужны ли цифры? (y/n) ")
need_uppercase_letters = input("Нужны ли прописные буквы? (y/n) ")
need_lowercase_letters = input("Нужны ли строчные буквы? (y/n) ")
need_symbols = input("Нужны ли символы? (y/n) ")
need_wired_symbols = input("Исключать ли неоднозначные символы il1Lo0O? (y/n) ")

if need_numbers == "y":
    chars += digits
if need_uppercase_letters == "y":
    chars += uppercase_letters
if need_lowercase_letters == "y":
    chars += lowercase_letters
if need_symbols == "y":
    chars += punctuation
if need_wired_symbols == "y":
    for c in wired:
        chars = chars.replace(c, "")


def generate_password(len_password, chars):
    password = ''
    for i in range(len_password):
        password += random.choice(chars)
    return password

for i in range(int(variants)):
    print(generate_password(int(len_password), chars))


