# An algorithm is a set of instructions for accomplishing a task

# BINARY SEARCH

# Its input is a sorted list of elements. 
# If an element you’re looking for is in that list, binary search
# returns the position where it’s located. Otherwise, binary
# search returns null.

# Simple search - go step by step | for list of n, n steps.
# Binary search - keep splitting list in half til element found | for list of n, log^2 n steps.

def binary_search(list, item):
    low = 0 
    high = len(list)
    high = high - 1 
    
    while low <= high:     
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid, guess
        if guess > item: 
            high = mid - 1
        else: 
            low = mid + 1
    return None 
# my_list = [1, 3, 5, 7, 9] 

my_list = []
for i in range(0, 100):
    my_list.append(i)

print(binary_search(my_list, 75)) # => 1
print(binary_search(my_list, -1)) # => None 

# RUNNING TIME

# linear time - maximum number of guesses is the same as the size of the list. O(n)
# logarithmic time - max number of guesses is the log^2 n of the list. O(Logn)

# Big O Notation - tells you how fast an algorithm is

# Big O doesn’t tell you the speed in seconds. Big O notation lets you compare the 
# number of operations. It tells you how fast the algorithm grows.

# Big O looks at worst case scenario

# Common Big O runtimes:

# O(log n) log time - Binary search.
# O(n) linear time - Simple search.
# O(n * log n) - A fast sorting algorithm, like quicksort 
# O(n2) - A slow sorting algorithm, like selection sort 
# O(n!). - A really slow algorithm, like the traveling salesperson*

# Traveling salesperson - Salesperson wants to hit all five cities while traveling the minimum distance. 
# look at every possible order in which he could travel to the cities. O(n!) 1x2x3x4x5...