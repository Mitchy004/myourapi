# Form implementation generated from reading ui file 'c:\Users\24Dan\OneDrive - Moreton Bay Colleges\Year 12\Digital Solutions\IA2\Code file\myourapi\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 557)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.requestText = QtWidgets.QTextEdit(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requestText.sizePolicy().hasHeightForWidth())
        self.requestText.setSizePolicy(sizePolicy)
        self.requestText.setMinimumSize(QtCore.QSize(0, 70))
        self.requestText.setMaximumSize(QtCore.QSize(16777215, 70))
        self.requestText.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.requestText.setLineWidth(0)
        self.requestText.setObjectName("requestText")
        self.verticalLayout_2.addWidget(self.requestText)
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.clientText = QtWidgets.QTextEdit(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clientText.sizePolicy().hasHeightForWidth())
        self.clientText.setSizePolicy(sizePolicy)
        self.clientText.setMinimumSize(QtCore.QSize(0, 250))
        self.clientText.setMaximumSize(QtCore.QSize(16777215, 250))
        self.clientText.setObjectName("clientText")
        self.verticalLayout_2.addWidget(self.clientText)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.resetSession = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetSession.sizePolicy().hasHeightForWidth())
        self.resetSession.setSizePolicy(sizePolicy)
        self.resetSession.setMinimumSize(QtCore.QSize(0, 30))
        self.resetSession.setMaximumSize(QtCore.QSize(16777215, 100))
        self.resetSession.setObjectName("resetSession")
        self.gridLayout.addWidget(self.resetSession, 0, 1, 1, 1)
        self.saveSession = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveSession.sizePolicy().hasHeightForWidth())
        self.saveSession.setSizePolicy(sizePolicy)
        self.saveSession.setMinimumSize(QtCore.QSize(0, 30))
        self.saveSession.setMaximumSize(QtCore.QSize(16777215, 100))
        self.saveSession.setObjectName("saveSession")
        self.gridLayout.addWidget(self.saveSession, 0, 0, 1, 1)
        self.testClientGet = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testClientGet.sizePolicy().hasHeightForWidth())
        self.testClientGet.setSizePolicy(sizePolicy)
        self.testClientGet.setMinimumSize(QtCore.QSize(0, 30))
        self.testClientGet.setMaximumSize(QtCore.QSize(16777215, 100))
        self.testClientGet.setObjectName("testClientGet")
        self.gridLayout.addWidget(self.testClientGet, 2, 0, 1, 1)
        self.testClientPost = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testClientPost.sizePolicy().hasHeightForWidth())
        self.testClientPost.setSizePolicy(sizePolicy)
        self.testClientPost.setMinimumSize(QtCore.QSize(0, 30))
        self.testClientPost.setMaximumSize(QtCore.QSize(16777215, 100))
        self.testClientPost.setObjectName("testClientPost")
        self.gridLayout.addWidget(self.testClientPost, 2, 1, 1, 1)
        self.apiSummary = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apiSummary.sizePolicy().hasHeightForWidth())
        self.apiSummary.setSizePolicy(sizePolicy)
        self.apiSummary.setMinimumSize(QtCore.QSize(0, 30))
        self.apiSummary.setMaximumSize(QtCore.QSize(16777215, 100))
        self.apiSummary.setObjectName("apiSummary")
        self.gridLayout.addWidget(self.apiSummary, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.responseText = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.responseText.setObjectName("responseText")
        self.verticalLayout.addWidget(self.responseText)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "URL Request"))
        self.label_3.setText(_translate("MainWindow", "Client Details"))
        self.resetSession.setText(_translate("MainWindow", "Reset Session"))
        self.saveSession.setText(_translate("MainWindow", "Save Session"))
        self.testClientGet.setText(_translate("MainWindow", "Test Client (GET)"))
        self.testClientPost.setText(_translate("MainWindow", "Test Client (POST)"))
        self.apiSummary.setText(_translate("MainWindow", "API Summary"))
        self.label_4.setText(_translate("MainWindow", "Server Reply"))
