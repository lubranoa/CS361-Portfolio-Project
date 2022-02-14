# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361
# Last Modified: 02/10/2022
# Description:
# -----------------------------------------------------------------------------


import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFrame, QLabel,
                             QHBoxLayout, QVBoxLayout, QCheckBox,
                             QPushButton, QLineEdit, QSlider, QSpinBox,
                             QSpacerItem, QSizePolicy)
from PyQt5.QtCore import Qt


class PasswordGenUI(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        main_layout = QHBoxLayout(self)

    # -------------------------------------------------------------------------
    # Left Layout of Application
    #
    # Will contain the password generation options and button followed by the
    # passphrase generation options and button.
    # ------------------------------------------------------------------------=

        # Init left layout of main layout
        left_layout = QVBoxLayout(self)

        left_layout.addWidget(QLabel('Generate a Password:'))

        # Add a horizontal layout to hold a password length slider and spin box
        # with labels
        length_layout = QHBoxLayout(self)
        length_layout.addWidget(QLabel('Length'))
        len_spinbox = QSpinBox(self)
        length_layout.addWidget(len_spinbox)
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
        left_layout.addWidget(QPushButton('Generate Password'))

        left_layout.addWidget(QLabel('Generate Passphrase:'))

        num_words_layout = QHBoxLayout(self)
        num_words_layout.addWidget(QLabel('Number of Words'))
        phrase_spinbox = QSpinBox(self)
        num_words_layout.addWidget(phrase_spinbox)
        num_words_layout.addWidget(QLabel('2'))
        phrase_slider = QSlider(self)
        phrase_slider.setOrientation(Qt.Horizontal)
        phrase_slider.setMinimum(2)
        phrase_slider.setMaximum(8)
        num_words_layout.addWidget(phrase_slider)
        num_words_layout.addWidget(QLabel('8'))
        left_layout.addLayout(num_words_layout)

        sep_char_layout = QHBoxLayout(self)
        sep_char_layout.addWidget(QLabel('Separator Character:'))
        sep_char_layout.addWidget(QLineEdit(self))
        left_layout.addLayout(sep_char_layout)

        left_layout.addWidget(QCheckBox('Include a number'))

        left_layout.addWidget(QPushButton('Generate Passphrase'))

    # -------------------------------------------------------------------------
    # Left Layout of Application
    #
    # Will contain the password generation options and button followed by the
    # passphrase generation options and button.
    # ------------------------------------------------------------------------=

        # Init right layout of main layout
        right_layout = QVBoxLayout(self)

        # Add widgets to the password output box of the application
        top_right_box = QVBoxLayout(self)
        top_right_box.addWidget(QLabel('Password Output:'))
        top_right_box.addWidget(QLineEdit(self))
        copy_layout = QHBoxLayout(self)
        copy_layout.addWidget(QPushButton('Copy'))
        copy_layout.addWidget(QPushButton('Clear'))
        top_right_box.addLayout(copy_layout)

        # Add widgets to the strength tester box of the application
        bottom_right_box = QVBoxLayout(self)
        bottom_right_box.addWidget(QLabel('Test Password Strength:'))
        enter_layout = QHBoxLayout(self)
        enter_layout.addWidget(QLabel('Enter Password:'))
        enter_layout.addWidget(QLineEdit())
        bottom_right_box.addLayout(enter_layout)
        bottom_right_box.addWidget(QPushButton('Calculate'))

        strength_layout = QHBoxLayout(self)
        strength_layout.addWidget(QLabel('Strength:'))
        strength_layout.addWidget(QLineEdit(self))
        bottom_right_box.addLayout(strength_layout)

        t2crack_layout = QHBoxLayout(self)
        t2crack_layout.addWidget(QLabel('Time to Crack:'))
        t2crack_layout.addWidget(QLineEdit(self))
        bottom_right_box.addLayout(t2crack_layout)

        # Add the two inner right boxes to the right layout of the main layout
        # and separated by a horizontal line
        right_layout.addLayout(top_right_box)
        horiz_split = QFrame(self)
        horiz_split.setFrameShape(QFrame.HLine)
        horiz_split.setFrameShadow(QFrame.Sunken)
        right_layout.addWidget(horiz_split)
        right_layout.addLayout(bottom_right_box)

        # Add the left and right layouts to the main layout separated by a
        # vertical line and padded by vertical spacers on each side
        left_spacer1 = QSpacerItem(10, 20, QSizePolicy.Minimum,
                                   QSizePolicy.Expanding)
        main_layout.addItem(left_spacer1)
        main_layout.addLayout(left_layout)
        verti_split = QFrame(self)
        verti_split.setFrameShape(QFrame.VLine)
        verti_split.setFrameShadow(QFrame.Sunken)
        left_spacer2 = QSpacerItem(10, 20, QSizePolicy.Minimum,
                                   QSizePolicy.Expanding)
        main_layout.addItem(left_spacer2)
        main_layout.addWidget(verti_split)
        right_spacer1 = QSpacerItem(10, 20, QSizePolicy.Minimum,
                                    QSizePolicy.Expanding)
        main_layout.addItem(right_spacer1)
        main_layout.addLayout(right_layout)
        right_spacer2 = QSpacerItem(10, 20, QSizePolicy.Minimum,
                                    QSizePolicy.Expanding)
        main_layout.addItem(right_spacer2)

        # Set the window layout to the main layout
        self.setLayout(main_layout)

        self.setGeometry(400, 400, 600, 550)
        self.setWindowTitle('Password Generator and Tester')
        self.show()


def main():

    app = QApplication(sys.argv)
    pw_gen = PasswordGenUI()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
