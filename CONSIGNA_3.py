# ============================================================
#  TPI - Análisis de rendimiento en un sistema distribuido
# ============================================================

# --- Definición de las matrices ---

M = [
    [120, 150, 100],
    [200, 180, 220],
    [ 90, 110,  95]
]

C = [
    [30, 20, 10],
    [15, 25, 20],
    [40, 10, 30]
]

filas    = 3
columnas = 3


#============================================================
#                       FUNCIONES
#============================================================

# ============================================================
# PARTE B - Punto 3: Tiempos promedio de ejecución
# ============================================================

for x in range(55):
    print("=",end="")
print()
print("  PARTE B — Tiempos promedio de ejecución")
for x in range(55):
    print("=",end="")
print()
# -- Tiempo promedio por FUNCIÓN (promedio de cada fila de M) --
funciones = ["Autenticacion", "Procesamiento de datos", "Generacion de reportes"]

print("\n Tiempo promedio de ejecución por función (fila de M):")
for i in range(filas):
    suma = 0
    for j in range(columnas):
        suma += M[i][j]
    promedio = suma / columnas
    print(funciones[i],":",promedio ,"ms")

# -- Tiempo promedio por SERVIDOR (promedio de cada columna de M) --
servidores = ["Servidor 1", "Servidor 2", "Servidor 3"]

print("\n Tiempo promedio de ejecución por servidor (columna de M):")
for j in range(columnas):
    suma = 0
    for i in range(filas):
        suma += M[i][j]
    promedio = suma / filas
    print(funciones[j],":",promedio ,"ms")

# ============================================================
# PARTE B - Punto 4: Transpuesta de M
# ============================================================

for x in range(55):
    print("=",end="")
print()
print("  PARTE B — Transpuesta de M")
for x in range(55):
    print("=",end="")
print()

MT = [[0]*filas for x in range(columnas)]
contador = 0

for i in range(filas):
    for j in range(columnas):
        MT[j][i] = M[i][j]

print("\n Matriz transpuesta M^T:")
for fila in MT:
    print(" ", fila)

print("""
 ¿Qué representa M^T en este contexto?
   En M original: filas = funciones, columnas = servidores.
   En M^T:        filas = servidores, columnas = funciones.
   Es decir, M^T nos permite analizar, para cada servidor,
   cuánto tarda en ejecutar cada funcion.
""")

# ============================================================
# PARTE C - Punto 5: Producto T = M * C
# ============================================================

for x in range(55):
    print("=",end="")
print()
print("  PARTE C — Producto matricial T = M * C")
for x in range(55):
    print("=",end="")
print()

T = [[0]*filas for x in range(columnas)]
for i in range(filas):
    fila = []
    for j in range(columnas):
        suma = 0
        for k in range(columnas):
            suma += M[i][k] * C[k][j]
        T[i][j] = suma


print("\n Matriz T = M * C:")
for fila in T:
    print(" ", fila)

print("""
    Que representa T?
   Cada valor T[i][j] es la suma ponderada del tiempo de
   ejecucion de la funcion i en todos los servidores,
   multiplicado por la cantidad de veces que se ejecuto
   en cada servidor.
   En otras palabras: T indica la CARGA TOTAL de tiempo
   de ejecucion de cada funcion en cada servidor.
""")