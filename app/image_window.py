from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
)

class ImageWindow(QMainWindow):
    def __init__(self, image_path):
        super().__init__()

        self.setWindowTitle("Fractal Image")
        self.setGeometry(100, 100, 800, 800)

        # Criar cena e view
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)

        # Carregar a imagem
        pixmap = QPixmap(image_path)
        self.image_item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.image_item)

        # Ajustar a view para caber a imagem
        self.view.setSceneRect(self.image_item.boundingRect())

        # Fator de escala inicial
        self.scale_factor = 1.0

        # Criar botões de zoom
        zoom_in_button = QPushButton("Zoom In")
        zoom_out_button = QPushButton("Zoom Out")

        # Conectar botões às funções
        zoom_in_button.clicked.connect(lambda: self.scale_image(1.2))
        zoom_out_button.clicked.connect(lambda: self.scale_image(1 / 1.2))

        # Layout dos botões
        button_layout = QVBoxLayout()
        button_layout.addWidget(zoom_in_button)
        button_layout.addWidget(zoom_out_button)

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.view)
        main_layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def scale_image(self, factor):
        # Aplicar o fator de escala
        self.scale_factor *= factor
        self.view.resetTransform()
        self.view.scale(self.scale_factor, self.scale_factor)
