from PyQt5 import QtWidgets

from MainDialog import MainDialog

app = QtWidgets.QApplication([])

dialog = MainDialog()

dialog.show()

app.exec_()