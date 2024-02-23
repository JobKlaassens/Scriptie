import networkx as nx
import random

def generate_srdigraph(num_nodes, indegree):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes to the graph
    G.add_nodes_from(range(num_nodes))

    # Add edges to satisfy the indegree requirement
    for i in range(num_nodes):
        # Choose distinct source nodes randomly
        population = list(set(range(num_nodes)) - {i})
        indegree_sources = random.sample(population, indegree)
        G.add_edges_from([(source_node, i) for source_node in indegree_sources])

    # Create a list to store neighbors for each node
    node_neighbors = [[] for _ in range(num_nodes)]

    # Populate the node_neighbors list
    for edge in G.edges:
        target_node = edge[1]
        source_node = edge[0]
        node_neighbors[target_node].append(source_node)

    return G, node_neighbors