# PPA-1


def Huffman(s):
    s_list = list(s)
    s_set = set(s)
    freq_list = []
    for ch in s_set:
        freq_list.append((s_list.count(ch), ch))
    nodes = []
    for nd in freq_list:
        nodes.append((nd, Node(nd[0], nd[1])))

    while len(nodes) > 1:
        nodes.sort()
        L = nodes[0][1]
        R = nodes[1][1]
        newnode = Node(L.frequency + R.frequency, L.symbol + R.symbol, L, R)
        nodes.pop(0)
        nodes.pop(0)
        nodes.append(
            ((L.frequency + R.frequency, L.symbol + R.symbol), newnode))

    chardic = {}
    for ch in s_set:
        temp = newnode
        code = ''
        while ch != temp.symbol:
            if ch in temp.left.symbol:
                code += '0'
                temp = temp.left
            else:
                code += '1'
                temp = temp.right
        chardic[ch] = code

    return chardic


# PPA-2


def minimizeLateness(N, jobs):
    sort_jobs = sorted(jobs, key=lambda s: (s[2], s[1]))
    prod_start = {}
    job_sch = []
    for i in range(N):
        prod_start[i] = 0
        job_sch.append([])
    for n, s, f in sort_jobs:
        L = sorted(prod_start.items(), key=lambda s: s[1])
        k = L[0][0]
        prod_start[k] += s
        job_sch[k].append(n)
    return (job_sch)


# GRPA-1


    def insert(self, v):
        if self.isempty():
            self.value = v
            self.height = 1
            self.right = AVLTree()
            self.left = AVLTree()
            self.rebalance(v)

        elif self.value == v:
            return

        elif v < self.value:
            self.left.insert(v)
            self.rebalance(v)
            return

        elif v > self.value:
            self.right.insert(v)
            self.rebalance(v)
            return

    def calc_height(self):
        if self.valve == None:
            return

        else:
            return (1 + max(self.left.hight, self.right.height))

    def rebalance(self, v):
        slope = self.left.height - self.right.height
        if slope > 1 and v < self.left.value:
            self.rightrotate()
            self.height = 1 + max(self.left.height, self.right.height)
            self.left.height = 1 + \
                max(self.left.left.height, self.right.right.height)
            self.right.height = 1 + \
                max(self.left.left.height, self.right.right.height)

        if slope < -1 and v > self.right.value:
            self.leftrotate()
            self.height = 1 + max(self.left.height, self.right.height)

        if slope > 1 and v > self.left.value:

            self.left.leftrotate()
            self.rightrotate()
            self.left.height = 1 + \
                max(self.left.left.height, self.right.right.height)
            self.right.height = 1 + \
                max(self.left.left.height, self.right.right.height)

        if slope < -1 and v < self.right.value:
            self.right.rightrotate()
            self.leftrotate()
            self.left.height = 1 + \
                max(self.left.left.height, self.right.right.height)
            self.right.height = 1 + \
                max(self.left.left.height, self.right.right.height)

        self.height = 1 + max(self.left.height, self.right.height)
        return


# GRPA - 2


def minimum_platform(schedule):
    sch = schedule
    n = 0
    while sch != []:
        r = []
        d_time = sch[0][2]
        sch.pop(0)
        for k in sch:
            if (k[1] >= d_time):
                d_time = k[2]
                r.append(k)
        for i in r:
            sch.remove(i)
        n += 1
    return n


# GRPA-3


def no_overlap(L):
    L_sort = sorted(L, key=lambda s: (s[2], s[1]))
    accepted = []
    end_day = 0
    for k in L_sort:
        if k[1] > end_day:
            end_day = k[2]
            accepted.append(k)
    return (accepted)
