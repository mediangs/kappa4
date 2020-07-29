import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import NearestNeighbors
import networkx as nx
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# x = np.array([0, 0, 1, 2, 3,  3, 2, 7, 8, 8,9,9])
# y = np.array([0, 2, 4, 4, 3,1.5, 0, 1, 2, 1,2,3])
# #z = np.array([0,0,0,0,0,0,0])
# plt.plot(x, y)
# plt.show()
#
# idx = np.random.permutation(x.size)
# x = x[idx]
# y = y[idx]

import point_data as data
org_points = [np.array(x) for x in data.P0]
x, y, z = [np.array(a) for a in zip(*org_points)]
idx = np.random.permutation(len(x))
x = x[idx]
y = y[idx]
z = z[idx]
points = np.c_[x, y]
ax.plot(x, y, z)
plt.show()


G = NearestNeighbors(2).fit(points).kneighbors_graph()
T = nx.from_scipy_sparse_matrix(G)
#nx.draw_networkx(T, with_labels = True, node_color ='green')

segments = list(nx.connected_components(T))
T_segments = [T.subgraph(x) for x in segments]
orders = [list(nx.dfs_preorder_nodes(x)) for x in T_segments]

paths=[]
for T_segment in T_segments:
    paths.append([list(nx.dfs_preorder_nodes(T_segment, x)) for x in T_segment.nodes])

mindist = np.inf
minidx = 0
for path in paths:
    for i in range(len(path)):
        p = path[i]           # order of nodes
        ordered = points[p]    # ordered nodes
        # find cost of that order by the sum of euclidean distances between points (i) and (i+1)
        cost = (((ordered[:-1] - ordered[1:])**2).sum(1)).sum()
        if cost < mindist:
            mindist = cost
            minidx = i

    opt_order = path[minidx]
    opt_order.append(opt_order[0])
    xx = x[opt_order]
    yy = y[opt_order]
    zz = z[opt_order]

    ax.plot(xx, yy, zz)
    ax.plot(x, y, z)
    plt.show()

