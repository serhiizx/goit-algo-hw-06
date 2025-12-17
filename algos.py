from collections import deque

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    parents = {vertex: None for vertex in graph}
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_vertex

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances, parents


def bfs_find_path(graph, start, end):
    visited = set()
    queue = deque([start])
    parent = {start: None}

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            
            if vertex == end:
                path = []
                while vertex is not None:
                    path.append(vertex)
                    vertex = parent[vertex]
                return path[::-1]
            
            for neighbor in set(graph[vertex]) - visited:
                if neighbor not in parent:
                    parent[neighbor] = vertex
                queue.append(neighbor)
    return []

def dfs_path_exists(graph, start, end):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex == end:
            return True
        
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return False