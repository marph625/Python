"""
We wish to program a function giving the shortest distance between
a starting point and a list of points. The points are given in
the form of a tuple of two integers. The list of points to be
processed is therefore an array of tuples. Recall that the distance
between two points of the plane with coordinates (x : y) and (x' : y')
is given by the formula:

d = sqrt((x - x')**2 + (y - y')**2)

We import the square root function (sqrt) from the Python math module.
Then we create a distance function and a shortest_distance function:

Outputs: distance((1, 0), (5, 3))
5.0

shortest_distance([(7, 9), (2, 5), (5, 2)], (0, 0))
(2, 5)
"""

# Import square root function
from math import sqrt
# Defining the formula to determine the distance between two given points


def distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# print(distance([1,2], [3,4]))

# tab is a list of tuples of points and start is a given starting point


def shortest_distance(tab, start):
    point = tab[0]
    min_dist = distance(tab[0], start)
    for i in range(1, len(tab)):
        if distance(tab[i], start) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], start)
        return point


test1 = distance((1, 0), (5, 3))
print(test1)
test2 = shortest_distance([(7, 9), (2, 5), (5, 2)], (0, 0))
print(test2)