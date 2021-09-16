# RECURSION

# “Loops may achieve a performance gain for your program.
#  Recursion may achieve a performance gain for your programmer. 
#  Choose which is more important in your situation!”

# Recursion - a function which calls its self.
# WARNING - make a base case, avoid infinite loop.
#         - 2 parts: base case and recursive case

def countdown(i):
    print(i)
    if i <= 0: 
        print("gamers are the most oppressed race")
        return
    else: 
        countdown(i-1)

countdown(4)

# STACK (Data Structure)

# call stack - When you insert an item, it gets added to the top. 
#              When you read an item, you only read the topmost item
#              and it’s taken off the list. 
# actions: push (insert) and pop (remove and read).

# Advantage:
# Stack is convenient
# Disadvantage:
# saving all that info can take up a lot of memory

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(4))