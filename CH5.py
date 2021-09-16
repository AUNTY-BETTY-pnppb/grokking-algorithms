# HASH TABLES/DICTIONARIES (Data Structure)

# Hash functions - a function where you put in a string and you get
# back a number.

# average case - O(1)
# worst case - O(n)

# “maps strings to numbers, name to index”

# Requires: Consistency - Apple = 4, 4 = Apple
#           map different words to different numbers
#           each key must be unique, and each value must be unique
#           if multiple keys map to the same slot, start a linked list at that slot.
#           - HOWEVER If those linked lists get long, it slows down your hash table a lot.
#           - MUST use a good hash function

# Collisions - when two different keys map to the same index
# to avoid: • A low load factor
#           • A good hash function

# CACHING

# Caching - fast memory containing recently looked up sites or
#           recurring sites.
# Check if site is Cache Hash, if yes take it from there to reduce
# memory load.