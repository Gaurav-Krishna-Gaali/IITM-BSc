# Week5 grpa1


def FiberLink(distance_map):
    (edges, component, t, l, s) = (
        list(), dict(), list(), list(distance_map.keys()), 0)
    for u in l:
        edges.extend((d, u, v) for (v, d) in distance_map[u])
        component[u] = u
    edges.sort()
    for [d, u, v] in edges:
        if(component[u] != component[v]):
            t.append((u, v))
            c = component[u]
            s += d
            for i in l:
                if(component[i] == c):
                    component[i] = component[v]
    return(s)


# Week5 grpa2

def bellmanford(WList, s):
    infinity = 1 + len(WList.keys()) * \
        max([d for u in WList.keys() for (v, d) in WList[u]])
    distance = {}
    prev = {}
    for v in WList.keys():
        distance[v] = infinity
        prev[v] = None
    distance[s] = 0
    for i in WList.keys():
        for u in WList.keys():
            for (v, d) in WList[u]:
                if distance[v] > distance[u] + d:
                    distance[v] = distance[u] + d
                    prev[v] = u
    return (distance, prev)


def min_cost_walk(route_map, source, destination, via):
    distance1, path1 = bellmanford(route_map, source)
    distance2, path2 = bellmanford(route_map, via)
    tot_dist = distance1[via]+distance2[destination]
    Route_S_D = []
    # shortest route for source to via
    if distance2[destination] != 0:
        dest = destination
        while dest != via:
            Route_S_D = [dest] + Route_S_D
            for k, l in path2.items():
                if dest == k:
                    dest = l
                    break
    Route_S_D = Route_S_D
    # shortest route for via to destination
    if distance1[via] != 0:
        dest = via
        while dest != source:
            Route_S_D = [dest] + Route_S_D
            for i, j in path1.items():
                if dest == i:
                    dest = j
                    break
        Route_S_D = [dest] + Route_S_D
    return (tot_dist, Route_S_D)


# week 5 grpa 3
def IsNegativeWeightCyclePresent(WL):
    inf = 1 + len(WL.keys()) * max([d for u in WL.keys() for (v, d) in WL[u]])
    distance = dict()
    for v in WL.keys():
        distance[v] = inf
    for i in range(len(WL.keys())+1):
        if(i < len(WL.keys())):
            for u in WL.keys():
                for (v, d) in WL[u]:
                    distance[v] = min(distance[v], distance[u] + d)
    else:
        for u in WL.keys():
            for (v, d) in WL[u]:
                if(distance[v] > distance[u] + d):
                    return(True)
    return(False)
