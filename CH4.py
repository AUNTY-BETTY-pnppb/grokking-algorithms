# DIVIDE AND CONQUER

# Divide and Conquer (D&C, A recursive algorithm)
# 1. Figure out the base case. This should be the simplest possible case.
# 2. Divide or decrease your problem until it becomes the base case.

# Euclid’s algorithm
# “If you find the biggest box that will work for this size, that will be the
# biggest box that will work for the entire farm.”

# TIP - in a recursive function involving an array, the base case is often
# an empty array or an array with one element.

def sumItUp(arr):

    if len(arr) == 1:
        return arr[0]
    else:
        return arr.pop() + sumItUp(arr)

x = [2,4,6]
print("The sum of numbers in the list is " + str(sumItUp(x)))

y = [1,2,4,6]
def numItems(arr):
    if len(arr) == 1:
        return 1
    else:
        arr.pop()
        return 1 + numItems(arr)

print("The number of items in the list is " + str(numItems(y)))

z = [8,75,2,34,21]
def maxNum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        m = max(arr[1:])
        return m if m > arr[0] else arr[0]

print("The largest number in the list is " + str(maxNum(z)))

# QUICKSORT (Recursive algorithm)

# A fast sorting algorithm

# Partitioning - Pick a pivot, sort items smaller than pivot to left, bigger to right. Recurse.

def quicksort(array):
    if len(array) < 2:
        return array 
    else:
        pivot = array[0] 
        less = [i for i in array[1:] if i <= pivot] 
        greater = [i for i in array[1:] if i > pivot] 
        return quicksort(less) + [pivot] + quicksort(greater)

print("The sorted list - ", end ="")
print(quicksort([10, 5, 2, 3]))

# quicksort and Big O
# Quicksort is unique because its speed depends on the pivot you choose.
# worst case, quicksort takes O(n2)
# average case, quicksort takes O(nlogn)