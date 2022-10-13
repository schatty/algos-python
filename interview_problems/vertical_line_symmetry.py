"""
Given a list of 2D point coordinates, determine if a symmetrical vertical
line x=a exists and return the value of that vertical line.
"""

def get_symmetry_line(points):
    points.sort(key=lambda x: x[0])
    n = len(points)
    print("points", points)

    if n % 2 == 0:
        symmetry = (points[n//2-1][0] + points[n//2][0]) / 2
    else:
        symmetry = points[n // 2][0]

    for i in range(n // 2):
        if points[i][0] + (points[-i-1][0] - points[i][0]) / 2 != symmetry or \
                points[i][1] != points[-i-1][1]:
            return -1

    return symmetry


points = [(1, 3), (2, 5), (3, 5), (4,3)]
print(get_symmetry_line(points))  # should be 2.5

points = [(1, 3), (2, 5), (3, 5), (4, 2)]
print(get_symmetry_line(points))  # should be -1
