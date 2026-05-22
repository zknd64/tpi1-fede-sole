#pt2 A
print("========== PARTE A ==========")

# Funciones

def A(x):

    return 40 * x + 200

def B(x):

    return 70 * x + 50

def C(x):

    return -2 * x * x + 80 * x + 100

def formula_cuadratica(a,b,c):
    discriminante = ((b**2)-(4*a*c))**(1/2)
    if discriminante > 0:
        raiz1 = (-b + discriminante)/(2*a)
        raiz2 = (-b - discriminante)/(2*a)
    return raiz1,raiz2


def barato(x):

    a = A(x)
    b = B(x)
    c = C(x)

    if a <= b and a <= c:

        return "A"

    elif b <= a and b <= c:

        return "B"

    else:

        return "C"


# 1) Pendiente y ordenada

print("\n1) Pendiente y ordenada")

print("Funcion A")
print("Pendiente:", 40)
print("Ordenada al origen:", 200)

print("\nFuncion B")
print("Pendiente:", 70)
print("Ordenada al origen:", 50)

# 2) Paralelas

print("\n2) Paralelas")

if 40 == 70:

    print("Son paralelas")

else:

    print("No son paralelas")

# 3) Interseccion

print("\n3) Punto de interseccion")

x = (200 - 50) / (70 - 40)

y = A(x)

print("x =", x)
print("y =", y)

# 4) Funcion C

print("\n4) Funcion C")

# Vertice

xv = -80 / (2 * -2)

yv = C(xv)

print("\nVertice")

print("x =", xv)
print("y =", yv)

# Raices aproximadas

print("\nRaices aproximadas")

raiz_1,raiz_2 = formula_cuadratica(-2,80,100)


print("\n========== PARTE B ==========")

# Valores
valores = [0, 5, 10, 15, 20, 25, 30, 40, 50]
LARGO_VALORES = 8
# 5 y 7) Evaluar funciones

print("\n5 y 7) Evaluacion")

for indice in range(LARGO_VALORES):
    x = valores[indice]    

    print("\nHoras:", x)

    print("A(x) =", A(x))
    print("B(x) =", B(x))
    print("C(x) =", C(x))

# 8) Plan mas baratos

print("\n8) Plan mas economico")

for indice in range(LARGO_VALORES):
    x = valores[indice]

    print("Para", x, "horas conviene el plan", barato(x))

print("\n========== PARTE C ==========")

# 9) Que plan conviene

print("\n9) Analisis")

for indice in range(LARGO_VALORES):
    x = valores[indice]

    print("Con", x, "horas conviene el plan", barato(x))

# 10) Valores negativos

print("\n10) Valores negativos de C")

for x in range(0, 51):

    if C(x) < 0:

        print("En", x, "horas el costo es negativo")


print("\nExplicacion")

print("Es un problema porque")
print("una empresa no puede")
print("tener costos negativos.")
print("Eso significa que")
print("la funcion deja de")
print("representar un caso real.")