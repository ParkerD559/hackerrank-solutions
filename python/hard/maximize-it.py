import functools
import operator
import itertools


"""
S = (X1^2 + X2^2 + ... + Xk^2) % M
"""


def func(xs, m):  # func to maximize (S)
    return functools.reduce(operator.add, [x ** 2 for x in xs]) % m


def main():
    num_lists, modulo = map(int, input().split())
    lines = [[int(num) for num in input().split()[1::]] for _ in range(num_lists)]
    answers = [func(xs, modulo) for xs in itertools.product(*lines)]
    print(max(answers))


if __name__ == "__main__":
    main()
