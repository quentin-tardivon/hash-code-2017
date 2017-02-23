import sort as st
import parser as ps
import algo

videoSize, endpointLatency, videoRequestByEndpoint, V, E, R, C, X = ps.parse("me_at_the_zoo.in")
endpointLatencyAsc = [[]]
for i in range(len(endpointLatency)):
    endpointLatencyAsc.append(st.quickSort(endpointLatency))

videoRequestByEndpointDesc = list(reversed(st.quickSort(videoRequestByEndpoint)))

print algo.algo(videoSize, endpointLatency,videoRequestByEndpoint, videoRequestDesc, endpointLatencyAsc, V, E, R, C, X)
