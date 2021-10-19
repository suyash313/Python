# Python PassWord generator

import random
import string

password = []
string.digits = "1234567890" # Numbers for your password
string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # Alphabets for your password
string.ascii_letters2 = "!@#$%^&*+=/|;:.,?" # Symbols for your password


def num():
    for i in range(4):
        password.append(random.choice(string.digits))


def letter():
    for i in range(4):
        password.append(random.choice(string.ascii_letters))


def signs():
    for i in range(8):
        password.append(random.choice(string.ascii_letters2))

num()
letter()
signs()

for q in range(len(password)-1, 0, -1):
    j = random.randint(0, q+1)
    password[q], password[j] = password[j], password[q]

print("Your password is : ", end="") # final result
print("".join(password))

