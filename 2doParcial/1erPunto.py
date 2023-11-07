from arbol_binario import BinaryTree

# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su name, número, type/types para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:


class Pokemon:
    def __init__(self, name, number, type):
        self.name = name
        self.number = number
        self.type = type
        
    def __str__(self):
        
        return f"Name: {self.name} - Number: {self.number} - Type: {self.type}"
    
    
pokemon_data = [
    {'name':"Bulbasaur", 'number':1, 'type':"Planta-Veneno"},
    {'name':"Charmander", 'number':4, 'type':"Fuego"},
    {'name':"Squirtle", 'number':7, 'type':"Agua"},
    {'name':"Pikachu", 'number':25, 'type':"Eléctrico"},
    {'name':"Jigglypuff", 'number':39,'type': "Normal-Hada"},
    {'name':"Gengar", 'number':94, 'type':"Fantasma-Veneno"},
    {'name':"Snorlax", 'number':143, 'type':"Normal"},
    {'name':"Mewtwo", 'number':150, 'type':"Psíquico"},
    {'name':"Gyarados", 'number':130, 'type':"Agua-Volador"},
    {'name':"Machamp", 'number':68, 'type':"Lucha"},
    {'name':"Jolteon", 'number':135, 'type':"Eléctrico"},
    {'name':"Lycanroc", 'number':745, 'type':"Roca"},
    {'name':"Tyrantrum", 'number':697, 'type':"Roca-Dragón"}
    ]


# a) los índices de cada uno de los árboles deben ser name, número y type;

name = BinaryTree()
number = BinaryTree()
type = BinaryTree()

for pokemon in pokemon_data:
    name.insert_node(pokemon['name'], [pokemon['number'], pokemon['type']])
    number.insert_node(pokemon['number'], [pokemon['name'], pokemon['type']])
    type.insert_node(pokemon['type'], [pokemon['number'], pokemon['name']])

# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;

def search_by_number(tree, number):
    value = tree.search(number)
    
    if value:
        print(f'{name}')
    
name.search_by_coincidence_proximity('Bul')
print()

number.search_number_pokemon(1)
print()

# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;

type.determinados_types()
print()

# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;

print("Inorden por numero")
number.inorden()
print()

print("Inorden por numero")
number.inorden()
print()

print("By level por nombre")
name.by_level()
print()

# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;

name.search_by_coincidence_proximity('Jolteon')
name.search_by_coincidence_proximity('Lycanroc')
name.search_by_coincidence_proximity('Tyrantrum')
print()

# f) Determina cuantos Pokémons hay de tipo eléctrico y acero.

electricos = type.pokemon_electrico()
acero = type.pokemon_acero()

print(f"Hay {electricos} pokemons de tipo electrico y {acero} pokemons de tipo acero")