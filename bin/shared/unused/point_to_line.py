# Given a line with coordinates 'start' and 'end' and the
# coordinates of a point 'point' the proc returns the shortest 
# distance from point to the line and the coordinates of the 
# nearest point on the line.
#
# 1  Convert the line segment to a vector ('line_vector').
# 2  Create a vector connecting start to point ('point_vector').
# 3  Find the length of the line vector ('line_len').
# 4  Convert line_vector to a unit vector ('line_unitvec').
# 5  Scale point_vector by line_len ('point_vector_scaled').
# 6  Get the dot product of line_unitvec and point_vector_scaled ('t').
# 7  Ensure t is in the range 0 to 1.
# 8  Use t to get the nearest location on the line to the end
#    of vector point_vector_scaled ('nearest').
# 9  Calculate the distance from nearest to point_vector_scaled.
# 10 Translate nearest back to the start/end line. 
# Malcolm Kesson 16 Dec 2012

from vector_class import vector


def point2line(point_on_contour, start, end, tangent_vector):
    """
    
    :param point_on_contour: vtx of contour 
    :param start: pt_at_crv_ref
    :param end: pt_at_opp_crv_ref
    :param tangent_vector: 
    :return: 
    """
    line_vector = vector(end) - vector(start)
    point_vector = vector(point_on_contour) - vector(start)

    t = line_vector.unit().dot(point_vector.scale(1.0/line_vector.length()))

    '''
    if t < 0.0:
        t = 0.0
    elif t > 1.0:
        t = 1.0
    '''

    nearest = line_vector.scale(t)
    dist = nearest.distance(point_vector)
    nearest_point_on_line = nearest+start
    direction = tangent_vector.dot(line_vector.cross(point_vector))

    '''
    0.0 <= t <= 1.0 : in between start and end, else out of line
     
    '''

    return [dist, nearest_point_on_line, point_on_contour, t, direction]

if __name__ == '__main__':
    point = [-1, 0, 0]
    start = [0, 0, 0]
    end = [5, 0, 0]
    tangent = [0, 0, 1]
    a = point2line(point, start, end, vector(tangent))
    print(a)
