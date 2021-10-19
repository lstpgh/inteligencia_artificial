# configuración inicial
  # cantidad de objetos
  # numero máximo de atributos por objeto
  # lista de objetos disponibles para el juego
  
# crear objeto
  # seleccionar objeto
  # crear atributos del objeto
  # asignar pesos a los atributos

# jugar
  # evaluar la agenda
  # seleccionar
    # si gana-> aprender(True)
    # sino gana-> aprender(False)

# aprender
  # (True): actualizar agenda de jugadas
  # (False): actualizar agenda de objetos, agenda de jugadas



import random
import numpy

# valores iniciales

COU = 10  #!!! configuración inicial del juego. Cantidad de Objetos del Universo

num_max_atr = COU // 2  #!!! Máximo de atributos por objeto

# listar objetos disponibles en forma aleatoria
objDisponibles = list(range(COU))   
objDisponibles = random.sample(objDisponibles, k=len(objDisponibles))

agenda = list()


# crear objeto

def crearObj():

  # crear objeto

  obj = objDisponibles.pop()  # extrae el último objeto de la lista de objDisponibles

  # objDisponibles = random.sample(objDisponibles, k=len(objDisponibles))
    #!!! volver a sortear?
  
  # crear atributos(num_atr)

  num_atr = random.randrange(1, num_max_atr + 1)  #!!! aleatorio. 1 ... COU/2 inclusive

  atrPosibles = list(range(COU))  #!!! generar lista de posibilidades. {(0 ... COU - 1]}
  atrPosibles = random.sample(atrPosibles, k=len(atrPosibles))  #!!! desordenar la lista
  atrPosibles.remove(obj)  #!!! descarta el objeto de la lista de atributos

  pesosAtrs = list()  # genera lista de pesos de los atributos, entre [0.5 ... 1)
  for n in range(num_atr):  
    pesosAtrs += [random.uniform(0.5, 1)]

  atrs = list()  # generar lista de atributos
  pesos = list()
  for n in range(num_atr):  
    atrs += [atrPosibles.pop()]  # extrae los atributos de la lista de atrPosibles
    pesos += [pesosAtrs.pop()]  # le asigna peso a cada atributo

  juego = [obj, atrs, pesos]

  tablaObj = list()
  for n in range(len(atrs)):
    tablaObj += [[n, juego[0], juego[1][n], juego[2][n]]]

  juego = numpy.array(tablaObj)

  return juego


# aprender
def aprenderObj(objApre): 
     return objApre # to do


# jugar  
def jugar(obj):
  pass  # to do


# - - -   T E S T   - - - #

#obj = juego[0]
#atrs = juego[1]
#pesos = juego[2]

#agenda = list()
#for n in range(len(atrs)):
#  agenda += [[n, juego[0], juego[1][n], juego[2][n]]]

# generar_universo()
#for n in range(COU):
#  juego = crearObj()
  #!!! print(juego)


obj = crearObj()
print("objeto: ")
print(obj)

# jugar
  # evaluar la agenda
if not len(agenda):  # si agenda está vacía -> perder -> aprender -> jugar
  print("agenda vacía")
  idAgenda = 0
  # aprender()
  agenda += [obj[idAgenda]]
  idAgenda += 1
  agenda = numpy.array(agenda)           
  print("agenda: ")
  print(agenda)
  # jugar()  #  volver a jugar
  atrSel = agenda[0, 2]  # selecciona primer atributo. recorrido en orden
  print("atributo seleccionado: ", atrSel)
    # evaluar seleccion
  if atrSel in (obj[:2]):  # evalua agenda
    # aprender(seleccion, ...)
    objSel = agenda[0, 1] # selecciona el objeto relacionado con el atributo
    print("objeto seleccionado: ", objSel)
    if objSel == obj[0, 1]:  # si ganó -> aprender -> finalizar
      print("ganó")


# - - -   T E S T   - - - #



# - - -   N O T A S   V A R I A S  - - - #

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
  # evaluar la agenda
  # seleccionar métodos ??
    # si gana-> aprender
      # actualiza agenda : historial
    # no gana-> aprender
      # actualiza agenda : historial, obj, atr(obj)


# obj = {3: [4, 9, 2, 7, 6] }  #!!! vector_atr no debe incluir al obj

# obj = {3: [2, 4, 6, 7, 9]}  #!!! aleatorios

# ale = [0.5, 0.9, 0,5, 0,6, 0.7]  #!!! aleatorios. pueden ser repetidos, redondeados

# objPeso = {3: [0.5, 0.9, 0,5, 0,6, 0.7]}  #!!!

#!!! obj = random.randrange(1, COU + 1)  #!!! aleatorio desde 1 hasta COU

# - - -   N O T A S   V A R I A S  - - - #
