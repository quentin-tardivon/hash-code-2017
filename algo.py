def algo(videosSize, endpointLatency,videoRequestByEndpoint, videoRequestDesc, endpointLatencyAsc, V, E, R, C, X):
    cacheFilled = [X for x in range(C)]
    videosInCache = [[] for x in range(C)]
    for i in range(len(videosSize)):
        videosSize[i] = int(videosSize[i])
    #request = (videoID, endpointID)
    for request in videoRequestDesc:
        #connection = (endpointID, cache)
        for connection in endpointLatencyAsc:
            if request[1] == connection[0]:
                if not (request[0] in videosInCache[connection[1] - 1]):
                    if int(cacheFilled[connection[1] - 1]) >= int(videosSize[request[0]]):
                        videosInCache[connection[1] - 1].append(request[0])
                        cacheFilled[connection[1] -1] -= videosSize[request[0]]
                        break
                else:
                    break

            #else:
                #print "no connection"
    return videosInCache
