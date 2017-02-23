
data = open("data.in", "r")

# First line parsing
line = data.readline()
V, E, R, C, X = line.split(" ")

# Second line parsing
line = data.readline()
videosSize = line.split(" ")

# Third part parsing
endpointLatency = [[0 for x in range(E)] 0 for y in range(C+1)]
for i in range(E):
    line = data.readline()
    LD , K = line.split(" ")
    endpointLatency[i][0] = LD
    for j in range(K):
        line = data.readline()
        idC, LC = line.split(" ")
        endpointLatency[i][j] = LC

#Fourth Part parsing
videoRequestByEndpoint = [[0 for x in range(V)] 0 for y in range(E)]
for i in range(R)
    line = data.getline()
    idV, idE, nbR = line.split(" ")
    videoRequestByEndpoint[idV][idE] = nbR

#Closing file
data.close()
