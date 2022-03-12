# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/27/2022
# Description:
#
# -----------------------------------------------------------------------------


import sys
import qtawesome as qta
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QLabel,
                               QHBoxLayout, QVBoxLayout, QCheckBox,
                               QPushButton, QLineEdit, QSlider, QSpinBox,
                               QSpacerItem, QSizePolicy, QButtonGroup,
                               QMessageBox, QStyle)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon
from password_gen import generate_password
# from passphrase_gen import generate_passphrase
# from get_words_client import close_word_gen_server_conn
# from get_strength_client import get_strength


class PasswordGenUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Password Generator and Tester')

        main_layout = QHBoxLayout(self)

    # -------------------------------------------------------------------------
    # Left Layout of Application
    #
    # Will contain the password generation options and button followed by the
    # passphrase generation options and button.
    # -------------------------------------------------------------------------

        # Init left layout of main layout
        left_layout = QVBoxLayout(self)

        # Add a new <h3> header for the password section
        SectionTitle(self, 'Generate Password:', left_layout)

        # Create a layout for choosing password length using a synced spin box
        # and slider with appropriate min and max labels
        length_layout = QHBoxLayout(self)
        length_layout.addSpacing(15)
        length_layout.addWidget(QLabel('Length', self))
        length_layout.addSpacing(5)
        self.len_spinbox = QSpinBox(self)
        self.len_spinbox.setRange(8, 30)
        length_layout.addWidget(self.len_spinbox)
        length_layout.addSpacing(10)
        length_layout.addWidget(QLabel('<h4>8</h4>', self))
        length_layout.addSpacing(5)
        self.len_slider = QSlider(Qt.Horizontal, self)
        self.len_slider.setRange(8, 30)
        self.len_slider.setTickInterval(2)
        self.len_slider.setTickPosition(self.len_slider.TicksBelow)
        length_layout.addWidget(self.len_slider)
        length_layout.addSpacing(5)
        length_layout.addWidget(QLabel('<h4>30</h4>', self))
        # Connect the value changed signals to slots that synchronize the spin
        # box and slider values
        self.len_spinbox.valueChanged.connect(self.set_len_slider)
        self.len_slider.valueChanged.connect(self.set_len_spinbox)
        self.len_slider.setValue(12)

        # Add the password length layout to the left layout
        left_layout.addLayout(length_layout)

        # Create 6 checkboxes and a label and add each to the left layout
        chbox_horiz_1 = QHBoxLayout(self)
        chbox_vert_1 = QVBoxLayout(self)
        self.lower_chbx = AppCheckbox(self, 'Include a - z', chbox_vert_1)
        self.upper_chbx = AppCheckbox(self, 'Include A - Z', chbox_vert_1)
        self.digit_chbx = AppCheckbox(self, 'Include 0 - 9', chbox_vert_1)
        self.spec_chbx = AppCheckbox(self, 'Include !@#$%^&&*', chbox_vert_1)
        chbox_horiz_1.addSpacing(15)
        chbox_horiz_1.addLayout(chbox_vert_1)
        chbox_horiz_1.addSpacing(150)
        left_layout.addLayout(chbox_horiz_1)

        left_layout.addWidget(QLabel('<h4>Advanced Options:</h4>', self))

        chbox_horiz_2 = QHBoxLayout(self)
        chbox_vert_2 = QVBoxLayout(self)
        ambig_chbx = AppCheckbox(self, 'Exclude ambiguous characters 1, l, I, 0, O, etc.', chbox_vert_2)
        dup_chbx = AppCheckbox(self, 'No duplicate characters', chbox_vert_2)

        min_num_layout = QHBoxLayout(self)
        min_num_layout.addWidget(QLabel('Minimum Numbers', self))
        min_num_layout.addSpacing(15)
        self.min_num_spin = QSpinBox(self)
        self.min_num_spin.setRange(0, 9)
        min_num_layout.addWidget(self.min_num_spin)
        min_num_layout.addSpacing(150)
        chbox_vert_2.addLayout(min_num_layout)

        min_spec_layout = QHBoxLayout(self)
        min_spec_layout.addWidget(QLabel('Minimum Special', self))
        min_spec_layout.addSpacing(27)
        self.min_spec_spin = QSpinBox(self)
        self.min_spec_spin.setRange(0, 9)
        min_spec_layout.addWidget(self.min_spec_spin)
        min_spec_layout.addSpacing(150)
        chbox_vert_2.addLayout(min_spec_layout)

        chbox_horiz_2.addSpacing(15)
        chbox_horiz_2.addLayout(chbox_vert_2)
        left_layout.addLayout(chbox_horiz_2)

        # Create a button group and add all 6 checkboxes to it
        self.pword_chbxs = QButtonGroup(self)
        self.pword_chbxs.addButton(self.lower_chbx.chbx, 1)
        self.pword_chbxs.addButton(self.upper_chbx.chbx, 2)
        self.pword_chbxs.addButton(self.digit_chbx.chbx, 3)
        self.pword_chbxs.addButton(self.spec_chbx.chbx, 4)
        self.pword_chbxs.addButton(ambig_chbx.chbx, 5)
        self.pword_chbxs.addButton(dup_chbx.chbx, 6)

        # Set the checkbox group to non-exclusive so that multiple boxes can
        # be checked at one time
        self.pword_chbxs.setExclusive(False)

        # Set lowercase and digit boxes to be checked by default
        self.lower_chbx.chbx.setChecked(True)
        self.digit_chbx.chbx.setChecked(True)

        left_layout.addSpacing(25)

        # Create a "generate password" button, add it to the left layout, and
        # connect its "clicked" signal to the generate_pword slot
        pword_gen_layout = QHBoxLayout(self)
        pword_gen_layout.addSpacing(90)
        AppButton(self, 'Generate Password', self.get_pword, pword_gen_layout)
        pword_gen_layout.addSpacing(90)
        left_layout.addLayout(pword_gen_layout)
        left_layout.addSpacing(30)

        # Add a new <h3> header for the passphrase section
        SectionTitle(self, 'Generate Passphrase:', left_layout)

        # Create a layout for choosing passphrase length using a synced spin
        # box and slider with appropriate min and max labels
        num_words_layout = QHBoxLayout(self)
        num_words_layout.addSpacing(15)
        num_words_layout.addWidget(QLabel('Number of Words', self))
        num_words_layout.addSpacing(5)
        self.pphrase_spinbox = QSpinBox(self)
        self.pphrase_spinbox.setRange(2, 8)
        num_words_layout.addWidget(self.pphrase_spinbox)
        num_words_layout.addSpacing(10)
        num_words_layout.addWidget(QLabel('2', self))
        num_words_layout.addSpacing(5)
        self.pphrase_slider = QSlider(Qt.Horizontal, self)
        self.pphrase_slider.setRange(2, 8)
        num_words_layout.addWidget(self.pphrase_slider)
        num_words_layout.addSpacing(5)
        num_words_layout.addWidget(QLabel('8', self))
        left_layout.addLayout(num_words_layout)
        # Connect the value changed signals to slots that synchronize the spin
        # box and slider values
        self.pphrase_spinbox.valueChanged.connect(self.set_pphrase_slider)
        self.pphrase_slider.valueChanged.connect(self.set_pphrase_spinbox)
        self.pphrase_slider.setValue(3)
        self.pphrase_slider.setTickInterval(1)
        self.pphrase_slider.setTickPosition(self.pphrase_slider.TicksBelow)

        # Create a layout for input of a separator character with a label and
        # an input line and add it to th left layout
        sep_char_layout = QHBoxLayout(self)
        sep_char_layout.addSpacing(15)
        sep_char_layout.addWidget(QLabel('Separator Character:', self))
        sep_char_layout.addSpacing(10)
        self.char_input = QLineEdit(self)
        self.char_input.setMaxLength(1)
        self.char_input.setPlaceholderText('!@#$%^&* Recommended')
        sep_char_layout.addWidget(self.char_input)
        sep_char_layout.addSpacing(45)
        left_layout.addLayout(sep_char_layout)

        chbox_horiz_3 = QHBoxLayout(self)
        chbox_vert_3 = QVBoxLayout(self)
        # Create a checkbox that allows the user to include a number
        self.include_a_num = QCheckBox('Include a number', self)
        chbox_vert_3.addWidget(self.include_a_num)
        # Create a checkbox that allows the user to capitalize the words
        self.capital_words = QCheckBox('Capitalize words', self)
        chbox_vert_3.addWidget(self.capital_words)
        chbox_horiz_3.addSpacing(15)
        chbox_horiz_3.addLayout(chbox_vert_3)
        left_layout.addLayout(chbox_horiz_3)
        left_layout.addSpacing(25)

        # Create a "generate passphrase" button, add it to the left layout, and
        # connect its "clicked" signal to the generate_pphrase slot
        pphrase_gen_layout = QHBoxLayout(self)
        pphrase_gen_layout.addSpacing(100)
        pphrase_btn = AppButton(self, 'Generate Passphrase',
                                self.get_pphrase, pphrase_gen_layout)
        pphrase_gen_layout.addSpacing(100)
        left_layout.addLayout(pphrase_gen_layout)
        left_layout.addSpacing(25)

    # -------------------------------------------------------------------------
    # Right Layout of Application
    #
    # Will contain the password generator output line with copy, calculate
    # strength, and clear buttons, followed by the password strength tester
    # section with an input box, a "calculate strength" button and two output
    # boxes for displaying the strength and time to crack.
    # -------------------------------------------------------------------------

        # Init right layout of main layout
        right_layout = QVBoxLayout(self)
        right_spacer = QSpacerItem(10, 20, QSizePolicy.Minimum,
                                   QSizePolicy.Expanding)

        # Create a top right box containing the password generator output. Each
        # widget has a spacer between it and the next widget
        top_right_box = QVBoxLayout(self)

        # Add spacers and a new <h3> header for the ouput section
        top_right_box.addItem(right_spacer)
        SectionTitle(self, 'Password Output:', top_right_box)
        top_right_box.addItem(right_spacer)

        # Create and add a read-only output line to the top right box
        self.output_line = QLineEdit(self)
        self.output_line.setReadOnly(True)
        top_right_box.addWidget(self.output_line)
        top_right_box.addSpacing(10)

        # Create and add a button layout with 3 buttons, copy, calculate
        # strength, and clear buttons
        output_btn_layout = QHBoxLayout(self)
        copy_btn = AppButton(self, 'Copy', self.copy_output, output_btn_layout)
        calc_out_btn = AppButton(self, 'Calculate Strength',
                                 self.calc_output_strength, output_btn_layout)
        clear_btn = AppButton(self, 'Clear',
                              self.clear_output, output_btn_layout)

        top_right_box.addLayout(output_btn_layout)
        top_right_box.addSpacing(25)
        top_right_box.addItem(right_spacer)

        # Create a bottom right box holding the password strength output. Each
        # widget has a spacer between it and the next widget
        bottom_right_box = QVBoxLayout(self)

        # Add spacers and a new <h3> header for the strength tester section
        bottom_right_box.addItem(right_spacer)
        SectionTitle(self, 'Test Password Strength:', bottom_right_box)
        bottom_right_box.addItem(right_spacer)

        # Create and add a password input line to bottom right box
        self.strength_input = QLineEdit(self)
        self.strength_input.setPlaceholderText('Enter password here')
        bottom_right_box.addWidget(self.strength_input)
        #bottom_right_box.addSpacing(25)
        bottom_right_box.addItem(right_spacer)

        # Create and add a "Calculate Strength" button
        calc_stren_layout = QHBoxLayout(self)
        calc_stren_layout.addSpacing(100)
        # Change None to self.test_strength later
        calc_stren_btn = AppButton(self, 'Calculate Strength',
                                   None, calc_stren_layout)
        calc_stren_layout.addSpacing(100)
        bottom_right_box.addLayout(calc_stren_layout)
        bottom_right_box.addSpacing(25)
        bottom_right_box.addItem(right_spacer)

        # Create and add a read-only strength output line to bottom right box
        strength_layout = QHBoxLayout(self)
        strength_layout.addWidget(QLabel('Strength Score:', self))
        self.strength_output = QLineEdit(self)
        self.strength_output.setReadOnly(True)
        strength_layout.addWidget(self.strength_output)
        bottom_right_box.addLayout(strength_layout)
        bottom_right_box.addSpacing(15)

        # Create and add a read-only time to crack output to bottom right box
        t2crack_layout = QHBoxLayout(self)
        t2crack_layout.addWidget(QLabel('Est. Time to Crack:', self))
        self.t2crack_output = QLineEdit(self)
        self.t2crack_output.setReadOnly(True)
        t2crack_layout.addWidget(self.t2crack_output)
        bottom_right_box.addLayout(t2crack_layout)
        bottom_right_box.addSpacing(25)
        bottom_right_box.addItem(right_spacer)

        clear_stren_layout = QHBoxLayout(self)
        clear_stren_layout.addSpacing(100)
        clear_stren_btn = AppButton(self, 'Clear Strength Fields',
                                    self.clear_strength, clear_stren_layout)
        clear_stren_layout.addSpacing(100)
        bottom_right_box.addLayout(clear_stren_layout)
        bottom_right_box.addItem(right_spacer)

        # Add the two inner right boxes to the right layout of the main layout
        # and separated by a horizontal line
        right_layout.addLayout(top_right_box)
        horiz_split = QFrame(self)
        horiz_split.setFrameShape(QFrame.HLine)
        horiz_split.setFrameShadow(QFrame.Sunken)
        right_layout.addWidget(horiz_split)
        right_layout.addLayout(bottom_right_box)
        right_layout.addSpacing(25)

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

    # TODO: Add "are you sure you want to quit?" popup

    # TODO: Add "are you sure you want to clear the output?" popup

    # TODO: Add "are you sure you want to clear the strength output?" popup

    # TODO: Add tooltips to customization options

    # TODO: Add help or info to menu bar

    def set_len_spinbox(self):
        """
        When signaled by a change in the password length slider's value,
        updates the value of the password length spin box
        """
        self.len_spinbox.setValue(self.len_slider.value())

    def set_len_slider(self):
        """
        When signaled by a change in the password length spin box's value,
        updates the value of the password length slider
        """
        self.len_slider.setValue(self.len_spinbox.value())

    def set_pphrase_spinbox(self):
        """
        When signaled by a change in the passphrase length slider's value,
        updates the value of the passphrase length spin box
        """
        self.pphrase_spinbox.setValue(self.pphrase_slider.value())

    def set_pphrase_slider(self):
        """
        When signaled by a change in the passphrase length spin box's value,
        updates the value of the passphrase length slider
        """
        self.pphrase_slider.setValue(self.pphrase_spinbox.value())

    def update_len_from_min_nums(self):
        """Does this"""
        pass

    def update_len_from_min_spec(self):
        """Does this"""
        pass

    def get_pword(self):
        """
        Will pass collected parameters to a microservice that will generate a
        password and return it to this function

        Displays it to the user in the designated output box
        """

        params = ['len', 'low_case', 'upp_case', 'digits', 'special',
                  'no_ambig', 'no_dup', 'min_dig', 'min_spec']
        pword_params = {}

        for i in range(len(params)):
            if i == 0:
                pword_params[params[i]] = self.len_slider.value()
            elif i < 7:
                curr_chbx = self.pword_chbxs.button(i)
                pword_params[params[i]] = curr_chbx.isChecked()
            elif i == 7:
                pword_params[params[i]] = self.min_num_spin.value()
            else:
                pword_params[params[i]] = self.min_spec_spin.value()

        print('Generating a password with these parameters:')
        [print(x + ':', pword_params[x], end='   ') for x in pword_params]
        print('\n')
        self.output_line.setText(generate_password(pword_params))

    def get_pphrase(self):
        """
        Will pass collected parameters to a microservice that will generate a
        passphrase and return it to this function

        Displays it to the user in the designated output box
        """

        params = ['words', 'sep_char', 'incl_num', 'cap_words']
        pphrase_params = {params[0]: self.pphrase_slider.value(),
                          params[1]: self.char_input.text(),
                          params[2]: self.include_a_num.isChecked(),
                          params[3]: self.capital_words.isChecked()}

        print('Generating a passphrase with these parameters:')
        [print(x + ':', pphrase_params[x], end='   ') for x in pphrase_params]
        print('\n')
        #self.output_line.setText(generate_passphrase(pphrase_params))

    def copy_output(self):
        """Copies the generated output to the clipboard"""

        print('Password output copied to clipboard')
        self.output_line.selectAll()
        self.output_line.copy()
        self.output_line.deselect()

    def calc_output_strength(self):
        """
        Copy-pastes the generated output into the strength tester input then
        calls the test strength method to calculate the output
        """
        print('Testing from password output')
        self.strength_input.setText(self.output_line.text())
        self.test_strength()

    def clear_output(self):
        """Clears the generated output from the output line"""
        print('Password output cleared')
        self.output_line.clear()

    def test_strength(self):
        """
        Calls a microservice that will calculate and returen password
        strength data
        """
        print('Testing this password:', self.strength_input.text())
        #result = get_strength(self.strength_input.text())
        #self.strength_output.setText(result[0])
        #self.t2crack_output.setText(result[1])

    def clear_strength(self):
        """Clears all text fields in the strength tester section"""
        print('Strength input and outputs cleared')
        self.strength_input.clear()
        self.strength_output.clear()
        self.t2crack_output.clear()

    def closeEvent(self, event):
        """
        Generate 'Are you sure you want to quit?' dialog box on user clicking
        'X' button in title bar.

        Message box includes a question, "close" button, and "cancel" button.

        """
        reply = QMessageBox.question(self,
                                     "Message",
                                     "Are you sure you want to quit?",
                                     QMessageBox.Close | QMessageBox.Cancel)

        if reply == QMessageBox.Close:
            #close_word_gen_server_conn()
            event.accept()
        else:
            event.ignore()


