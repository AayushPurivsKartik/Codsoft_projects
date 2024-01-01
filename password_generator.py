import random
import string
def password_generator(length):
    sample=string.ascii_letters+string.punctuation+string.digits
    password=''.join(random.choice(sample) for n in range(length))
    return password
while True:
    try:
        length=int(input('enter the length of the password: '))
        if length<=0:
            print("please enter the positive number: ")
    except ValueError:
        print("invalid input. please enter a positive integer: ")
    password=password_generator(length)
    print("generate password: ",password)
    repeat=input("do you want to generate more password: ")
    if repeat=="no" or repeat=="no":
        break
print("Thank you")
