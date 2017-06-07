from operations import *
from evolutionary_algorithm import EvolutionaryAlgorithm

if __name__ == '__main__':
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
    algorithm = EvolutionaryAlgorithm(operations, 4, 5, 0.3, 0.7)
    pop, log, hof = algorithm.run(1000)
    print('===========================')
    print('Final population:', pop)
    print('===========================')
    print('Hall of fame:', hof.items[0], 'Value:', hof.value)