class InfoIcon(QWidget):
    """"""
    def __init__(self, parent=None):
        super(InfoIcon, self).__init__(parent)
        pixmapi = QStyle.SP_MessageBoxInformation
        icon_pixmap = self.style().standardIcon(pixmapi)
        self.icon_label = QLabel(parent)
        self.icon_label.setPixmap(icon_pixmap.pixmap(QSize(14, 14)))
        self.icon_label.setObjectName('info-icon')


class SectionTitle(QWidget):
    """"""
    def __init__(self, parent=None, text='Untitled', layout=None):
        super(SectionTitle, self).__init__(parent)
        title_layout = QHBoxLayout(parent)
        self.info_icon = InfoIcon(parent)
        title_layout.addWidget(self.info_icon.icon_label)
        title_layout.addWidget(QLabel('<h3>' + text + '</h3>', parent))
        title_layout.addSpacing(200)
        layout.addLayout(title_layout)


class AppCheckbox(QWidget):
    """
    Custom QT Widget that creates a QCheckbox with text and an icon, and adds
    it to a layout.

    AppButton(parent, text, on_click, layout)
        - parent: parent widget
        - text: the display text of the button (string)
        - layout: the QT layout that the object button should be added to
    """
    def __init__(self, parent=None, text=None, layout=None):
        super(AppCheckbox, self).__init__(parent)
        self.chbx = QCheckBox(text, parent)
        chbx_layout = QHBoxLayout(parent)
        chbx_layout.addWidget(self.chbx)
        layout.addLayout(chbx_layout)


class AppButton(QWidget):
    """
    Custom QT Widget that creates a QPushButton with text, connects a click
    signal event, and adds it to a layout.

    AppButton(parent, text, on_click, layout)
        - parent: parent widget
        - text: the display text of the button (string)
        - on_click: action that should happen on button click (class method)
        - layout: the QT layout that the object button should be added to
    """
    def __init__(self, parent=None, text='Click Me', on_click=None, layout=None):
        super(AppButton, self).__init__(parent)
        self.button = QPushButton(text, parent)
        self.button.clicked.connect(on_click)
        layout.addWidget(self.button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # TODO: Set up a style sheet for nicer UI
    pw_gen = PasswordGenUI()
    pw_gen.resize(750, 700)
    pw_gen.show()
    # Open the sqq styles file and read in the css-alike styling code
    with open('styles.qss', 'r') as f:
        style = f.read()
        # Set the stylesheet of the application
        app.setStyleSheet(style)
    sys.exit(app.exec())

