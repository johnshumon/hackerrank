"""Sort a given stack in descending order"""

# problem statement: https://practice.geeksforgeeks.org/problems/sort-a-stack/1


def sorted(s):
    s.sort(reverse=True)
    return s


print("sorted: ", sorted([3, 1, 2]))
print("sorted: ", sorted([11, 2, 32, 3, 41]))
