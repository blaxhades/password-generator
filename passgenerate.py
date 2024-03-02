from random import *
import string

letter = string.ascii_letters
digits = string.digits
special_char = string.punctuation

alphabet = letter + digits + special_char

pwd = ''
pwd_length = int(input("Length Password : "))

for i in range(pwd_length):
    pwd += ''.join(choice(alphabet))

print("\033[1;32mPassword \033[0m:","\033[1;31m",pwd,"\033[0m")
