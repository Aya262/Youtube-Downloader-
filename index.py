import sys
import requests
import pytube

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import os
FORM_CLASS,_=loadUiType(os.path.join(os.path.dirname(__file__),'attempt1.ui'))

class MainApp(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_UI()
        self.pushButton_2.clicked.connect(self.handle_download_btn)
        self.pushButton.clicked.connect(self.handle_browser_btn)

    def handle_UI(self):
         self.setWindowTitle("Download App")
         self.setFixedSize(652,381)

    def handle_browser_btn(self):
        folder=QFileDialog.getExistingDirectory(self,'Select Folder')
        self.lineEdit_2.setText(folder)

    def handle_download_btn(self):
        url=self.lineEdit.text()
        save_location=self.lineEdit_2.text()
        yt_object=pytube.YouTube(url,on_progress_callback=self.handle_progress_bar)
        yt_object=yt_object.streams.first()
        yt_object.download(save_location)


        #r=requests.get(url,allow_redirects=True,stream=True)
        #total_size=int(r.headers['Content-Length'])
        #already_downloaded=0
        #with open(os.path.join(save_location,'Downloaded_file'),'wb') as f:
            #for chunk in r.iter_content(chunk_size=1024):
                #f.write(chunk)
                #already_downloaded+=len(chunk)
                #self.progressBar.setValue((already_downloaded/total_size)*100)

    def handle_progress_bar(self,stream,chunk,bytes_remining):
        total_size=stream.filesize
        percentage=((total_size-bytes_remining)/total_size)*100
        self.progressBar.setValue(percentage)



def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()
