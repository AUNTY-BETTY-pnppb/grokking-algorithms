# NP-COMPLETE PROBLEMS

# NP-complete problems - problems that have no fast algorithmic solution

# greedy algorithm - at each step, pick the optimal move. (Pick the smallest dinstance)
# this algorithm is simple to write and gets pretty close to the actual answer

# HOW TO MAXIMIZE SUBSETS (set-covering problem)

# 1. List every possible subset of stations. This is called the power set. There are
# 2^n possible subsets. O(2^n)

# 2. From these, pick the set with the smallest number of stations that
# covers all 50 states.

# Step 1 takes very long to do

# Approximation algorithms - If calculating the exact answer takes too long, find the approx

# 1. Pick the station that covers the most states that haven’t been covered yet. 
# It’s OK if the station covers some states that have been covered already. 

# 2. Repeat until all the states are covered. O(n^2) much better than O(2^n)

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# Sets can’t have duplicates

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = []

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states            # Since we are using sets, this is a set intersection, so
        if len(covered) > len(states_covered):      # imagine the two circles, covered looks at the place of intersection
            best_station = station
            states_covered = covered

states_needed -= states_covered
final_stations.add(best_station)

print(final_stations)

# The traveling-salesperson problem and the set-covering problem both
# have something in common: you calculate every possible solution and
# pick the smallest/shortest one - N-COMPLETE

# HOW TO NOTICE N-COMPLETE:
# Your algorithm runs quickly with a handful of items but really slows down with more items.

# “All combinations of X” usually point to an NP-complete problem

# have to calculate “every possible version” of X because you can’t break it down into smaller sub-problems

# If your problem involves a sequence and it’s hard to solve

# If your problem involves a set and it’s hard to solve