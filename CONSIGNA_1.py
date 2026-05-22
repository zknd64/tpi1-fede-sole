


A = [101, 102, 103, 104, 105, 106]
B = [104, 105, 106, 107, 108]
C = [102, 105, 109]

INDICE_A = 6
INDICE_B = 5
INDICE_C = 3

def usuario_en_vector(vector_objetivo,usuario_objetivo,largo_vector):
    for usuario in range(largo_vector):
        if vector_objetivo[usuario] == usuario_objetivo:
            return True
    return False


#usuarios que utilizan ambas plataformas
print("A U B = " ,end= " ")
for usuario in range(INDICE_A):
   if usuario_en_vector(B,A[usuario],INDICE_B):
    print (A[usuario], end=" ")

#usuarios que utilizan al menos una plataforma 
print("\n x E A ∨ x E B = " ,end = " ")
for usuario in range(INDICE_A):
  print (A[usuario], end= " ") 

for usuario in range(INDICE_B):
  print (B[usuario], end=" " )

#Usuarios que utilizan la plataforma, pero no presentan errores 
print("\nUsuarios sin errores:")
for usuario in range(INDICE_C):
    if not usuario_en_vector(C,A[usuario],INDICE_C):
        print(A[usuario],end= " ")
for usuario in range(INDICE_C):
        if not usuario_en_vector(C,A[usuario],INDICE_C):
            print(B[usuario],end= " ")

#Usuarios que utilizan exclusivamente una sola plataforma
print ("\n usuarios que utilizan exclusivamente una sola plataforma:")
for usuario in range(INDICE_A):
    usuario_objetivo = A[usuario]
    if not usuario_en_vector(B,usuario_objetivo,INDICE_B):
        print (usuario_objetivo,end=" ")
for usuario in range(INDICE_B):
    usuario_objetivo = B[usuario]
    if not usuario_en_vector(A,usuario_objetivo,INDICE_A):
        print (usuario_objetivo, end=" ")

print("\n========== PARTE C ==========")

#Crear union A U B
union = [0]*(INDICE_A+INDICE_B)

for usuario in range(INDICE_A):
    union[usuario] = A[usuario]

indice_union = INDICE_A
for usuario in range(INDICE_B):
    if not usuario_en_vector(A, B[usuario], INDICE_A):
        union[indice_union] = B[usuario]
        indice_union += 1



#Crear lista con todos los usuarios
todos = [0]*(INDICE_A+INDICE_B+INDICE_C)
for usuario in range(INDICE_A + INDICE_B):
    todos[usuario] = union[usuario]
    
for usuario in range(INDICE_C):
    todos[INDICE_A + INDICE_B + usuario] = C[usuario]
#1) ¿Qué tipo de usuario representa mayor riesgo?
print("\n1) Usuarios de mayor riesgo:")

for usuario in range(INDICE_A + INDICE_B + INDICE_C):
    aux3 = todos[usuario]
    if aux3 == 0:
        continue  # saltar slots vacíos
    if usuario_en_vector(union, aux3, INDICE_A + INDICE_B) and usuario_en_vector(C, aux3, INDICE_C):
        print("El usuario", aux3, "es un usuario Critico.")
    elif aux3 != 0:
        print("El usuario", aux3, "es un usuario No Critico")
#2) ¿Qué significa que un usuario este en C pero no en A U B?
print("\n2) Usuarios en C pero no en A U B:")

for usuario in range(INDICE_A+INDICE_B+INDICE_C):
    aux4 = todos[usuario]
    if not usuario_en_vector(union, aux4,INDICE_A+INDICE_B) and aux4 != 0:
        
        print("El usuario", aux4,"genera errores pero no aparece registrado en API ni WEB, significando que esta accediendo al programa por metodos no aprobados, que puede indicar una falla de vulnerabilidad del sistema")

#3) ¿Que decision tomarian como equipo programador?
print("\n3) Decision del equipo programador:")

print("Como equipo programador tomariamos las siguientes decisiones:")
print("- Revisar los usuarios criticos y sus errores para poder ver los errores del sistema")
print("- Mejorar la seguridad del sistema")
print("- Corregir errores detectados")
print("- Mejorar la validacion de accesos")

# Tabla de la verdad
INDICE = 2
valores = [True, False]

print("p\tq\tr\tp or q\t\t(p or q) and r")

for p in range(INDICE):
    for q in range(INDICE):
        for r in range(INDICE):
            resultado1 = valores[p] or valores[q]
            resultado2 = resultado1 and valores[r]
            print(valores[p], "\t", valores[q], "\t", valores[r], "\t", resultado1, "\t\t", resultado2)