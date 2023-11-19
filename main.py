from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import sys
import random


class YellowCircles(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.Init()

    def Init(self):
        self.setGeometry(821, 400, 621, 621)
        self.setFixedSize(533, 493)
        self.do_paint = False
        self.setWindowTitle('Yellow Circles')
        self.pushButton.clicked.connect(self.circle)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.run(qp)
            qp.end()
        self.do_paint = False

    def circle(self):
        self.do_paint = True
        self.update()

    def run(self, qp):
        x = random.randint(10, 500)
        y = random.randint(10, 300)
        w = random.randint(10, 100)
        h = w
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, w, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec_())
