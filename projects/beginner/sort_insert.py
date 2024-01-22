"""
Make a sort_insert function that takes as argument a list L
and sorts this list using the insertion sort method.

Outputs:
sort_insert([2, 5, -1, 7, 0, 28])
==> [-1, 0, 2, 5, 7, 28]
sort_insert([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
==> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

def sort_insert(list):
    end = len(list)
    if end == 0:
        return list
    for element in range(1, end):
        e = list[element]
        i = element
        while i > 0 and list[i - 1] > list[element]:
            i = i - 1
        if i != element:
            for k in range(element, i, -1):
                list[k] = list[k - 1]
            list[i] = e
    return list


first = sort_insert([2, 3, 1, 9, 5, 6, 8, 7, 4, 0])
print(first)
