import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from RK4 import run

# Nuestros parámetros, puedes modificarlos para ver diferentes resultados
P = 0.3 #1.8 a 3, mientras más cerca 1.8 más enrollamiento
Q = 0.2
U = 25 #valores mayores a 24.7815 y menores que 25

def nuestra_funcion(t, y):
    dy = [U*(-y[1] - y[2]),  # Introducción de no linealidad
          y[0]*P + y[1],
          Q + y[2]*(y[0] - U)]
    return np.array(dy)

y0 = [-1, 3, 6]  # estos son los valores iniciales
dt = 0.001  # dt y T finalmente establecerán el número de iteraciones
T = 45
Y = [[], [], []]

Y[0], Y[1], Y[2], min_values, max_values = run(y0, dt, T, nuestra_funcion)

# Valores
print("Valores X: " + str(Y[0]))
print("Valores Y: " + str(Y[1]))
print("Valores Z: " + str(Y[2]))

# Crear una figura de Plotly
fig = go.Figure()

# Agregar la traza 3D
fig.add_trace(go.Scatter3d(
    x=Y[0],
    y=Y[1],
    z=Y[2],
    mode='lines',
    line=dict(color='blue', width=2)
))

# Configuración de la gráfica
fig.update_layout(
    title='Gráfica 3D Interactiva',
    scene=dict(
        xaxis_title='Eje X',
        yaxis_title='Eje Y',
        zaxis_title='Eje Z'
    )
)

# Mostrar la gráfica
fig.show()
