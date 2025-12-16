import networkx as nx

# Фінансові установи (вершини)
NODES = [
    "PrivatBank", "Monobank", "Wise", "Revolut", "PayPal", "Binance", "I_AM_ALONE"
]

# Перекази з комісіями (ребра з вагами)
TRANSFERS = [
    ("PrivatBank", "Binance", 50),
    ("PrivatBank", "Monobank", 2),
    ("Monobank", "Revolut", 3),
    ("Revolut", "PayPal", 4),
    ("PayPal", "Binance", 5),    
    ("PrivatBank", "Wise", 10),
    ("Wise", "Binance", 15),
]


def create_graph():
    G = nx.Graph()
    G.add_nodes_from(NODES)
    G.add_weighted_edges_from(TRANSFERS)
    return G

