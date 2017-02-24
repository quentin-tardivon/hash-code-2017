import sort as st
import simplesort as simplest
import parser as ps
import algo

result = ps.parse("me_at_the_zoo.in")
videoSize = result[0]
endpointLatency = result[1]
videoRequestByEndpoint = result[2]
V = result[3]
E = result[4]
R = result[5]
C = result[6]
X = result[7]

endpointLatencyAsc = [[]]
for i in range(len(endpointLatency)):
    endpointLatencyAsc.append(simplest.quickSort(endpointLatency[i]))

print endpointLatencyAsc
endpointLatencyAsc.pop(0)


videoRequestDesc = list(reversed(st.quickSort(videoRequestByEndpoint)))

print algo.algo(videoSize, endpointLatency,videoRequestByEndpoint, videoRequestDesc, endpointLatencyAsc, V, E, R, C, X)
