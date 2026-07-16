from brainbridge.simulation.component import Component

class Brain(Component):
    def __init__(self, name, id):
        self.neuron_groups = []

    def update(self):
        for neuron_group in self.neuron_groups:
            neuron_group.update()

    def add_neuron_group(self, neuron_group):
        self.neuron_groups.append(neuron_group)

    def remove_neuron_group(self, neuron_group):
        if neuron_group in self.neuron_groups:
            self.neuron_groups.remove(neuron_group)