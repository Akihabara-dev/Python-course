# English: 
# It is possible t modify the natural behavior of our cycles with some instructions.
# break: allows to interrupt a cycle, regardless of its condition of term
# continue: allows you to make a jump in the cycle, and continue with the next iteration.

# Spanish: 
# Es posible modificar el comportamiento natural de nuestros ciclos con algunas instrucciones.
# break: permite interrumpir un ciclo, independientemente de su condición de termino.
# continue: permite hacer un salto en el ciclo, y continuar con la siguiente iteración.

# Break statement
for i in range(1,10):
    if i%3 == 0:
        print ("The number, ",i,"is divisible by 3")
        break
    print (i)
print ("Done")

# Continue statement
for i in range(1,10):
    if i%3 == 0:
        print ("The number, ",i,"is divisible by 3")
        continue
    print (i)
print ("Done")