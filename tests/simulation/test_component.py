import unittest
from brainbridge.simulation.component import Component

class TestComponent(unittest.TestCase):
    def test_component_update_called(self):
        component = FakeComponent()
        component.update()
        assert component.update_called == True

class FakeComponent(Component):
        def __init__(self):
             self.update_called = False
        @property
        def enabled(self) -> bool:
            return True

        def update(self):
            self.update_called = True