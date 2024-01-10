import unittest
import pandas as pd
from model import predict_price  # assuming your file is named model.py

class TestModel(unittest.TestCase):
    def test_predict_price(self):
        # Test case: 3 habitaciones, 5 piso, 1 barrio
        result = predict_price(3, 5, 1)
        self.assertIsInstance(result, float)  # The result should be a float

        # Test case: 2 habitaciones, 1 piso, 2 barrio
        result = predict_price(2, 1, 2)
        self.assertIsInstance(result, float)  # The result should be a float

        # Test case: 4 habitaciones, 10 piso, 3 barrio
        result = predict_price(4, 10, 3)
        self.assertIsInstance(result, float)  # The result should be a float

if __name__ == '__main__':
    unittest.main()
    