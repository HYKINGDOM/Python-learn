from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("PyQt6 App")
window.setGeometry(100, 100, 300, 200)

button = QPushButton("Click Me", window)
button.setGeometry(100, 100, 100, 30)

window.show()
sys.exit(app.exec())