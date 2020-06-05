import hashlib
import base64
import sys
from PyQt5 import QtWidgets, uic

qtCreatorFile = "CryptoPass.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QDialog, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.secretkey.textChanged.connect(self.Password_update)
        self.username.textChanged.connect(self.Password_update)
        self.website.textChanged.connect(self.Password_update)

    def Password_update(self):
        test = base64.b64encode(hashlib.pbkdf2_hmac('sha256', str.encode(self.secretkey.text()), str.encode(self.username.text() + '@' + self.website.text()), 5000))[:25]
        self.password.setText((test).decode())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
