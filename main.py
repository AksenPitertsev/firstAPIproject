from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import io
from PIL import Image
from API_work import APIWork


class Main(QWidget):
    def __init__(self):
        super().__init__(windowTitle="Я карта")
        self.showMaximized()

        self.search = QLineEdit(self)
        self.layers = [
            QRadioButton("Схема"),
            QRadioButton("Спутник"),
            QRadioButton("Гибрид"),
        ]

        qimage = QImage()
        qimage.loadFromData(APIWork.get_map().read())
        pix = QPixmap.fromImage(qimage)
        self.map = QLabel()
        self.map.setPixmap(pix)

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.map)
        # hbox.addLayout(vbox)
        self.setLayout(vbox)


app = QApplication([])
ex = Main()
ex.show()
app.exec()
