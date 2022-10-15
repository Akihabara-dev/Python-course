# English: Tennis ball is thrown from a height H meters.
# A tennis ball is thrown from a height H meters. Every time the ball
# bounces back reaches a maximum height equal to 5/7 of its previous height, as long as
# when there is no friction. In the case of friction, the height reached is a
# 6% less. When the ball reaches a bounce height of less than 3 centimeters stop rebound. 
# ** Deliver results of how many bounces are made with a ball of height h, with and without friction **
# Example >>> Rebound | No Frinction |  Friction
#               0     |   10,00      |   10,000
#               1     |   7,14       |   6,71
#               2     |   5,10       |   4,51
#               3     |   3,64       |   3,03
#               4     |   2,60       |   2,03
#               5     |   1,86       |   1,36
#               6     |   1,33       |   0,92

# Spanish: Entregar resultados de cuantos rebotes se dan con una pelota de altura h, con y sin rozamiento.



h = int(input("Enter Height value: "))
# Variables
h_n_friction = h
h_friction = h
rebound = 0
rebound_n = 0
#print ("Rebound | Friction \t\t\t| No Friction")
# Loop to compute bounces
while h_n_friction >= 0.03:
    print(rebound,"\t", h_n_friction,"\t\t", h_friction)
    if h_friction >= 0.03:
        aux = h_friction
        rebound_n = rebound_n+1
        h_friction = h_friction*(5/7)*0.94
    aux_no = h_n_friction
    h_n_friction = h_n_friction*(5/7)
    rebound = rebound+1
print ("Rebound: ",rebound-1, "no friction: ", aux_no, "Meters \nRebound: ", rebound_n-1, "friction: ", aux, "Meters")
