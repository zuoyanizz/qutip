#This file is part of QuTIP.
#
#    QuTIP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#    QuTIP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with QuTIP.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2011-2012, Paul D. Nation & Robert J. Johansson
#
###########################################################################

import sys,os,time

if os.environ['QUTIP_GUI']=="PYSIDE":
    from PySide import QtGui, QtCore

elif os.environ['QUTIP_GUI']=="PYQT4":
    from PyQt4 import QtGui, QtCore
   
import numpy,scipy,matplotlib
CD_BASE = os.path.dirname(__file__)

class AboutBox(QtGui.QWidget):
    def __init__(self, Qversion, parent=None):
        QtGui.QWidget.__init__(self, parent)
        #WINDOW PROPERTIES
        self.setWindowTitle('About QuTiP')
        self.resize(430, 450)
        self.center()
        self.setFocus()
        #self.setAttribute(Qt.WA_TranslucentBackground)#transparent
        #self.setWindowOpacity(0.95)
        #self.setWindowFlags(Qt.Popup)#no titlebar
        #IMAGES--------------------
        logo=QtGui.QLabel(self)
        logo.setGeometry((self.width()-200)/2, 0, 200, 163)
        logo.setPixmap(QtGui.QPixmap(CD_BASE + "/logo.png"))
        #TEXT--------------------
        tlabel = QtGui.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPointSize(20)
        fm = QtGui.QFontMetrics(font)
        tstring="QuTiP: The Quantum Toolbox in Python"
        pixelswide = fm.width(tstring)
        tlabel.setFont(font)
        tlabel.setText(tstring)
        tlabel.move((self.width()-pixelswide)/2.0, 170)
        #
        try:
            import PySide
            pyside_ver=PySide.__version__
        except:
            pyside_ver='None'
        try:
            import PyQt4.QtCore as qt4Core
            pyqt4_ver=qt4Core.PYQT_VERSION_STR
        except:
            pyqt4_ver='None'
        if sys.platform=='darwin':
            try:
                import Foundation
                pyobjc='Yes'
            except:
                pyobjc='No'
        label = QtGui.QLabel(self)
        font.setFamily("Arial")
        font.setBold(False)
        font.setPointSize(14)
        label.setFont(font)
        fm = QtGui.QFontMetrics(font)
        if sys.platform!='darwin':
            lstring="QuTiP Version:           "+Qversion+"\n"
            pixelswide = fm.width(lstring)
            lstring+="NumPy Version:         "+str(numpy.__version__)+"\n"
            lstring+="SciPy Version:            "+str(scipy.__version__)+"\n"
            lstring+="MatPlotLib Version:    "+str(matplotlib.__version__)+"\n\n"
            lstring+="PySide Version:         "+str(pyside_ver)+"\n"
            lstring+="PyQt4 Version:           "+str(pyqt4_ver)
            label.setText(lstring)
            label.move((self.width()-pixelswide)/2,210)
        else:
            lstring="QuTiP Version:           "+Qversion+"\n"
            pixelswide = fm.width(lstring)
            lstring+="NumPy Version:         "+str(numpy.__version__)+"\n"
            lstring+="SciPy Version:            "+str(scipy.__version__)+"\n"
            lstring+="MatPlotLib Version:    "+str(matplotlib.__version__)+"\n\n"
            lstring+="PySide Version:         "+str(pyside_ver)+"\n"
            lstring+="PyQt4 Version:           "+str(pyqt4_ver)+"\n"
            lstring+="PyObjc Installed:        "+str(pyobjc)
            label.setText(lstring)
            label.move((self.width()-pixelswide)/2,210)
        #
        alabel = QtGui.QLabel(self)
        astring="Copyright (c) 2011-2012, Paul D. Nation & Robert J. Johansson"
        pixelswide = fm.width(astring)
        alabel.setFont(font)
        alabel.setText(astring)
        alabel.move((self.width()-pixelswide)/2, 350)
        #
        clabel = QtGui.QLabel(self)
        alabel.setFont(font)
        clabel.setText("QuTiP is released under the GPL3.\n"
                        +"See the enclosed COPYING.txt\nfile for more information.")
        clabel.move((self.width()-pixelswide)/2, 380)
        #BUTTONS-----------------
        quit = QtGui.QPushButton('Close', self)
        quit.setStyleSheet("QPushButton {font-family:Arial;font-size: 14px;}")
        quit.setGeometry((self.width()-80-10), 395, 80, 40)
        #quit.setFocusPolicy(QtCore.Qt.NoFocus)
        quit.clicked.connect(self.close)
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    abox = AboutBox('0.1')
    abox.show()
    abox.raise_()
    app.exec_()
    
