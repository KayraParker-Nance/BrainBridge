from brainbridge.simulation.component import Component

class NeuronGroup(Component):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.neurons = []

    def update(self):
        for neuron in self.neurons:
            neuron.update()

    def add_neuron(self, neuron):
        self.neurons.append(neuron)

    def remove_neuron(self, neuron):
        if neuron in self.neurons:
            self.neurons.remove(neuron)

