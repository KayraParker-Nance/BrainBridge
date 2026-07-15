from abc import ABC, abstractmethod

class Component(ABC):
    @property
    @abstractmethod
    def enabled(self) -> bool:
        pass
        
    @abstractmethod
    def update(self):
        pass