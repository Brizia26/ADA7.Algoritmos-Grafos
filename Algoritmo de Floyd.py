
INF = float('inf')

def floyd_warshall(graph):
    num_vertices = len(graph)

    dist = [[graph[i][j] for j in range(num_vertices)] for i in range(num_vertices)]

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
            
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

if __name__ == "__main__":

    graph = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ]

    shortest_paths = floyd_warshall(graph)

    print("Distancias más cortas entre todos los pares de nodos:")
    for row in shortest_paths:
        print(row)
