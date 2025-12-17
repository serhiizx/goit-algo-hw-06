import networkx as nx
from graph_data import create_graph
import sys
from algos import dijkstra

print("--- Пошук найдешевшого варіанту (Дейкстра) ---")

G = create_graph()

start = sys.argv[1] if len(sys.argv) > 1 else "PrivatBank"
end = sys.argv[2] if len(sys.argv) > 2 else "PayPal"

def nx_to_dict(G):
    return {node: {n: G[node][n]['weight'] for n in G.neighbors(node)} for node in G.nodes()}

def get_path(parents, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents[current]
    return path[::-1]

G = create_graph()
graph_dict = nx_to_dict(G)

start = sys.argv[1] if len(sys.argv) > 1 else "PrivatBank"
end = sys.argv[2] if len(sys.argv) > 2 else "PayPal"

distances, parents = dijkstra(graph_dict, start)

cheapest_path = get_path(parents, start, end)
cheapest_cost = distances[end]

print(f"Оптимальний маршрут: {cheapest_path}")
print(f"Сумарна комісія: {cheapest_cost} $")

bfs_path = nx.shortest_path(G, source=start, target=end)
bfs_cost = sum(G[bfs_path[i]][bfs_path[i+1]]['weight'] for i in range(len(bfs_path)-1))

print("\n--- ВИСНОВКИ ---")
print(f"1. Прямий шлях (BFS): {bfs_path}")
print(f"Вартість: {bfs_cost} $")

print(f"\n2.Оптимальний шлях (Дейкстра): {cheapest_path}")
print(f"Вартість: {cheapest_cost} $")

if cheapest_cost < bfs_cost:
    print(f"\nЕкономія: {bfs_cost - cheapest_cost} $")
