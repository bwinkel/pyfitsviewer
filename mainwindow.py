# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Dec  5 17:53:54 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(846, 601)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.splitter = QtGui.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.fileGroup = QtGui.QGroupBox(self.splitter)
        self.fileGroup.setObjectName(_fromUtf8("fileGroup"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.fileGroup)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.url = QtGui.QLineEdit(self.fileGroup)
        self.url.setObjectName(_fromUtf8("url"))
        self.verticalLayout.addWidget(self.url)
        self.files = QtGui.QListView(self.fileGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.files.sizePolicy().hasHeightForWidth())
        self.files.setSizePolicy(sizePolicy)
        self.files.setObjectName(_fromUtf8("files"))
        self.verticalLayout.addWidget(self.files)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.sectionsGroup = QtGui.QGroupBox(self.splitter)
        self.sectionsGroup.setObjectName(_fromUtf8("sectionsGroup"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.sectionsGroup)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.sections = QtGui.QTableView(self.sectionsGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sections.sizePolicy().hasHeightForWidth())
        self.sections.setSizePolicy(sizePolicy)
        self.sections.setObjectName(_fromUtf8("sections"))
        self.verticalLayout_4.addWidget(self.sections)
        self.dataGroup = QtGui.QGroupBox(self.splitter_3)
        self.dataGroup.setObjectName(_fromUtf8("dataGroup"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.dataGroup)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.splitter_2 = QtGui.QSplitter(self.dataGroup)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.filterHeader = QtGui.QLineEdit(self.layoutWidget)
        self.filterHeader.setMaximumSize(QtCore.QSize(200, 16777215))
        self.filterHeader.setObjectName(_fromUtf8("filterHeader"))
        self.horizontalLayout_3.addWidget(self.filterHeader)
        self.clearHeaderFilter = QtGui.QPushButton(self.layoutWidget)
        self.clearHeaderFilter.setObjectName(_fromUtf8("clearHeaderFilter"))
        self.horizontalLayout_3.addWidget(self.clearHeaderFilter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.header = QtGui.QTableView(self.layoutWidget)
        self.header.setObjectName(_fromUtf8("header"))
        self.verticalLayout_5.addWidget(self.header)
        self.layoutWidget1 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_2.addLayout(self.verticalLayout_7)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.indicesButton = QtGui.QPushButton(self.layoutWidget1)
        self.indicesButton.setObjectName(_fromUtf8("indicesButton"))
        self.horizontalLayout_2.addWidget(self.indicesButton)
        self.indicesLineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.indicesLineEdit.setMaximumSize(QtCore.QSize(25, 16777215))
        self.indicesLineEdit.setObjectName(_fromUtf8("indicesLineEdit"))
        self.horizontalLayout_2.addWidget(self.indicesLineEdit)
        self.plotButton = QtGui.QPushButton(self.layoutWidget1)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.horizontalLayout_2.addWidget(self.plotButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.filterData = QtGui.QLineEdit(self.layoutWidget1)
        self.filterData.setMaximumSize(QtCore.QSize(200, 16777215))
        self.filterData.setObjectName(_fromUtf8("filterData"))
        self.horizontalLayout_2.addWidget(self.filterData)
        self.clearDataFilter = QtGui.QPushButton(self.layoutWidget1)
        self.clearDataFilter.setObjectName(_fromUtf8("clearDataFilter"))
        self.horizontalLayout_2.addWidget(self.clearDataFilter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.contents = QtGui.QTableView(self.layoutWidget1)
        self.contents.setObjectName(_fromUtf8("contents"))
        self.verticalLayout_2.addWidget(self.contents)
        self.verticalLayout_6.addWidget(self.splitter_2)
        self.verticalLayout_3.addWidget(self.splitter_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.clearDataFilter, QtCore.SIGNAL(_fromUtf8("clicked()")), self.filterData.clear)
        QtCore.QObject.connect(self.clearHeaderFilter, QtCore.SIGNAL(_fromUtf8("clicked()")), self.filterHeader.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.fileGroup.setTitle(_translate("MainWindow", "Select file", None))
        self.sectionsGroup.setTitle(_translate("MainWindow", "Sections in file", None))
        self.dataGroup.setTitle(_translate("MainWindow", "Section contents", None))
        self.label.setText(_translate("MainWindow", "Header", None))
        self.filterHeader.setPlaceholderText(_translate("MainWindow", "Filter...", None))
        self.clearHeaderFilter.setText(_translate("MainWindow", "Clear", None))
        self.label_2.setText(_translate("MainWindow", "Data", None))
        self.indicesButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Use this index when the selected data field contains an array.</p><p>* to leave array untouched.</p><p>Click to reset to &quot;*&quot;.</p></body></html>", None))
        self.indicesButton.setText(_translate("MainWindow", "Indices:", None))
        self.indicesLineEdit.setText(_translate("MainWindow", "*", None))
        self.plotButton.setText(_translate("MainWindow", "Plot selected", None))
        self.filterData.setPlaceholderText(_translate("MainWindow", "Filter...", None))
        self.clearDataFilter.setText(_translate("MainWindow", "Clear", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

