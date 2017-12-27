import unittest
import ps1b

class PS1BTest(unittest.TestCase):

    def test_compute(self):

        values = [
            (120000, 0.05, 500000, 0.03, 142), #TestCase 1
            (80000, 0.1, 800000, 0.03, 159), #TestCase 2
            (75000, 0.05, 1500000, 0.05, 261) #TestCase 3
        ]

        for value in values:

            self.assertEqual(ps1b.compute(value[0], value[1], value[2], value[3]), value[4])


if __name__ == "__main__":

    unittest.main()
