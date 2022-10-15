# English: Reading in Python is simple, just use the input() function.
# 1. In our case, we want to detect the condition a is not equal to 0 and, only in that case, do not perform the calculation of x.

# Spanish: Leer en Python es simple, solo usa la función input().
# 1. En nuestro caso, queremos detectar la condición a no es igual a 0 y, sólo en ese caso, no realice el cálculo de x.

from re import A


a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))

if (a != 0):
    x = -b/a
    print ("The value of x is: ", x)