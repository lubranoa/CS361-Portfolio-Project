# Author: Alexander Lubrano
# Course: CS 361
# Last Modified: 02/10/2022
# Description:

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFrame, QLabel,
                             QHBoxLayout, QVBoxLayout, QCheckBox,
                             QPushButton, QLineEdit, QAbstractSlider,
                             QSlider, QSpinBox, QSpacerItem)
from PyQt5.QtCore import Qt


class PasswordGen(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        main_layout = QHBoxLayout(self)

        left_layout = QVBoxLayout(self)
        left_layout.addWidget(QLabel('Generate a Password:'))

    # Add a horizontal layout for password length slider with a labels
        length_layout = QHBoxLayout(self)
        length_layout.addWidget(QLabel('Length     '))
        length_layout.addWidget(QLabel('8'))
        len_slider = QSlider(self)
        len_slider.setOrientation(Qt.Horizontal)
        len_slider.setMinimum(8)
        len_slider.setMaximum(20)
        length_layout.addWidget(len_slider)
        length_layout.addWidget(QLabel('20'))
        left_layout.addLayout(length_layout)

        left_layout.addWidget(QCheckBox('Include a - z'))
        left_layout.addWidget(QCheckBox('Include A - Z'))
        left_layout.addWidget(QCheckBox('Include 0 - 9'))
        left_layout.addWidget(QCheckBox('Include !@#$%^&*'))
        left_layout.addWidget(QLabel('Advanced Options:'))
        left_layout.addWidget(QCheckBox(
            'Exclude ambiguous characters l, I, 0, O, etc.'))
        left_layout.addWidget(QCheckBox(
            'No duplicate characters'))

        right_layout = QVBoxLayout(self)

    # Add widgets to the password output box of the application
        top_right_box = QVBoxLayout(self)
        top_right_box.addWidget(QLabel('Password Output:'))
        top_right_box.addWidget(QPushButton('hello'))

    # Add widgets to the strength tester box of the application
        bottom_right_box = QVBoxLayout(self)
        bottom_right_box.addWidget(QLabel('Test Password Strength:'))
        bottom_right_box.addWidget(QPushButton('hello'))

    # Add the two inner right boxes to the right layout of the main layout and
    # separated by a horizontal line
        right_layout.addLayout(top_right_box)
        horiz_split = QFrame(self)
        horiz_split.setFrameShape(QFrame.HLine)
        horiz_split.setFrameShadow(QFrame.Sunken)
        right_layout.addWidget(horiz_split)
        right_layout.addLayout(bottom_right_box)

    # Add the left and right layouts to the main layout separated by a
    # vertical line
        main_layout.addLayout(left_layout)
        verti_split = QFrame(self)
        verti_split.setFrameShape(QFrame.VLine)
        verti_split.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(verti_split)
        main_layout.addLayout(right_layout)

    # Set the window layout to the main layout
        self.setLayout(main_layout)

        self.setGeometry(400, 400, 600, 550)
        self.setWindowTitle('Password Generator and Tester')
        self.show()


def main():

    app = QApplication(sys.argv)
    pw_gen = PasswordGen()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
