import unittest
import product
import shipping
import basket

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(product))
suite.addTests(loader.loadTestsFromModule(shipping))
suite.addTests(loader.loadTestsFromModule(basket))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)