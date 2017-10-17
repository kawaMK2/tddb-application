
def loadOBJ(file_path):
    numVertices = 0
    numUVs = 0
    numNormals = 0
    numFaces = 0
    vertices = []
    uvs = []
    normals = []
    vertexColors = []
    faceVertIDs = []
    uvIDs = []
    normalIDs = []
    for line in open(file_path, "r"):
        vals = line.split()
        if len(vals) == 0:
            continue
        if vals[0] == "v":
            v = list(map(float, vals[1:4]))
            vertices.append(v)
            if len(vals) == 7:
                vc = list(map(float, vals[4:7]))
                vertexColors.append(vc)
            numVertices += 1
        if vals[0] == "vt":
            vt = list(map(float, vals[1:3]))
            uvs.append(vt)
            numUVs += 1
        if vals[0] == "vn":
            vn = list(map(float, vals[1:4]))
            normals.append(vn)
            numNormals += 1
        if vals[0] == "f":
            fvID = []
            uvID = []
            nvID = []
            for f in vals[1:]:
                w = f.split("/")
                if numVertices > 0:
                    fvID.append(int(w[0]) - 1)
                if numUVs > 0:
                    uvID.append(int(w[1]) - 1)
                if numNormals > 0:
                    nvID.append(int(w[2]) - 1)
            faceVertIDs.append(fvID)
            uvIDs.append(uvID)
            normalIDs.append(nvID)
            numFaces += 1
    print("numVertices: ", numVertices)
    print("numUVs: ", numUVs)
    print("numNormals: ", numNormals)
    print("numFaces: ", numFaces)
    return vertices, uvs, normals, faceVertIDs, uvIDs, normalIDs, vertexColors


def saveOBJ(file_path, vertices, uvs=[], normals=[], faceVertIDs=[], uvIDs=[], normalIDs=[], vertexColors=[],
            withMTL=False):
    f_out = open(file_path, 'w')
    f_out.write("####\n")
    f_out.write("#\n")
    f_out.write("# Vertices: %s\n" % (len(vertices)))
    f_out.write("# Faces: %s\n" % (len(faceVertIDs)))
    f_out.write("#\n")
    f_out.write("####\n")
    if withMTL:
        f_out.write("mtllib %s.mtl\n" % file_path.split("/")[::-1][0][:-4])
    for vi, v in enumerate(vertices):
        vertex = "v %s %s %s" % (v[0], v[1], v[2])
        if len(vertexColors) > 0:
            color = vertexColors[vi]
            vertex += " %s %s %s" % (color[0], color[1], color[2])
        vertex += "\n"
        f_out.write(vertex)
    f_out.write("# %s vertices\n\n" % (len(vertices)))
    for uv in uvs:
        uv = [float(i) for i in uv]
        uv = "vt %s %s\n" % (uv[0], uv[1])
        f_out.write(uv)
    f_out.write("# %s uvs\n\n" % (len(uvs)))
    for n in normals:
        normal = "vn %s %s %s\n" % (n[0], n[1], n[2])
        f_out.write(normal)
    f_out.write("# %s normals\n\n" % (len(normals)))
    if withMTL:
        f_out.write("usemtl %s\n" % file_path.split("/")[::-1][0][:-4])
    for fi, fvID in enumerate(faceVertIDs):
        face_vertex = "f"
        for fvi, fvIDi in enumerate(fvID):
            face_vertex += " %s/" % (fvIDi + 1)
            if len(uvIDs) > 0:
                face_vertex += "%s" % (uvIDs[fi][fvi] + 1)
            if len(normalIDs) > 0:
                face_vertex += "/%s" % (normalIDs[fi][fvi] + 1)
        # print(face_vertex)
        face_vertex += "\n"
        f_out.write(face_vertex)
    f_out.write("# %s faces\n\n" % (len(faceVertIDs)))
    f_out.write("# End of File\n")
    f_out.close()


def saveMTL(file_path, rgb):
    f_out = open(file_path, 'w')
    name = file_path.split('/')[::-1][0][:-4]
    f_out.write("# MTL File %s\n\n" % name)
    f_out.write("newmtl %s\n" % name)
    f_out.write("Ns 96.078431\n")
    f_out.write("Ka 1.000000 1.000000 1.000000\n")
    f_out.write("Kd %s %s %s\n" % (rgb[0], rgb[1], rgb[2]))
    f_out.write("Ks 0.500000 0.500000 0.500000\n")
    f_out.write("Ke 0.000000 0.000000 0.000000\n")
    f_out.write("Ni 1.000000\n")
    f_out.close()


def convert_rgb(rgb):
    return [i/256 for i in rgb]
