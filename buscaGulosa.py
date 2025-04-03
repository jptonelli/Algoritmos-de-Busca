class Vertex:
    def __init__(self, label, heuristic):
        self.label = label
        self.heuristic = heuristic
        self.adjacent = []
        self.visited = False

    def add_adjacent(self, vertex, cost):
        self.adjacent.append((vertex, cost))


class Sort:

    def __init__(self):
        self.cities = []

    def insert(self, vertex):
        self.cities.append(vertex)
        self.cities.sort(key=lambda x: x.heuristic) 

    def get_best(self):
        return self.cities.pop(0) if self.cities else None


class Map:

    def __init__(self, heuristic_data):
        self.cities = {label: Vertex(label, h) for label, h in heuristic_data.items()}

        self.add_edge("Arad", "Zerind", 75)
        self.add_edge("Arad", "Timisoara", 118)
        self.add_edge("Arad", "Sibiu", 140)
        self.add_edge("Zerind", "Oradea", 71)
        self.add_edge("Oradea", "Sibiu", 151)
        self.add_edge("Timisoara", "Lugoj", 111)
        self.add_edge("Lugoj", "Mehadia", 70)
        self.add_edge("Mehadia", "Drobeta", 75)
        self.add_edge("Drobeta", "Craiova", 120)
        self.add_edge("Craiova", "Pitesti", 138)
        self.add_edge("Craiova", "Rimnicu Vilcea", 146)
        self.add_edge("Sibiu", "Fagaras", 99)
        self.add_edge("Sibiu", "Rimnicu Vilcea", 80)
        self.add_edge("Rimnicu Vilcea", "Pitesti", 97)
        self.add_edge("Fagaras", "Bucareste", 211)
        self.add_edge("Pitesti", "Bucareste", 101)
        self.add_edge("Bucareste", "Giurgiu", 90)
        self.add_edge("Bucareste", "Urziceni", 85)
        self.add_edge("Urziceni", "Vaslui", 142)
        self.add_edge("Urziceni", "Hirsova", 98)
        self.add_edge("Hirsova", "Eforie", 86)
        self.add_edge("Vaslui", "Iasi", 92)
        self.add_edge("Iasi", "Neamt", 87)

    def add_edge(self, city1, city2, cost):
        self.cities[city1].add_adjacent(self.cities[city2], cost)
        self.cities[city2].add_adjacent(self.cities[city1], cost)


class Routes:
    def __init__(self, target):
        self.target = target
        self.found = False
        self.path = []

    def search(self, current):

        print(f"Visitando: {current.label}")
        current.visited = True
        self.path.append(current.label)

        if current == self.target:
            self.found = True
            return

        sorted_routes = Sort()

        for adjacent, _ in current.adjacent:
            if not adjacent.visited:
                sorted_routes.insert(adjacent)

        best_next = sorted_routes.get_best()
        if best_next:
            self.search(best_next)

heuristic_data = {
    "Arad": 366, "Zerind": 374, "Oradea": 380, "Timisoara": 329, "Lugoj": 244, "Mehadia": 241, 
    "Drobeta": 242, "Craiova": 160, "Sibiu": 253, "Rimnicu Vilcea": 193, "Fagaras": 176, 
    "Pitesti": 100, "Bucareste": 0, "Giurgiu": 77, "Urziceni": 80, "Hirsova": 151, 
    "Eforie": 161, "Vaslui": 199, "Iasi": 226, "Neamt": 234
}

mapa = Map(heuristic_data)

rota = Routes(mapa.cities["Bucareste"])
rota.search(mapa.cities["Arad"])

if rota.found:
    print("\nCaminho encontrado:")
    print(" -> ".join(rota.path))
else:
    print("Nenhum caminho encontrado.")
