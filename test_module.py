import unittest
import mean_var_std

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean_var_std.calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])
        expected = {
            'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
            'variance': [[6.888888888888889, 0.6666666666666666, 8.666666666666666], [3.555555555555556, 10.666666666666666, 6.222222222222222], 7.876543209876543],
            'standard deviation': [[2.624669295116709, 0.816496580927726, 2.943920288734949], [1.8856180831641267, 3.2659863237109044, 2.494438257849294], 2.806518001402248],
            'max': [[8, 6, 7], [6, 8, 7], 8],
            'min': [[1, 4, 0], [2, 0, 1], 0],
            'sum': [[11, 15, 9], [10, 12, 13], 35]
        }
        self.assertEqual(actual, expected, "Expected a different output dictionary formatting.")

    def test_calculate_with_few_digits(self):
        with self.assertRaises(ValueError) as context:
            mean_var_std.calculate([2, 6, 2, 8, 4, 0, 1])
        self.assertEqual(str(context.exception), "List must contain nine numbers.", "Expected precise ValueError string structure.")

if __name__ == "__main__":
    unittest.main()