from ncr import ncr #n choose r
import numpy as np


def you_win(photo_order, n):
    """WLOG you have photos 0 to n-1, opponent has n to 2n-1
    Check if all of your photos appear before any of your opponents"""
    n_count = 0
    for i in photo_order:
        if i < n:
            n_count += 1
        if n <= i < 2*n:
            return False
        if n_count == n:
            return True


def main():
    N = 54           # Total number of photos
    n = 16           # Number of photos per player
    num_sim = 10000  # Number of simulations

    # Simulate Unique
    count = 0
    for _ in xrange(num_sim):
        list_1 = np.random.choice(N, n, replace=False) # Your photos
        list_2 = np.random.choice(N, n, replace=False) # Opponent's photos
        if set(list_1) & set(list_2): # Check for intersection
            count += 1
    print "probability unique:", \
        ncr(N-n, n) / float(ncr(N, n)), \
        1.0 - count / float(num_sim)

    # Simulate You Win
    count = 0
    for _ in xrange(num_sim):
        photo_order = np.arange(N)
        np.random.shuffle(photo_order)
        if you_win(photo_order, n):
            count += 1
    print "probability you win:", 1./ncr(2 * n, n), count / float(num_sim)


if __name__ == "__main__":
    main()
