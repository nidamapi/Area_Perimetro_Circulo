import math

print("························")
print("Area del circulo")
print("························")
      

# input 
r=input("ingrese el radio: ")
r=int(r)

#processing
p = 2*math.pi*r
a = math.pi*r**2

#output
print("························")
print("el area es: "+str(a))
print("el perimetro  es: "+str(p))
print("························")
