from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import QUrl, Signal
from os.path import abspath
from navigator import Navigator
from ui.ui_nav_path import Ui_PathWindow
from ui.ui_main import Ui_MainWindow
from PySide2.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QListWidget
from pandas import read_csv
from re import compile, search, IGNORECASE

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 初始化UI界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.web.load(QUrl.fromLocalFile(abspath("graphs/map.html")))
        # 创建导航器
        self.nav = Navigator()
        # 创建显示导航路径的子窗口， 默认为hide
        self.nav_window = NavPathWindow()
        self.nav_window.setParent(self)
        self.nav_window.hide()
        # 绑定信号与槽函数
        self.ui.srcButton.clicked.connect(self.select_src)
        self.ui.dstButton.clicked.connect(self.select_des)
        self.ui.navButton.clicked.connect(self.go_to_nav)

        self.nav.nav_done.connect(self.show_nav_path)
        self.nav_window.ui.returnButton.clicked.connect(self.hide_nav_path)
        # 显示页面
        self.show()

    def show_nav_path(self, src_id, des_id, alg_type):  # 显示导航路径的槽函数
        # 改变nav_window窗口的标签内容
        self.nav_window.ui.algLabel.setText(f"算法：{self.ui.algBox.currentText()}")
        self.nav_window.ui.srcLabel.setText(f"起点：{self.ui.srcEdit.text()}")
        self.nav_window.ui.dstLabel.setText(f"终点：{self.ui.dstEdit.text()}")
        # 为nav_window选择要显示的html地图
        self.nav_window.load_web(src_id, des_id, alg_type)
        self.hide_all_ui()
        self.nav_window.show()

    def go_to_nav(self):  # 开始导航的函数
        src = self.ui.srcEdit.text()
        des = self.ui.dstEdit.text()
        alg = self.ui.algBox.currentText()
        # 起点或终点为空时，提示用户并跳过
        if src == "" or des == "":
            QMessageBox.about(self, "警告", "起点或终点不能为空!")
            return
        # 获取起点和终点的osmid
        src_id = self.nav.loc2id[src]
        des_id = self.nav.loc2id[des]
        if src_id == des_id:
            QMessageBox.about(self, "警告", "起点或终点不能相同或太相近!")
            return
        # 为起点和终点间寻找导航路径
        try:
            if alg == "Dijkstra":
                self.nav.nav_by_dijkstra(src_id, des_id)
            else:
                self.nav.nav_by_astar(src_id, des_id)
        except:
            QMessageBox.about(self, "错误", "未找到最短路径!")

    def hide_nav_path(self):
        self.nav_window.hide()
        self.show_all_ui()

    def select_src(self):
        diglog = SelectDialog()
        diglog.selected_item.connect(self.ui.srcEdit.setText)
        diglog.exec_()

    def select_des(self):
        diglog = SelectDialog()
        diglog.selected_item.connect(self.ui.dstEdit.setText)
        diglog.exec_()


    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.nav_window.resize(self.width(), self.height())

    def hide_all_ui(self):
        self.ui.titleLabel.hide()
        self.ui.srcEdit.hide()
        self.ui.srcButton.hide()
        self.ui.dstEdit.hide()
        self.ui.dstButton.hide()
        self.ui.algBox.hide()
        self.ui.algBox.hide()
        self.ui.navButton.hide()
        self.ui.web.hide()

    def show_all_ui(self):
        self.ui.titleLabel.show()
        self.ui.srcEdit.show()
        self.ui.srcButton.show()
        self.ui.dstEdit.show()
        self.ui.dstButton.show()
        self.ui.algBox.show()
        self.ui.algBox.show()
        self.ui.navButton.show()
        self.ui.web.show()


class NavPathWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PathWindow()
        self.ui.setupUi(self)  # 用ui初始化界面

    def load_web(self, src_id, des_id, alg_type):
        alg = "dijkstra" if alg_type == 1 else "astar"
        path = f"graphs/{src_id}-{des_id}({alg}).html"
        self.ui.web.load(QUrl.fromLocalFile(abspath(path)))


class SelectDialog(QDialog):
    # 定义信号
    selected_item = Signal(str)

    def __init__(self):
        super().__init__()
        # 从loc_to_id文件中添加位置
        self.items = read_csv("data/loc_to_id.csv")['location'].tolist()
        # 初始化UI
        self.setWindowTitle("选择地点")
        self.layout = QVBoxLayout()
        self.searchEdit = QLineEdit()
        self.listWidget = QListWidget()
        self.listWidget.addItems(self.items)

        self.layout.addWidget(self.searchEdit)
        self.layout.addWidget(self.listWidget)
        self.setLayout(self.layout)
        # 绑定信号与槽函数
        self.searchEdit.textChanged.connect(self.search_items)
        self.listWidget.itemDoubleClicked.connect(self.selected)

    def search_items(self, text):
        pattern = compile(text, IGNORECASE)  # 不区分大小写匹配正则表达式
        self.listWidget.clear()
        matched_items = [i for i in self.items if search(pattern, i)]
        self.listWidget.addItems(matched_items)

    def selected(self, item):
        self.selected_item.emit(item.text())
        self.accept()
