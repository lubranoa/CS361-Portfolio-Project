# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/27/2022
# Description:
#
# -----------------------------------------------------------------------------


import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QLabel,
                               QHBoxLayout, QVBoxLayout, QCheckBox,
                               QPushButton, QLineEdit, QSlider, QSpinBox,
                               QSpacerItem, QSizePolicy, QButtonGroup,
                               QMessageBox, QStyle, QToolTip)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QCursor
from password_gen import generate_password
from passphrase_gen import generate_passphrase
from get_words_client import close_word_gen_server_conn
from get_strength_client import get_strength

min_pw_len, max_pw_len = 8, 30
min_pph_len, max_pph_len = 2, 8

# Tooltip strings
increase_str = 'Can Increase Password Strength'
decrease_str = 'May Decrease Password Strength'


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

        pw_tooltip = 'Generate a password of a specified length with your \n' \
                     'choice of customization options. Generally, the more \n' \
                     'options you select, the more secure the password.'
        SectionTitle(self, 'Generate Password:', pw_tooltip, left_layout)

        self.pw_len_set = AppLengthSetter(self, 'Length', 'Character Length of Generated Password', min_pw_len, max_pw_len, 12, 2, left_layout)

        chbox_horiz_1 = QHBoxLayout(self)
        chbox_vert_1 = QVBoxLayout(self)
        self.lower_chbx = AppCheckbox(self, 'Include a - z', increase_str, chbox_vert_1)
        self.upper_chbx = AppCheckbox(self, 'Include A - Z', increase_str, chbox_vert_1)
        self.digit_chbx = AppCheckbox(self, 'Include 0 - 9', increase_str, chbox_vert_1)
        self.spec_chbx = AppCheckbox(self, 'Include !@#$%^&&*', increase_str, chbox_vert_1)
        chbox_horiz_1.addSpacing(15)
        chbox_horiz_1.addLayout(chbox_vert_1)
        chbox_horiz_1.addSpacing(150)
        left_layout.addLayout(chbox_horiz_1)

        left_layout.addWidget(QLabel('<h4>Advanced Options:</h4>', self))

        chbox_horiz_2 = QHBoxLayout(self)
        chbox_vert_2 = QVBoxLayout(self)
        ambig_chbx = AppCheckbox(self, 'Exclude ambiguous characters 1, l, I, 0, O, etc.', decrease_str, chbox_vert_2)
        dup_chbx = AppCheckbox(self, 'No duplicate characters', decrease_str, chbox_vert_2)

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

        self.pword_chbxs = QButtonGroup(self)
        self.pword_chbxs.addButton(self.lower_chbx.chbx, 1)
        self.pword_chbxs.addButton(self.upper_chbx.chbx, 2)
        self.pword_chbxs.addButton(self.digit_chbx.chbx, 3)
        self.pword_chbxs.addButton(self.spec_chbx.chbx, 4)
        self.pword_chbxs.addButton(ambig_chbx.chbx, 5)
        self.pword_chbxs.addButton(dup_chbx.chbx, 6)

        self.pword_chbxs.setExclusive(False)
        self.lower_chbx.chbx.setChecked(True)
        self.digit_chbx.chbx.setChecked(True)

        left_layout.addSpacing(25)

        pword_gen_layout = QHBoxLayout(self)
        pword_gen_layout.addSpacing(90)
        AppButton(self, 'Generate Password', 'Generate a New Password', self.get_pword, pword_gen_layout)
        pword_gen_layout.addSpacing(90)
        left_layout.addLayout(pword_gen_layout)
        left_layout.addSpacing(30)

        pph_tooltip = 'Generate a passhprase with a specified number of words \n' \
                      'and some customization options. Generally, the more \n' \
                      'options you select, the more secure the passphrase.'
        SectionTitle(self, 'Generate Passphrase:', pph_tooltip, left_layout)

        self.pph_len_set = AppLengthSetter(self, 'Word Amount:', 'Number of Words in Generated Passphrase', min_pph_len, max_pph_len, 3, 1, left_layout)

        sep_char_layout = QHBoxLayout(self)
        sep_char_layout.addSpacing(15)
        sep_char_layout.addWidget(QLabel('Separator Character:', self))
        sep_char_layout.addSpacing(10)
        self.char_input = QLineEdit(self)
        self.char_input.setMaxLength(1)
        self.char_input.setPlaceholderText('!@#$%^&* Recommended')
        sep_char_layout.addWidget(self.char_input)
        sep_char_layout.addSpacing(40)
        left_layout.addLayout(sep_char_layout)

        chbox_horiz_3 = QHBoxLayout(self)
        chbox_vert_3 = QVBoxLayout(self)
        # Create a checkbox that allows the user to include a number
        self.include_a_num = AppCheckbox(self, 'Include Number', increase_str, chbox_vert_3)
        # Create a checkbox that allows the user to capitalize the words
        self.capital_words = AppCheckbox(self, 'Capitalize words', increase_str, chbox_vert_3)
        chbox_horiz_3.addSpacing(15)
        chbox_horiz_3.addLayout(chbox_vert_3)
        left_layout.addLayout(chbox_horiz_3)
        left_layout.addSpacing(25)

        # Create a "generate passphrase" button, add it to the left layout, and
        # connect its "clicked" signal to the generate_pphrase slot
        pphrase_gen_layout = QHBoxLayout(self)
        pphrase_gen_layout.addSpacing(90)
        pphrase_btn = AppButton(self, 'Generate Passphrase', 'Generate a New Passphrase',
                                self.get_pphrase, pphrase_gen_layout)
        pphrase_gen_layout.addSpacing(90)
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
        output_tooltip = 'All generated passwords and passphrases will be output \n' \
                         'here. It can be copied and pasted into other programs \n' \
                         'like web browsers or password managers.'
        SectionTitle(self, 'Password Output:', output_tooltip, top_right_box)
        top_right_box.addItem(right_spacer)

        # Create and add a read-only output line to the top right box
        self.output_line = QLineEdit(self)
        self.output_line.setReadOnly(True)
        top_right_box.addWidget(self.output_line)
        top_right_box.addSpacing(10)

        # Create and add a button layout with 3 buttons, copy, calculate
        # strength, and clear buttons
        output_btn_layout = QHBoxLayout(self)
        copy_btn = AppButton(self, 'Copy', 'Copy Password', self.copy_output, output_btn_layout)
        calc_out_btn = AppButton(self, 'Calculate Strength', 'Calculate Password Strength',
                                 self.calc_output_strength, output_btn_layout)
        clear_btn = AppButton(self, 'Clear', 'Clear Password Output',
                              self.clear_output, output_btn_layout)

        top_right_box.addLayout(output_btn_layout)
        top_right_box.addSpacing(25)
        top_right_box.addItem(right_spacer)

        # Create a bottom right box holding the password strength output. Each
        # widget has a spacer between it and the next widget
        bottom_right_box = QVBoxLayout(self)

        # Add spacers and a new <h3> header for the strength tester section
        bottom_right_box.addItem(right_spacer)
        stren_tooltip = 'Test the generated passwords and passphrases as well as \n' \
                        'your own passwords here. This will tell you how strong it \n' \
                        'is and how long it would take to crack.'
        SectionTitle(self, 'Test Password Strength:', stren_tooltip, bottom_right_box)
        bottom_right_box.addItem(right_spacer)

        # Create and add a password input line to bottom right box
        self.strength_input = QLineEdit(self)
        self.strength_input.setPlaceholderText('Enter password here')
        bottom_right_box.addWidget(self.strength_input)
        #bottom_right_box.addSpacing(25)
        bottom_right_box.addItem(right_spacer)

        # Create and add a "Calculate Strength" button
        calc_stren_layout = QHBoxLayout(self)
        calc_stren_layout.addSpacing(90)
        # Change None to self.test_strength later
        calc_stren_btn = AppButton(self, 'Calculate Strength', 'Calculate Password Strength',
                                   self.test_strength, calc_stren_layout)
        calc_stren_layout.addSpacing(90)
        bottom_right_box.addLayout(calc_stren_layout)
        bottom_right_box.addSpacing(30)
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
        clear_stren_layout.addSpacing(90)
        clear_stren_btn = AppButton(self, 'Clear Strength Fields', 'Clear Strength Tester Output',
                                    self.clear_strength, clear_stren_layout)
        clear_stren_layout.addSpacing(90)
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
                pword_params[params[i]] = self.pw_len_set.get_value()
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
        pphrase_params = {params[0]: self.pph_len_set.get_value(),
                          params[1]: self.char_input.text(),
                          params[2]: self.include_a_num.chbx.isChecked(),
                          params[3]: self.capital_words.chbx.isChecked()}

        print('Generating a passphrase with these parameters:')
        [print(x + ':', pphrase_params[x], end='   ') for x in pphrase_params]
        print('\n')
        self.output_line.setText(generate_passphrase(pphrase_params))

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
        Calls a microservice that will calculate and return password
        strength data
        """
        print('Testing this password:', self.strength_input.text())
        result = get_strength(self.strength_input.text())
        self.strength_output.setText(result[0])
        self.t2crack_output.setText(result[1])

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
            close_word_gen_server_conn()
            event.accept()
        else:
            event.ignore()


class InfoIcon(QWidget):
    """
    Creates an instance of a label containing a pixmap of the default Qt info
    icon to be added into section titles
    """
    def __init__(self, parent=None, tooltip='Tooltip'):
        super(InfoIcon, self).__init__(parent)
        pixmapi = QStyle.SP_MessageBoxInformation
        icon_pixmap = self.style().standardIcon(pixmapi)
        self.label = QLabel(parent)
        self.label.setPixmap(icon_pixmap.pixmap(QSize(14, 14)))
        self.label.setAlignment(Qt.AlignRight)
        self.label.setObjectName('info-icon')
        self.label.setToolTip(tooltip)


class SectionTitle(QWidget):
    """
    Creates an instance of a section title with specified text and adds it to
    the specified layout
    """
    def __init__(self, parent=None, text='Untitled', tooltip='Tooltip', layout=None):
        super(SectionTitle, self).__init__(parent)
        title_lyt = QHBoxLayout(parent)
        title = QLabel(text, parent)
        title.setObjectName('section-title')
        title_lyt.addWidget(title)
        self.info_icon = InfoIcon(parent, tooltip)
        title_lyt.addWidget(self.info_icon.label)
        layout.addLayout(title_lyt)


class AppLengthSetter(QWidget):
    """
    Creates a custom length setter with a main label, min and max values, a
    starting value, a step value for ticks, then adds it to a specified layout

    Syncs the values of the slider and spinbox using private class methods

    Has a method to get the current value of the length setter widget
    """
    def __init__(self, parent=None, text='Untitled', tooltip='Tooltip', low=0, hi=100, init_val=0, tick_pos=0, layout=None):
        super(AppLengthSetter, self).__init__(parent)
        self.lyt = QHBoxLayout(parent)
        self.lyt.addSpacing(15)
        self.lyt.addWidget(QLabel(text, parent))
        self.lyt.addSpacing(5)
        # Create and add spinbox
        self._spinbox = QSpinBox(parent)
        self._spinbox.setRange(low, hi)
        self.lyt.addWidget(self._spinbox)
        self.lyt.addSpacing(10)
        # Create and add left slider label
        self.lyt.addWidget(QLabel('<h4>'+str(low)+'</h4>', parent))
        self.lyt.addSpacing(5)
        # Create and add slider with ticks
        self._slider = QSlider(Qt.Horizontal, parent)
        self._slider.setRange(low, hi)
        self._slider.setTickPosition(self._slider.TicksBelow)
        self._slider.setTickInterval(tick_pos)
        self.lyt.addWidget(self._slider)
        self.lyt.addSpacing(5)
        self.lyt.addWidget(QLabel('<h4>'+str(hi)+'</h4>', parent))
        self._spinbox.valueChanged.connect(self._set_slider_from_spinbox)
        self._slider.valueChanged.connect(self._set_spinbox_from_slider)
        self._slider.setValue(init_val)
        self._spinbox.setToolTip(tooltip)
        self._slider.setToolTip(tooltip)
        layout.addLayout(self.lyt)

    def _set_slider_from_spinbox(self):
        """"""
        self._slider.setValue(self._spinbox.value())

    def _set_spinbox_from_slider(self):
        """"""
        self._spinbox.setValue(self._slider.value())

    def get_value(self):
        """"""
        return self._slider.value()


class AppCheckbox(QWidget):
    """
    Custom QT Widget that creates a QCheckbox with specified text and adds
    it to a specified layout
    """
    def __init__(self, parent=None, text='Untitled', tooltip='Tooltip', layout=None):
        super(AppCheckbox, self).__init__(parent)
        self.chbx = QCheckBox(text, parent)
        self.chbx.setToolTip(tooltip)
        chbx_layout = QHBoxLayout(parent)
        chbx_layout.addWidget(self.chbx)
        layout.addLayout(chbx_layout)


class AppButton(QWidget):
    """
    Custom QT Widget that creates a QPushButton with text, connects a click
    signal event, and adds it to the specified layout
    """
    def __init__(self, parent=None, text='Click Me', tooltip='tooltip', on_click=None, layout=None):
        super(AppButton, self).__init__(parent)
        self.button = QPushButton(text, parent)
        self.button.clicked.connect(on_click)
        self.button.setToolTip(tooltip)
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
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

