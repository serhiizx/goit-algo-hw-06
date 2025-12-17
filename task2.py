from graph_data import create_graph
import sys
from algos import bfs_find_path, dfs_path_exists

G = create_graph()

start = sys.argv[1] if len(sys.argv) > 1 else "PrivatBank"
end = sys.argv[2] if len(sys.argv) > 2 else "PayPal"

bfs_result = bfs_find_path(G, start, end)
dfs_result = dfs_path_exists(G, start, end)

print(f"Ціль: Переказати кошти з {start} на {end}")
print(f"\nШлях BFS (Найменше кроків): {bfs_result}")
print(f"-> Кількість кроків: {len(bfs_result) - 1}")

print(f"\nDFS перевірка: Шлях від {start} до {end} {'існує' if dfs_result else 'не існує'}")
