from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon
from window import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('image/whu.png'))
    w = MainWindow()
    app.exec_()
