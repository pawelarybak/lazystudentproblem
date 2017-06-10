from operations import *
from evolutionary_algorithm import EvolutionaryAlgorithm
import sys

def save_to_csv(log_obj, arg, filename):
    out = [l[arg] for l in log_obj]
    with open(filename, 'w') as csvfile:
        for num, val in enumerate(out):
            csvfile.write('{:f} {}\n'.format(num, float(val)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')
        exec(f.read())
        operations = EvolutionaryOperations(subjects, semesters, max_times, min_points)
        algorithm = EvolutionaryAlgorithm(operations, 4, 40, 0.3, 0.7)
        pop, log, hof = algorithm.run(1000)
        save_to_csv(log.chapters['fitness'], 'min', 'min.csv')
        save_to_csv(log.chapters['limits'], 'number', 'out_of_limits.csv')
        
        best = min(hof.items, key=lambda x: x.fitness.values)
        if not best.out_of_limits:
            print('Found solution within limits')
        else:
            print('Best solution out of limits')

        print('hof = ', best, ';')