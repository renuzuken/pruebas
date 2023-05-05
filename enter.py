
# flujos de control


valor = 0

if (valor>-1) :
    print ("Mayor que -1")
else:
    print("Menor que -1")


for n in range (1,10):
    print (n)

n=1
while(n<10):
    print("Con while ",n)
    n=n+1

#Prueba de Break

for n in range(5):
    print("Con break ",n)
    if(n>2):
        break

#Recorrer cadena

cadena="Python"

for letra in cadena:
    print(letra)
    if(letra=="o"):
        print("Se encontro la o")
        break

#Recorrer cadena y usar continue para saltar el ciclo al siguiente, en este ejemplo se salta la B y en lugar de imprimirla continua en el siguiente ciclo

cadena="Palabra"

for letra in cadena:
    if(letra=="b"):
        continue
    print(letra)