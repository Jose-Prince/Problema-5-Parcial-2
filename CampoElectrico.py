import math

def Ccono(Q,R,H,d): #Q = carga, R = radio, H = altura, d = distancia de la figura a la partícula
    constante = float((3*Q)/(2*math.pi*(8.85*10**-12)*R**2*H))
    frac1 = -(H*(H**2*d**2)**1/2+R**2*H+H**3)/(R**2+H**2)
    frac12 = (H*(H**2*(-d-H)**2+R*H**2)**1/2)/(R**2+H**2)
    frac2 = -(H*R**2*d*math.log(abs((R**2+H**2)**1/2*((R**2+H**2)*H**2-2*H**2*H**2*(H*(d+H)+R**2)+H**2*d**2+2*H**3*d+H**2*R**2+H**4)**1/2)+(R**2+H**2)*H-H**2*d-H*R**2-H**3))/(R**2+H**2)**3/2
    frac22 = (H*R**2*d*math.log(abs((R**2+H**2)**1/2*(H**2*d**2+2*H**3*d+H**2*R**2+H**4)**1/2-H**2*d-H*R**2-H**3)))/(R**2+H**2)**3/2
    
    resultado = constante*(frac1+frac2+frac12+frac22)
    
    return resultado

def CconoT(Q,R,r,H,d): #Q = carga, R = radio mayor, r = radio menor H = altura, d = distancia de la figura a la partícula
    constante = (3*Q)/(2*math.pi*(8.85*10**-12)*H*(R**2+r**2+R*r))
    aux1 = H*((r-R)**2+H**2)**1/2*(-(2*H*R*(r-H)-2*H**2*(d+H))/(2*(r**2-2*R*r+R**2+H**2))-d-H)
    deno = ((r-R)**2+H**2)*(-(H**2*(R*(r-R)+H*(-d-H))**2)/((r-R)**2+H**2)+H**2*(d+H)**2+H**2*R**2)
    num1 = ((r-R)**2+H**2)*H+H*R*r-H**2*d-H*R**2-H**3
    num2 = H*R*r-H**2*d-H*R**2-H**3
    
    frac1 = math.log(abs(((num1)/(deno)+1)**1/2+(num1)/deno))
    frac12 = math.log(abs(((num2)/(deno)+1)**1/2+(num2)/deno))
    
    frac2 = (H*(((r-R)*H+H*R)**2+H**2*d**2)**1/2)/(r**2-2*R*r+R**2+H**2) + H
    frac22 = -(H*(H**2*R**2+H**2*(-d-H)**2)**1/2)/(r**2-2*R*r+R**2+H**2)
    
    fract1 = (aux1*frac1)/(r**2-2*R*r+R**2+H**2)
    fract12 = -(aux1*frac12)/(r**2-2*R*r+R**2+H**2)
    
    resultado = constante*(fract1-frac2+fract12-frac22)
    
    return resultado

def Chemisferio(Q,R,d): #Q = carga, R = radio, d = distancia de la figura a la partícula
    constante = (3*Q)/(4*math.pi*(8.85*10**-12)*R**3)
    frac1 = -(d*math.log(abs(2**1/2*(2*R**2-2*(d+2*R)*R+d**2+2*R*d+2*R)**1/2-d)))/(2**3/2)+d/2+R
    frac2 = (d*math.log(abs(2**1/2*(d**2+2*R*d+2*R**2)**1/2-d-2*R)))/(2**3/2)+((-d-R)**2+R**2)**1/2/(2)
    
    resultado = constante*(frac1+frac2)
    
    return resultado