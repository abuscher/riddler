import numpy as np
import operator as op
from functools import reduce
from collections import namedtuple

Solution = namedtuple('Solution', 'coefficients roots')


def ncr(n, r):
    """Implementation of n choose r = n!/(r!*(n-r)!)"""
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


def create_polys(coincount):
    """Creates polynomial expansions in list form for n-1 to 1 heads"""
    polys = []
    for i in range(1, coincount):
        poly = []
        neg = (-1)**i
        for j in range(0, i+1):
            poly.append(ncr(i, j) * neg)
            neg *= -1
        for k in range(i+1, coincount):
            poly.append(0)

        polys.append(poly)
    return polys


def create_coeff_limits(num_coins, num_astronauts):
    """Determines the maximum allocation of head/tail outcomes based off the number of coins and astronauts"""
    coeffs = []
    for i in range(1, num_coins):
        coeffs.append(ncr(num_coins, i) // (num_astronauts - 1) + 1)
    return coeffs


def is_valid_solution(root):
    """Checks if root is valid.  Must be real and between 0 and 1."""
    return np.isreal(root) and 0 < root < 1


def solve_poly(coeffs, polys, prob):
    """Generates and solves polynomials using np.roots
    coeffs: list of "coefficients", i.e. multipliers for the number of out head/tail outcomes
    polys: generated with create_polys
    prob: the negated probability -1/num_astronauts
    returns all valid solutions a list on named tuples
    """
    sum_poly = []
    valid_solutions = []
    for degree in range(len(polys[0])):
        term = 0
        for j in range(len(polys)):  # for each polynomial
            term += coeffs[j] * polys[j][degree]
        sum_poly.append(term)
    sum_poly.append(prob)
    ans = np.roots(sum_poly)
    for root in ans:
        if is_valid_solution(root):
            valid_solutions.append(Solution(coeffs, root))

    return valid_solutions


def main():
    num_astronauts = 3
    num_coins = 6
    prob = -1.0/num_astronauts
    polys = create_polys(num_coins)
    coeff_limits = create_coeff_limits(num_coins, num_astronauts)
    solutions = []

    # Loop through all possible coefficient combinations
    coeff_dividers = []
    for i in range(1, len(coeff_limits)):
        coeff_dividers.append(reduce(op.mul, coeff_limits[i:], 1))

    # This helps us avoid recursion and nested for loops
    for i in range(reduce(op.mul, coeff_limits, 1)):
        coeffs = []
        for j in range(len(coeff_dividers)):
            coeffs.append((i // coeff_dividers[j]) % coeff_limits[j])
        coeffs.append(i % coeff_limits[-1])
        solutions += solve_poly(coeffs, polys, prob)

    for solution in solutions:
        print "[", solution.coefficients, ", ", np.round(np.real(solution.roots), 4), "],"
    print "Number of solutions:", len(solutions)


if __name__ == '__main__':
    main()
