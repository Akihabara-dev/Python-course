# English: To perform an action contrary to an IF, the else is applied as follows
# Spanish: Para realizar una acción contraria a un IF, el else se aplica de la siguiente manera

from re import A


a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

if (a != 0):
    x = -b/a
    print("The value of x is: ", x)
else:
    print("Has no solution")