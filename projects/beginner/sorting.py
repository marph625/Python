"""
We consider an array of integers, tab (type list whose elements are 0 or 1).
We propose to sort this array according to the following algorithm:
at each step of the sorting, the array is made of three consecutive zones,
the first one containing only 0's, the second one not being
sorted and the last one containing only 1's.

As long as the unsorted zone is not reduced to a single elements,
we look at its first element: if this element is worth 1, it is
exchanged with the last element of the unsorted zone, and it is
then considered to belong to the zone containing only 1s.
In all cases, the length of the unsorted zone decreases by 1.

Output:

sorting([0,1,0,1,0,1,0])
[0,0,0,0,1,1,1]
"""


def sort(tab):
    i = 0
    j = len(tab)-1
    while i != j:
        if tab[i] == 0:
            i = i + 1
        else:
            value = tab[j]
            tab[j] = tab[i]
            tab[i] = value
            j = j - 1
    return tab


sorted_list = sort([0, 1, 0, 1, 0, 1, 0, 1, 0])
print(sorted_list)
