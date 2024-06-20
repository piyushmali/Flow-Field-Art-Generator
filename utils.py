import numpy as np
from PyQt5.QtGui import QColor


def QColor_HSV(hue, sat, val, alpha=255):
    color = QColor()
    color.setHsv(int(hue), int(sat), int(val), int(alpha))
    return color


def save(painter, fname, folder=".", overwrite=True):
    path = f"{folder}/{fname}.png"
    painter.image.save(path, "PNG")


class Perlin2D:
    def __init__(self, width, height, factor_w, factor_h):
        self.width = width
        self.height = height
        self.factor_w = factor_w
        self.factor_h = factor_h
        self.data = self.generate_perlin_noise()

    def generate_perlin_noise(self):
        # Generate Perlin noise here; this is a placeholder implementation
        return np.random.rand(self.width, self.height)

    def __getitem__(self, indices):
        x, y = indices
        x = int(x * self.factor_w) % self.width
        y = int(y * self.factor_h) % self.height
        return self.data[x, y]
