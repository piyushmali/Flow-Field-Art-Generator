from PyQt5.QtGui import QPainter, QImage, QColor
from PyQt5.QtCore import Qt


class Painter(QPainter):
    def __init__(self, width, height):
        self.image = QImage(width, height, QImage.Format_ARGB32)
        self.image.fill(QColor(0, 0, 0))
        super().__init__(self.image)

    def save(self, fname, folder=".", overwrite=True):
        path = f"{folder}/{fname}.png"
        self.image.save(path, "PNG")
