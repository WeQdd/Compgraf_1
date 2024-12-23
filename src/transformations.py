def translation_matrix(tx, ty):
    return [[1, 0, tx],
            [0, 1, ty],
            [0, 0, 1]]

def scaling_matrix(sx, sy):
    return [[sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]]

def rotation_matrix(angle):
    import math
    rad = math.radians(angle)
    return [[math.cos(rad), -math.sin(rad), 0],
            [math.sin(rad), math.cos(rad), 0],
            [0, 0, 1]]

def apply_transformation(matrix, point):
    x, y = point
    homogeneous_point = [x, y, 1]
    transformed_point = [sum(matrix[i][j] * homogeneous_point[j] for j in range(3)) for i in range(3)]
    return transformed_point[0], transformed_point[1]

def to_pixel_coordinates(x, y, width, height):
    return x + width / 2, height / 2 - y

def from_pixel_coordinates(px, py, width, height):
    return px - width / 2, height / 2 - py