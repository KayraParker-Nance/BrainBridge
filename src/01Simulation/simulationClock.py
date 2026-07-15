class SimulationClock:
    def __init__(self):
        self.current_time = 0.0

    def step(self, delta_time):
        self.current_time += delta_time

    def get_current_time(self):
        return self.current_time
        