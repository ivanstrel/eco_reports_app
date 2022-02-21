from utilites import converters
import sys
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QWidget
from qt_themes import breeze_theme

app = QApplication(sys.argv)

# Set Dark theme
file = QFile(":/dark/stylesheet.qss")
file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(file)
app.setStyleSheet(stream.readAll())

# All code goes here
w = QWidget()
w.resize(300, 300)
w.setWindowTitle("test")
w.show()
sys.exit(app.exec_())
