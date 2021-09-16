# ARRAYS & LINKED LISTS (Data Structure)

# array - Using an array means all your tasks are stored 
# contiguously (right next to each other) in memory.

# Advantage:
# easy look up time
# Disadvantage:
# IF array is full and you want to add another item, MUST move
# list to another space in memory.

# reading - O(1)
# insertion - O(n)
# deletion - O(n)

#-------------------------------------------------------------------
# linked list - item can be anywhere in memory
# Each item stores the address of the next item in the list.
# A bunch of random memory addresses are linked together.

# Advantage:
# Doesn't waste memory, as items are stored anywhere they can be
# Disadvantage:
# gotta jump around, if you want to find a specific element, you
# have to sif through the memory addresses


# reading - O(n)
# insertion - O(1)
# deletion - O(1)


# LISTS ARE BETTER FOR INSERTION AND DELETION

#---------------------------------------------------------------------
# ACCESS

# Sequential access - reading the elements one by one, starting
# at the first element. Linked lists can only do sequential access.

# Random access - means you can jump directly to the nth element.
# Arrays are faster at reads because they provide random access.

#----------------------------------------------------------------------
# SORTING

# Selection sort - search entire list for element, put into another list, repeat.
# So you have an operation that takes O(n) time, and you have to do that n times.
# O(n × n) = O(n^2)

def findSmallest(arr):
    smallest = arr[0] 
    smallest_index = 0 
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr): 
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        print(smallest, end=", ")
        print(arr[smallest])
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))