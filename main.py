import sort as st
import parser as ps

videoSize, endpointLatency, videoRequestByEndpoint = ps.parse("me_at_the_zoo.in")
endpointLatencyAsc = [[]]
for i in range(len(endpointLatency)):
    endpointLatencyAsc.append(st.quickSort(endpointLatency))

videoRequestByEndpointDesc = list(reversed(st.quickSort(videoRequestByEndpoint)))
