**Guion de Presentación**

Persona 1:
👋 ¡Hola a todos! Hoy les presentamos nuestro juego del Ahorcado en Python. Es un juego clásico donde un jugador intenta adivinar una palabra oculta antes de quedarse sin vidas.

Persona 2:
El código comienza definiendo las etapas del ahorcado en una lista llamada dibujo, que muestra visualmente el progreso del juego a medida que fallamos.

Persona 1:
Después, damos la bienvenida al jugador y seleccionamos aleatoriamente una palabra de una lista predefinida usando random.choice(). Luego, la convertimos en guiones bajos _ para que el jugador pueda ver cuántas letras tiene la palabra.

Persona 2:
Aquí viene la mecánica principal del juego. Usamos la función buscador_letras_palabra_secreta(), que pide al usuario que ingrese una letra y verifica si está en la palabra secreta.

Persona 1:
Si la letra es correcta, la mostramos en su posición dentro de la palabra. Si es incorrecta, restamos una vida, agregamos la letra a la lista de errores y actualizamos el dibujo del ahorcado.

Persona 2:
El juego sigue en un bucle while, que se ejecuta hasta que el jugador adivine toda la palabra o se quede sin vidas. Al final, mostramos un mensaje de victoria 🎉 o de derrota con la palabra secreta.

Persona 1:
Este código incluye validaciones para evitar errores como ingresar números, símbolos o más de una letra a la vez. ¡Así aseguramos una experiencia fluida para el usuario!

Persona 2:
Y eso es todo. ¡Gracias por escucharnos! ¿Tienen alguna pregunta? 🤓