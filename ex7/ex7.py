from SolveLinear3 import solve_linear_3


def is_point_inside_triangle(point, v1, v2, v3):
    '''Gets the coordinates of a point [point] and of triangle's vertices [v1]
       [v2] [v3] and determines whether the point is inside the triangle
       or not. returns a tuple =(True/False - depends if the point is inside
       the triangle, (a,b,c) - floats that are the solution to the linear set
       of equations that determine if the point is in the triangle) '''

    coeff = [0,0] # coefficients for the first 2 equations
    for i in range(len(v1)):
        coeff[i] = [v1[i], v2[i], v3[i]]
    
    in_abc = [[1, 1, 1]] # coefficients for the 3rd equation
    coeff_list = coeff + in_abc # the combined coefficients list
    rh_list = [point[0], point[1], 1] # right_hand_list
    a, b, c = solve_linear_3(coeff_list, rh_list)

    # checks if one of the values a,b,c is negative. if so, the point isn't in
    # the triangle.
    is_inside = True
    if min(a, b, c) < 0:
        is_inside = False    
    return (is_inside, (a,b,c))


def create_triangles(list_of_points):
    '''Gets a list of points and returns a list of triangles (list of tuples 
       in the size of 3 of points which are tuples in the size of 2). '''

    def make_new_list(point, index, tri, tri_list):
        '''Gets a triangles list and makes a new one by removing specific
           triangle [tri] and adding 3 new triangles that are made from this
           [tri] vertices and a given point [point]. returns the new list '''
        length = len(tri)
        triangles = tri_list # copies the list
        triangles.pop(index) # removes the triangle
        for i in range(length): #makes the new triangles and adds to the list
                               # in the same index of the one that was removed
            triangles = triangles[:index] +\
                        [((point, tri[i], tri[(i + 1) % length]))] +\
                        triangles[index:]
        return triangles
   
    out_list = []
    # first makes 2 big triangles: p[0],p[1],p[2] and p[2],p[3],p[0]
    FIRST_PTS = 4
    for i in range(0, FIRST_PTS, 2):
        out_list.append((list_of_points[i], list_of_points[i + 1],\
                         list_of_points[(i + 2) % FIRST_PTS]))

    # runs through each point to check in which triangle it is
    # and make new triangles instead of it.
    for index in range(FIRST_PTS, len(list_of_points)):
        point = list_of_points[index]
        for i, tri in enumerate(out_list):
                if is_point_inside_triangle(point, tri[0], tri[1], tri[2])[0]:
                    out_list = make_new_list(point, i, tri, out_list)
                    break # no need to check if the point is in another tri

    return out_list
   
            

def do_triangle_lists_match(list_of_points1, list_of_points2):
    '''Checks if the points of the same index from 2 lists are inside
       triangles of the same index in triangles list made out of these set
       of points. Returns True if so and False otherwise. '''
    is_match = False
    length_1 = len(list_of_points1)
    length_2 = len(list_of_points2)
    if length_1 != length_2:
        return is_match # we must have the same number of points in the lists
    # creates 2 triangle lists for the 2 points lists
    tri_list_1, tri_list_2 = create_triangles(list_of_points1),\
                             create_triangles(list_of_points2)
    # checks in what index of triangle every point is in one list
    for i, point1 in enumerate(list_of_points1):
        for j in range(len(tri_list_1)):
            tri_1 = tri_list_1[j]
            # when the triangle was found, checks if the point of the same 
            # index in the second list is in the triangle of the same index in
            # the second triangles list
            if is_point_inside_triangle(point1, tri_1[0],\
                                        tri_1[1], tri_1[2])[0]:
                point2 = list_of_points2[i]
                tri_2 = tri_list_2[j]
                if not is_point_inside_triangle(point2, tri_2[0],\
                                                tri_2[1], tri_2[2])[0]:
                    return is_match # when not in the same index of triangle
                break # !continues! to the next point (breaks the triangles
                      #                                           loop only)
    # if False was not returned, the obvious answer is True.
    is_match = True
    return is_match


def get_point_in_segment(p1, p2, alpha):
    '''Gets 2 points and a value from 0 to 1 [alpha] and divides the line that
       connects these two points to the ratio [alpha] / (1-[alpha]).
       Returns the point that answers this division. '''
    v = [0] * len(p1)
    for i in range(len(p1)):
        v[i] = (1 - alpha) * p1[i] + alpha * p2[i]
    return tuple(v)


