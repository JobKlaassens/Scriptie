from mesa import Model
from mesa.time import RandomActivation
from mesa.space import NetworkGrid
from agent import myAgent

class myModel(Model):
    def __init__(self, graph, node_neighbors):
        self.graph = graph
        self.num_nodes = len(graph.nodes)
        self.grid = NetworkGrid(self.graph)
        self.schedule = RandomActivation(self)

        # Create agents for each node in the graph
        for node_id in self.graph.nodes:
            agent = myAgent(node_id, self, node_neighbors)  # Pass node_neighbors to each agent
            self.grid.place_agent(agent, node_id)
            self.schedule.add(agent)

    def step(self):
        node_neighbors = {}  # Define node_neighbors here if you need it in the step method
        for node_id in self.graph.nodes:
            node_neighbors[node_id] = [neighbor for neighbor in self.graph.neighbors(node_id)]

        self.schedule.step()