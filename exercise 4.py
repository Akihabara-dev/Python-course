# Calculate apartment price
# Apartment is to 20 flats with 8 sites for flat
# Values Flat 1 >>> $85000 | Flat 20 >>> $160000
# Value base for restant apartment is : $100000
# Flats >>> [4][5][6][7]  flats 3 and 7 +15% more
#           [0][1][2][3]  flats 0 and 4 -20% down

# Calcular precio de un departamento

apartment = input("Enter number apartment: ")

flat1 = int(str(apartment)[0])
flat2 = int(str(apartment)[1])

flat = (flat1*10)+flat2

position = int(str(apartment)[3])

if position == 8 or position == 9 or flat < 1 or flat > 20:
    print ("The apartment n°", apartment ," is no exist")
else:
    print ("Flat: ", flat)
    print ("Position: ", position)

    flat_10 = 85000
    flat_20 = 160000
    flat_base = 100000

    if flat == 1:
        print ("The value of apartment", apartment, "is: $", flat_10)
    elif flat == 20:
        print ("The value of apartment", apartment, "is: $", flat_20)
    elif position == 3 or position == 7:
        print ("The value of apartment", apartment, "is: $", flat_base+flat_base*0.15)
    elif position == 0 or position == 4:
        print ("The value of apartment", apartment, "is: $", flat_base-flat_base*0.2)