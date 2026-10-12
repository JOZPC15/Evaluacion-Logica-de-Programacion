# Mini Atari Pong

**Hecho por:** Joz Pérez  
**Fecha:** 11 de octubre de 2026

## Objetivo

Incorporar estructuras fundamentales de programación a través de un programa ejecutado con lenguaje Python para comprender la lógica y sentar las bases del desarrollo.

## Funcionalidades

El desarrollo inicia con la instanciación de las bibliotecas **Tkinter** y **time**, permitiendo crear ventanas, dibujar elementos gráficos, capturar eventos del teclado y ratón, y gestionar interfaces gráficas en general en caso de **Tkinter**, y permitiendo pausar la ejecución del programa durante un bloque de código en caso de **time**.

Después se configura la ventana con sus dimensiones de alto y ancho, lo que será útil para establecer los puntos de referencia para la colisión, tanto de la pelota para que se mantenga dentro de la pantalla y rebote, como de la raqueta para que se mantenga dentro de la pantalla de la interfaz.

Aprovechando la biblioteca **Tkinter**, se puede invocar a la clase **Canvas**, que permite crear el lienzo digital sobre el que se crearán los elementos visuales que representarán a la pelota, la raqueta, la mitad del tablero y el marcador del juego. También se declara una variable que almacenará el puntaje y las tuplas que determinarán la posición inicial de los elementos visuales una vez creados.

Posteriormente, se definen las variables que establecerán la velocidad inicial de los elementos visuales, para luego pasar a construir los mismos, **raqueta** y **pelota**, vinculados a sus coordenadas almacenadas en las tuplas, para que se muestren sobre la interfaz. También se instancian las funciones **Tecla presionada** y **Tecla liberada** que vinculan la información recibida por el dispositivo de entrada, el teclado, con las variables que modificarán la posición de la raqueta dentro de la interfaz.

Inicia el juego y la pelota empieza su movimiento de inmediato, mientras que la raqueta aguardará registrar información del teclado para actualizar sus coordenadas. Las coordenadas se actualizarán en tiempo real a través de la función **Actualizar**, que recibirá los valores de velocidad de la raqueta y actualizará en bucle la posición de la pelota para garantizar su movimiento continuo, invocándose a sí misma cada 0.02 segundos.

Dentro de la misma función, también se utilizan las coordenadas de cada objeto para determinar si alguno ha colisionado con cualquiera de los bordes de la ventana configurada o incluso con la raqueta.

En caso de que las coordenadas de la pelota coincidan con las coordenadas de la raqueta, esta rebotará y le otorgará 1 punto al usuario, pero si las coordenadas de la pelota llegan a coincidir con las coordenadas del borde izquierdo de la ventana configurada, la ejecución se detendrá y el juego terminará.
