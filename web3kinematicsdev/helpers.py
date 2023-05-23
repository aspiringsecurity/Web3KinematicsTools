"""
    Physics, a 2D Physics Playground for Kids
    Copyright (C) 2008  Alex Levenson and Brian Jordan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
# ==================================================================
#                           Physics.activity
#                     Helper classes and functions
#                           By Alex Levenson
# ==================================================================
import math


def distance(pt1, pt2):
    """Distance calculator, pt1 and pt2 are ordred pairs.
    """
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)


def getAngle(pt1, pt2):
    """Returns angle between line segment pt1 -> pt2 and x axis, from -pi to pi.
    """
    xcomp = pt2[0] - pt1[0]
    ycomp = pt1[1] - pt2[1]
    return math.atan2(ycomp, xcomp)


def constructTriangleFromLine(p1, p2):
    """
    Returns list of ordered pairs describing equilteral triangle around
    segment pt1 --> pt2.
    """
    halfHeightVector = (0.57735 * (p2[1] - p1[1]), 0.57735 * (p2[0] - p1[0]))
    p3 = (p1[0] + halfHeightVector[0], p1[1] - halfHeightVector[1])
    p4 = (p1[0] - halfHeightVector[0], p1[1] + halfHeightVector[1])
    return [p2, p3, p4]


def polyArea(vertices):
    """Returns the area of a polygon.
    """
    n = len(vertices)
    A = 0
    p = n - 1
    q = 0
    while q < n:
        A += vertices[p][0] * vertices[q][1] - vertices[q][0] * vertices[p][1]
        p = q
        q += 1
    return A / 2.0


def insideTriangle(pt, triangle):
    """Returns true if pt is in triangle.

    Some polygon magic, thanks to John W. Ratcliff on www.flipcode.com
    """
    ax = triangle[2][0] - triangle[1][0]
    ay = triangle[2][1] - triangle[1][1]
    bx = triangle[0][0] - triangle[2][0]
    by = triangle[0][1] - triangle[2][1]
    cx = triangle[1][0] - triangle[0][0]
    cy = triangle[1][1] - triangle[0][1]
    apx = pt[0] - triangle[0][0]
    apy = pt[1] - triangle[0][1]
    bpx = pt[0] - triangle[1][0]
    bpy = pt[1] - triangle[1][1]
    cpx = pt[0] - triangle[2][0]
    cpy = pt[1] - triangle[2][1]

    aCROSSbp = ax * bpy - ay * bpx
    cCROSSap = cx * apy - cy * apx
    bCROSScp = bx * cpy - by * cpx
    return aCROSSbp >= 0.0 and bCROSScp >= 0.0 and cCROSSap >= 0.0


def polySnip(vertices, u, v, w, n):
    EPSILON = 0.0000000001

    Ax = vertices[u][0]
    Ay = vertices[u][1]

    Bx = vertices[v][0]
    By = vertices[v][1]

    Cx = vertices[w][0]
    Cy = vertices[w][1]

    if EPSILON > (((Bx - Ax) * (Cy - Ay)) - ((By - Ay) * (Cx - Ax))):
        return False

    for p in range(0, n):
        if p == u or p == v or p == w:
            continue
        Px = vertices[p][0]
        Py = vertices[p][1]
        if insideTriangle((Px, Py), ((Ax, Ay), (Bx, By), (Cx, Cy))):
            return False

    return True


def decomposePoly(vertices):
    """Decomposes a polygon into its triangles.
    """
    vertices = list(vertices)
    n = len(vertices)
    result = []
    if(n < 3):
        return []  # not a poly!

    # Force counter-clockwise polygon
    if 0 >= polyArea(vertices):
        vertices.reverse()

    # Remove nv-2 vertices, creating 1 triangle every time
    nv = n
    count = 2 * nv  # error detection
    v = nv - 1
    while nv > 2:
        count -= 1
        if 0 >= count:
            return []  # Error -- probably bad polygon

        # Three consecutive vertices
        u = v
        if nv <= u:
            u = 0      # previous
        v = u + 1
        if nv <= v:
            v = 0    # new v
        w = v + 1
        if nv <= w:
            w = 0    # next

        if(polySnip(vertices, u, v, w, nv)):

            # Record this triangle
            result.append((vertices[u], vertices[v], vertices[w]))

            # Remove v from remaining polygon
            vertices.pop(v)
            nv -= 1
            # Reset error detection
            count = 2 * nv
    return result


def tuple_to_int(tuple_input):
    """Cast tuple values to ints to avoid gtk+ and pygame's dislike of floats.
    """
    return [int(i) for i in tuple_input]


def find_body(world, pos):
    body = world.get_bodies_at_pos(tuple_to_int(pos))
    if isinstance(body, list) and len(body) > 0:
        return body[0]
    else:
        return None
