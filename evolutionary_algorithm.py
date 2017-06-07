from deap import base, creator, tools, algorithms
import random
import numpy as np


class EvolutionaryAlgorithm(object):

    def __init__(self, operations, tournsize, population_size, cross_pb, mut_pb):
        self.operations = operations
        self.tournsize = tournsize
        self.toolbox = self.create_toolbox()
        self.population_size = population_size
        self.cross_pb = cross_pb
        self.mut_pb = mut_pb

    def create_toolbox(self):
        creator.create('Fitness', base.Fitness, weights=(-1.0,))
        creator.create('Individual', list, fitness=creator.Fitness)

        toolbox = base.Toolbox()
        toolbox.register('attr_item', random.randint, 0, self.operations.semesters)
        toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_item,
                         len(self.operations.subjects))
        toolbox.register('population', tools.initRepeat, list, toolbox.individual)
        toolbox.register('evaluate', self.operations.evaluate_individual)
        toolbox.register('mate', self.operations.crossover)
        toolbox.register('mutate', self.operations.mutate_individual)
        toolbox.register('select', tools.selTournament, tournsize=self.tournsize)
        return toolbox

    def run(self, ngen):
        lam = 100
        mu = 20

        pop = self.toolbox.population(n=self.population_size)
        hof = tools.ParetoFront()

        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register('avg', np.mean, axis=0)
        stats.register('var', np.var, axis=0)
        stats.register('min', np.min, axis=0)
        stats.register('max', np.max, axis=0)

        pop, log = algorithms.eaMuCommaLambda(pop, self.toolbox, mu, lam, self.cross_pb,
                                              self.mut_pb, ngen, stats, halloffame=hof)
        hof.value = self.toolbox.evaluate(hof.items[0])

        return pop, log, hof
