import random
import string

def pwd_generator():
    how_many = 2
    pwd_long = 20
    pwd_table = ''

    for i in range(how_many):
#    pwd_small = string.ascii_lowercase
#    pwd_big = string.ascii_uppercase
#    pwd_numbers = string.digits
#    pwd_other = string.punctuation
#    pwd_table += pwd_small + pwd_big + pwd_numbers + pwd_other
        pwd_table += string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    pwd_generator = random.sample(pwd_table, pwd_long)
    password = ''.join(pwd_generator)
    return password
#est 2
print(pwd_generator())
