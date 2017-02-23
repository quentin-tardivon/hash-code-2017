def algo(videosSize, endpointLatency,videoRequestByEndpoint, videoRequestDesc, endpointLatencyAsc, V, E, R, C, X):
    cacheFilled = [C for x in range(E)]
    videosInCache = [[] for x in range(E)]
    #request = (videoID, endpointID)
    for request in videoRequestDesc:
        #connection = (endpointID, cache)
        for connection in [connections for connections in endPointLatencyDesc if (connections(0) == request(1))]:
            if not (request(0) in videosInCache[connection(1)]):
                if cacheFilled[connection(1)] > request(0):
                    videosInCache[connection(1)].append(request(0))
                    cacheFilled -= request(0)
                    break
            else:
                break
    return videosInCache
