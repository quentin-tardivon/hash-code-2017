import sort as st
import simplesort as simplest
import parser as ps
import algo

result = ps.parse("videos_worth_spreading.in")
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

endpointLatencyAsc.pop(0)


videoRequestDesc = list(reversed(st.quickSort(videoRequestByEndpoint)))

result = algo.algo(videoSize, endpointLatency,videoRequestByEndpoint, videoRequestDesc, endpointLatencyAsc, V, E, R, C, X)

ps.output(result)
