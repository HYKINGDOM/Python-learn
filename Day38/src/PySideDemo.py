from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("PySide6 App")
button = QPushButton("Click Me", window)
window.setCentralWidget(button)
window.show()
sys.exit(app.exec())