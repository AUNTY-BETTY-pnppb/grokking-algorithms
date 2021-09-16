# DYNAMIC PROGRAMMING

# dynamic programming - technique to solve a hard problem by breaking it up
# into subproblems and solving those subproblems first

# Dynamic programming is useful when you’re trying to optimize something given a constraint
# by dividing into subproblems we can use use the answers to those subproblems to figure
# out later calculations

# dynamic programming keeps progressively building on your estimate, so you can keep adding
# items later on

# HOWEVER - Dynamic programming only works when each subproblem is discrete — when it
# doesn’t depend on other subproblems

# cell[i][j] = max of 1. the previous max(value at cell[i-1][j])
#                           VS
#                     2. value of current item + value of remaining space
#                                                 ^ cell[i-1][j-item's weight]

# HOW TO IDENTIFY DYNAMIC PROGRAMMING

# Every dynamic-programming solution involves a grid.
# The values in the cells are usually what you’re trying to optimize.
# Each cell is a subproblem, so think about how you can divide your problem into subproblems.
