# Name: Alice Liang
# EID: axl84
# Unique Section Number: 84825
# Assignment: #4
# Date: 6/20/20

import math


class Point (object):

    # constructor with default values
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # create a string representation of a Point, returns a string of the form (x, y, z)
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

    # get distance to another Point object, other is a Point object, returns the distance as a floating point number
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    # test for equality between two points, other is a Point object, returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-06
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol))


class Sphere (object):

    # constructor with default values
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.center = Point(x, y, z)

    # returns string representation of a Sphere of the form: Center: (x, y, z), Radius: value
    def __str__(self):
        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '), ' + 'Radius: ' + str(self.radius)

    # compute surface area of Sphere, returns a floating point number
    def area(self):
        return 4 * math.pi * self.radius * self.radius

    # compute volume of a Sphere, returns a floating point number
    def volume(self):
        return 4/3 * math.pi * self.radius * self.radius * self.radius

    # determines if a Point is strictly inside the Sphere, p is Point object, returns a Boolean
    def is_inside_point(self, p):
        return self.center.distance(p) < self.radius
        # return (self.x - p.x) ** 2 + (self.y - p.y) ** 2 + (self.z - p.z) ** 2 < self.radius * self.radius

    # determine if another Sphere is strictly inside this Sphere, other is a Sphere object, returns a Boolean
    def is_inside_sphere(self, other):
        # cant be larger than distance btwn large sphere and smaller sphere center plus radius of smaller sphere <= RL - Rs
        return self.center.distance(other.center) < self.radius - other.radius

    # determine if a Cube is strictly inside this Sphere, determine if the eight corners of the Cube are inside the Sphere, a_cube is a Cube object, returns a Boolean
    def is_inside_cube(self, a_cube):
        p1 = Point(a_cube.x - a_cube.side * 0.5, a_cube.y -
                   a_cube.side * 0.5, a_cube.z - a_cube.side * 0.5)
        p2 = Point(a_cube.x + a_cube.side * 0.5, a_cube.y -
                   a_cube.side * 0.5, a_cube.z - a_cube.side * 0.5)
        p3 = Point(a_cube.x + a_cube.side * 0.5, a_cube.y +
                   a_cube.side * 0.5, a_cube.z - a_cube.side * 0.5)
        p4 = Point(a_cube.x - a_cube.side * 0.5, a_cube.y +
                   a_cube.side * 0.5, a_cube.z - a_cube.side * 0.5)
        p5 = Point(a_cube.x - a_cube.side * 0.5, a_cube.y -
                   a_cube.side * 0.5, a_cube.z + a_cube.side * 0.5)
        p6 = Point(a_cube.x + a_cube.side * 0.5, a_cube.y -
                   a_cube.side * 0.5, a_cube.z + a_cube.side * 0.5)
        p7 = Point(a_cube.x + a_cube.side * 0.5, a_cube.y +
                   a_cube.side * 0.5, a_cube.z + a_cube.side * 0.5)
        p8 = Point(a_cube.x - a_cube.side * 0.5, a_cube.y +
                   a_cube.side * 0.5, a_cube.z + a_cube.side * 0.5)

        inside1 = self.center.distance(p1) < self.radius
        inside2 = self.center.distance(p2) < self.radius
        inside3 = self.center.distance(p3) < self.radius
        inside4 = self.center.distance(p4) < self.radius
        inside5 = self.center.distance(p5) < self.radius
        inside6 = self.center.distance(p6) < self.radius
        inside7 = self.center.distance(p7) < self.radius
        inside8 = self.center.distance(p8) < self.radius

        return inside1 and inside2 and inside3 and inside4 and inside5 and inside6 and inside7 and inside8

    # determine if a Cylinder is strictly inside this Sphere, a_cyl is a Cylinder object, returns a Boolean
    def is_inside_cyl(self, a_cyl):
        if a_cyl.height > self.radius * 2 or a_cyl.radius > self.radius:
            return False
        bottomRadius = math.sqrt((self.radius) ** 2 - (self.z - a_cyl.z) ** 2)
        topRadius = math.sqrt((self.radius) ** 2 -
                              (a_cyl.z + a_cyl.z - self.z) ** 2)
        dist = math.sqrt((self.x - a_cyl.x) ** 2 + (self.y - a_cyl.y) ** 2)
        return bottomRadius > dist + a_cyl.radius and topRadius > dist + a_cyl.radius

    # determine if another Sphere intersects this Sphere, there is a non-zero volume of intersection other is a Sphere object, returns a Boolean
    def does_intersect_sphere(self, other):
        return self.center.distance(other.center) < self.radius + other.radius

    # determine if a Cube intersects this Sphere, there is a non-zero volume of intersection, there is at least one corner of the Cube in the Sphere
    # a_cube is a Cube object, returns a Boolean
    def does_intersect_cube(self, a_cube):
        p1 = Point(a_cube.x - a_cube.side * 0.5, a_cube.y -
                   a_cube.side * 0.5, a_cube.z - a_cube.side * 0.5)
        p2 = Point(a_cube.x + a_cube.side * 0.5, a_cube.y -
                   a_cube.side * 0.5, a_cube.z - a_cube.side * 0.5)
        p3 = Point(a_cube.x + a_cube.side * 0.5, a_cube.y +
                   a_cube.side * 0.5, a_cube.z - a_cube.side * 0.5)
        p4 = Point(a_cube.x - a_cube.side * 0.5, a_cube.y +
                   a_cube.side * 0.5, a_cube.z - a_cube.side * 0.5)
        p5 = Point(a_cube.x - a_cube.side * 0.5, a_cube.y -
                   a_cube.side * 0.5, a_cube.z + a_cube.side * 0.5)
        p6 = Point(a_cube.x + a_cube.side * 0.5, a_cube.y -
                   a_cube.side * 0.5, a_cube.z + a_cube.side * 0.5)
        p7 = Point(a_cube.x + a_cube.side * 0.5, a_cube.y +
                   a_cube.side * 0.5, a_cube.z + a_cube.side * 0.5)
        p8 = Point(a_cube.x - a_cube.side * 0.5, a_cube.y +
                   a_cube.side * 0.5, a_cube.z + a_cube.side * 0.5)

        inside1 = self.center.distance(p1) < self.radius
        inside2 = self.center.distance(p2) < self.radius
        inside3 = self.center.distance(p3) < self.radius
        inside4 = self.center.distance(p4) < self.radius
        inside5 = self.center.distance(p5) < self.radius
        inside6 = self.center.distance(p6) < self.radius
        inside7 = self.center.distance(p7) < self.radius
        inside8 = self.center.distance(p8) < self.radius

        return inside1 or inside2 or inside3 or inside4 or inside5 or inside6 or inside7 or inside8

    # return the largest Cube object that is circumscribed by this Sphere, all eight corners of the Cube are on the Sphere, returns a Cube object
    def circumscribe_cube(self):
        side = 2/3 * math.sqrt(3) * self.radius
        cube = Cube(self.center.x, self.center.y, self.center.z, side)
        return cube


