import unittest
from brainbridge.simulation.simulationClock import SimulationClock

class TestSimulationClock(unittest.TestCase):
    def test_clock_initialization(self):
        clock = SimulationClock()
        assert clock.current_time == 0.0

    def test_clock_step(self):
        clock = SimulationClock()
        clock.step(1.0)
        assert clock.current_time == 1.0
        clock.step(2.0)
        assert clock.current_time == 3.0