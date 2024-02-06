from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import io
from PIL import Image
from API_work import APIWork


class Main(QWidget):
    def __init__(self):
        super().__init__(windowTitle="Я карта")
        self.setGeometry(350, 150, 650, 450)

        # self.search = QLineEdit(self)
        self.layers = [
            QRadioButton("Схема"),
            QRadioButton("Спутник"),
            QRadioButton("Гибрид"),
        ]

        self.zoom = 12
        self.map = QLabel()
        self.zoom_map()

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        # vbox.addWidget(self.search)
        vbox.addWidget(self.map)
        # hbox.addLayout(vbox)
        self.setLayout(vbox)

    def keyPressEvent(self, e):
        if e.key() == 16777238 and self.zoom < 21:  # pgup
            self.zoom += 1
            self.zoom_map()
        elif e.key() == 16777239 and self.zoom != 0:  # pgdn
            self.zoom -= 1
            self.zoom_map()

    def zoom_map(self):
        qimage = QImage()
        qimage.loadFromData(APIWork.get_map(self.zoom).read())
        pix = QPixmap.fromImage(qimage)
        self.map.setPixmap(pix)


app = QApplication([])
ex = Main()
ex.show()
app.exec()
