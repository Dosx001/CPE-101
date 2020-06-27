# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VIII
# Term:         Winter 2020
import pset8


p1 = pset8.Point(0, 0)
p2 = pset8.Point(1, 1)
p3 = pset8.Point(1, 2)
p4 = pset8.Point(6, 9)
assert p1.x == 0
assert p2.x == 1
assert p3.x == 1
assert p4.x == 6
assert p1.y == 0
assert p2.y == 1
assert p3.y == 2
assert p4.y == 9
assert p1.__init__(0, 0) == None
assert p2.__init__(1, 1) == None
assert p3.__init__(1, 2) == None
assert p4.__init__(6, 9) == None

assert p1 != p2
assert p2 != p3
assert p3 != p4

assert str(p1) == '(0, 0)'
assert str(p2) == '(1, 1)'
assert str(p3) == '(1, 2)'

assert p1.distance(p2) == 2 ** .5
assert p2.distance(p3) == 1
assert p3.distance(p1) == 5 ** .5

assert p1.get_slope_intercept(p2) == (1, 0)
assert p1.get_slope_intercept(p3) == (2, 0)
assert p1.get_slope_intercept(p4) == (1.5, 0)

c1 = pset8.Circle(p1, 1)
c2 = pset8.Circle(p2, 1)
c3 = pset8.Circle(p3, 1)

assert str(c1.center) == '(0, 0)'
assert str(c2.center) == '(1, 1)'
assert str(c3.center) == '(1, 2)'

assert c1.radius == 1
assert c2.radius == 1
assert c3.radius == 1

assert c1.__init__(p1, 1) == None
assert c2.__init__(p2, 1) == None
assert c3.__init__(p3, 1) == None

assert c1 != c2
assert c2 != c3
assert c3 != c1

assert str(c1) == '1r @ (0, 0)'
assert str(c2) == '1r @ (1, 1)'
assert str(c3) == '1r @ (1, 2)'

assert c1.overlaps(c2) == True
assert c2.overlaps(c3) ==  True
assert c3.overlaps(c1) == False

l1 = pset8.Line(pset8.Point(4, 4), pset8.Point(6, 9))
l2 = pset8.Line(pset8.Point(2, 4), pset8.Point(4, 5))
l3 = pset8.Line(pset8.Point(1, 2), pset8.Point(5, 10))

assert c1.bisects(l1) == False
assert c2.bisects(l2) == False
assert c3.bisects(l3) == True

assert l1 != l2
assert l2 != l3
assert l3 != l1

assert str(l1) == 'y = 2.5x - 6.0'
assert str(l2) == 'y = 0.5x + 3.0'
assert str(l3) == 'y = 2.0x'

assert str(l1.to_parallel(p1)) == 'y = 2.5x'
assert str(l1.to_parallel(p1)) == 'y = 2.5x'
assert str(l1.to_parallel(p1)) == 'y = 2.5x'

str(l2.to_perpendicular()) == '-2.0x + 3.0'
str(l2.to_perpendicular()) == '-2.0x + 3.0'
str(l3.to_perpendicular()) == '-0.5x'

x = [p1, p2, p3, p4]
y = [c1, c2, c3]
z = [l1, l2, l3]

assert pset8.get_point_distances(x) == pset8.get_point_distances(x)
assert pset8.get_point_distances(x) == pset8.get_point_distances(x)
assert pset8.get_point_distances(x) == pset8.get_point_distances(x)

assert pset8.get_circle_distances(y) ==  pset8.get_circle_distances(y)
assert pset8.get_circle_distances(y) ==  pset8.get_circle_distances(y)
assert pset8.get_circle_distances(y) ==  pset8.get_circle_distances(y)

assert str(pset8.are_in_first_quadrant(x)) == '[(1, 1), (1, 2), (6, 9)]'
assert str(pset8.are_in_first_quadrant(x)) == '[(1, 1), (1, 2), (6, 9)]'
assert str(pset8.are_in_first_quadrant(x)) == '[(1, 1), (1, 2), (6, 9)]'

assert pset8.overlaps_unit_circle(y) == pset8.overlaps_unit_circle(y)
assert pset8.overlaps_unit_circle(y) == pset8.overlaps_unit_circle(y)
assert pset8.overlaps_unit_circle(y) == pset8.overlaps_unit_circle(y)
