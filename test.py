import sys
import re
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QListWidgetItem, QDialog


class SearchDialog(QDialog):
    def __init__(self, items):
        super(SearchDialog, self).__init__()
        self.setWindowTitle('Search Dialog')
        self.layout = QVBoxLayout()

        self.input_field = QLineEdit()
        self.input_field.textChanged.connect(self.search_items)
        self.list_widget = QListWidget()
        self.list_widget.itemDoubleClicked.connect(self.item_selected)
        self.list_widget.addItems(items)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.list_widget)
        self.setLayout(self.layout)

        self.selected_item = None

    def search_items(self, text):
        pattern = re.compile(text, re.IGNORECASE)
        self.list_widget.clear()
        matching_items = [item for item in items if re.search(pattern, item)]
        self.list_widget.addItems(matching_items)

    def item_selected(self, item):
        self.selected_item = item.text()
        self.accept()


class MainWindow(QWidget):
    def __init__(self, items):
        super(MainWindow, self).__init__()
        self.items = items
        self.layout = QVBoxLayout()

        self.select_button = QPushButton('Select')
        self.select_button.clicked.connect(self.show_search_dialog)
        self.selected_item = None

        self.layout.addWidget(self.select_button)
        self.setLayout(self.layout)

    def show_search_dialog(self):
        dialog = SearchDialog(self.items)
        if dialog.exec_() == QDialog.Accepted:
            self.selected_item = dialog.selected_item


if __name__ == "__main__":
    items = ['Apple', 'Banana', 'Orange', 'Pineapple', 'Grapes', 'Strawberry']
    app = QApplication(sys.argv)

    main_window = MainWindow(items)
    main_window.show()

    sys.exit(app.exec_())