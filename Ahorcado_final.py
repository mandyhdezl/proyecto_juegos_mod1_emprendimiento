dibujo = [
    '''
    +---+
    |   |
        |
        |
        |
        |
        =======
    
    ''',
    '''
    +---+
    |   |
    0   |
        |
        |
        |
        =======
    
    ''',
    '''
    +---+
    |   |
    0   |
    |   |
        |
        |
        =======
    ''',
    '''
    +---+
    |   |
  \ 0   |
    |   |
        |
        |
        =======
    ''',
    '''
    +---+
    |   |
  \ 0 / |
    |   |
        |
        |
        =======
    ''',
    '''
    +---+
    |   |
  \ 0 / |
    |   |
    \  |
        |
        =======
    ''',
    '''
    +---+
    |   |
  \ 0 / |
    |   |
   / \  |
        |GAME OVER
        =======
    '''
]

print('🕹¡¡¡Bienvenido al juego del AHORCADO!!!🕹. Tienes 6 vidas')
print(dibujo[0])

#partiendo de una lista de palabras, seleccionamos una aleatoriamente para iniciar el juego:
import random
lista_palabras = ['adalab', 'python', 'bucles', 'juego', 'mujer', 'grupo', 'funcion']
palabra_secreta = random.choice(lista_palabras)

def transformar_a_guiones(palabra_secreta):
    return ["_"] * len(palabra_secreta)

print (("  ").join(transformar_a_guiones(palabra_secreta)))
print ('\n')

resultado_juego = transformar_a_guiones(palabra_secreta)
vidas = 6
letras_incorrectas = [] 

def buscador_letras_palabra_secreta():
    global vidas # necesitamos que la variable sea global para que pueda hacer asociación con el valor inicial de vidas = 6
    letra_usuario = input("Introduce una letra: ").lower().strip()
    
    if letra_usuario >= 'a' and letra_usuario <= 'z' and len(letra_usuario) == 1: 
    # para evitar que se inserten números, frases o palabras enteras o caracteres especiales (espacios o signos de puntuación) en lugar de letras:

        if letra_usuario in palabra_secreta:
            for indice, l in enumerate(palabra_secreta):
                if l == letra_usuario and 'a' <= l <= 'z':
                    resultado_juego[indice] = l
            print(f'✅¡Letra "{letra_usuario}" correcta!')
        else:
            if letra_usuario not in letras_incorrectas: #para evitar duplicados de letras incorrectas
                letras_incorrectas.append(letra_usuario)
            vidas -= 1
            print(f'❌ Letra "{letra_usuario}" incorrecta. Te quedan {vidas} vidas.')
            print(dibujo[6 - vidas])
        
        print("Estado actual: ", " ".join(resultado_juego))
        print ('\n')
        print(f'Letras incorrectas: {letras_incorrectas}')
        
        print('-'* 40 )
    
    else: #en el caso de que la letra insertada en el input sea un num, una frase/palabra o un caracter especial:
        print(f'"{letra_usuario}" no es válido. Introduce una letra')
        print('-'* 40 )
        letra_usuario = input("Introduce una letra: ").lower().strip()

# Bucle del juego hasta que se acaben las vidas o se complete la palabra
while vidas > 0 and "_" in resultado_juego:
    if buscador_letras_palabra_secreta():
        break


if "_" not in resultado_juego:
    print("¡Felicidades! Has ganado el juego 🎉")
else:
    print("Has perdido. La palabra secreta era:", palabra_secreta)