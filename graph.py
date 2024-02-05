from geopy.distance import geodesic
import heapq
from road_net import RoadNet

class Digraph:   # 有向图类
    """ 初始化函数，用给定的顶点和边初始化有向图
        nodes为顶点列表，每个元素表示一个osmid
        edges为边的列表，每个元素为[起点, 终点, 长度]的格式
        其中节点的id为int类型，长度为float类型
    """
    def __init__(self, nodes, edges):
        self.nodes = nodes  # 顶点列表
        self.edges = edges  # 边列表

    def add_edge(self, u, v, w):  # 添加边的函数
        self.edges.append([u, v, w])

    def remove_edge(self, u, v):  # 移除边的函数
        for e in self.edges:
            if e[0] == u and e[1] == v:
                self.edges.remove(e)
                return

    # Dijkstra算法求解单源点最短路径方法
    def dijkstra(self, src_vertex):
        visited = []  # visited为被访问的节点列表
        # dist用于记录从src_vertex（起点）到图中各顶点的最短路径长度
        Dist = {v: float("inf") for v in self.nodes}
        Dist[src_vertex] = 0
        # pre_nodes用于记录从src_vertex到图中各顶点最短路径的前一顶点
        pre_nodes = {}
        # cands存储了当前待选择的顶点序列
        cands = [(0, src_vertex)]
        while len(cands) > 0:
            # 用heapq的heappop函数获取cands中的最小值
            dist, current_vertex = heapq.heappop(cands)
            visited.append(current_vertex)
            for node in self.nodes:  # 遍历图的全部顶点
                for edge in self.edges:
                    # 对于那些以当前考察的顶点为起点、以当前遍历到的顶点为终点的边
                    if current_vertex == edge[0] and node == edge[1]:
                        elen = edge[2]  # 获取这条边的长度
                        if node not in visited:  # 若终点尚未被访问
                            old_plen = Dist[node]  # 获取终点在Dist字典中的距离记录（原来的距离）
                            new_plen = Dist[current_vertex] + elen  # 获取起点在Dist字典中的距离记录并加上当前边的长度（新的距离）
                            if new_plen < old_plen:  # 若更新的最短路径长度小于之前的最短路径长度
                                heapq.heappush(cands, (new_plen, node))
                                Dist[node] = new_plen  # 更新Dist字典中的记录
                                pre_nodes[node] = current_vertex  # 更新“前一顶点”字典中的记录
        return Dist, pre_nodes

    @staticmethod
    # 从dist和pre_nodes字典中获取到指定地点最短路径的方法(返回距离和路径list)
    def get_path(dist, pre_nodes, start_node, target_node) -> (float, list):
        path = []
        node = target_node
        while node != start_node:  # 回溯路径上的顶点
            path.append(node)
            node = pre_nodes[node]
        path.append(start_node)
        return dist[target_node], list(reversed(path))


class AStarGraph:   # 用AStar算法计算路径的图类
    # 通过一个RoadNet类初始化AStarGraph
    def __init__(self, road_net: RoadNet):
        # 包含一个graph和edges属性(用于计算邻接边)
        self.graph = road_net.graph
        self.edges = road_net.get_nodes_edges()[1]

    @staticmethod  # 根据两点的经纬度计算测地距离的静态方法
    def cal_heudis(lat1, lon1, lat2, lon2):
        # 返回(lat1, lon1)和(lat2, lon2)两坐标点之间的测地距离
        return geodesic((lat1, lon1), (lat2, lon2)).m

    def get_neighbors(self, n):  # 获取顶点n的邻接顶点以及对应邻接边长度方法
        neighbors_list = []
        for e in self.edges:
            if e[0] == n:
                neighbors_list.append([e[1], e[2]])
        return neighbors_list

    # A*算法求解从起点到终点的最短路径方法
    def astar(self, src_vertex, dst_vertex):
        open_lst: set = {src_vertex}  # 将起点放入到开放列表中
        closed_lst: set = set([])  # 关闭列表中的所有元素已经不需要被关注
        lat1 = self.graph.nodes[src_vertex]['y']
        lon1 = self.graph.nodes[src_vertex]['x']
        # poo字典记录起点到其他顶点的最优距离，默认值为正无穷
        poo: dict = {src_vertex: 0}
        # par字典记录最优路径上各顶点的前驱顶点映射
        par: dict = {src_vertex: src_vertex}

        while len(open_lst) > 0:  # 遍历开放列表
            n = None
            # 计算列表中每一个顶点的评价函数，查找评价函数值最小的顶点，把它作为当前要处理的顶点
            for v in open_lst:
                lat2 = self.graph.nodes[v]['y']
                lon2 = self.graph.nodes[v]['x']
                if (n is None
                    or poo[v] + self.cal_heudis(lat1, lon1, lat2, lon2)
                        < poo[n] + self.cal_heudis(lat1, lon1, lat2n, lon2n)):
                    n = v
                    lat2n = self.graph.nodes[v]['y']
                    lon2n = self.graph.nodes[v]['x']

            # 程序终止条件1:无法查找到终点，并且此时开放列表是空列表（此时没有路径）
            if n is None:
                # print('Path does not exist!')
                return None

            # 程序终止条件2:将终点加入到了开放列表中（此时路径已经找到了）
            if n == dst_vertex:
                # 若终点已经找到，查找最短路径：从终点开始，每个顶点都沿着前驱顶点移动，直到起点
                reconst_path = []
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
                reconst_path.append(src_vertex)
                for i in range(0, len(reconst_path)):  # osmid浮点型转整型
                    reconst_path[i] = int(reconst_path[i])
                path = list(reversed(reconst_path))
                return path

            # 对与当前顶点相邻的其他所有顶点做如下操作
            neighbor_list = self.get_neighbors(n)
            for adj_edge in neighbor_list:
                m, weight = adj_edge[0], adj_edge[1]

                # 如果相邻顶点既不在关闭列表（表明需要考察）也不在开放列表中，则将其加入开放列表，并将当前顶点设置为其前驱顶点，计算相邻顶点的poo值
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight

                # 如果相邻顶点已经在开放列表中，则需要检查先经过当前顶点再到达相邻顶点的路径是否更好，若这条路径更好，则更新相邻顶点的par值和poo值
                # 如果相邻顶点在关闭列表中，则将其从关闭列表中移除，加入到开放列表中
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            # 考察完其全部相邻顶点后，将当前顶点从开放列表中移除，加入到关闭列表中
            open_lst.remove(n)
            closed_lst.add(n)

        # print('Path does not exist!')
        return None

    def get_length(self, astar_path):
        edge_length = {}  # 该字典用于存放边元组和边长度（距离）的键值对
        for i in self.edges:  # 将路网图的边数据逐个存入边长字典
            edge_length[(i[0], i[1])] = i[2]

        length = 0
        for i in range(len(astar_path)-1):  # 循环计算路径中每条边的长度
            sub_edge = (astar_path[i], astar_path[i+1])
            length += edge_length[sub_edge]
        return length
