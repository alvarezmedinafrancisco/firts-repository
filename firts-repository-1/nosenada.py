va = input("escribe una frase")
va.lower().replace(" ","")
frase1 = "Anita lava la tina"
frase2 = frase1.lower().replace(" ","")
if va == va[::-1]:
    print(va + " es un palindromo")
else:
    print(va + " no es un palindromo")
    
        
        
        
contador = 0 
while(contador < 5):
            contador = contador +1 
            print("iteracion numero {}".format(contador ))
            if contador == 3:
                break
print("fin")



va = int(input("teclea un numero"))
va1= int(input("teclea otro numero"))
va2 = va + va1 
print(va2)


nose = int(input("teclea un numero"))
if nose == nose/2:
        print("tu numero no es primo")
else:
    print("tu numero es primo")
    
    
    
    
    
    
    
    edad = int(input("teclea tu edad"))
if edad == edad <= 18:
    print ("no eres mayor de edad")
else:
    print("eres mayor de edad")
    
    
    
    
    
    
    alumnos = ["ana","pepe","mikel","unai","lorena"]
for alumno in alumnos:
    print(alumnos)
    
    
    
    frase = "aprendiendo desde python"
for c in frase:
    print(c)
    
    
    
    numeros = [4,8,2,7,1,9,3,5]
total = 0
for n in numeros:
    total += n 
    if total > 10:
        break
    print(total)
    
    
    
    
    numeros = [4,8,2,7,1,9,3,5]
total = 0
for n in numeros:
    if n % 2 == 0:
        print("numero par,no lo sumamos")
    total += n
    
    
    for i in range(1,10):
        if i%2 !=0:
            print(i)
            
            
            
            
nose = int(input("teclea un numero"))
total = 1

for n in range(1, nose + 1):
    total *= n

print("el factorial de", nose, "es", total)

    
    
def saludo(nombre):
    print("hola " + nombre + " bienvenido")

saludo("pepe") 

def suma(a,b):
    return a + b    
print(suma(4,5))
