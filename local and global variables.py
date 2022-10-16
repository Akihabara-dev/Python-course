# English: Local and global variables
# Local: In the body of functions it is possible to define and use variables.
# Global: Global variables are declared outside the body of any function
# and are accessible from any point in the program after their declaration.

# Spanish: Variables locales y globales
# Local: En el cuerpo de las funciones es posible definir y usar variables.
# Global: La variables globale se declaran fuera del cuerpo de cualquier función
# y son accesibles desde cualquier punto del programa posterior a su declaración.

# Example local variable > where i & n is local variable
print("Example Local Variable: ", end=" ")
def addition(i, n):
    sum = 0
    for j in range(i, n + 1):
        sum = sum + j
    return sum

j = 1
sum = 0
print(addition(j, 10), j , sum)

# Example Global variable > where s is global variable
print("Example Global Variable: ", end=" ")
s = 1

def sum(x):
    return (x + s)

def subtract(x):
    y = 2
    s = y + 3
    return x - s

s = s + 1
print(sum(1), end=" ")
s = s + 2
print(subtract(1))