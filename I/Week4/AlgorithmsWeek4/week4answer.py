# coding=utf-8
import sys
import threading
import copy

threading.stack_size(67108864)
sys.setrecursionlimit(70000)

def DFS(edges, i, index):
    global t, vertices, new_vertices, s, compare
    if index == 1:  # 1st pass
        vertices[i-1][1] = True  # mark it explored
    if index == 2:  # 2nd pass
        vertices[compare[i]-1][1] = True
        vertices[compare[i]-1].append(s)  # set leader(i) = node s
    if i in edges:
        for v in edges[i]:
            if index == 1:
                if vertices[v-1][1] == False:
                    DFS(edges, vertices[v-1][0], index)
            if index == 2:
                if vertices[compare[v]-1][1] == False:
                    DFS(edges, vertices[compare[v]-1][0], index)
    if index == 1:
        t = t + 1  # i's finishing time
        vertices[i-1].append(t)
        temp = vertices[i-1].copy()
        temp[1] = False
        new_vertices.append(temp)
        compare[vertices[i-1][0]] = t

def DFS_loop(edges, index):
    global t, vertices, s
    t = 0  # for finishing times in 1st pass
    n = len(vertices)
    for i in range(1, n+1):
        v = vertices[n-i]
        if v[1] == False:
                s = v[0]
                DFS(edges, v[0], index)

def main():
    global vertices, new_vertices, compare  # newVertices是第一遍DFS之后添加了t的数组, compare是字典,key为vertice,value为t

    # 读取文件,分为定点和边两部分,直接读入逆向图
    f = open('/Users/hanying/Desktop/SCC.txt')
    _f = list(f)
    vertices = list()  # [number, False] false indicates unexplored
    new_vertices = list()  # [number, False, t, s]
    edges = dict()  # {1:[2,5,6...]...}
    edges_rev = dict()  # {2:[8,9,5...]...}
    compare = dict()
    for i in range(0, 875714):  # 875714 initialize V
        vertices.append([i+1, False])
    for edge in _f:  # initialize E
        temp = edge.split()
        edge_temp = [int(temp[0]), int(temp[1])]
        edge_rev_temp = [edge_temp[1], edge_temp[0]]
        if edge_temp[0] not in edges:
            edges[edge_temp[0]] = [edge_temp[1]]
        else:
            edges[edge_temp[0]].append(edge_temp[1])
        if edge_rev_temp[0] not in edges_rev:
            edges_rev[edge_rev_temp[0]] = [edge_rev_temp[1]]
        else:
            edges_rev[edge_rev_temp[0]].append(edge_rev_temp[1])

    # 两次DFS搜索
    DFS_loop(edges_rev, 1)
    vertices = copy.deepcopy(new_vertices)
    DFS_loop(edges, 2)

    result = dict()
    for item in vertices:  # nodes with the same 'leader'
        if item[3] not in result:
            result[item[3]] = 1
        else:
            result[item[3]] = result[item[3]] + 1

    r = list()  # output the sizes of the 5 largest SCCs
    for key in result:
        r.append(result[key])
    r = sorted(r, reverse = True)
    print(r[0:4])


if __name__ == '__main__':
    thread = threading.Thread(target = main)
    thread.start()