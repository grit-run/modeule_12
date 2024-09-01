import module_12_3
import unittest


allTests = unittest.TestSuite()
allTests.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.TournamentTest))
allTests.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(allTests)