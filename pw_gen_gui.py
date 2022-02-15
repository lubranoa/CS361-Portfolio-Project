# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361
# Last Modified: 02/10/2022
# Description:
# -----------------------------------------------------------------------------


import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QLabel,
                               QHBoxLayout, QVBoxLayout, QCheckBox,
                               QPushButton, QLineEdit, QSlider, QSpinBox,
                               QSpacerItem, QSizePolicy, QButtonGroup)
from PySide6.QtCore import Qt


class PasswordGenUI(QWidget):

    def __init__(self):
        super().__init__()

        # self.setGeometry(400, 400, 700, 650)
        self.setWindowTitle('Password Generator and Tester')

        main_layout = QHBoxLayout(self)

    # -------------------------------------------------------------------------
    # Left Layout of Application
    #
    # Will contain the password generation options and button followed by the
    # passphrase generation options and button.
    # ------------------------------------------------------------------------=

        # Init left layout of main layout
        left_layout = QVBoxLayout(self)

        # Add a new <h3> header for the password section
        left_layout.addWidget(QLabel('<h3>Generate Password:</h3>', self))

        # Create a layout for choosing password length using a synced spin box
        # and slider with appropriate min and max labels
        length_layout = QHBoxLayout(self)
        length_layout.addWidget(QLabel('Length', self))
        self.len_spinbox = QSpinBox(self)
        self.len_spinbox.setRange(8, 20)
        length_layout.addWidget(self.len_spinbox)
        length_layout.addWidget(QLabel('8', self))
        self.len_slider = QSlider(Qt.Horizontal, self)
        self.len_slider.setRange(8, 20)
        length_layout.addWidget(self.len_slider)
        length_layout.addWidget(QLabel('20', self))
        # Connect the value changed signals to slots that synchronize the spin
        # box and slider values
        self.len_spinbox.valueChanged.connect(self.set_len_slider)
        self.len_slider.valueChanged.connect(self.set_len_spinbox)

        # Add the password length layout to the left layout
        left_layout.addLayout(length_layout)

        # Create 6 checkboxes and a label and add each to the left layout
        lowercase_chbx = QCheckBox('Include a - z', self)
        left_layout.addWidget(lowercase_chbx)
        uppercase_chbx = QCheckBox('Include A - Z', self)
        left_layout.addWidget(uppercase_chbx)
        digit_chbx = QCheckBox('Include 0 - 9', self)
        left_layout.addWidget(digit_chbx)
        left_layout.addWidget(QLabel('Advanced Options:', self))
        special_chbx = QCheckBox('Include !@#$%^&*', self)
        left_layout.addWidget(special_chbx)
        ambig_chbx = QCheckBox(
            'Exclude ambiguous characters i, l, I, L, 0, O, etc.', self)
        left_layout.addWidget(ambig_chbx)
        dup_chbx = QCheckBox('No duplicate characters', self)
        left_layout.addWidget(dup_chbx)

        # Create a button group and add all 6 checkboxes to it
        self.pword_chbxs = QButtonGroup(self)
        self.pword_chbxs.addButton(lowercase_chbx, 1)
        self.pword_chbxs.addButton(uppercase_chbx, 2)
        self.pword_chbxs.addButton(digit_chbx, 3)
        self.pword_chbxs.addButton(special_chbx, 4)
        self.pword_chbxs.addButton(ambig_chbx, 5)
        self.pword_chbxs.addButton(dup_chbx, 6)

        # Set the checkbox group to non-exclusive so that multiple boxes can
        # be checked at one time
        self.pword_chbxs.setExclusive(False)

        # Set lowercase and digit boxes to be checked by default
        lowercase_chbx.setChecked(True)
        digit_chbx.setChecked(True)

        # Create a "generate password" button, add it to the left layout, and
        # connect its "clicked" signal to the generate_pword slot
        pword_gen_btn = QPushButton('Generate Password', self)
        left_layout.addWidget(pword_gen_btn)
        pword_gen_btn.clicked.connect(self.generate_pword)

        # Add a new <h3> header for the passphrase section
        left_layout.addWidget(QLabel('<h3>Generate Passphrase:</h3>', self))

        # Create a layout for choosing passphrase length using a synced spin
        # box and slider with appropriate min and max labels
        num_words_layout = QHBoxLayout(self)
        num_words_layout.addWidget(QLabel('Number of Words', self))
        self.pphrase_spinbox = QSpinBox(self)
        self.pphrase_spinbox.setRange(2, 8)
        num_words_layout.addWidget(self.pphrase_spinbox)
        num_words_layout.addWidget(QLabel('2', self))
        self.pphrase_slider = QSlider(Qt.Horizontal, self)
        self.pphrase_slider.setRange(2, 8)
        num_words_layout.addWidget(self.pphrase_slider)
        num_words_layout.addWidget(QLabel('8', self))
        left_layout.addLayout(num_words_layout)
        # Connect the value changed signals to slots that synchronize the spin
        # box and slider values
        self.pphrase_spinbox.valueChanged.connect(self.set_pphrase_slider)
        self.pphrase_slider.valueChanged.connect(self.set_pphrase_spinbox)

        # Create a layout for input of a separator character with a label and
        # an input line and add it to th left layout
        sep_char_layout = QHBoxLayout(self)
        sep_char_layout.addWidget(QLabel('Separator Character:', self))
        self.char_input = QLineEdit(self)
        self.char_input.setMaxLength(1)
        sep_char_layout.addWidget(self.char_input)
        left_layout.addLayout(sep_char_layout)

        # Create a checkbox that allows the user to include a number
        self.include_a_num = QCheckBox('Include a number', self)
        left_layout.addWidget(self.include_a_num)

        # Create a "generate passphrase" button, add it to the left layout, and
        # connect its "clicked" signal to the generate_pphrase slot
        self.pphrase_gen_btn = QPushButton('Generate Passphrase', self)
        left_layout.addWidget(self.pphrase_gen_btn)
        self.pphrase_gen_btn.clicked.connect(self.generate_pphrase)

    # -------------------------------------------------------------------------
    # Left Layout of Application
    #
    # Will contain the password generation options and button followed by the
    # passphrase generation options and button. Sliders and spin boxes in both
    # sections will change simultaneously.
    # ------------------------------------------------------------------------=

        # Init right layout of main layout
        right_layout = QVBoxLayout(self)

        # Add widgets to the password output box of the application
        top_right_box = QVBoxLayout(self)
        top_right_spacer = QSpacerItem(10, 20, QSizePolicy.Minimum,
                                       QSizePolicy.Expanding)
        top_right_box.addItem(top_right_spacer)
        top_right_box.addWidget(QLabel('<h3>Password Output:</h3>', self))
        top_right_box.addItem(top_right_spacer)

        self.output_line = QLineEdit(self)
        self.output_line.setReadOnly(True)
        top_right_box.addWidget(self.output_line)
        top_right_box.addItem(top_right_spacer)

        copy_layout = QHBoxLayout(self)
        self.copy_btn = QPushButton('Copy', self)
        copy_layout.addWidget(self.copy_btn)
        self.calc_output_btn = QPushButton('Calculate Strength')
        copy_layout.addWidget(self.calc_output_btn)
        self.clear_btn = QPushButton('Clear', self)
        copy_layout.addWidget(self.clear_btn)

        top_right_box.addLayout(copy_layout)
        top_right_box.addItem(top_right_spacer)

        # Add widgets to the strength tester box of the application
        bottom_right_box = QVBoxLayout(self)
        bott_right_spacer = QSpacerItem(10, 20, QSizePolicy.Minimum,
                                        QSizePolicy.Expanding)
        bottom_right_box.addItem(bott_right_spacer)

        bottom_right_box.addWidget(
            QLabel('<h3>Test Password Strength:</h3>', self))

        bottom_right_box.addItem(bott_right_spacer)

        enter_layout = QHBoxLayout(self)

        self.strength_input = QLineEdit(self)
        self.strength_input.setPlaceholderText('Enter password here')
        enter_layout.addWidget(self.strength_input)
        bottom_right_box.addLayout(enter_layout)

        self.calc_stren_btn = QPushButton('Calculate Strength', self)
        bottom_right_box.addWidget(self.calc_stren_btn)

        bottom_right_box.addItem(bott_right_spacer)

        strength_layout = QHBoxLayout(self)
        strength_layout.addWidget(QLabel('Est. Strength:', self))
        self.strength_output = QLineEdit(self)
        self.strength_output.setReadOnly(True)
        strength_layout.addWidget(self.strength_output)
        bottom_right_box.addLayout(strength_layout)

        t2crack_layout = QHBoxLayout(self)
        t2crack_layout.addWidget(QLabel('Time to Crack:', self))
        self.t2crack_output = QLineEdit(self)
        self.t2crack_output.setReadOnly(True)
        t2crack_layout.addWidget(self.t2crack_output)
        bottom_right_box.addLayout(t2crack_layout)

        bottom_right_box.addItem(bott_right_spacer)

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
        main_layout.addItem(
            QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        main_layout.addLayout(left_layout)
        verti_split = QFrame(self)
        verti_split.setFrameShape(QFrame.VLine)
        verti_split.setFrameShadow(QFrame.Sunken)
        main_layout.addItem(
            QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        main_layout.addWidget(verti_split)
        main_layout.addItem(
            QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        main_layout.addLayout(right_layout)
        main_layout.addItem(
            QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Set the window layout to the main layout
        self.setLayout(main_layout)

    def set_len_spinbox(self):
        self.len_spinbox.setValue(self.len_slider.value())

    def set_len_slider(self):
        self.len_slider.setValue(self.len_spinbox.value())

    def set_pphrase_spinbox(self):
        self.pphrase_spinbox.setValue(self.pphrase_slider.value())

    def set_pphrase_slider(self):
        self.pphrase_slider.setValue(self.pphrase_spinbox.value())

    def generate_pword(self):

        pword_params = [0 for x in range(7)]

        for i in range(len(pword_params)):
            if i == 0:
                pword_params[i] = self.len_slider.value()
            else:
                curr_chbx = self.pword_chbxs.button(i)
                if curr_chbx.isChecked():
                    pword_params[i] = 1
        print('Password parameters:', pword_params)
        self.output_line.setText('h5fip2gt')

    def generate_pphrase(self):

        pphrase_params = [0 for x in range(3)]

        pphrase_params[0] = self.pphrase_slider.value()
        pphrase_params[1] = self.char_input.text()
        if self.include_a_num.isChecked():
            pphrase_params[2] = 1

        print('Passphrase Parameters:', pphrase_params)
        self.output_line.setText('words#7are#fun')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    pw_gen = PasswordGenUI()
    pw_gen.resize(750, 700)
    pw_gen.show()

    sys.exit(app.exec())
