# English: 
# Design a program that, given an integer, Determine if this is twice an odd number. 
# (Example: 10 is double of 5, which is odd.)

# Spanish: 
# Diseñe un programa que, dado un número entero, Determina si es el doble de un número impar. 
# (Ejemplo: 10 es el doble de 5, que es impar.)

# Input value
num = int(input("Enter number: "))

# Math operation
if (num%2 != 0):
    print ("The number is odd")
else:
    if ((num/2)%2 != 0):
        print (num, "is double of ", num/2,"because it's odd")
    else:
        print ("does not meet the condition")