class Cube (object):
    # Cube is defined by its center (which is a Point object), and side. The faces of the Cube are parallel to x-y, y-z, and x-z planes.
    def __init__(self, x=0, y=0, z=0, side=1):
        self.x = x
        self.y = y
        self.z = z
        self.side = side

    # string representation of a Cube of the form: Center: (x, y, z), Side: value
    def __str__(self):
        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '), ' + 'Side: ' + str(round(self.side, 5))

    # compute the total surface area of Cube (all 6 sides), returns a floating point number
    def area(self):
        return 6 * self.side * self.side

    # compute volume of a Cube, returns a floating point number
    def volume(self):
        return self.side * self.side * self.side

    # determines if a Point is strictly inside this Cube, p is a point object, returns a Boolean
    def is_inside_point(self, p):
        ret1 = self.x - self.side * 0.5 < p.x and self.x + self.side * 0.5 < p.x
        ret2 = self.y - self.side * 0.5 < p.y and self.y + self.side * 0.5 < p.y
        ret3 = self.x - self.side * 0.5 < p.z and self.z + self.side * 0.5 < p.z
        return ret1 and ret2 and ret3

    # determine if a Sphere is strictly inside this Cube or, a_sphere is a Sphere object, returns a Boolean
    def is_inside_sphere(self, a_sphere):
        ret1 = self.x - self.side * 0.5 < a_sphere.x - a_sphere.radius and self.x + \
            self.side * 0.5 < a_sphere.x + a_sphere.radius
        ret2 = self.y - self.side * 0.5 < a_sphere.y - a_sphere.radius and self.y + \
            self.side * 0.5 < a_sphere.y + a_sphere.radius
        ret3 = self.x - self.side * 0.5 < a_sphere.z - a_sphere.radius and self.z + \
            self.side * 0.5 < a_sphere.z + a_sphere.radius
        return ret1 and ret2 and ret3

    # determine if another Cube is strictly inside this Cube, other is a Cube object, returns a Boolean
    def is_inside_cube(self, other):
        ret1 = self.x - self.side * 0.5 < other.x - other.side * \
            0.5 and self.x + self.side * 0.5 < other.x + other.side * 0.5
        ret2 = self.y - self.side * 0.5 < other.y - other.side * \
            0.5 and self.y + self.side * 0.5 < other.y + other.side * 0.5
        ret3 = self.x - self.side * 0.5 < other.z - other.side * \
            0.5 and self.z + self.side * 0.5 < other.z + other.side * 0.5
        return ret1 and ret2 and ret3

    # determine if a Cylinder is strictly inside this Cube, a_cyl is a Cylinder object, returns a Boolean
    def is_inside_cylinder(self, a_cyl):
        ret1 = self.x - self.side * 0.5 < a_cyl.x - \
            a_cyl.radius and self.x + self.side * 0.5 < a_cyl.x + a_cyl.radius
        ret2 = self.y - self.side * 0.5 < a_cyl.y - \
            a_cyl.radius and self.y + self.side * 0.5 < a_cyl.y + a_cyl.radius
        ret3 = self.x - self.side * 0.5 < a_cyl.z - \
            a_cyl.radius and self.z + self.side * 0.5 < a_cyl.z + a_cyl.radius
        return ret1 and ret2 and ret3

    # determine if another Cube intersects this Cube, there is a non-zero volume of intersection, there is at least one vertex of the other Cube in this Cube
    # other is a Cube object, returns a Boolean
    def does_intersect_cube(self, other):
        if self.x - self.side * 0.5 > other.x + other.side * 0.5 or self.x + self.side * 0.5 < other.x - other.side * 0.5:
            return False
        if self.y - self.side * 0.5 > other.y + other.side * 0.5 or self.y + self.side * 0.5 < other.y - other.side * 0.5:
            return False
        if self.z - self.side * 0.5 > other.z + other.side * 0.5 or self.z + self.side * 0.5 < other.z - other.side * 0.5:
            return False

        return True

    # determine the volume of intersection if this Cube intersects with another Cube, other is a Cube object, returns a floating point number
    def intersection_volume(self, other):
        if self.does_intersect_cube(other) == False:
            return 0.0

        if self.x - self.side * 0.5 < other.x - other.side * 0.5:
            x1 = other.x - other.side * 0.5
        else:
            x1 = self.x - self.side * 0.5
        if self.x + self.side * 0.5 > other.x + other.side * 0.5:
            x2 = other.x + other.side * 0.5
        else:
            x2 = self.x + self.side * 0.5

        if self.y - self.side * 0.5 < other.y - other.side * 0.5:
            y1 = other.y - other.side * 0.5
        else:
            y1 = self.y - self.side * 0.5
        if self.y + self.side * 0.5 > other.y + other.side * 0.5:
            y2 = other.y + other.side * 0.5
        else:
            y2 = self.y + self.side * 0.5

        if self.z - self.side * 0.5 < other.z - other.side * 0.5:
            z1 = other.z - other.side * 0.5
        else:
            z1 = self.z - self.side * 0.5
        if self.z + self.side * 0.5 > other.z + other.side * 0.5:
            z2 = other.z + other.side * 0.5
        else:
            z2 = self.z + self.side * 0.5

        volume = (x2-x1) * (y2-y1) * (z2-z1)
        return volume

    # return the largest Sphere object that is inscribedby this Cube, Sphere object is inside the Cube and the faces of the Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere(self):
        s = Sphere(self.x, self.y, self.z, self.side * 0.5)
        return s