def get_intermediate_triangles(source_triangles_list, target_triangles_list, 
                                                                       alpha):
    '''Gets 2 lists of triangles and a value from 0 to 1 [alpha] and makes
       a new list of triangles. every vertex of a triangle in the new list is
       on the line that connects two vertices of triangles of the same index
       in the two lists and is set by the function "get_point_in_segment".
       Returns the new triangles list. '''

    tri_len = len(source_triangles_list[0]) # usually == 3
    new_list = []
    # gets the values of triangles from the two lists
    for i, tri_1 in enumerate(source_triangles_list):
        tri_2 = target_triangles_list[i]
        new_tri = [0] * tri_len
        # makes the new intermediate triangle
        for j in range(tri_len):
            new_tri[j] = get_point_in_segment(tri_1[j], tri_2[j], alpha)
        new_list.append(tuple(new_tri)) # adds the new one to the list

    return new_list

# until here should be submitted by next week - 18.12.2014


def get_array_of_matching_points(size,triangles_list ,
                                 intermediate_triangles_list):

    def get_new_xy(abc, dest_tri):
        v1,v2,v3 = dest_tri[0], dest_tri[1], dest_tri[2]
        a,b,c = abc
        new_point = [0] * len(v1)
        for i in range(len(v1)):
            new_point[i] = a * v1[i] + b * v2[i] + c * v3[i]
        return tuple(new_point)
        
    max_x, max_y = size
    new_list = [[(0,0) for x in range(max_x)] for y in range(max_y)]
    last_tri = None
    last_i = 0
    for y in range(max_y):
        for x in range(max_x):
            point = (x, y)
            if not last_tri == None: 
                in_last_tri = is_point_inside_triangle(point, last_tri[0], \
                                                 last_tri[1], last_tri[2])
                if in_last_tri[0]:                    
                    orig_tri = triangles_list[last_i]
                    new_point = get_new_xy(in_last_tri[1], orig_tri)
                    new_list[y][x] = new_point
                    continue

            for i, tri in enumerate(intermediate_triangles_list):

                v1,v2,v3 = tri[0], tri[1], tri[2]
                is_tri = is_point_inside_triangle(point, v1, v2, v3)

                if is_tri[0]:
                    orig_tri = triangles_list[i]
                    new_point = get_new_xy(is_tri[1], orig_tri)
                    last_tri = tri
                    last_i= i
                    new_list[y][x] = new_point        
                    

    return new_list


def create_intermediate_image(alpha, size, source_image, target_image,
                              source_triangles_list, target_triangles_list):
    max_x,max_y = size
    out_image = [[(0,0,0) for x in range(max_x)] for y in range(max_y)]
    int_tri_list = get_intermediate_triangles(source_triangles_list,\
                                      target_triangles_list, alpha)

    src_matching = get_array_of_matching_points(size, source_triangles_list,\
                                                                int_tri_list)
    tgt_matching = get_array_of_matching_points(size, target_triangles_list,\
                                                                int_tri_list)
    for y in range(max_y):
        for x in range(max_x):
            src_xy = src_matching[y][x]
            src_x, src_y = src_xy[0], src_xy[1]
            tgt_xy = tgt_matching[y][x]
            tgt_x, tgt_y = tgt_xy[0], tgt_xy[1]
            source_RGB = source_image[src_x, src_y]
            target_RGB = target_image[tgt_x, tgt_y]
            new_rgb= [0,0,0]
            for rgb in range(3):
                new_rgb[rgb] = int((1 - alpha) * source_RGB[rgb] +\
                                        alpha  * target_RGB[rgb])
            out_image[y][x] = tuple(new_rgb)
           

    return out_image


def create_sequence_of_images(size, source_image, target_image, 
                source_triangles_list, target_triangles_list, num_frames):
    sequence = []
    for i in range(num_frames):
        alpha = i / (num_frames - 1)
        int_image = create_intermediate_image(alpha, size, source_image, \
                                          target_image, source_triangles_list,
                                                        target_triangles_list)
        sequence.append(int_image)
        
    return sequence

# until here should be submitted by 25.12.2014
