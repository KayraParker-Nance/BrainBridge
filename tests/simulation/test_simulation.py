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
        self.assertIn(component, simulation.components)

    def test_update_calls_component_update(self):
        simulation = Simulation(clock=SimulationClock(), configuration=Configuration(), logger=Logger())
        component = FakeComponent()
        simulation.add_component(component)
        simulation.update()
        self.assertTrue(component.update_called)

    def test_empty_simulation(self):
        simulation = Simulation(clock=SimulationClock(), configuration=Configuration(), logger=Logger())
        self.assertEqual(len(simulation.components), 0)
        simulation.update()  # Should not raise any exceptions

class FakeComponent(Component):
        def __init__(self):
             self.update_called = False
        @property
        def enabled(self) -> bool:
            return True

        def update(self):
            self.update_called = True