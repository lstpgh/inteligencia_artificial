hechos = {1: "fiebre",
          2: "malestar",
          3: "dolor de garganta",
          4: "faringitis",
          5: "gripa"}

antecedentes = (1, 2, 3)

consecuentes = (4, 5)

reglas = ((1, 5, 0.2),  # antecedente, consecuente, difuso
          (2, 5, 0.7),
          (3, 4, 0.8),
          (2, 4, 0.6))

# vaciar la agenda

agenda = {1: 0,  # antecedente: ocurrencias en la agenda
          2: 0,  
          3: 0,
          4: 0.0,  # consecuente: difuso acumulado
          5: 0.0}

loop = True
while loop:  # Mientras se disponga de hechos
    
    print("seleccione un síntoma: (1)", hechos[1], "\n"
          "                       (2)", hechos[2], "\n"
          "                       (3)", hechos[3], "\n"
          "                       (0) -terminar-\n")

    antecedente = input(": ")# Leer un hecho

    if antecedente not in ("1", "2", "3", "0"):
        print("ingrese el número del síntoma")
        continue

    else:
        antecedente = int(antecedente)
    
    if antecedente in antecedentes:  # Para todas las reglas donde este hecho es
                                     # antecedente
        
        if agenda[antecedente] != 0:
            print("el síntoma ya fue evaluado. Seleccione otro síntoma")
            continue

        for n in range (len(reglas)):

            if reglas[n][0] == antecedente:  # actualizar agenda
                agenda[antecedente] = 1  # actualizar antecedente en agenda
                # actualizar consecuente en agenda
                consecuente = reglas[n][1]  # leer consecuente
                # calcular consecuente
                # consecuente + (1 - consecuente) * difuso
                agenda[consecuente] += (1 - agenda[consecuente]) * reglas[n][2] 
                       
    elif antecedente == 0:
        loop = False

    else:
        print("síntoma no válido, intente otra vez")

    print(hechos[4], agenda[4], hechos[5], agenda[5])

if agenda[4] == 0 and agenda[5] == 0:  # Cuando el ciclo termine:
    print("agenda vacía")  #  Si la agenda está vacía, informar esta anomalía

else:  # En caso contrario, se elige como enfermedad aquella que tenga el mayor
       # valor difuso
       
    if agenda[4] > agenda[5] :
        enfermedad = hechos[4]
        porcentaje = agenda[4] * 100
    if agenda[5] > agenda[4] :
        enfermedad = hechos[5]
        porcentaje = agenda[5] * 100
    if agenda[4] == agenda[5] :  # Si hay un empate, se informa sobre dicho empate
        print("empate entre", hechos[4], "y", hechos[5])
    else :
        print("el impaciente tiene :", enfermedad, "(en un", porcentaje, "%)")
                                                    
