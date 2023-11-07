from grafo import Grafo
from random import randint

# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar 
# los algoritmos necesarios para resolver las siguientes tareas: 


# d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader,
# Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.

grafo = Grafo(dirigido=False)

star_wars_personajes = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C 3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2 D2", "BB 8"]

for i in star_wars_personajes:
    grafo.insert_vertice(i)

    
# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad 
# de episodios en los que aparecieron juntos ambos personajes que se relacionan; 

j=0

for i in star_wars_personajes:
    posicion = grafo.search_vertice(i)
    value = grafo.get_element_by_index(posicion)
    
    if value[1].size() < 4:
        k = 0
        while j == 0:
            if k >= len(star_wars_personajes):
                j=1
            else:
                lugar = star_wars_personajes[k]
                posicionB = grafo.search_vertice(lugar)
                valueB = grafo.get_element_by_index(posicionB)
                checker = grafo.is_adyacent(value[0],valueB[0])
                grafo.mark_as_not_visited()
                
                if valueB[1].size() < 3 and value[0] != valueB[0] and checker == False:
                    peso = randint(1, 20)
                    grafo.insert_arist(value[0], valueB[0], peso)
                    if value[1].size() == 3:
                        j=1
                k += 1
        j=0

grafo.barrido()

arbol_min = grafo.kruskal()


# b) hallar el árbol de expansión minino y determinar si contiene a Yoda; 
# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son. 

max_value = 0
max_node = list
i=0

for arbol in arbol_min:
    print("Arbol minimo:")
    for node in arbol.split(";"):
        value = node.split("-")
        print(node)
        if value[0]=="Yoda" or value[1]=="Yoda":
            i = 1
        if int(value[2])>max_value:
            max_node = value
    if i ==1:
        print("Yoda existe en el arbol minimo")
        print()
        
        print(f"{max_node[0]} y {max_node[1]} comparten el numero maximo de episodios ({max_node[2]})")