class Cylinder (object):

    # Cylinder is defined by its center (which is a Point object), radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = height

    # returns a string representation of a Cylinder of the form: Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '), ' + 'Radius: ' + str(self.radius) + ', ' + 'Height: ' + str(self.height)

    # compute surface area of Cylinder, returns a floating point number
    def area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius * self.radius

    # compute volume of a Cylinder, returns a floating point number
    def volume(self):
        return math.pi * self.radius * self.radius * self.height

    # determine if a Point is strictly inside this Cylinder, p is a Point object, returns a Boolean
    def is_inside_point(self, p):
        dist = math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
        return dist < self.radius and p.z > self.z and p.z < self.z + self.height

    # determine if a Sphere is strictly inside this Cylinder, a_sphere is a Sphere object, returns a Boolean
    def is_inside_sphere(self, a_sphere):
        dist = math.sqrt((self.x - a_sphere.x) ** 2 +
                         (self.y - a_sphere.y) ** 2)
        return dist < self.radius - a_sphere.radius and a_sphere.z - a_sphere.raduis > self.z and a_sphere.z + a_sphere.raduis < self.z + self.height

    # determine if a Cube is strictly inside this Cylinder, determine if all eight corners of the Cube are in the Cylinder
    # a_cube is a Cube object, returns a Boolean
    def is_inside_cube(self, a_cube):
        dist1 = math.sqrt((self.x - (a_cube.x - a_cube.side * 0.5))
                          ** 2 + (self.y - (a_cube.y - a_cube.side * 0.5)) ** 2)
        dist2 = math.sqrt((self.x - (a_cube.x + a_cube.side * 0.5))
                          ** 2 + (self.y - (a_cube.y - a_cube.side * 0.5)) ** 2)
        dist3 = math.sqrt((self.x - (a_cube.x + a_cube.side * 0.5))
                          ** 2 + (self.y - (a_cube.y + a_cube.side * 0.5)) ** 2)
        dist4 = math.sqrt((self.x - (a_cube.x - a_cube.side * 0.5))
                          ** 2 + (self.y - (a_cube.y + a_cube.side * 0.5)) ** 2)

        return dist1 < self.radius and dist2 < self.radius and dist3 < self.radius and dist4 < self.radius and a_cube.z - a_cube.side * 0.5 > self.z and a_cube.z + a_cube.side * 0.5 < self.z + self.height

    # determine if another Cylinder is strictly inside this Cylinder, other is Cylinder object, returns a Boolean
    def is_inside_cylinder(self, other):
        dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return dist < self.radius - other.radius and other.z > self.z and other.z + other.height < self.z + self.height

    # determine if another Cylinder intersects this Cylinder, there is a non-zero volume of intersection, other is a Cylinder object, returns a Boolean
    def does_intersect_cylinder(self, other):
        if other.z > self.z + self.height or other.z + other.height < self.z:
            return False

        dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return dist < self.radius + other.radius


