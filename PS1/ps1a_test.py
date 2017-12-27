import unittest
import ps1a

class PS1ATest(unittest.TestCase):

    def test_compute(self):

        values = [
            (120000, 0.1, 1000000, 183), #TestCase 1
            (80000, 0.15, 500000, 105), #TestCase 2
        ]

        for value in values:

            self.assertEqual(ps1a.compute(value[0], value[1], value[2]), value[3])

    def test_compute_geometrical(self):

        values = [
            (120000, 0.1, 1000000, 183), #TestCase 1
            (80000, 0.15, 500000, 105), #TestCase 2
        ]

        for value in values:

            self.assertEqual(ps1a.compute_geometrical(value[0], value[1], value[2]), value[3])


if __name__ == "__main__":

    unittest.main()
