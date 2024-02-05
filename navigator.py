from road_net import RoadNet
from graph import Digraph, AStarGraph
from folium import Marker, Icon, Element
from osmnx import plot_route_folium
from os.path import exists
from PySide2.QtCore import QObject, Signal
from pandas import read_csv

class Navigator(QObject):
    # 定义信号nav_done，当导航完成后发送该信号，三个参数为src_id、des_id和算法类型
    # 因为int型的osm_id超出了int信号的表示范围，所以用str发送信号
    nav_done = Signal(str, str, int)

    def __init__(self):
        super().__init__()
        # 创建导航用的路网
        self.net = RoadNet()
        self.net.create_road_net()
        nodes, edges = self.net.get_nodes_edges()
        # 定义digraph和astargraph
        self.digraph = Digraph(nodes, edges)
        self.astargraph = AStarGraph(self.net)
        # 构建地名到osm_id的映射字典
        data = read_csv("data/loc_to_id.csv")
        self.loc2id = data.set_index('location')['osmid'].to_dict()

    def nav_by_dijkstra(self, src_id, des_id):
        if not exists(f"graphs/{src_id}-{des_id}(dijkstra).html"):
            dist, pre_nodes = self.digraph.dijkstra(src_id)
            length, path = Digraph.get_path(dist, pre_nodes, src_id, des_id)
            map = self.draw_map(path, length, 10, 'purple', 'Dijkstra')
            map.save(f"graphs/{src_id}-{des_id}(dijkstra).html")
        self.nav_done.emit(str(src_id), str(des_id), 1)

    def nav_by_astar(self, src_id, des_id):
        if not exists(f"graphs/{src_id}-{des_id}(astar).html"):
            path = self.astargraph.astar(src_id, des_id)
            length = self.astargraph.get_length(path)
            map = self.draw_map(path, length, 10, 'blue', 'A*')
            map.save(f"graphs/{src_id}-{des_id}(astar).html")
        self.nav_done.emit(str(src_id), str(des_id), 2)

    # 参数为: 最短路径path，距离length，路径宽度w，路径颜色c，算法名称name
    def draw_map(self, path, length, w, c, name):  # 根据导航结果绘制html地图
        src_node = self.net.graph.nodes[path[0]]  # 路径中第一个点为起点
        src_lat, src_lon = src_node['y'], src_node['x']
        des_node = self.net.graph.nodes[path[-1]]  # 路径中最后一个点为终点
        des_lat, des_lon = des_node['y'], des_node['x']

        map = plot_route_folium(self.net.graph, path, popup_attribute="length",
                                tiles="openstreetmap", weight=w, color=c)
        # 添加起点和终点的标记
        src_marker = Marker(
            location=(src_lat, src_lon), popup="Departure", icon=Icon(color='green')
        )
        des_marker = Marker(
            location=(des_lat, des_lon), popup="Destination", icon=Icon(color='red')
        )
        src_marker.add_to(map)
        des_marker.add_to(map)
        map.get_root().html.add_child(Element(
            "<h3 align='center' style='font-size:16px'><b>"
            f"Shortest path calculated with {name} algorithm - Total distance = {length:.2f} m"
            "</b></h3>"
        ))
        return map
