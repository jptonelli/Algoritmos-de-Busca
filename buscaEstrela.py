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

    def insert(self, vertex, cost, accumulated_cost):
        total_cost = accumulated_cost + cost + vertex.heuristic
        self.cities.append((vertex, cost, total_cost))
        self.cities.sort(key=lambda x: x[2])

    def get_best(self):
        return self.cities.pop(0) if self.cities else None


class Map:

    def __init__(self, heuristic_data):
        self.cities = {label: Vertex(label, h) for label, h in heuristic_data.items()}

        self.add_edge("Curitiba", "Araucária", 37)
        self.add_edge("Curitiba", "Balsa Nova", 29)
        self.add_edge("Curitiba", "São José dos Pinhais", 15)
        self.add_edge("Araucária", "Lapa", 18)
        self.add_edge("Balsa Nova", "Campo Largo", 22)
        self.add_edge("Balsa Nova", "Contenda", 19)
        self.add_edge("São José dos Pinhais", "Tijucas do Sul", 49)
        self.add_edge("Campo Largo", "Palmeira", 55)
        self.add_edge("Palmeira", "Irati", 75)
        self.add_edge("Palmeira", "São Mateus do Sul", 77)
        self.add_edge("Irati", "Paulo Frontin", 75)
        self.add_edge("Paulo Frontin", "Porto União", 46)
        self.add_edge("Porto União", "Canoinhas", 78)
        self.add_edge("Canoinhas", "Três Barras", 12)
        self.add_edge("Três Barras", "São Mateus do Sul", 43)
        self.add_edge("São Mateus do Sul", "Lapa", 60)
        self.add_edge("Lapa", "Contenda", 26)
        self.add_edge("Lapa", "Mafra", 57)
        self.add_edge("Mafra", "Tijucas do Sul", 99)

    def add_edge(self, city1, city2, cost):
        self.cities[city1].add_adjacent(self.cities[city2], cost)
        self.cities[city2].add_adjacent(self.cities[city1], cost)


class Routes:
    def __init__(self, target):
        self.target = target
        self.found = False
        self.path = []
        self.total_distance = 0

    def search(self, current, accumulated_cost=0):
        
        print(f"Visitando: {current.label}")
        current.visited = True
        self.path.append(current.label)

        if current == self.target:
            self.found = True
            self.total_distance = accumulated_cost
            return

        sorted_routes = Sort()

        for adjacent, cost in current.adjacent:
            if not adjacent.visited:
                sorted_routes.insert(adjacent, cost, accumulated_cost)

        best_next = sorted_routes.get_best()
        if best_next:
            next_vertex, edge_cost, _ = best_next
            self.search(next_vertex, accumulated_cost + edge_cost)


heuristic_data = {
    "Curitiba": 203, "Araucária": 180, "Balsa Nova": 190, "São José dos Pinhais": 195,
    "Campo Largo": 185, "Palmeira": 170, "Irati": 160, "Paulo Frontin": 150,
    "Porto União": 0, "Canoinhas": 20, "Três Barras": 40, "São Mateus do Sul": 60,
    "Lapa": 140, "Contenda": 175, "Mafra": 50, "Tijucas do Sul": 90
}

mapa = Map(heuristic_data)

rota = Routes(mapa.cities["Porto União"])
rota.search(mapa.cities["Curitiba"])

if rota.found:
    print("\nCaminho encontrado:")
    print(" -> ".join(rota.path))
    print(f"Distância total: {rota.total_distance}")
else:
    print("Nenhum caminho encontrado.")