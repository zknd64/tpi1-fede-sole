# Tabla de verdad de: (p or q) and r

valores = [True, False]

print("p\tq\tr\tp or q\t(p or q) and r")

for p in valores:
    for q in valores:
        for r in valores:
            resultado1 = p or q            
            resultado2 = resultado1 and r
                

            print(p, "\t", q, "\t", r, "\t", resultado1, "\t", resultado2)