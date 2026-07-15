import unittest
from brainbridge.simulation.configuration import Configuration

class TestConfiguration(unittest.TestCase):
    def test_get_existing_key(self):
        config = Configuration({'key1': 'value1'})
        self.assertEqual(config.get('key1'), 'value1')

    def test_get_non_existing_key_with_default(self):
        config = Configuration({'key1': 'value1'})
        self.assertEqual(config.get('key2', 'default_value'), 'default_value')

    def test_set_and_get_key(self):
        config = Configuration()
        config.set('key1', 'value1')
        self.assertEqual(config.get('key1'), 'value1')
        