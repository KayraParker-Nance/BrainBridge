class Configuration:
    def __init__(self, configs = {}):
        self.configs = configs

    def get(self, key, default=None):
        return self.configs[key] if key in self.configs else default

    def set(self, key, value):
        self.configs[key] = value