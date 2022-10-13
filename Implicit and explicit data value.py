# English: Type conversion.
# 1. Implicit keeps the numeric format
# 2. Explicit modifies the format to INT generating a loss of information

# Spanish: Conversión de tipos.
# 1. Implícito mantiene el formato numerico
# 2. Explícito modifica el formato a entero generando una perdidad de información

a = 10
b = 5.5

print (a + b)
print ((a) + int(b))