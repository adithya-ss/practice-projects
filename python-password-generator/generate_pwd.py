import random
import string

print("*************************************************")
print("     P A S S W O R D     G E N E R A T O R       ")
print("*************************************************")

chrs_in_pwd = string.ascii_letters + string.digits + string.punctuation

number_of_passwords = input("How many passwords do you want to generate?: ")
number_of_passwords = int(number_of_passwords)

password_length = input("How long should the passwords be?: ")
password_length = int(password_length)

print("***************")
print("Your passwords:")
print("***************")

for each_password in range(number_of_passwords):
    pwds = ''
    for ch in range(password_length):
        pwds += random.choice(chrs_in_pwd)
    print(pwds)