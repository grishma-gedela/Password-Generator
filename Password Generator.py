import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','@','%','$','&','*','+','/','<']
print(" \n\n\n -------- WELCOME TO PASSWORD GENERATOR --------\n")
print("\n Password consists of letters symbols and numbers \n")
n_letters=int(input('\n How many letters do you want in your password ?\n '))
n_symbols=int(input('\n How many symbols do you want in your password ?\n '))
n_numbers=int(input('\n How many numbers do you want in your password ?\n '))
password_list=[]
for i in range(1,n_letters+1):
         char=random.choice(letters)
         password_list+=char
for i in range(1,n_symbols+1):
         char=random.choice(symbols)
         password_list+=char
for i in range(1,n_numbers+1):
         char=random.choice(numbers)
         password_list+=char
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print("\n\n The Suggested Password for you is : ",password)
print("\n\n This is 'hard level' password")
