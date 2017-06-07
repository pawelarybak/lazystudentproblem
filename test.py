import unittest
from operations import *


class MyTestCase(unittest.TestCase):
    subjects = [
            Subject(1, 10, 5),
            Subject(2, 5, 2),
            Subject(3, 7, 4),
            Subject(4, 8, 2),
            Subject(5, 6, 3),
            Subject(6, 4, 2),
            Subject(7, 8, 4),
            Subject(8, 6, 2),
            Subject(9, 7, 3),
            Subject(10, 6, 5),
        ]
    semesters = 2
    max_times = [20, 20]
    min_points = 20
    operations = EvolutionaryOperations(subjects, semesters, max_times, min_points)

    def test_points_penalty(self):
        ind1 = [2, 0, 1, 0, 2, 0, 0, 0, 1, 1]
        ind2 = [2, 2, 1, 1, 0, 0, 2, 0, 0, 1]
        ind3 = [1, 1, 0, 0, 2, 2, 0, 0, 0, 2]
        p1 = self.operations.points_penalty(ind1)
        self.assertEqual(p1, 0)
        p2 = self.operations.points_penalty(ind2)
        self.assertEqual(p2, 0)
        p3 = self.operations.points_penalty(ind3)
        self.assertEqual(p3, 49)

    def test_time_penalty(self):
        ind1 = [2, 0, 1, 0, 2, 0, 0, 0, 1, 1]
        ind2 = [2, 2, 1, 1, 0, 0, 2, 0, 0, 1]
        ind3 = [1, 1, 0, 0, 2, 2, 0, 0, 0, 2]
        p1 = self.operations.time_penalty(ind1)
        self.assertEqual(p1, 0)
        p2 = self.operations.time_penalty(ind2)
        self.assertEqual(p2, 10)
        p3 = self.operations.time_penalty(ind3)
        self.assertEqual(p3, 0)

    def test_evaluate(self):
        ind1 = [2, 0, 1, 0, 2, 0, 0, 0, 1, 1]
        ind2 = [2, 2, 1, 1, 0, 0, 2, 0, 0, 1]
        ind3 = [1, 1, 0, 0, 2, 2, 0, 0, 0, 2]
        f1, = self.operations.evaluate_individual(ind1)
        self.assertEqual(f1, 36)
        f2, = self.operations.evaluate_individual(ind2)
        self.assertEqual(f2, 54)
        f3, = self.operations.evaluate_individual(ind3)
        self.assertEqual(f3, 80)

    def test_mutate_range(self):
        ind1 = [2, 0, 1, 0, 2, 0, 0, 0, 1, 1]
        print(ind1)
        new_ind, = self.operations.mutate_individual(ind1)
        print(new_ind)
        for val in new_ind:
            self.assertIn(val, range(0, self.semesters + 1))

    def test_crossover(self):
        ind1 = [2, 0, 1, 0, 2, 0, 0, 0, 1, 1]
        ind2 = [2, 2, 1, 1, 0, 0, 2, 0, 0, 1]
        old = []
        old.extend(ind1)
        old.extend(ind2)
        print('{} {}'.format(ind1, ind2))
        ind1, ind2 = self.operations.crossover(ind1, ind2)
        new = []
        new.extend(ind1)
        new.extend(ind2)
        print('{} {}'.format(ind1, ind2))
        for sem in range(0, self.semesters + 1):
            self.assertEqual(new.count(sem), old.count(sem))


if __name__ == '__main__':
    unittest.main()
