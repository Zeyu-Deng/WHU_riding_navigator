from networkx import MultiDiGraph
from os.path import exists
import pickle
from osmnx import graph_from_place, graph_to_gdfs

class RoadNet:  # 路网类，从open street map获取的武汉大学路网
    def __init__(self):
        self.graph = MultiDiGraph()

    def create_road_net(self):
        # 如果存在pkl文件，直接从本地读取路网
        if exists("data/road_net.pkl"):
            with open("data/road_net.pkl", 'rb') as f:
                self.graph = pickle.load(f)
        # 否则，联网从Open Street Map官网获取路网，并保存本地
        else:
            self.graph = graph_from_place("Wuhan University", network_type="bike")
            with open("data/road_net.pkl", 'wb') as f:
                pickle.dump(self.graph, f)

    def get_nodes_edges(self):   # 获取路网顶点和边列表的函数
        nodes, edges = graph_to_gdfs(self.graph, nodes=True, edges=True)
        nodes_ls = list(nodes.index)  # 从nodes中获取其osmid构成顶点列表

        edges_ls = []
        for edge in list(self.graph.edges(data="length")):  # 将路网图的边数据逐个存入边长字典
            # 边长为保留3位小数的float类型
            edges_ls.append([edge[0], edge[1], round(edge[2], 3)])
        return nodes_ls, edges_ls
