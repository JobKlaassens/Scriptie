import networkx as nx
import matplotlib.pyplot as plt
from plot_graph import generate_srdigraph
from model import myModel
import random

# Generate a directed graph as the network
num_nodes = 20
indegree = 1
graph, node_neighbors = generate_srdigraph(num_nodes, indegree)

# Create an instance of the model
model = myModel(graph, node_neighbors)

# Randomly activate one node at the start
initial_active_node = random.choice(list(graph.nodes))
print("Initial active node:", initial_active_node)
agents_in_cell = model.grid.get_cell_list_contents([initial_active_node])
agents_in_cell[0].status = 'active'

# Define color map
color_map = {'active': 'green', 'inactive': 'red'}


# Run the model for a certain number of steps
num_steps = 5
for step in range(num_steps):

    # Get node statuses and map them to colors
    node_statuses = [agent.status for agent in model.schedule.agents]
    node_colors = [color_map[status] for status in node_statuses]

    # Visualize the model
    plt.figure(figsize=(10, 6))
    pos = nx.circular_layout(graph)  # Circular layout
    nx.draw(graph, pos=pos, with_labels=True, node_size=700, node_color=node_colors, cmap=plt.cm.RdYlGn, font_size=8,
            font_color="black", font_weight="bold", arrowsize=10)
    plt.title(f"Model Visualization (Step {step + 1})")
    plt.show()


    model.step()



