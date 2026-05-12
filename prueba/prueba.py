import time


usuario=input('Introduce tu nombre de pila : ')

nombres=[]

print('Bienvenido',usuario.capitalize(),'que tal estas')

pregunta_1=input('Quieres Jugar a un juego ').capitalize()

if pregunta_1== 'Si':
	edad=int(input('Que edad tienes : '))
	if edad< 18 and edad> 0:
		
		with open('menores.txt','a') as f:
			contenido =  f.write('Nombre : ' + usuario.capitalize()+'\n'
					   + 'Edad   : ' + str(edad) + '\n'
					   + '-----------------------'+ '\n' 	)
			print('Lo siento eres un mocoso ')
	if edad >= 18:
		
		for i in range(3):
			nombre=input('Introduce el nombre de la lista :')
			nombres.append(nombre)
			with open('mayores.txt','a') as f:
				contenido= f.writelines('nombre : '+ nombre+'\n')
		for nombre in nombres:
				print(nombre)
				time.sleep(1)
			

elif pregunta_1=='No':
	print('Eres una cagona')

