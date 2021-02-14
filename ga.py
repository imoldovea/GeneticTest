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

if __name__ == '__main__':
    #print (create_reference_solution(70))
    print(create_starting_population(4, 10))
