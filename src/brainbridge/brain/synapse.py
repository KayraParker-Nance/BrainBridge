class Synapse:
    def __init__(self, target_neuron, weight, delay):
        self.target_neuron = target_neuron
        self.weight = weight
        self.delay = delay

    def transmit_signal(self):
        strength = self.weight
        self.target_neuron.receive_signal(strength, self.delay)