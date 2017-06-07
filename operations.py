from collections import namedtuple
import random

Subject = namedtuple('Subject', ['no', 'time', 'points'])


class EvolutionaryOperations(object):

    def __init__(self, subjects, semesters, max_times, min_points, sigma=0.5):

        self.subjects = subjects

        self.semesters = semesters
        self.max_times = max_times
        self.min_points = min_points
        self.sigma = sigma

    def time_penalty(self, individual):
        penalty = 0

        for i in range(1, self.semesters + 1):
            times = sum([self.subjects[no].time for no, sem in enumerate(individual) if sem == i])
            if times > self.max_times[i - 1]:
                penalty += (times - self.max_times[i - 1]) ** 2

        return penalty

    def points_penalty(self, individual):
        penalty = 0

        points = sum([self.subjects[no].points for no, sem in enumerate(individual) if sem != 0])

        if points < self.min_points:
            penalty += sum(self.max_times)
            penalty += (self.min_points - points) ** 2

        return penalty

    def evaluate_individual(self, individual):
        time = sum([self.subjects[no].time for no, sem in enumerate(individual) if sem != 0])
        p1 = self.time_penalty(individual)
        p2 = self.points_penalty(individual)

        return time + p1 + p2,

    def mutate_individual(self, ind):
        for no, _ in enumerate(ind):
            k = round(random.gauss(0, self.sigma))
            ind[no] = abs(ind[no] + k) % (self.semesters + 1)

        return ind,

    def crossover(self, ind1, ind2):
        k = random.randint(1, len(self.subjects))
        indices = random.sample(range(0, len(self.subjects)), k)
        for i in indices:
            tmp = ind1[i]
            ind1[i] = ind2[i]
            ind2[i] = tmp

        return ind1, ind2,