def main():

    # open file "geometry.txt" for reading
    infile = open("geometry.txt", "r")

    # read the coordinates of the first Point p
    line = infile.readline().strip()
    nums = line.split()
    x = float(nums[0])
    y = float(nums[1])
    z = float(nums[2])

    # create a Point object and print its coordinates
    p = Point(x, y, z)
    print("Point p:", p)

    # read the coordinates of the second Point q
    line = infile.readline().strip()
    nums = line.split()
    x = float(nums[0])
    y = float(nums[1])
    z = float(nums[2])

    # create a Point object and print its coordinates
    q = Point(x, y, z)
    print("Point q:", q)

    # read the coordinates of the center and radius of sphereA
    line = infile.readline().strip()
    nums = line.split()
    x = float(nums[0])
    y = float(nums[1])
    z = float(nums[2])
    rad = float(nums[3])

    # create a Sphere object and print it
    sphereA = Sphere(x, y, z, rad)
    print("sphereA:", sphereA)

    # read the coordinates of the center and radius of sphereB
    line = infile.readline().strip()
    nums = line.split()
    x = float(nums[0])
    y = float(nums[1])
    z = float(nums[2])
    rad = float(nums[3])

    # create a Sphere object and print it
    sphereB = Sphere(x, y, z, rad)
    print("sphereB:", sphereB)

    # read the coordinates of the center and side of cubeA
    line = infile.readline().strip()
    nums = line.split()
    x = float(nums[0])
    y = float(nums[1])
    z = float(nums[2])
    s = float(nums[3])

    # create a Cube object and print it
    cubeA = Cube(x, y, z, s)
    print("cubeA:", cubeA)

    # read the coordinates of the center and side of cubeB
    line = infile.readline().strip()
    nums = line.split()
    x = float(nums[0])
    y = float(nums[1])
    z = float(nums[2])
    s = float(nums[3])

    # create a Cube object and print it
    cubeB = Cube(x, y, z, s)
    print("cubeB:", cubeB)

    # read the coordinates of the center, radius and height of cylA
    line = infile.readline().strip()
    nums = line.split()
    x = float(nums[0])
    y = float(nums[1])
    z = float(nums[2])
    r = float(nums[3])
    h = float(nums[4])

    # create a Cylinder object and print it
    cylA = Cylinder(x, y, z, r, h)
    print("cylA:", cylA)

    # read the coordinates of the center, radius and height of cylB
    line = infile.readline().strip()
    nums = line.split()
    x = float(nums[0])
    y = float(nums[1])
    z = float(nums[2])
    r = float(nums[3])
    h = float(nums[4])

    # create a Cylinder object and print it
    cylB = Cylinder(x, y, z, r, h)
    print("cylB:", cylB)

    # close file geometry.txt
    infile.close()

    # print distance between p and q
    dist_pq = p.distance(q)
    print("Distance between p and q:", round(dist_pq, 5))

    # print area of sphereA
    sphereAreaA = sphereA.area()
    print("Area of sphereA:", round(sphereAreaA, 5))

    # print volume of sphereA
    sphereVolA = sphereA.volume()
    print("Volume of sphereA:", round(sphereVolA, 5))

    # print if Point p is inside sphereA
    isInside = sphereA.is_inside_point(p)
    if isInside:
        print("Point p is inside sphereA")
    else:
        print("Point p is not inside sphereA")

    # print if sphereB is inside sphereA
    isInside = sphereA.is_inside_sphere(sphereB)
    if isInside:
        print("sphereB is inside sphereA")
    else:
        print("sphereB is not inside sphereA")

    # print if cubeA is inside sphereA
    isInside = sphereA.is_inside_cube(cubeA)
    if isInside:
        print("cubeA is inside sphereA")
    else:
        print("cubeA is not inside sphereA")

    # print if cylA is inside sphereA
    isInside = sphereA.is_inside_cyl(cylA)
    if isInside:
        print("cylA is inside sphereA")
    else:
        print("cylA is not inside sphereA")

    # print if sphereA intersects with sphereB
    intersects = sphereA.does_intersect_sphere(sphereB)
    if intersects:
        print("sphereA does intersect sphereB")
    else:
        print("sphereA does not intersect sphereB")

    # print if cubeB intersects with sphereB
    intersects = sphereB.does_intersect_cube(cubeB)
    if intersects:
        print("cubeB does intersect sphereB")
    else:
        print("cubeB does not intersect sphereB")

    # print the largest Cube that is circumscribed by sphereA
    largestCube = sphereA.circumscribe_cube()
    print("Largest Cube circumscribed by sphereA:", largestCube)

    # print area of cubeA
    cubeAreaA = cubeA.area()
    print("Area of cubeA:", round(cubeAreaA, 5))

    # print volume of cubeA
    volCubeA = cubeA.volume()
    print("Volume of cubeA:", round(volCubeA, 5))

    # print if Point p is inside cubeA
    isInside = cubeA.is_inside_point(p)
    if isInside:
        print("Point p is inside cubeA")
    else:
        print("Point p is not inside cubeA")

    # print if sphereA is inside cubeA
    isInside = cubeA.is_inside_sphere(sphereA)
    if isInside:
        print("sphereA is inside cubeA")
    else:
        print("sphereA is not inside cubeA")

    # print if cubeB is inside cubeA
    isInside = cubeA.is_inside_cube(cubeB)
    if isInside:
        print("cubeB is inside cubeA")
    else:
        print("cubeB is not inside cubeA")

    # print if cylA is inside cubeA
    isInside = cubeA.is_inside_cylinder(cylA)
    if isInside:
        print("cylA is inside cubeA")
    else:
        print("cylA is not inside cubeA")

    # print if cubeA intersects with cubeB
    intersects = cubeA.does_intersect_cube(cubeB)
    if intersects:
        print("cubeA does intersect cubeB")
    else:
        print("cubeA does not intersect cubeB")

    # print the intersection volume of cubeA and cubeB
    intersects = cubeA.intersection_volume(cubeB)
    print("Intersection volume of cubeA and cubeB:", round(intersects, 5))

    # print the largest Sphere object inscribed by cubeA
    largestSphere = cubeA.inscribe_sphere()
    print("Largest Sphere inscribed by cubeA:", largestSphere)

    # print area of cylA
    cylAreaA = cylA.area()
    print("Area of cylA:", round(cylAreaA, 5))

    # print volume of cylA
    volCylA = cylA.volume()
    print("Volume of cylA:", round(volCylA, 5))

    # print if Point p is inside cylA
    isInside = cylA.is_inside_point(p)
    if isInside:
        print("Point p is inside cylA")
    else:
        print("Point p is not inside cylA")

    # print if sphereA is inside cylA
    isInside = cylA.is_inside_sphere(sphereA)
    if isInside:
        print("sphereA is inside cylA")
    else:
        print("sphereA is not inside cylA")

    # print if cubeA is inside cylA
    isInside = cylA.is_inside_cube(cubeA)
    if isInside:
        print("cubeA is inside cylA")
    else:
        print("cubeA is not inside cylA")

    # print if cylB is inside cylA
    isInside = cylA.is_inside_cylinder(cylB)
    if isInside:
        print("cylB is inside cylA")
    else:
        print("cylB is not inside cylA")

    # print if cylB intersects with cylA
    intersects = cylA.does_intersect_cylinder(cylB)
    if intersects:
        print("cylA does intersect cylB")
    else:
        print("cylA does not intersect cylB")


if __name__ == "__main__":
    main()
