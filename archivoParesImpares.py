def num_pares(n=20):
    
    pares=[]

    contador = 0
    numero = 0

    while contador < n:
        if numero % 2 == 0:
            pares.append(numero)
            contador += 1
        
        numero += 1
    
    return pares

def num_impares(n=20):
    
    impares=[]

    contador = 0
    numero = 0

    while contador < n:
        if numero % 2 != 0:
            impares.append(numero)
            contador += 1
        
        numero += 1
    
    return impares        

n = int(input('Escriba un numero '))

pares = num_pares(n)
impares = num_impares(n)

print('Estos son los primeros' , (n) , 'numeros pares: ' , (pares))
print('Estos son los primeros' , (n) , 'numeros impares: ' , (impares))