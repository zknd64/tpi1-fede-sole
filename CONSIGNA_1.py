A = [101, 102, 103, 104, 105, 106]
B = [104, 105, 106, 107, 108]
C = [102, 105, 109]

LARGO_A = 5
LARGO_B = 4
LARGO_C = 2

def union_grupos(vector_A,vector_B,largo_vector_A,largo_vector_B):
    vector_resultado = []*largo_vector_A+largo_vector_B
    contador = 0
    for  i in range(largo_vector_A):
        vector_resultado[i] = vector_A[i]
        contador =+ 1
    for i in range(largo_vector_B):
        vector_resultado[i] = vector_A[i]
        contador += 1
    return vector_resultado

def usuario_en_vector(vector_objetivo,usuario_objetivo,largo_vector):
    for usuario in range(largo_vector):
        if usuario == usuario_objetivo:
            return True
    return False



#usuarios que utilizan ambas plataformas
print("A U B = " ,end= " ")
for usuario in range(LARGO_A):
   if usuario_en_vector(B,A[usuario],LARGO_B):
    print (usuario, end=" ")

#usuarios que utilizan al menos una plataforma 
print("\n x ∈ A ∨ x ∈ B = " ,end = " ")
for usuario in range(LARGO_A):
  print (A[usuario], end= " ") 
for usuario in range(LARGO_B):
  print (B[usuario], end=" " )
#Usuarios que utilizan la plataforma, pero no presentan errores 
print("\nUsuarios sin errores:")
for usuario in range(LARGO_C):
    if not usuario_en_vector(A,C[usuario],LARGO_A):
        print(usuario)
for usuario in range(LARGO_B):
    if not usuario_en_vector(B,B[usuario],LARGO_B):
        print(usuario)
#Usuarios que utilizan exclusivamente una sola plataforma
print ("\n usuarios que utilizan exclusivamente una sola plataforma:")
for usuario in range(LARGO_A):
    usuario_objetivo = A[usuario]
    if not usuario_en_vector(B,usuario_objetivo,LARGO_B):
        print (usuario)
for usuario in B:
    if usuario not in A:
        print (usuario)

print("========== PARTE C ==========")

# Crear union A U B
union = [0]*6
contador = 0
for usuario in A:
    if usuario in B:
        union[contador] = usuario
        contador += 1


# Crear lista con todos los usuarios

todos = [0]*14
contador= 0 
for usuario in A and B and C:
    todos[0]  = usuario
    contador += 1
    

        


# 1) ¿Qué tipo de usuario representa mayor riesgo?

print("\n1) Usuarios de mayor riesgo:")

for usuario in todos:

    p = usuario in A
    q = usuario in B
    r = usuario in C

    if (p or q) and r:

        print("El usuario", usuario,"es un usuario Critico.")
    else:
        print("El usuario", usuario, "es un usuario No Critico")

# 2) ¿Qué significa que un usuario este en C pero no en A U B?

print("\n2) Usuarios en C pero no en A U B:")

for usuario in C:

    if usuario not in union:

        print("El usuario", usuario,"genera errores pero no aparece registrado en API ni WEB, significando que esta accediendo al programa por metodos no aprobados, que puede indicar una falla de vulnerabilidad del sistema")

# 3) ¿Que decision tomarian como equipo programador?

print("\n3) Decision del equipo programador:")

print("Como equipo programador tomariamos las siguientes decisiones:")
print("- Revisar los usuarios criticos y sus errores para poder ver los errores del sistema")
print("- Mejorar la seguridad del sistema")
print("- Corregir errores detectados")
print("- Mejorar la validacion de accesos")