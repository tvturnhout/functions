def check_zero_sums(values, sum_goal=0):
    """ This function checks whether any possible sum returns zero """
    from itertools import combinations
    zero_sums = []
    for i in range(0, len(values)+1):
        for subset in combinations(values, i):
            if sum(subset) == sum_goal:
                zero_sums.append([values.index(item) for item in subset])
    return zero_sums
