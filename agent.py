import random
from mesa import Agent

class myAgent(Agent):
    def __init__(self, unique_id, model, node_neighbors):
        super().__init__(unique_id, model)
        self.neighbors = node_neighbors[unique_id]
        self.threshold = random.random()  # Random threshold between 0 and 1
        self.status = "inactive"  # Initially, all agents are inactive

    def step(self):
        # Print the neighbors for each node
        print(f"Node {self.unique_id}: Neighbors = {self.neighbors}")

        print(f"Before step: Node {self.unique_id}, Status={self.status}")
        if self.status == 'active':
            print(f"Already active: Node {self.unique_id}")
            return  # If already active, no need to check neighbors

        # Get all neighbors
        all_neighbors = self.neighbors

        # Get active neighbors
        active_neighbors = [agent for agent in self.model.schedule.agents if agent.unique_id in all_neighbors and agent.status == 'active']

        # Calculate the fraction of active neighbors among all neighbors
        fraction_active_neighbors = len(active_neighbors) / len(all_neighbors) if len(all_neighbors) > 0 else 0
        print(f"Node {self.unique_id}: Fraction of active neighbors = {fraction_active_neighbors}, Threshold = {self.threshold}")

        # Check if the fraction is greater than threshold and the node is not already active
        if fraction_active_neighbors >= self.threshold and self.status != 'active':
            self.status = 'active'
            print(f"Now active: Node {self.unique_id}")