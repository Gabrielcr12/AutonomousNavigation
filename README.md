# Autonomous Navigation

Este proyecto simula el comportamiento de un rover autónomo que se desplaza desde un punto de origen hacia una ubicación aleatoria en busca del marcador "ArUco". El objetivo principal es explorar y mapear un área definida alrededor del marcador "ArUco". 

![Rover](https://i.postimg.cc/q7gHSDKz/Python5.png)

## Descripción

El código simula un entorno de exploración para el rover y desarrolla un algoritmo de búsqueda en el área definida. Utiliza coordenadas aproximadas del marcador "ArUco"para generar un rectangulo delimitando el área a explorar por el rover.

## Funcionalidades

- Simulación del entorno de exploración.
- Desarrollo del algoritmo de búsqueda en un área predefinida.
- Cálculo de la dirección y distancia del rover con respecto al punto de destino.
- Movimiento estratégico del rover siguiendo un patrón en cuadrados concéntricos.
####Instalación y Requisitos
Python: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [Python.org](https://www.python.org/downloads/)
## Bibliotecas Utilizadas

Este proyecto hace uso de las siguientes bibliotecas de Python:

- **Turtle**: Proporciona un entorno gráfico para dibujar y simular movimiento.
  - [Documentación de Turtle](https://docs.python.org/3/library/turtle.html)

- **Random**: Utilizada para generar números aleatorios.
  - [Documentación de Random](https://docs.python.org/3/library/random.html)

- **Math**: Proporciona funciones matemáticas comunes.
  - [Documentación de Math](https://docs.python.org/3/library/math.html)



**Tabla de contenidos**

[TOCM]
#Descripción del código
######Función para dibujar un rectángulo
La función dibujar_rectangulo permite dibujar un rectángulo centrado en las coordenadas (aruco_x, aruco_y) con lados de longitud 2m. Es útil para visualizar el área de exploración del rover. Donde "m" es una variable que define la longitud del plano.

```
def dibujar_rectangulo(x, y, m):
    turtle.penup()
    turtle.goto(x - m, y - m)  # Esquina superior izquierda
    turtle.pendown()
    
    for _ in range(2):
        turtle.forward(2 * m)  # Lado horizontal
        turtle.left(90)
        turtle.forward(2 * m)  # Lado vertical
        turtle.left(90) ``` 
[![Python2.png](https://i.postimg.cc/NFcmBMwP/Python2.png)](https://postimg.cc/r0fK9qsS)

######Función para dibujar mallado
La función dibujar_mallado crea un patrón de puntos en forma de cuadrícula dentro de un rectángulo alrededor de la posición del marcador "ArUco". Aquí está cómo funciona en resumen:

Cálculo de la cantidad de puntos: Se calcula cuántos puntos en filas y columnas caben en el rectángulo basado en su tamaño y la distancia entre puntos.

Generación de puntos: Se crean puntos en una cuadrícula dentro del rectángulo, comenzando desde la esquina superior izquierda y avanzando hacia la derecha y hacia abajo.

Dibujar el rectángulo: Se dibuja un rectángulo alrededor de la posición del marcador "ArUco" para visualizar el área de exploración.

Dibujar los puntos: Cada punto en la cuadrícula se dibuja como un pequeño círculo en la ventana de Turtle.

Retorno de puntos: La función devuelve una lista de coordenadas de puntos dentro del área de exploración.
```
	def dibujar_mallado(aruco_x, aruco_y, m, dce):
    # Calcular la cantidad de puntos en cada fila y columna del rectángulo
    num_puntos_x = int(2 * m / dce)
    num_puntos_y = int(2 * m / dce)

    # Generar puntos en el mallado dentro del rectángulo
    puntos = []

    for i in range(num_puntos_x + 1):
        for j in range(num_puntos_y + 1):
            x = aruco_x - m + i * dce
            y = aruco_y - m + j * dce
            puntos.append((x, y))

    # Dibujar el rectángulo centrado en (arucox, arucoy)
    dibujar_rectangulo(aruco_x, aruco_y, m)

    # Dibujar los puntos estáticamente
    turtle.penup()
    for x, y in puntos:
        turtle.goto(x, y)
        turtle.dot(5)  # Dibujar un punto de tamaño 5
    return puntos
    puntos = dibujar_mallado(aruco_x, aruco_y, m, dce)  ``` 
[![Python4.png](https://i.postimg.cc/8cpcZrGD/Python4.png)](https://postimg.cc/hzYKjvh3)
###### Función PPA
La función comienza calculando la distancia del rover al objetivo ArUco y el ángulo en radianes entre el rover y el ArUco. Luego, convierte el ángulo a grados y ajusta su valor para que esté dentro del rango de 0 a 360 grados.

Luego, la función configura la dirección del rover hacia el ArUco y avanza hacia él. Después de moverse, calcula las coordenadas actuales del rover y muestra el ángulo en grados y la distancia diagonal al ArUco.

El rover luego se mueve a través de un patrón de puntos en cuadrados concéntricos alrededor del ArUco. Para hacer esto, se generan puntos en un rectángulo alrededor del ArUco, y estos puntos se ordenan por su distancia al centro del ArUco. Luego, el rover se mueve secuencialmente hacia cada uno de estos puntos, girando 360 grados en su propio eje después de cada movimiento. Las coordenadas del rover se imprimen después de cada movimiento.

Al final, se llama a la función PPA con las coordenadas aproximadas del ArUco y se finaliza la simulación de Turtle.
```
# Función para llevar el rover a las coordenadas aproximadas
def PPA(aruco_x, aruco_y):

# Calcular la distancia al objetivo
    DRA = math.sqrt(aruco_x**2 + aruco_y**2)
    
    # Calcular el ángulo en radianes con respecto al ArUco
    ARAR = math.atan2(aruco_y, aruco_x)

    # Convertir el ángulo a grados
    ARA = math.degrees(ARAR)

    # Ajustar el ángulo para que esté en el rango de 0 a 360 grados
    ARAA = ((ARA + 360) % 360)
    
    # Configurar la dirección del rover hacia el ArUco y avanzar hacia él
    pen.setheading(ARAA)
    pen.forward(DRA)
    
    # Cambiar la dirección del rover para que mire hacia arriba (180 grados)
    pen.setheading(180)
    
    print(f"Ángulo en grados: {ARAA:.2f}")
    
    # Obtener las coordenadas actuales del rover después de moverlo
    rover_x, rover_y = pen.pos()
    print(f"Distancia diagonal del rover a ArUco: DRA= {DRA:.2f}")
    
    # Calcular la cantidad de puntos en cada fila y columna del rectángulo
    num_puntos_x = int(2 * m / dce)
    num_puntos_y = int(2 * m / dce)

    # Generar puntos en el mallado dentro del rectángulo
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
        print(f"Coordenadas del rover: x = {rover_x:.2f}, y = {rover_y:.2f}")```
El rover se mueve a la coordenada donde es probable encontrar el ArUco.
[![Python4-5.png](https://i.postimg.cc/bvDcxY2J/Python4-5.png)](https://postimg.cc/3yTc7T15)
Aplica la estrategia de búsqueda, el patrón en cuadrados concéntricos es una estrategia de exploración que permite al rover buscar sistemáticamente el marcador en el mallado para encontrar el ArUco.
[![Python4-9.png](https://i.postimg.cc/DyHt2kN3/Python4-9.png)](https://postimg.cc/mt3dwqRm)

## Agradecimientos

Se agradece el tiempo tomado para revisar este proyecto. 

Estoy comprometido con la excelencia y el aprendizaje continuo, y espero que este proyecto sea una pequeña muestra de mis habilidades y dedicación. 

Si deseas obtener más información o ponerte en contacto conmigo, no dudes en hacerlo. Estoy disponible para responder a cualquier pregunta o proporcionar información adicional.


Gabriel Castillo

