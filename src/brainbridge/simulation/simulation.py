class Simulation:
    def __init__(self, clock, configuration, logger):
        self.clock = clock
        self.configuration = configuration
        self.logger = logger
        self.components = []

    def run(self):
        while self.clock.get_current_time() < self.configuration.get('duration', duration):
            self.update()
            self.logger.log(f"Current time: {self.clock.get_current_time()}")
            self.clock.step(self.configuration.get('step', step))

    def update(self):
        for c in self.components:
            if c.enabled:
                c.update()
                self.logger.log(f"Updated component: {c.__class__.__name__}")


    def add_component(self, component):
        self.components.append(component)
        
        