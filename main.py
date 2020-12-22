# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from lib.design import Ui_Dialog
from lib.logic import Main_logic

class CsFail(QThread):

    sig_for_start = pyqtSignal(list)
    # sig_for_break = pyqtSignal(int)

    def __init__(self, parent=None):

        QtCore.QThread.__init__(self, parent)
        self.csfailmain_logic = Main_logic()

    def status_of_what_do(self, status):
        self.status = status

    def status_for_break(self, isbreak):
        self.isbreak = isbreak

    def run(self):

        if self.status == "Start":
            for i in self.csfailmain_logic.load_last_game():
                if self.isbreak == 1:
                    break
                self.sig_for_start.emit(i)





class QthreadApp(QtWidgets.QWidget):

    sig_for_status = pyqtSignal(str)
    sig_for_sig_for_break = pyqtSignal(int)


    def __init__(self, parent=None):

        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        QtWidgets.QWidget.__init__(self, parent)
        self.Dialog.show()

        self.total_site_bank = []
        self.win_pr = []
        self.winn = []
        self.flag = 0
        self.last_game = 0
        self.pred_last = 0
        self.pred_last_last = 0


        self.csfailthread = CsFail()

        self.ui.pushButton.clicked.connect(self.start_load)
        self.ui.pushButton_2.clicked.connect(self.stop_load)

        sys.exit(self.app.exec_())

    def start_load(self):
        self.start_load_gif()
        self.sig_for_status.connect(self.csfailthread.status_of_what_do)
        self.sig_for_status.emit("Start")
        self.sig_for_sig_for_break.connect(self.csfailthread.status_for_break)
        self.sig_for_sig_for_break.emit(0)
        self.csfailthread.start()
        self.csfailthread.sig_for_start.connect(self.watch_it)

    def start_load_gif(self):
        self.ui.movie.start()

    def stop_load_gif(self):
        self.ui.movie.stop()


    def watch_it(self, text_from):
        _translate = QtCore.QCoreApplication.translate
        if len(text_from) == 1:
            if self.flag == 0:
                self.stop_load_gif()
                self.flag = 1
            if text_from[0] >= 1.85 or self.pred_last - text_from[0] < -0.2:
                self.ui.textEdit_9.setHtml(_translate("Dialog",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Times New Roman\',\'Georgia\',\'Serif\'; font-size:8.25pt; font-weight:448; font-style:normal;\">\n"
                                                   f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:30pt;\">{str(round(text_from[0], 2))}</span></p></body></html>"))
            else:
                self.ui.textEdit_9.setHtml(_translate("Dialog",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Times New Roman\',\'Georgia\',\'Serif\'; font-size:8.25pt; font-weight:448; font-style:normal;\">\n"
                                                   "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:30pt;\">No Bet</span></p></body></html>"))
            self.ui.textEdit_11.setHtml(_translate("Dialog",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Times New Roman\',\'Georgia\',\'Serif\'; font-size:8.25pt; font-weight:448; font-style:normal;\">\n"
                                                f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:30pt;\">{str(self.last_game_bank)}</span></p></body></html>"))
            self.ui.textEdit_14.setHtml(_translate("Dialog",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Times New Roman\',\'Georgia\',\'Serif\'; font-size:8.25pt; font-weight:448; font-style:normal;\">\n"
                                                f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:30pt;\">{str(self.last_game_crash)}</span></p></body></html>"))
            self.pred_last_last = self.pred_last
            self.pred_last = round(text_from[0], 2)
        elif len(text_from) == 3:
            self.total_site_bank.append(text_from[2])
            self.last_game_crash = round(text_from[1], 2)
            self.last_game_bank = int(text_from[2])
            self.ui.textEdit_5.setHtml(_translate("Dialog",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Times New Roman\',\'Georgia\',\'Serif\'; font-size:8.25pt; font-weight:448; font-style:normal;\">\n"
                                               f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:30pt;\">{str(int(sum(self.total_site_bank)))}</span></p></body></html>"))
            if self.flag == 1:
                if self.pred_last >= 1.85 or self.pred_last_last - self.pred_last < -0.2:
                    if self.last_game_crash >= 1.80:
                        self.winn.append(0.8)
                        self.win_pr.append(1)
                    else:
                        self.winn.append(-1)
                        self.win_pr.append(0)
                self.ui.textEdit_6.setHtml(_translate("Dialog",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Times New Roman\',\'Georgia\',\'Serif\'; font-size:8.25pt; font-weight:448; font-style:normal;\">\n"
                                                   f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:30pt;\">{str(sum(self.winn))}</span></p></body></html>"))
                self.ui.textEdit_7.setHtml(_translate("Dialog",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Times New Roman\',\'Georgia\',\'Serif\'; font-size:8.25pt; font-weight:448; font-style:normal;\">\n"
                                                   f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:30pt;\">{str(100 * round(sum(self.win_pr) / len(self.win_pr), 1))}</span></p></body></html>"))



    def stop_load(self):
        self.sig_for_sig_for_break.connect(self.csfailthread.status_for_break)
        self.sig_for_sig_for_break.emit(1)







obj = QthreadApp()



