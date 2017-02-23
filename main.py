import sort as st
import parser as ps

def main():
    videoSize, endpointLatency, videoRequestByEndpoint = ps.parse("me_at_the_zoo.in")
    endPointLatencyDesc = st.quickSort(endpointLatency)
    videoRequestByEndpointAsc = list(reversed(st.quickSort(videoRequestByEndpoint)))

    
