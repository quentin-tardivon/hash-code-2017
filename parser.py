def parse(path):
    data = open(path, "r")

    # First line parsing
    line = data.readline()
    V, E, R, C, X = line.split(" ")
    V, E, R, C, X = int(V), int(E), int(R), int(C), int(X)

    # Second line parsing
    line = data.readline()
    videosSize = line.split(" ")

    # Third part parsing
    endpointLatency = [[0 for x in range(C+1)] for y in range(E)]
    for i in range(E):
        line = data.readline()
        LD , K = line.split(" ")
        LD, K = int(LD), int(K)
        endpointLatency[i][0] = LD
        for j in range(K):
            line = data.readline()
            idC, LC = line.split(" ")
            idC, LC = int(idC), int(LC)
            endpointLatency[i][j] = LC

    #Fourth Part parsing
    videoRequestByEndpoint = [[0 for x in range(E)] for y in range(V)]
    for i in range(R):
        line = data.readline()
        idV, idE, nbR = line.split(" ")
        idV, idE, nbR = int(idV), int(idE), int(nbR)
        videoRequestByEndpoint[idV][idE] = nbR

    #Closing file
    data.close()

    return videosSize, endpointLatency,videoRequestByEndpoint
