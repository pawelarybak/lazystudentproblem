from operations import *
from evolutionary_algorithm import EvolutionaryAlgorithm
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')
        exec(f.read())
        operations = EvolutionaryOperations(subjects, semesters, max_times, min_points)
        algorithm = EvolutionaryAlgorithm(operations, 4, 5, 0.3, 0.7)
        pop, log, hof = algorithm.run(1000)
        print('hof = ', hof.items[0], ';')
        print('value = ', hof.value[0], ';')