from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from ctypes import *
import time
from app.image_window import ImageWindow


so_file = "./fractal.so"
c_functions = CDLL(so_file)
generate_in_c = c_functions.generate_fractal
generate_in_c.argtypes = [c_int, c_int, c_int]

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QGroupBox, QFormLayout, QPushButton, QLineEdit
)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mandelbrot Fractal using Python and C")

        # Criando os widgets
        title = QLabel("Mandelbrot Fractal usando Python e C")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; padding: 12px")

        explanation = QTextEdit()
        explanation.setReadOnly(True)
        explanation.setText(
            "O conjunto de Mandelbrot é um conjunto de pontos no plano complexo que "
            "permite a geração de fractais complexos e visualmente impressionantes. "
            "Este projeto demonstra como gerar um fractal de Mandelbrot usando Python e C."
        )

        authors_label = QLabel("Autores:")
        authors = QLabel("Daniel Núñez, Bruno Silveira")
        discipline_label = QLabel("Disciplina:")
        discipline = QLabel("Conceitos de Linguagens de Prorgramação")

        # Layouts para as seções de autores e disciplina
        authors_layout = QHBoxLayout()
        authors_layout.addWidget(authors_label)
        authors_layout.addStretch(1)
        authors_layout.addWidget(authors)

        discipline_layout = QHBoxLayout()
        discipline_layout.addWidget(discipline_label)
        discipline_layout.addStretch(1)
        discipline_layout.addWidget(discipline)

        # Layout do grupo de informações
        info_group = QGroupBox("Informações")
        info_layout = QVBoxLayout()
        info_layout.addLayout(authors_layout)
        info_layout.addLayout(discipline_layout)
        info_group.setLayout(info_layout)

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(title)
        main_layout.addWidget(info_group)
        main_layout.addWidget(explanation)

        # Seção de input
        input_layout = QFormLayout()
        width_label = QLabel("Largura:")
        self.width_input = QLineEdit()
        self.width_input.setText("1000")  # Set default value
        self.width_input.setValidator(QIntValidator(1, 2000))
        input_layout.addRow(width_label, self.width_input)

        height_label = QLabel("Altura:")
        self.height_input = QLineEdit()
        self.height_input.setText("1000")  # Set default value
        self.height_input.setValidator(QIntValidator(1, 2000))
        input_layout.addRow(height_label, self.height_input)

        max_iter_label = QLabel("Max Iterações:")
        self.max_iter_input = QLineEdit()
        self.max_iter_input.setText("20")  # Set default value
        self.max_iter_input.setValidator(QIntValidator(1, 2000))
        input_layout.addRow(max_iter_label, self.max_iter_input)

        main_layout.addLayout(input_layout)

        # Label para mostrar o tempo de execução
        self.execution_time_label = QLabel("")
        self.execution_time_label.setAlignment(Qt.AlignCenter)
        self.execution_time_label.setStyleSheet("font-size: 12px; font-style: italic;")
        main_layout.addWidget(self.execution_time_label)

        # Botão "Gerar Fractal"
        self.button_label_text = "Gerar Fractal"
        self.gerar_fractal_button = QPushButton(self.button_label_text)
        self.gerar_fractal_button.clicked.connect(self.gerar_fractal)
        self.gerar_fractal_button.setStyleSheet("font-size: 18px; font-weight: bold;")
        main_layout.addWidget(self.gerar_fractal_button)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def gerar_fractal(self):
        print(type(c_functions))
        print("Gerando fractal")

        start_time = time.time()
        width = min(int(self.width_input.text()), 2000)
        height = min(int(self.height_input.text()), 2000)
        max_iter = min(int(self.max_iter_input.text()), 2000)

        print(f"width: {width}, height: {height}, max_iter: {max_iter}")
        generate_in_c(width, height, max_iter)
        end_time = time.time()

        execution_time = end_time - start_time
        self.execution_time_label.setText(f"Tempo de execução: {execution_time:.2f} segundos")

        print(f"Tempo de execução: {execution_time} segundos")
        print("Fractal gerado com sucesso!")

        # Abrir imagem gerada em uma nova janela
        self.image_window = ImageWindow("mandelbrot.ppm")
        self.image_window.show()