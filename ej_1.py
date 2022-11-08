# 1 - Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas de personajes de la saga de Star Wars, de los cuales se sabe su nombre, altura y peso. Además deberá contemplar los siguientes requerimientos(debe cargar al menos 20 personajes):

# a. se debe poder cargar un nuevo personaje, modificarlo(cualquiera de sus campos) y darlo de baja
# b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker
# c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro
# d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos
# e. mostrar un listado por nivel de los personajes del árbol
# f. determinar si Grogu esta en el árbol y responder lo siguiente:
# mostrar toda su información
# en que tipo de nodo esta(hoja, intermedio o raíz)
# que altura tiene el nodo dentro del árbol.


from arbol import (
    nodoArbol,
    insertar_nodo,
    preorden,
    inorden,
    postorden,
    busqueda,
    inorden_yoda,
    inorden_mandalorian,
    inorden_luke,
    inorden_090,
    inorden_mayor_75k,
    por_nivel,
    inorden_grogu,
    inorden_empieza_con,
    eliminar_nodo,
    inorden_datos,
    altura,
)


arbol_stars_wars = nodoArbol()


star_wars = [
    {'nombre': 'han solo', 'altura': 1.90, 'peso': 80},
    {'nombre': 'finn', 'altura': 1.78, 'peso': 78},
    {'nombre': 'padme amidala', 'altura': 1.75, 'peso': 80},
    {'nombre': 'rose tico', 'altura': 1.70, 'peso': 65},
    {'nombre': 'kylo ren', 'altura': 1.80, 'peso': 78},
    {'nombre': 'lando', 'altura': 1.76, 'peso': 78},
    {'nombre': 'r2d2', 'altura': 1.60, 'peso': 60},
    {'nombre': 'mace windu', 'altura': 1.78, 'peso': 80},
    {'nombre': 'cara dune', 'altura': 1.67, 'peso': 75},
    {'nombre': 'moff guideon', 'altura': 1.86, 'peso': 90},
    {'nombre': 'mayfeld', 'altura': 1.78, 'peso': 80},
    {'nombre': 'boba fett', 'altura': 1.82, 'peso': 82},
    {'nombre': 'yoda', 'altura': 0.80, 'peso': 50},
    {'nombre': 'darth maul', 'altura': 0.70, 'peso': 75},
    {'nombre': 'chewbacca', 'altura': 1.80, 'peso': 85},
    {'nombre': 'obi wan kenobi', 'altura': 1.75, 'peso': 70},
    {'nombre': 'luke skywalker', 'altura': 1.70, 'peso': 80},
    {'nombre': 'mandalorian', 'altura': 1.76, 'peso': 80},
    {'nombre': 'grogu', 'altura': 1.60, 'peso': 60},
    {'nombre': 'darth vader', 'altura': 1.90, 'peso': 90}
]

for personaje in star_wars:
    insertar_nodo(arbol_stars_wars,personaje['nombre'],personaje)

# A
#agregar personaje al arbol
clave = input('desea agregar un personaje? si-no: ')

if clave == 'si':
    nombre = input('nombre del personaje que desea agregar: ')
    altura = input('altura del personaje que desea agregar: ')
    peso = input('peso del personaje que desea agregar: ')
    datos = {'nombre': nombre, 'altura': altura, 'peso': peso}
    insertar_nodo(arbol_stars_wars,nombre,datos)
print()

#modificar un personaje
aux = input('desea modificar un personaje? si-no: ')
if aux == 'si':
    clave = input('ingrese el personaje que desea modificar: ')
    pos = busqueda(arbol_stars_wars, clave)

    if pos is not None:
        nuevo_nombre = input('ingrese el personaje nuevo: ')
        datos = {'nombre': nuevo_nombre, 'altura': pos['datos']['altura'], 'peso': pos['datos']['peso']}
        eliminar_nodo(arbol_stars_wars, clave)
        insertar_nodo(arbol_stars_wars, nuevo_nombre, datos)
print()


#eliminar del arbol
aux = input('desea eliminar un personaje? si-no: ')
if aux == 'si':
    clave = input('ingrese el personaje que desea eliminar: ')
    eliminar_nodo(arbol_stars_wars,clave)

inorden_datos(arbol_stars_wars)

# # B
inorden_yoda(arbol_stars_wars)
print()
inorden_mandalorian(arbol_stars_wars)
print()
inorden_luke(arbol_stars_wars)
print()

# # C
inorden_090(arbol_stars_wars)
print()

# # D
inorden_mayor_75k(arbol_stars_wars)
print()

# # E
print('barrido por nivel')
por_nivel(arbol_stars_wars)
print()

# F 
inorden_grogu(arbol_stars_wars)
print('altura del arbol: ', altura(arbol_stars_wars))














