import random
import numpy

# valores iniciales

COU = 10  #!!! configuración inicial del juego. Cantidad de Objetos del Universo

num_max_atr = COU // 2  #!!! Máximo de atributos por objeto

objJugados = list()  #!!! Lista de objetos jugados

objCreados = list() # lista de objetos creados

# listar objetos disponibles en forma aleatoria
objDisponibles = list(range(COU))   
objDisponibles = random.sample(objDisponibles, k=len(objDisponibles))

id_uConocido = 0

def crearObj():

  # crear objeto

  obj = objDisponibles.pop()  # extrae el último objeto de la lista de objDisponibles

  # objDisponibles = random.sample(objDisponibles, k=len(objDisponibles))
    #!!! volver a sortear?
  
  # crear atributos(num_atr)

  num_atr = random.randrange(1, num_max_atr + 1)  #!!! aleatorio. 1 ... COU/2 inclusive

  atrPosibles = list(range(COU))  #!!! generar lista de posibilidades. {(0 ... COU - 1]}
  atrPosibles = random.sample(atrPosibles, k=len(atrPosibles))  #!!! desordenar la lista de
  atrPosibles.remove(obj)  #!!! descarta el objeto de la lista de atributos

  atr = list()  # generar lista de atributos
  for n in range(num_atr):  
    atr += [atrPosibles.pop()]  # extrae los atributos de la lista de atrPosibles

  juego = [obj, atr]

  return juego

juego = crearObj()

  

# jugar
  # evaluar
    # consultar agenda

  # seleccionar
    # si gana-> aprender
      # actualiza agenda : historial
    
#uConocido = [[id_uConocido], juego] 

    # no gana-> aprender
      # actualiza agenda : historial, obj, atr(obj)
  


# - - -   T E S T   - - - #

obj = juego[0]
atr = juego[1]
agenda = list()
for n in range(len(atr)):
  agenda += [[n, juego[0], juego[1][n]]]

uConocido = numpy.array(agenda)

print("objeto generado: ")
print(juego, "\n")
print("objeto tabulado: ")
print(agenda, "\n")
print("objeto numpy: ")
print(uConocido, "\n")

# generar_universo()
#for n in range(COU):
#  juego = crearObj()
#  print(n, ":", juego)
  
#  objCreados += [juego]  # actualiza la lista de objCreados
#  objJugados += [juego]  # actualiza la lista de objJugados
#  print(n, ":", juego)

#!!!print(objCreados)
#!!!print(objJugados)


# - - -   T E S T   - - - #


# - - -   N O T A S   - - - #

# crear obj - juego
  # configurar el juego
    # definir la cantidad de obj de u (constante en cada juego)
    # definir num__max_atr (COU //2) 
    # definir num_atr(num_max_atr) : aleatorio
  # construir_obj()
    # crear objPosibles: lista
    # crear atributos(num_atr)    
    # ordenar_atr() ??
    # asignar_$((COU/2 ... COU-1) / COU) ??
      # tabla_$()

# jugar
  # evaluar
    # consultar agenda
  # seleccionar
    # si gana-> aprender
      # actualiza agenda : historial
    # no gana-> aprender
      # actualiza agenda : historial, obj, atr(obj)


# obj = {3: [4, 9, 2, 7, 6] }  #!!! vector_atr no debe incluir al obj

# obj = {3: [2, 4, 6, 7, 9]}  #!!! aleatorios

# ale = [0.5, 0.9, 0,5, 0,6, 0.7]  #!!! aleatorios. pueden ser repetidos, redondeados

# objPeso = {3: [0.5, 0.9, 0,5, 0,6, 0.7]}  #!!!

#!!! obj = random.randrange(1, COU + 1)  #!!! aleatorio desde 1 hasta COU



