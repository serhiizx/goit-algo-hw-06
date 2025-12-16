from collections import deque
from graph_data import create_graph

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


G = create_graph()

start = "PrivatBank"
end = "PayPal"

bfs_result = bfs_find_path(G, start, end)
dfs_result = dfs_path_exists(G, start, end)

print(f"Ціль: Переказати кошти з {start} на {end}")
print(f"\nШлях BFS (Найменше кроків): {bfs_result}")
print(f"-> Кількість кроків: {len(bfs_result) - 1}")

print(f"\nDFS перевірка: Шлях від {start} до {end} {'існує' if dfs_result else 'не існує'}")
