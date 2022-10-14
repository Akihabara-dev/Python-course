# English: To read in Python is simple, just use the input() function.
# 1. Design a program and flowchart ow to read five integers by keyboard and 
# determine which of the last four numbers is more close to the first. For example, 
# if the user enters the numbers 2; 6; 4; 1 and 10, the program answers that the number 
# closest to 2 is the 1. Always consider that the numbers to enter are different.
# 2. Note: Consider the abs() functionality to calculate the absolute value. 
# For example, if we write in python a = abs(-3), the interpreter saves the 
# value 3 in variable a.

# Spanish: Leer en Python es simple, solo usa la función input().
# 1. Diseñar un programa y un diagrama de flujo Cómo leer cinco números enteros por teclado y 
# determinar cuál de los últimos cuatro números es más cerca del primero. Por ejemplo, 
# si el usuario ingresa los números 2; 6; 4; 1 y 10, el programa responde que el número 
# más cercano a 2 es el 1. Considere siempre que los números a ingresar son diferentes.
# 2. Nota: Considere la funcionalidad abs() para calcular el valor absoluto. Por ejemplo, 
# si escribimos en python a = abs(-3), el intérprete guarda el valor 3 en la variable a.

# Data entry
value1 = int(input('Enter first value: '))
value2 = int(input('Enter second value: '))
value3 = int(input('Enter Third value: '))
value4 = int(input('Enter fourth value: '))
value5 = int(input('Enter fifth value: '))

# Distance calculation
calculate_2 = abs(value1 - value2)
calculate_3 = abs(value1 - value3)
calculate_4 = abs(value1 - value4)
calculate_5 = abs(value1 - value5)

# Shortets distance calculation
if (calculate_2 < calculate_3 and calculate_2 < calculate_4 and calculate_2 < calculate_5):
    print ("The number with the shortest distance is: ", value2)
elif (calculate_3 < calculate_2 and calculate_3 < calculate_4 and calculate_3 < calculate_5):
    print ("The number with the shortest distance is: ", value3)
elif (calculate_4 < calculate_2 and calculate_4 < calculate_3 and calculate_4 < calculate_5):
    print ("The number with the shortest distance is: ", value4)
elif (calculate_5 < calculate_2 and calculate_5 < calculate_3 and calculate_5 < calculate_4):
    print ("The number with the shortest distance is: ", value5)