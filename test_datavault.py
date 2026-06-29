# test_datavault.py
"""
Tests for DataVault module.
"""

import unittest
from datavault import DataVault

class TestDataVault(unittest.TestCase):
    """Test cases for DataVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataVault()
        self.assertIsInstance(instance, DataVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
