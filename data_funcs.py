import math

# assuming the lists are cleansed for NaNs
def min_lst(lst):
    return min(lst)

def max_lst(lst):
    return max(lst)

def mean_lst(lst):
    return sum(lst) / len(lst)

def stddev_lst(lst):
    mu = mean_lst(lst)
    return math.sqrt(sum([pow(x - mu, 2) for x in lst]) / len(lst))

def median_lst(lst):
    lst.sort()
    if len(lst)%2 == 1:
        return lst[len(lst) // 2]
    else:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2