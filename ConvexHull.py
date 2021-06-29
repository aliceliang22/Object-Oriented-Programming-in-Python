
# Name: Alice Liang
# EID: axl84
# Unique Section Number: 84825
# Assignment: #6
# Date: 7/2/20
import math


class Point (object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y < other.y)
            return (self.x < other.x)

    def __le__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
            return (self.x <= other.x)

    def __gt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y > other.y)
            return (self.x > other.x)

    def __ge__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
            return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value


def det(p, q, r):

    d = (p.x * q.y) - (p.y * q.x) + (p.y * r.x) - \
        (p.x * r.y) + (q.x * r.y) - (r.x * q.y)

    return d

    # if d < 0:
    #     # its a right hand turn/ clockwise turn
    # if d > 0:
    #     # its a left hand turn / counterclockwise turn
    # if d == 0:
    #     # three points are colinear


def detConvexPoly(points):

    n = len(points)

    sum = 0
    for i in range(n):

        p1 = points[i]
        x1 = p1.x
        y1 = p1.y

        if i == (n-1):
            p2 = points[0]

        else:
            p2 = points[i+1]

        x2 = p2.x
        y2 = p2.y

        sum += x1 * y2 - x2 * y1

    return sum

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order returns the convex hull


def convex_hull(sorted_points):

    n = len(sorted_points)
    upper_hull = []

    p1 = sorted_points[0]
    p2 = sorted_points[1]

    upper_hull.append(p1)
    upper_hull.append(p2)

    for i in range(2, n):
        upperL = sorted_points[i]
        upper_hull.append(upperL)

        numUpper = len(upper_hull)
        while numUpper >= 3:

            p = upper_hull[numUpper - 3]
            q = upper_hull[numUpper - 2]
            r = upper_hull[numUpper - 1]
            deter = det(p, q, r)
            if deter >= 0:
                upper_hull.pop(numUpper - 2)
                numUpper -= 1
            else:
                break

    lower_hull = []

    p1 = sorted_points[n-1]
    p2 = sorted_points[n-2]

    lower_hull.append(p1)
    lower_hull.append(p2)

    for i in range(n-3, -1, -1):
        lowerL = sorted_points[i]
        lower_hull.append(lowerL)

        numLower = len(lower_hull)
        while numLower >= 3:

            p = lower_hull[numLower - 3]
            q = lower_hull[numLower - 2]
            r = lower_hull[numLower - 1]
            deter = det(p, q, r)
            if deter >= 0:
                lower_hull.pop(numLower - 2)
                numLower -= 1
            else:
                break

    lower_hull.pop(numLower - 1)
    lower_hull.pop(0)

    convex_hull = upper_hull + lower_hull

    return convex_hull

# Input: convex_poly is a list of Point objects that define the vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon


def area_poly(convex_poly):

    area = (1/2) * abs(detConvexPoly(convex_poly))
    return area

# Input: no input
# Output: a string denoting all test cases have passed
# def test_cases():
#   # write your own test cases

#   return "all test cases passed"


def main():
    # create an empty list of Point objects
    sorted_points = []

    # open file hull.in for reading
    infile = open("hull.in.txt", "r")

    # read file line by line, create Point objects and store in a list
    n = int(infile.readline().strip())
    coords = []
    for i in range(n):
        string = infile.readline().strip()
        num = string.split()
        x = int(num[0])
        y = int(num[1])
        point = Point(x, y)
        sorted_points.append(point)
        coords.append((x, y))

    infile.close()

    # sort the list according to x-coordinates
    sorted_points.sort(key=lambda p: (p.x, p.y))

    # get the convex hull
    c = convex_hull(sorted_points)
    # return c
    # run your test cases

    # open file hull.out for writing

    # print the convex hull

    # get the area of the convex hull
    a = area_poly(c)
    return a
    # print the area of the convex hull


# if __name__ == "__main__":
main()
