import sys
import numpy as np
from .io_obj import *
import triangle


# z値による高さに従って面を伸ばす
def solidify(vertices, z=1.0):
    print(vertices)
    bottom_verts = len(vertices)
    vertices = np.append(vertices, [i + np.array([0, z, 0]) for i in vertices], axis=0)
    faceVertsIDs = []
    if bottom_verts < 3:
        a = [1 + bottom_verts, 1 + bottom_verts + 1 if 1 + bottom_verts + 1 < len(vertices) else bottom_verts,
             1 + 1 if 1 + 1 < bottom_verts else 0, 1]
        faceVertsIDs.append([a[0], a[1], a[2]])
        faceVertsIDs.append([a[2], a[3], a[0]])
    else:
        for i in range(bottom_verts):
            a = [i + bottom_verts, i + bottom_verts + 1 if i + bottom_verts + 1 < len(vertices) else bottom_verts,
                 i + 1 if i + 1 < bottom_verts else 0, i]
            faceVertsIDs.append([a[0], a[1], a[2]])
            faceVertsIDs.append([a[2], a[3], a[0]])
    return vertices, np.array(faceVertsIDs)


# solidifyで貼った面の法線に対して厚みをつける
def solidify2(file_path, vertices, thickness=1.0, z=1.0, with_MTL=False):
    origin_verts = len(vertices)
    verts = np.array(vertices)
    verts, faces_IDs = solidify(verts, z)
    verts = np.array(verts)

    # print("verts: %s" % verts)
    # print("faces IDs: %s" % faces_IDs)
    normals = []
    for i in range(0, len(faces_IDs), 2):
        current_faceIDs = faces_IDs[i]
        v1 = verts[current_faceIDs[0]] - verts[current_faceIDs[2]]
        v2 = verts[current_faceIDs[1]] - verts[current_faceIDs[2]]
        normal = np.cross(v1, v2)
        normal /= np.linalg.norm(normal)
        normals.append(normal)
        # print("normal: %s" % normal)
        # print(i)

    count = origin_verts
    new_verts = []
    for i in range(origin_verts):
        normal = normals[i]
        # print("norm: %s" % normal)
        new = np.array([verts[i] - (normal * thickness), verts[i + 1 if i + 1 < origin_verts else 0] - (normal * thickness)])
        new_verts.append(new)
        new, ids = solidify(new, z=z)
        count += len(new)

    points = np.empty((0, 3), float)
    for i in range(origin_verts):
        line1 = new_verts[i]
        line2 = new_verts[i + 1 if i + 1 < origin_verts else 0]
        x1 = line1[0][0]
        y1 = line1[0][2]
        x2 = line1[1][0]
        y2 = line1[1][2]
        x3 = line2[0][0]
        y3 = line2[0][2]
        x4 = line2[1][0]
        y4 = line2[1][2]
        a1 = (y4 - y3)*(x4 - x1) - (x4 - x3)*(y4 - y1)
        a2 = (y4 - y3)*(x2 - x1) - (x4 - x3)*(y2 - y1)
        lam = a1/a2
        point = line1[0] + lam*(line1[1]-line1[0])
        points = np.append(points, [point], axis=0)
    points_origin = len(points)
    points, point_IDs = solidify(points, z=z)
    verts = np.append(verts, points, axis=0)
    faces_IDs = np.append(faces_IDs, np.fliplr(point_IDs)+origin_verts+points_origin, axis=0)

    # print("verts \n%s" % verts)
    # print("faces_IDs \n%s" % faces_IDs)

    # fill top and bottom faces
    for i in range(origin_verts):
        incr = i + 1 if i + 1 < origin_verts else 0
        faces = np.array([[i, incr, i + origin_verts*2],
                          [incr, incr + origin_verts*2, i + origin_verts*2]])
        faces_IDs = np.append(faces_IDs, faces, axis=0)
    for i in range(origin_verts, origin_verts*2, 1):
        incr = i + 1 if i + 1 < origin_verts*2 else origin_verts
        faces = np.array([[i + origin_verts*2, incr, i],
                          [i + origin_verts*2, incr + origin_verts*2, incr]])
        faces_IDs = np.append(faces_IDs, faces, axis=0)

    # print("faces_IDs \n%s" % faces_IDs)
    saveOBJ(file_path=file_path, vertices=verts, faceVertIDs=faces_IDs, withMTL=with_MTL)


# if __name__ == "__main__":
#     if len(sys.argv) != 6:
#         print("Usage: # python %s inputfile thickness R G B" % sys.argv[0])
#         quit()
#     vertices, _, _, _, uvIDs, _, _ = loadOBJ(sys.argv[1])
#     solidify2("output.obj", vertices, 0.2, 1.0, True)
#     saveMTL('output.mtl', convert_rgb([255, 0, 0]))
