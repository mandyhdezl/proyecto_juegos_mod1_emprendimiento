puntos_finales = 9

import random
opciones = ['piedra', 'papel', 'tijera']
puntos_pc = 0
puntos_usuario = 0

def eleccion_jugador ():
    
    opciones = "piedra", "papel", "tijera"
    
    usuario = input('Elige piedra, papel o tijera: ').lower()
    
    if usuario in opciones:
        print (f" Tu elección ha sido:'{usuario}'")
        
    
    if usuario not in opciones:
        print (f" Tu elección '{usuario}' no es correcta")
        return (usuario)


while puntos_finales <= 9:
    
    pc = random.choice(opciones)
    eleccion_jugador()
    print(f'Tu contrincante eligió: {pc}')
    
    if eleccion_jugador == pc:
        print('Has empatado 🤓')
    
    elif (eleccion_jugador== 'piedra' and pc == 'tijera') or\
        (eleccion_jugador == 'tijera' and pc == 'papel') or\
        (eleccion_jugador == 'papel' and pc == 'piedra'):
        print('"Has Ganado esta ronda! Enhorabuena!!!')
        puntos_usuario += 1
        print (puntos_usuario)
    
    elif (eleccion_jugador== 'piedra' and pc == 'papel') or\
        (eleccion_jugador == 'tijera' and pc == 'piedra') or\
        (eleccion_jugador == 'papel' and pc == 'tijera'):
        print("Has perdido! Lo sentimos, prueba en la siguiente ronda")
        puntos_pc += 1
        print (puntos_pc)
    
    
    elif puntos_usuario == puntos_finales:
        print ("Has ganado el juego")
        break
    
    elif puntos_pc == puntos_finales:
        print ("Has perdido. Inténtalo de nuevo 🤪") 
        break
    

print('\nResultado final:')
print(f'Tú: {puntos_usuario} puntos')
print(f'Computadora: {puntos_pc} puntos')