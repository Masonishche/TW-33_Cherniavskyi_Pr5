import pytest
from algorithm import Individual, SimpleGeneticAlgorithm

@pytest.fixture
def ga_instance():
    problem_size = 5
    population_size = 10
    num_iterations = 100
    return SimpleGeneticAlgorithm(problem_size, population_size, num_iterations)

def test_population_initialization(ga_instance):
    # Перевірка ініціалізації популяції
    ga_instance.initialize_population()
    assert len(ga_instance.population) == ga_instance.population_size
    for individual in ga_instance.population:
        assert len(individual.genes) == ga_instance.problem_size
        for gene in individual.genes:
            assert 0 <= gene <= 1

def test_fitness_evaluation(ga_instance):
    # Перевірка обчислення придатності
    ga_instance.initialize_population()
    for individual in ga_instance.population:
        ga_instance.evaluate_fitness(individual)
        assert individual.fitness is not None

def test_selection(ga_instance):
    # Перевірка процесу вибору
    ga_instance.initialize_population()
    selected_individual = ga_instance.selection()
    assert selected_individual in ga_instance.population

def test_crossover(ga_instance):
    # Перевірка операції кросовера
    parent1 = Individual([0.1, 0.2, 0.3, 0.4, 0.5])
    parent2 = Individual([0.6, 0.7, 0.8, 0.9, 0.0])
    child1, child2 = ga_instance.crossover(parent1, parent2)
    assert len(child1.genes) == len(child2.genes) == len(parent1.genes)
