
class Grafo:
    def __init__(self, vertices):
        self.V = vertices  
        self.grafo = []    

    def agregar_arista(self, u, v, peso):
        self.grafo.append((peso, u, v))

    def encontrar(self, parent, i):
        if parent[i] == i:
            return i
        return self.encontrar(parent, parent[i])

    def unir(self, parent, rango, x, y):
        xraiz = self.encontrar(parent, x)
        yraiz = self.encontrar(parent, y)

        if xraiz != yraiz:
            if rango[xraiz] < rango[yraiz]:
                parent[xraiz] = yraiz
            elif rango[xraiz] > rango[yraiz]:
                parent[yraiz] = xraiz
            else:
                parent[yraiz] = xraiz
                rango[xraiz] += 1

    def kruskal(self):
        resultado = []  
        i = 0  
        e = 0 

        self.grafo = sorted(self.grafo, key=lambda item: item[0])

        parent = []
        rango = []

        for node in range(self.V):
            parent.append(node)
            rango.append(0)

        while e < self.V - 1:

            peso, u, v = self.grafo[i]
            i += 1
            x = self.encontrar(parent, u)
            y = self.encontrar(parent, v)

            if x != y:
                e += 1
                resultado.append((u, v, peso))
                self.unir(parent, rango, x, y)

       
        print("Las aristas del árbol de expansión mínima son:")
        for u, v, peso in resultado:
            print(f"{u} - {v}: {peso}")


g = Grafo(4)
g.agregar_arista(0, 1, 10)
g.agregar_arista(0, 2, 6)
g.agregar_arista(0, 3, 5)
g.agregar_arista(1, 3, 15)
g.agregar_arista(2, 3, 4)

g.kruskal()
