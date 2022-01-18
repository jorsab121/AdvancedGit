from math import sqrt

def custom_sqrt(number):
    if (number < 0):
        return -sqrt(-number)
    return sqrt(number)

number = input("Enter a number: ")
print(custom_sqrt(float(number)))
