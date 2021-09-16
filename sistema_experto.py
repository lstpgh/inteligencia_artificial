
antecedentes = ["fiebre", "tos", "malestar", "dolor de garganta"]

consecuentes = ["gripa", "faringitis"]

gripa, faringitis = 0, 0  # Vaciar la agenda 

síntoma = True
while síntoma:  # Mientras se disponga de hechos
    
    síntoma = input("síntoma: ")  # Leer un hecho
    
    if síntoma in antecedentes:  # Para todas las reglas donde este hecho es
                                 #  antecedente:
                                 #     El consecuente se coloca en la agenda,
                                 #      si no estaba allí.
                                 #     Si el consecuente está en la agenda,
                                 #      se le suma 1
        
        if síntoma == "fiebre": gripa += 1 
        if síntoma == "tos" : gripa += 1
        if síntoma == "malestar" : gripa += 1
        if síntoma == "malestar" : faringitis += 1
        if síntoma == "dolor de garganta" : faringitis += 1
    else :
        print("síntoma no válido")

    print("gripa: ", gripa, "faringitis: ", faringitis)

if gripa == 0 and faringitis == 0:  # Cuando el ciclo termine:
                                    #  Si la agenda está vacía, informar esta anomalía
    print("agenda vacía")  

else:  # En caso contrario, se elige como enfermedad aquella que tenga el mayor
       #  número de síntomas
    if gripa > faringitis : enfermedad = "gripa"
    if faringitis > gripa : enfermedad = "faringitis"
    if gripa == faringitis :  # Si hay un empate, se informa sobre dicho empate
        print("empate entre gripa y faringitis")
    else :
        print("enfermedad:", enfermedad)
                                                    
