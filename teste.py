# test_pyqt.py
import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel('Olá, PyQt!')
label.show()
sys.exit(app.exec_())