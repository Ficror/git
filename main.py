from random import randint

import sys
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QFileDialog


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        w = h = randint(10, 200)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(255, 255, 0))
        #pen.setColor(QColor(*[randint(0, 255) for i in range(3)]))
        painter.setPen(pen)
        painter.drawEllipse(100, 200, w, h)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
