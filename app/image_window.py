from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel
)

class ImageWindow(QMainWindow):
    def __init__(self, image_path):
        super().__init__()

        self.setWindowTitle("Fractal Image")
        self.setGeometry(100, 100, 800, 800)

        layout = QVBoxLayout()

        label = QLabel()
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)