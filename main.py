from operations import *
from evolutionary_algorithm import EvolutionaryAlgorithm


def save_to_csv(log_obj, arg, filename):
    out = [l[arg] for l in log_obj]
    with open(filename, 'w') as csvfile:
        for num, val in enumerate(out):
            csvfile.write('{:f} {}\n'.format(num, float(val)))


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
    pop, log, hof = algorithm.run(100)
    save_to_csv(log.chapters['fitness'], 'min', 'min.csv')
    save_to_csv(log.chapters['limits'], 'number', 'out_of_limits.csv')
    print('===========================')
    print('Final population:', pop)
    print('===========================')
    if not hof.items[0].out_of_limits:
        print('Found solution within limits')
    else:
        print('Best solution out of limits')
    print('Individual:', hof.items[0], 'Value:', hof.items[0].fitness.values)
