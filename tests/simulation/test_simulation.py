import unittest
from brainbridge.simulation.simulation import Simulation
from brainbridge.simulation.simulationClock import SimulationClock
from brainbridge.simulation.configuration import Configuration
from brainbridge.simulation.logger import Logger
from brainbridge.simulation.component import Component

class TestSimulation(unittest.TestCase):
    def test_add_component(self):
        simulation = Simulation(clock=SimulationClock(), configuration=Configuration(), logger=Logger())
        component = FakeComponent()
        simulation.add_component(component)
        assert len(simulation.components) == 1

    def test_update_calls_component_update(self):
        simulation = Simulation(clock=SimulationClock(), configuration=Configuration(), logger=Logger())
        component = FakeComponent()
        simulation.add_component(component)
        simulation.update()
        assert component.update_called == True

    def test_empty_simulation(self):
        simulation = Simulation(clock=SimulationClock(), configuration=Configuration(), logger=Logger())
        assert len(simulation.components) == 0
        simulation.update()  # Should not raise any exceptions

    def test_multiple_components_update(self):
        simulation = Simulation(clock=SimulationClock(), configuration=Configuration(), logger=Logger())
        component1 = FakeComponent()
        component2 = FakeComponent()
        simulation.add_component(component1)
        simulation.add_component(component2)
        simulation.update()
        assert component1.update_called == True
        assert component2.update_called == True

    def test_disabled_component_does_not_update(self):
        simulation = Simulation(clock=SimulationClock(), configuration=Configuration(), logger=Logger())
        component = FakeComponent()
        component.set_enabled(False)  # Disable the component
        simulation.add_component(component)
        simulation.update()
        assert component.update_called == False

class FakeComponent(Component):
        def __init__(self):
             self.update_called = False
             self._enabled: bool = True
        @property
        def enabled(self) -> bool:
            return self._enabled

        def update(self):
            self.update_called = True

        def set_enabled(self, enabled: bool):
            self._enabled = enabled