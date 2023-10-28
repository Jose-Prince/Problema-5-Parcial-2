import math

#Velocida de escape
def escapeV(mass):
    return ((2*(8.85*10**-12))/(mass*(8.99*10**9)))**1/2

#Distancia plano infinito
def distanceP(velocity, density, protons, neutrons):
    return abs(((protons+neutrons)*(1.67*10**-27)*velocity**2*(8.85*10**-12))/(protons*(1.6*10**-19)*density))

#Distancia esfera
def distanceS(radio, protons, neutrons, velocity):
    return abs((2*math.pi*(8.85*10**-12)*radio**2*(protons+neutrons)*(1.67*10**-27)*velocity**2)/(protons*(1.6*10**-19)))