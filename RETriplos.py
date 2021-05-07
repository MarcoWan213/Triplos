#Integrantes: 
#Aguilar Camara Oscar David
#Carrillo Espadas Alondra Jacquelin
#Wan Martinez Marco Mauricio

import re

#Lectura del archivo
f = open ('C:/Users/Marco/Documents/Pruebas/prueba5.jar','r')
mensaje = f.read()
f.close()
sMs = mensaje.split()
cOp = 0
cOp2 = 0

for x in sMs:
    if x == '*' or x == '/' or x == '-' or x == '+':
        cOp = cOp + 1      

#Metodo de RE para encontrar por prioridas las operaciones
while re.findall(r"(\( ([a-zA-Z0-9]|t[0-9]) [\*\/] (t[0-9]|[a-zA-Z0-9]) \))", mensaje):
    aux = re.findall(r"(\( ([a-zA-Z0-9]|t[0-9]) [\*\/] (t[0-9]|[a-zA-Z0-9]) \))", mensaje)[0]
    cOp2 = cOp2 +1
    a = ('t' + str(cOp2))
    print(str(a) + " = " + str(aux[0]))
    mensaje = re.sub(r"(\( ([a-zA-Z0-9]|t[0-9]) [\*\/] (t[0-9]|[a-zA-Z0-9]) \))", a, mensaje)
    #print(mensaje)

#Metodo de RE para encontrar por prioridas las operaciones
while re.findall(r"(\( ([a-zA-Z0-9]|t[0-9]) [\+\-] (t[0-9]|[a-zA-Z0-9]) \))", mensaje):
    aux = re.findall(r"(\( ([a-zA-Z0-9]|t[0-9]) [\+\-] (t[0-9]|[a-zA-Z0-9]) \))", mensaje)[0]    
    cOp2 = cOp2 +1
    a = ('t' + str(cOp2))
    print(str(a) + " = " + str(aux[0]))
    mensaje = re.sub(r"(\( ([a-zA-Z0-9]|t[0-9]) [\+\-] (t[0-9]|[a-zA-Z0-9]) \))", a, mensaje)
    #print(mensaje)

#Metodo de RE para encontrar por prioridas las operaciones
while re.findall(r"((t[0-9]|[a-zA-Z0-9]) [\*\/] (t[0-9]|[a-zA-Z0-9]))", mensaje):
    aux = re.findall(r"((t[0-9]|[a-zA-Z0-9]) [\*\/] (t[0-9]|[a-zA-Z0-9]))", mensaje) [0]   
    cOp2 = cOp2 +1
    a = ('t' + str(cOp2))
    print(str(a) + " = " + str(aux[0]))
    mensaje = re.sub(r"((t[0-9]|[a-zA-Z0-9]) [\*\/] (t[0-9]|[a-zA-Z0-9]))", a, mensaje)
    #print(mensaje)

#Metodo de RE para encontrar por prioridas las operaciones
while re.findall(r"((t[0-9]|[a-zA-Z0-9]) [\+\-] (t[0-9]|[a-zA-Z0-9]))", mensaje):
    aux = re.findall(r"((t[0-9]|[a-zA-Z0-9]) [\+\-] (t[0-9]|[a-zA-Z0-9]))", mensaje)[0]   
    cOp2 = cOp2 +1
    a = ('t' + str(cOp2))
    b = aux[0]
    #print(b)
    prim = aux[0]      
    print(str(a) + " = " + str(aux[0]))
    mensaje = re.sub(r"((t[0-9]|[a-zA-Z0-9]) [\+\-] (t[0-9]|[a-zA-Z0-9]))", a, mensaje)
    #print(mensaje)

print(mensaje)

print("Integrantes: ")
print("Aguilar Camara Oscar David")
print("Carrillo Espadas Alondra Jacquelin")
print("Wan Martinez Marco Mauricio")