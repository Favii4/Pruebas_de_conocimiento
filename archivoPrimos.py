

def primo(x):
    if x==2:
        return True
    if x%2==0:
        return False
    i=3
    while i**2<=x:
        if x%i==0:
            return False
        i=i+2
    return True
 
x = int(input("Ingrese un numero: "))
c=2
contador=1
while contador<=x:
           if primo(c):
                   print ('El' , (contador) , 'numero primo es' , (c))
                   contador=contador+1
           c=c+1