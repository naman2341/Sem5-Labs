from collections import deque
import queue
from numpy import *
import copy


def A_star_Traversal(cost, heuristic, start_point, goals):
    path = []
    cost_len = len(cost)   

    nodes_visited = [0 for i in range(cost_len)]
    pri_queue = queue.PriorityQueue()

    pri_queue.put((heuristic[start_point], ([start_point], start_point, 0)))
    while(pri_queue.qsize() != 0):
        est_cost, s_node = pri_queue.get()
        path = s_node[0]
        node = s_node[1]
        node_cost = s_node[2]

        if nodes_visited[node] == 0:
            nodes_visited[node] = 1

            if node in goals:
                return path

            for i in range(1, cost_len):
                if cost[node][i] > 0 and nodes_visited[i] == 0:

                    final_cost = node_cost + cost[node][i]
                    est_cost = final_cost + heuristic[i]

                    pri_neigh = copy.deepcopy(path)
                    pri_neigh.append(i)
                    
                    pri_queue.put((est_cost, (pri_neigh, i, final_cost)))


    return list()
    #return path

def env(adjList):
    path = []
    for index, node in enumerate(adjList[1::], start=1):
        if node > 0:
            path.append(index)
    return path[::-1]




def DFS_Traversal(cost, start_point, goals):
   
    path = []
    c = deque()
    c.append({
        "node": start_point,
        "path": [start_point]
    })
    explored_nodes = set()
    while (c):
        p = c.pop()
        if p["node"] in explored_nodes:
            continue
        explored_nodes.add(p["node"])
        if(p["node"] in goals):
            return p["path"]
        pop_neigh_nd = env(cost[p["node"]])
        for nodes in pop_neigh_nd:
            if nodes not in explored_nodes:
                node_rec = {
                    "node": nodes,
                    "path": p["path"] + [nodes]
                }
                c.append(node_rec)
    return path

