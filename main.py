# This file is used for development and local testing
import mean_var_std
import unittest

# Print a manual execution test to your console terminal
print(mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Automatically run the assertions written inside test_module.py
print("\nRunning Unit Tests:")
unittest.main(module='test_module', exit=False)