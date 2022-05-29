# GRPA1
def neighbours(Amat, v):
    (rows, cols) = (len(Amat), len(Amat[0]))
    nbrs = []
    for i in range(cols):
        if Amat[i][v] == 1:
            nbrs.append(i)
    return nbrs


def findConnectionLevel(v, Amat, X, Y):
    level = {}
    (rows, cols) = (len(Amat), len(Amat[0]))
    for i in range(rows):
        level[i] = -1
    q = []
    q.append(X)
    level[X] = 0

    while q != []:
        j = q.pop()
        for k in neighbours(Amat, j):

            if k == Y:
                level[k] = level[j]+1
                break

            if level[k] == -1:
                level[k] = level[j]+1
                q.append(k)

    if level[Y] >= 0:
        return level[Y]
    else:
        return 0


# GRPA2

def DFSInitGlobal(Alist):
    visited = {}
    for i in Alist.keys():
        visited[i] = False
    return visited


def DFSGlobal(Alist, visited, v):
    visited[v] = True
    for k in Alist[v]:
        if not visited[k]:
            DFSGlobal(Alist, visited, k)
    return visited


def findMasterTank(v, e):
    n = len(v)
    Alist = {}
    for i in range(int(v[0]), int(v[-1])+1):
        Alist[i] = []
    for (i, j) in e:
        Alist[int(i)].append(int(j))
    DFSInitGlobal(Alist)
    for i in Alist.keys():
        visited = DFSGlobal(Alist, DFSInitGlobal(Alist), i)
        Flag = True
        for k in visited.keys():
            if visited[k] != True:
                Flag = False
                break
        if Flag:
            return i
    return 0


# GRPA3
def longJourney(Alist):
    visited = {}
    for i in Alist.keys():
        visited[i] = False

    cities = []

    def DFS(s, path):
        visited[s] = True
        if path == []:
            path.append(s)
        for k in Alist[s]:
            if not visited[k]:
                DFS(k, path+[k])
        path.append(s)
        cities.append(path)
        path.pop()
        visited[s] = False

    DFS('Leh', path=[])
    max = 0
    index = 0
    for i in range(len(cities)):
        if len(cities[i]) > max:
            max = len(cities[i])
            index = i
    return cities[index]
