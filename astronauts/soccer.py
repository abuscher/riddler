import itertools


def brute_soccer(team_list):
    average_score = sum([1./i for i in team_list])
    if abs(average_score-2.0) < 1e-8:
        print team_list, average_score

for i in itertools.combinations(range(1, 25), 11):
    brute_soccer(i)
