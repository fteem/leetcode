import itertools


def combine(n, k):
    return list(itertools.combinations([i+1 for i in range(n)], k))

if __name__ == '__main__':
    assert(combine(4, 2) == [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])