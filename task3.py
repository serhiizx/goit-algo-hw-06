import networkx as nx
from graph_data import create_graph

print("--- Пошук найдешевшого варіанту (Дейкстра) ---")

G = create_graph()

start = "PrivatBank"
end = "PayPal"

# Найдешевший шлях (мінімальна сумарна комісія)
cheapest_path = nx.dijkstra_path(G, source=start, target=end, weight='weight')
cheapest_cost = nx.dijkstra_path_length(G, source=start, target=end, weight='weight')

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
