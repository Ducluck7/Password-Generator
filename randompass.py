import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QVBoxLayout, QTextEdit, QSpinBox

class PasswordGenerator(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    # Create widgets
    self.lengthLabel = QLabel("Password Length:")
    self.lengthSpinBox = QSpinBox(self)
    self.lengthSpinBox.setRange(1, 99)
    self.lengthSpinBox.setValue(12)
    self.numbersCheckBox = QCheckBox("Include numbers")
    self.punctuationCheckBox = QCheckBox("Include punctuation")
    self.capsCheckBox = QCheckBox("Include capital letters")
    self.generateButton = QPushButton("Generate")
    self.passwordLabel = QLabel("")
    self.passwordEdit = QTextEdit(self)
    self.passwordEdit.setReadOnly(True)
    

    # Create layout and add widgets
    layout = QVBoxLayout(self)
    layout.addWidget(self.lengthLabel)
    layout.addWidget(self.lengthSpinBox)
    layout.addWidget(self.numbersCheckBox)
    layout.addWidget(self.punctuationCheckBox)
    layout.addWidget(self.capsCheckBox)
    layout.addWidget(self.generateButton)
    layout.addWidget(self.passwordLabel)
    layout.addWidget(self.passwordEdit)
    self.setLayout(layout)

    # Connect signal and slot
    self.generateButton.clicked.connect(self.generatePassword)

    # Set window properties
    self.setWindowTitle("Password Generator")
    self.setGeometry(300, 300, 300, 200)

  def generatePassword(self):
  # Get password length and options
    length_str = self.lengthSpinBox.text()
    length = int(length_str)
    include_numbers = self.numbersCheckBox.isChecked()
    include_punctuation = self.punctuationCheckBox.isChecked()
    include_caps = self.capsCheckBox.isChecked()

    # Generate password
    password_chars = ""
    if include_numbers:
      password_chars += string.digits
    if include_punctuation:
      password_chars += string.punctuation
    if include_caps:
      password_chars += string.ascii_uppercase
    password_chars += string.ascii_lowercase
    password = "".join(random.choices(password_chars, k=length))

    # Set password label text
    self.passwordEdit.setPlainText(password)

if __name__ == "__main__":
  app = QApplication([])
  generator = PasswordGenerator()
  generator.show()
  app.exec_()