import random

class Individual:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = None

class SimpleGeneticAlgorithm:
    def __init__(self, problem_size, population_size, num_iterations):
        self.problem_size = problem_size
        self.population_size = population_size
        self.num_iterations = num_iterations
        self.population = []
        self.iteration = 0

    def initialize_population(self):
        self.population = [self.generate_random_individual() for _ in range(self.population_size)]

    def generate_random_individual(self):
        # Генерація випадкової особини (кандидата на рішення)
        genes = [random.uniform(0, 1) for _ in range(self.problem_size)]
        return Individual(genes)

    def evaluate_fitness(self, individual):
        # Обчислення фітнес-функції для конкретної особини
        individual.fitness = sum(individual.genes)

    def fitness_evaluation(self):
        # Обчислення значень придатності для кожної особини у популяції
        for individual in self.population:
            self.evaluate_fitness(individual)

    def selection(self):
        # Вибір батьків для наступної генерації
        # Вибір випадкового батька зі зваженим ймовірністю на основі придатності
        self.fitness_evaluation()

        return random.choices(self.population, weights=[ind.fitness for ind in self.population])[0]

    def crossover(self, parent1, parent2):
        # Застосування кросоверу для створення нової особини (нащадка)
        crossover_point = random.randint(0, self.problem_size - 1)
        child1_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
        child2_genes = parent2.genes[:crossover_point] + parent1.genes[crossover_point:]
        return Individual(child1_genes), Individual(child2_genes)

    def mutation(self, individual, mutation_rate):
        # Мутація з деякою ймовірністю для кожного гена
        for i in range(self.problem_size):
            if random.random() < mutation_rate:
                individual.genes[i] = random.uniform(0, 1)

    def elitism_selection(self, new_population):
        # Вибір для наступної популяції, зберігаючи найкращих
        # Впевнитися, що всі особини мають обчислене значення fitness
        for individual in new_population:
            if individual.fitness is None:
                self.evaluate_fitness(individual)
        new_population.sort(key=lambda x: x.fitness, reverse=True)
        return new_population[:self.population_size]

    def stop_condition(self):
        # Перевірка умови зупинки (за досягненням кількості ітерацій)
        return self.iteration >= self.num_iterations

    def run(self):
        self.initialize_population()

        while not self.stop_condition():
            self.fitness_evaluation()

            new_population = []
            for _ in range(self.population_size):
                parent1 = self.selection()
                parent2 = self.selection()
                child1, child2 = self.crossover(parent1, parent2)
                self.mutation(child1, mutation_rate=0.1)
                self.mutation(child2, mutation_rate=0.1)
                new_population.append(child1)
                new_population.append(child2)

            self.population = self.elitism_selection(new_population)
            self.iteration += 1

        # Повернення найкращого знайденого рішення
        best_individual = max(self.population, key=lambda x: x.fitness)
        return best_individual

