from itertools import combinations

initial_elements = [1, 2, 3, 4]

possible_extra_elements = list(combinations(range(1, 5), 2))

all_possible_die_A = [initial_elements + list(extra_elements) for extra_elements in possible_extra_elements]

all_possible_die_B = list(combinations(range(1, 9), 6))

def calculate_sum_probabilities(die_A, die_B):
    sum_probabilities = [0] * 13
    
    for i in die_A:
        for j in die_B:
            sum_probabilities[i + j] += 1
    
    sum_probabilities = [prob for prob in sum_probabilities[2:13]]
    
    return sum_probabilities

def prob_distribution_matches(sum_probabilities):
    target_distribution = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    return sum_probabilities == target_distribution

for die_A in all_possible_die_A:
    for die_B in all_possible_die_B:
        sum_probabilities = calculate_sum_probabilities(die_A, die_B)
        if prob_distribution_matches(sum_probabilities):
            print("\nNew_DIE A:", die_A, "\nNew_DIE B:", list(die_B))
            print()
            
            