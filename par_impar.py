import random
numeros=[]

for i in range(0,11):
    i=random.randint(1,50)
    numeros.append(i)

for i in numeros:
    if i % 2 == 0:
        print(f'El numero {i} un numero Par')
    else:
        print(f'El numero {i} es un numero Impar')

print('\n')

print(f'El numero mas alto es ',max(numeros))
print('\n')
total=sum(numeros)
media=total/len(numeros)
print(f'La media de todos los numeros es ',media )
