import numpy as np
import random

def create_reference_solution(chromosome_length):
    number_of_ones = int(chromosome_length / 2)
    # Build an array with an equal mix of zero and ones
    reference = np.zeros(chromosome_length)
    reference[0: number_of_ones] = 1

    # Shuffle the array to mix the zeros and ones
    np.random.shuffle(reference)
    return reference

def create_starting_population(individuals, chromosome_length):
    # Set up an initial array of all zeros
    population = np.zeros((individuals, chromosome_length))
    # Loop through each row (individual)
    for i in range(individuals):
        # Choose a random number of ones to create
        ones = random.randint(0, chromosome_length)
        # Change the required number of zeros to ones
        population[i, 0:ones] = 1
        np.random.shuffle(population[i])

    return population

def calculate_fitness(reference, population):
    # Create an array of True/False compared to reference
    identical_to_reference = population == reference
    # Sum number of genes that are identical to the reference
    fitness_scores = identical_to_reference.sum(axis=1)

    return fitness_scores




if __name__ == '__main__':
    reference = create_reference_solution(10)
    print('Reference solution: \n', reference)
    population = create_starting_population(6, 10)
    print('\nStarting population: \n', population)
    scores = calculate_fitness(reference, population)
    print('\nScores: \n', scores)
