# Author: Alexander Lubrano
# Course: CS 361
# Last Modified: 02/10/2022
# Description:

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFrame, QLabel,
                             QHBoxLayout, QVBoxLayout, QCheckBox,
                             QPushButton, QLineEdit, QAbstractSlider,
                             QSlider)
from PyQt5.QtCore import Qt


class PasswordGen(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        outer_box = QHBoxLayout(self)

        left_box = QVBoxLayout(self)
        left_box.addWidget(QLabel('Generate a Password:'))
        slider = QSlider(self)
        slider.setOrientation(Qt.Horizontal)
        left_box.addWidget(slider)

        left_box.addWidget(QPushButton('Two'))
        left_box.addWidget(QPushButton('Three'))
        left_box.addWidget(QPushButton('Four'))

        right_box = QVBoxLayout(self)

        top_right_box = QVBoxLayout(self)
        top_right_box.addWidget(QPushButton('hello'))

        bottom_right_box = QVBoxLayout(self)
        bottom_right_box.addWidget(QPushButton('hello'))

        right_box.addLayout(top_right_box)
        right_box.addLayout(bottom_right_box)

        outer_box.addLayout(left_box)
        outer_box.addLayout(right_box)

        self.setLayout(outer_box)

        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('Password Generator')
        self.show()


def main():

    app = QApplication(sys.argv)
    pw_gen = PasswordGen()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
