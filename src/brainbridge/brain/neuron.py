class Neuron:
    def __init__(self, id, restingV, thresholdV):
        self.id = id
        self.restingV = restingV
        self.thresholdV = thresholdV
        self.currentV = restingV
        self.outgoing_synapses = []
    
    def fire(self):
        for synapse in self.outgoing_synapses:
            synapse.transmit_signal()
    
    def receive_signal(self, signal_strength, delay=0):
        self.currentV += signal_strength
        if self.currentV >= self.thresholdV:
            self.fire()
            #delay
            self.reset()
            
    def reset(self):
        self.currentV = self.restingV

    def update(self):
        pass