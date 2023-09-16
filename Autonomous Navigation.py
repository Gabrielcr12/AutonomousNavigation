
                                    # A U T O N O M U S       N A V I G A T I O N #
import random
import turtle
import math

# Rango de coordenadas X e Y en el que puede estar el ArUco
min_x = -250  # Valor mínimo para la coordenada X
max_x = 250   # Valor máximo para la coordenada X
min_y = -250  # Valor mínimo para la coordenada Y
max_y = 250   # Valor máximo para la coordenada Y

# Generar coordenadas aleatorias para el ArUco
aruco_x = random.uniform(min_x, max_x)
aruco_y = random.uniform(min_y, max_y)

# Imprimir las coordenadas generadas para el ArUco
print(f"Coordenadas del ArUco: x = {aruco_x:.2f}, y = {aruco_y:.2f}")

#distancia de nuestro plano
m = 100
# Valor de DCE cámara estereo
dce = 20
# Crear una ventana de Turtle
screen = turtle.Screen()

# Crear una tortuga
pen = turtle.Turtle()

# Cambiar la velocidad de la tortuga
pen.speed(1)  

# Lista de coordenadas de puntos estáticos
puntos_estaticos = [(aruco_x,aruco_y)]

# Dibujar puntos estáticos en las coordenadas especificadas
for x, y in puntos_estaticos:
    pen.penup()  # Levantar el lápiz para moverse sin dibujar
    pen.goto(x, y)  # Ir a la coordenada (x, y)
    pen.dot(7, "orange")  # Dibujar un punto de tamaño 5 en naranja
    
    
pen.penup()     
pen.goto(0, 0)  # Ir a las coordenadas (0, 0)
pen.pendown()   

        #---------------------------------------------------------------------------------#

# Función para dibujar un cuadrado centrado en (x, y) con lados de longitud 2 m
def dibujar_cuadrado(x, y, m):
    turtle.penup()
    turtle.goto(x - m, y - m)  # Esquina superior izquierda
    turtle.pendown()
    
    for _ in range(2):
        turtle.forward(2 * m)  # Lado horizontal
        turtle.left(90)
        turtle.forward(2 * m)  # Lado vertical
        turtle.left(90)

# Función para dibujar un mallado completo en el cuadrado
def dibujar_mallado(aruco_x, aruco_y, m, dce):
    # Calcular la cantidad de puntos en cada fila y columna del cuadrado
    num_puntos_x = int(2 * m / dce)
    num_puntos_y = int(2 * m / dce)

    # Generar puntos en el mallado dentro del cuadrado
    puntos = []

    for i in range(num_puntos_x + 1):
        for j in range(num_puntos_y + 1):
            x = aruco_x - m + i * dce
            y = aruco_y - m + j * dce
            puntos.append((x, y))

    # Dibujar el cuadrado centrado en (arucox, arucoy)
    dibujar_cuadrado(aruco_x, aruco_y, m)

    # Dibujar los puntos estáticamente
    turtle.penup()
    for x, y in puntos:
        turtle.goto(x, y)
        turtle.dot(5)  # Dibujar un punto de tamaño 5
    return puntos

# Llamar a la función para dibujar el mallado completo en el cuadrado y obtener los puntos
puntos = dibujar_mallado(aruco_x, aruco_y, m, dce)

        #---------------------------------------------------------------------------#

## Función para llevar el rover al las coordenadas aproximadas
def PPA(aruco_x, aruco_y):

    
    
    
    # Calcular el ángulo en radianes
    ARAR = math.atan2(aruco_y, aruco_x)

    # Convertir el ángulo a grados
    ARA = math.degrees(ARAR)

    #Ajustar el ángulo para que esté en el rango de 0 a 360 grados
    ARAA = ((ARA + 360) % 360)
    
    # Distancia del rover al ArUco
    
    DRA = math.sqrt(aruco_x**2 + aruco_y**2)
    
    pen.setheading(ARAA)
    pen.forward(DRA)
    pen.setheading(180)
    
    print(f"Ángulo en grados: {ARAA:.2f}")
    
    rover_x, rover_y = pen.pos()  # Obtener las coordenadas actuales del rover
    print(f"Distancia diagonal del rover a ArUco: DRA= {DRA:.2f}")
    
  # Calcular la cantidad de puntos en cada fila y columna del cuadrado
    num_puntos_x = int(2 * m / dce)
    num_puntos_y = int(2 * m / dce)

    # Generar puntos en el mallado dentro del cuadrado
    puntos = []

    for i in range(num_puntos_x + 1):
        for j in range(num_puntos_y + 1):
            x = aruco_x - m + i * dce
            y = aruco_y - m + j * dce
            puntos.append((x, y))

    # Ordenar los puntos por distancia al centro (aruco_x, aruco_y)
    puntos.sort(key=lambda punto: math.sqrt((punto[0] - aruco_x) ** 2 + (punto[1] - aruco_y) ** 2))

    # Mover el rover desde el centro hacia los puntos más cercanos
    for x, y in puntos:
        pen.goto(x, y)  # Mover el rover al siguiente punto
        pen.setheading(0)  # Establecer la dirección del rover a 0 grados (hacia arriba)
  
        pen.right(360)  # Hacer que el rover gire 360 grados sobre su propio eje
        
        # Imprimir las coordenadas actuales del rover después de cada movimiento
        rover_x, rover_y = pen.pos()
        
        print(f"Coordenadas del rover: x = {rover_x:.2f}, y = {rover_y:.2f}")
   
    
   # Llamar a la función PPA
PPA(aruco_x, aruco_y)

# Finalizar la sesión de Turtle
turtle.done()






    

