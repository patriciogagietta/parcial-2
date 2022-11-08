# 2 - Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas: 

# a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan
# b. hallar el árbol de expansión mínimo desde el vértice que contiene a C-3PO, Yoda y la princesa Leia
# c. determinar cuales personajes comparten con otro dos episodios o mas(mostrar el par de pesonajes)
# d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, Obi-Wan kenobi
# BB-8
# e. determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los personajes.


from grafo import Grafo

g = Grafo(False)

# A - D cargar grafo
g.insertar_vertice('luke skywalker')
g.insertar_vertice('darth vader')
g.insertar_vertice('yoda')
g.insertar_vertice('boba fett')
g.insertar_vertice('c 3po')
g.insertar_vertice('leia')
g.insertar_vertice('rey')
g.insertar_vertice('kylo ren')
g.insertar_vertice('chewbacca')
g.insertar_vertice('han solo')
g.insertar_vertice('r2 d2')
g.insertar_vertice('obi wan kenobi')
g.insertar_vertice('bb 8')


g.insertar_arista('luke skywalker', 'darth vader', 3)
g.insertar_arista('luke skywalker', 'boba fett', 5)
g.insertar_arista('luke skywalker', 'c 3po', 1)
g.insertar_arista('rey', 'luke skywalker', 6)
g.insertar_arista('chewbacca', 'han solo', 7)
g.insertar_arista('han solo', 'r2 d2', 4)
g.insertar_arista('obi wan kenobi', 'kylo ren', 5)
g.insertar_arista('obi wan kenobi', 'r2 d2', 8)
g.insertar_arista('obi wan kenobi', 'bb 8', 7)
g.insertar_arista('bb 8', 'luke skywalker', 1)
g.insertar_arista('bb 8', 'leia', 2)
g.insertar_arista('kylo ren', 'yoda', 3)
g.insertar_arista('rey', 'chewbacca', 4)
g.insertar_arista('chewbacca', 'leia', 5)
g.insertar_arista('chewbacca', 'bb 8', 10)
g.insertar_arista('darth vader', 'chewbacca', 1)
g.insertar_arista('darth vader', 'r2 d2', 1)
g.insertar_arista('darth vader', 'han solo', 6)
g.insertar_arista('han solo', 'rey', 2)
g.insertar_arista('han solo', 'c 3po', 1)

# B
arbol_min = g.kruskal()

arbol_min = arbol_min[0].split('-')
peso_total = 0

print('arbol de expansion minima:')
for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]} - {nodo[1]} - {nodo[2]}')
print()

print('cantidad de episodios: ', peso_total)
print()

# c. 



# E 

























