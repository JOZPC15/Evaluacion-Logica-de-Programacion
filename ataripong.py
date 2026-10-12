# Instanciación de las bibliotecas Python necesarias
import tkinter as tk
import time

# Configuración de la ventana de la interfaz gráfica Tkinter
ANCHO = 800
ALTO = 500
ventana = tk.Tk()

# Configuración del lienzo que permite crear formar y textos sobre la interfaz
canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="black")
canvas.pack()

# Variable de puntos
puntos = 0

# Tuplas para posiciones iniciales
pos_raqueta = (30, 200, 50, 300)
pos_pelota = (390, 240, 410, 260)

# Creación de la representación visual de la raqueta
raqueta = canvas.create_rectangle(
    pos_raqueta[0],
    pos_raqueta[1],
    pos_raqueta[2],
    pos_raqueta[3],
    fill="white"
)

# Creación de la representación visual de la pelota
pelota = canvas.create_oval(
    pos_pelota[0],
    pos_pelota[1],
    pos_pelota[2],
    pos_pelota[3],
    fill="white"
)
# Creación de la representación visual del marcador
texto_puntos = canvas.create_text(
    700, 30,
    text="Puntos: 0",
    fill="white",
    font=("Arial", 16)
)

# Creación de una línea decorativa en medio del tablero para implementar la estructura "for"
for y in range(0, ALTO, 30):
    canvas.create_line(
        ANCHO/2, y,
        ANCHO/2, y+15,
        fill="gray"
    )
  
# Variables de velocidad de la pelota
dx = 4
dy = 4

# Variable de velocidad de la raqueta
vel_raqueta = 0

# Incorporación de estructura "while" para desplegar un contador
contador = 3
while contador > 0:
    canvas.create_text(
        ANCHO/2,
        ALTO/2,
        text=str(contador),
        fill="yellow",
        font=("Arial", 40)
    )
    ventana.update()
    time.sleep(1)
    canvas.delete("all")
    
# Inicio del juego, se redibuja representaciones visuales eliminadas por el contador anterior
    for y in range(0, ALTO, 30):
        canvas.create_line(
            ANCHO/2, y,
            ANCHO/2, y+15,
            fill="gray"
        )
    raqueta = canvas.create_rectangle(
        pos_raqueta[0],
        pos_raqueta[1],
        pos_raqueta[2],
        pos_raqueta[3],
        fill="white"
    )
    pelota = canvas.create_oval(
        pos_pelota[0],
        pos_pelota[1],
        pos_pelota[2],
        pos_pelota[3],
        fill="white"
    )
    texto_puntos = canvas.create_text(
        700, 30,
        text=f"Puntos: {puntos}",
        fill="white",
        font=("Arial", 16)
    )
    contador -= 1

# Declaración de las funciones que leerán información ingresada desde el teclado
def tecla_presionada(event):
    global vel_raqueta
    if event.keysym == "Up":
        vel_raqueta = -8
    else:
        if event.keysym == "Down":
            vel_raqueta = 8
def tecla_liberada(event):
    global vel_raqueta
    vel_raqueta = 0

# Vinculación de las funciones con los eventos Tkinter
ventana.bind("<KeyPress>", tecla_presionada)
ventana.bind("<KeyRelease>", tecla_liberada)

# Declaración de la función de actualización de coordenadas de la raqueta y la pelota
def actualizar():
    global dx, dy, puntos
# Mover raqueta
    canvas.move(raqueta, 0, vel_raqueta)
    x1, y1, x2, y2 = canvas.coords(raqueta)
# Establece puntos de colisión de la raqueta en los límites superior e inferior de la ventana Tkinter
# Impide que la raqueta avance fuera de los límites establecidos  
    if y1 < 0:
        canvas.move(raqueta, 0, -y1)
    if y2 > ALTO:
        canvas.move(raqueta, 0, ALTO - y2)
# Mover pelota
    canvas.move(pelota, dx, dy)
    bx1, by1, bx2, by2 = canvas.coords(pelota)
# Establece puntos de colisión de la pelota en los límites superior e inferior de la ventana Tkinter
    if by1 <= 0 or by2 >= ALTO:
        dy = -dy
# Establece puntos de colisión de la raqueta en el límite derecho de la ventana Tkinter
    if bx2 >= ANCHO:
        dx = -dx
# Establece los puntos de colisión entre la pelota y la raqueta
    px1, py1, px2, py2 = canvas.coords(raqueta)
    if (bx1 <= px2 and
        bx2 >= px1 and
        by2 >= py1 and
        by1 <= py2):
        dx = abs(dx)
# Incrementa el puntaje cada vez que la pelota colisione con la raqueta
        puntos += 1
        canvas.itemconfig(
            texto_puntos,
            text=f"Puntos: {puntos}"
        )
# Termina el juego si la pelota colisiona con el borde izquierdo de la pantalla
    if bx1 <= 0:
        canvas.create_text(
            ANCHO/2,
            ALTO/2,
            text="FIN DEL JUEGO",
            fill="red",
            font=("Arial", 30)
        )
        return
# Permite que la función "Actualizar" se invoque a sí misma cada 0.02 segundos
# Permite aparentar movimiento en los elementos de Canvas
    ventana.after(20, actualizar)

#Instanciación de la función "Actualizar"
actualizar()
ventana.mainloop()
