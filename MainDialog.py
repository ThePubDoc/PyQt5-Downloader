from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QLabel


from urllib import request

class MainDialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()

        self.l1 = QLabel()
        self.l1.setText("Downloader")

        self.l2 = QLabel()
        self.l2.setText("Enter URL of file")


        self.edit_utl = QtWidgets.QLineEdit()

        self.l3 = QLabel()
        self.l3.setText("Select Output Folder")


        self.edit_path = QtWidgets.QLineEdit()

        self.browser = QtWidgets.QPushButton("Save As")

        self.progress = QtWidgets.QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.setValue(0)
        submit = QtWidgets.QPushButton("Start")

        submit.clicked.connect(self.submit_clicked)
        self.browser.clicked.connect(self.browse)

        layout.addWidget(self.l1)
        layout.addWidget(self.l2)
        layout.addWidget(self.edit_utl)
        layout.addWidget(self.l3)
        layout.addWidget(self.edit_path)
        layout.addWidget(self.browser)
        layout.addWidget(self.progress)
        layout.addWidget(submit)

        self.setLayout(layout)


    def submit_clicked(self):

        QtWidgets.QMessageBox.information(self,"Clicked","Successfull")

        path = self.edit_path.text()
        url = self.edit_utl.text()

        request.urlretrieve(url , path , self.handle)


    def browse(self):


        path , type = QtWidgets.QFileDialog.getSaveFileName(self , "Browser" , "File Locaton To Be Saved")
        self.edit_path.setText(path)


    def handle(self, index, frame, size):

        percent = index * frame *size / 100
        self.progress.setValue(int(percent))


