import sort as st
import parser as ps

def main():
    videoSize, endpointLatency, videoRequestByEndpoint, V, E, R, C, X = ps.parse("me_at_the_zoo.in")
    endPointLatencyDesc = st.quickSort(endpointLatency)
    videoRequestByEndpointAsc = list(reversed(st.quickSort(videoRequestByEndpoint)))
