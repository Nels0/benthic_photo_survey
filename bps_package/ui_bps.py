# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_gui.ui'
#
# Created: Mon Oct  7 17:18:33 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(919, 627)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.photoInfoGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.photoInfoGroupBox.setMinimumSize(QtCore.QSize(240, 0))
        self.photoInfoGroupBox.setMaximumSize(QtCore.QSize(240, 16777215))
        self.photoInfoGroupBox.setAutoFillBackground(True)
        self.photoInfoGroupBox.setObjectName(_fromUtf8("photoInfoGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.photoInfoGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.photoCountValue = QtGui.QLabel(self.photoInfoGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.photoCountValue.setFont(font)
        self.photoCountValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.photoCountValue.setObjectName(_fromUtf8("photoCountValue"))
        self.verticalLayout_2.addWidget(self.photoCountValue)
        self.directoryLabel = QtGui.QLabel(self.photoInfoGroupBox)
        self.directoryLabel.setObjectName(_fromUtf8("directoryLabel"))
        self.verticalLayout_2.addWidget(self.directoryLabel)
        self.directoryValue = QtGui.QLabel(self.photoInfoGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.directoryValue.setFont(font)
        self.directoryValue.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.directoryValue.setText(_fromUtf8(""))
        self.directoryValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.directoryValue.setObjectName(_fromUtf8("directoryValue"))
        self.verticalLayout_2.addWidget(self.directoryValue)
        self.filenameLabel = QtGui.QLabel(self.photoInfoGroupBox)
        self.filenameLabel.setObjectName(_fromUtf8("filenameLabel"))
        self.verticalLayout_2.addWidget(self.filenameLabel)
        self.filenameValue = QtGui.QLabel(self.photoInfoGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.filenameValue.setFont(font)
        self.filenameValue.setText(_fromUtf8(""))
        self.filenameValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filenameValue.setObjectName(_fromUtf8("filenameValue"))
        self.verticalLayout_2.addWidget(self.filenameValue)
        self.gridLayout_2.addWidget(self.photoInfoGroupBox, 0, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.photoDisplay = QtGui.QLabel(self.centralwidget)
        self.photoDisplay.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photoDisplay.sizePolicy().hasHeightForWidth())
        self.photoDisplay.setSizePolicy(sizePolicy)
        self.photoDisplay.setMinimumSize(QtCore.QSize(500, 350))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.photoDisplay.setPalette(palette)
        self.photoDisplay.setAutoFillBackground(True)
        self.photoDisplay.setFrameShape(QtGui.QFrame.Panel)
        self.photoDisplay.setFrameShadow(QtGui.QFrame.Sunken)
        self.photoDisplay.setText(_fromUtf8(""))
        self.photoDisplay.setScaledContents(False)
        self.photoDisplay.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.photoDisplay.setWordWrap(True)
        self.photoDisplay.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.photoDisplay.setObjectName(_fromUtf8("photoDisplay"))
        self.verticalLayout.addWidget(self.photoDisplay)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.previousButton = QtGui.QPushButton(self.centralwidget)
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.horizontalLayout.addWidget(self.previousButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.geotagButton = QtGui.QPushButton(self.centralwidget)
        self.geotagButton.setObjectName(_fromUtf8("geotagButton"))
        self.horizontalLayout.addWidget(self.geotagButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.depthTempTagButton = QtGui.QPushButton(self.centralwidget)
        self.depthTempTagButton.setObjectName(_fromUtf8("depthTempTagButton"))
        self.horizontalLayout.addWidget(self.depthTempTagButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 3, 1)
        self.exifDataGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.exifDataGroupBox.setMinimumSize(QtCore.QSize(240, 0))
        self.exifDataGroupBox.setMaximumSize(QtCore.QSize(240, 16777215))
        self.exifDataGroupBox.setObjectName(_fromUtf8("exifDataGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.exifDataGroupBox)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.dateLabel = QtGui.QLabel(self.exifDataGroupBox)
        self.dateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateLabel.setObjectName(_fromUtf8("dateLabel"))
        self.gridLayout.addWidget(self.dateLabel, 0, 0, 1, 1)
        self.timeValue = QtGui.QLabel(self.exifDataGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.timeValue.setFont(font)
        self.timeValue.setText(_fromUtf8(""))
        self.timeValue.setObjectName(_fromUtf8("timeValue"))
        self.gridLayout.addWidget(self.timeValue, 1, 1, 1, 1)
        self.latitudeLabel = QtGui.QLabel(self.exifDataGroupBox)
        self.latitudeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.latitudeLabel.setObjectName(_fromUtf8("latitudeLabel"))
        self.gridLayout.addWidget(self.latitudeLabel, 2, 0, 1, 1)
        self.directionValue = QtGui.QLabel(self.exifDataGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.directionValue.setFont(font)
        self.directionValue.setText(_fromUtf8(""))
        self.directionValue.setObjectName(_fromUtf8("directionValue"))
        self.gridLayout.addWidget(self.directionValue, 4, 1, 1, 1)
        self.temperatureLabel = QtGui.QLabel(self.exifDataGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temperatureLabel.sizePolicy().hasHeightForWidth())
        self.temperatureLabel.setSizePolicy(sizePolicy)
        self.temperatureLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temperatureLabel.setObjectName(_fromUtf8("temperatureLabel"))
        self.gridLayout.addWidget(self.temperatureLabel, 6, 0, 1, 1)
        self.depthLabel = QtGui.QLabel(self.exifDataGroupBox)
        self.depthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.depthLabel.setObjectName(_fromUtf8("depthLabel"))
        self.gridLayout.addWidget(self.depthLabel, 5, 0, 1, 1)
        self.latitudeValue = QtGui.QLabel(self.exifDataGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.latitudeValue.setFont(font)
        self.latitudeValue.setText(_fromUtf8(""))
        self.latitudeValue.setObjectName(_fromUtf8("latitudeValue"))
        self.gridLayout.addWidget(self.latitudeValue, 2, 1, 1, 1)
        self.longitudeLabel = QtGui.QLabel(self.exifDataGroupBox)
        self.longitudeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.longitudeLabel.setObjectName(_fromUtf8("longitudeLabel"))
        self.gridLayout.addWidget(self.longitudeLabel, 3, 0, 1, 1)
        self.longitudeValue = QtGui.QLabel(self.exifDataGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.longitudeValue.setFont(font)
        self.longitudeValue.setText(_fromUtf8(""))
        self.longitudeValue.setObjectName(_fromUtf8("longitudeValue"))
        self.gridLayout.addWidget(self.longitudeValue, 3, 1, 1, 1)
        self.directionLabel = QtGui.QLabel(self.exifDataGroupBox)
        self.directionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.directionLabel.setObjectName(_fromUtf8("directionLabel"))
        self.gridLayout.addWidget(self.directionLabel, 4, 0, 1, 1)
        self.depthValue = QtGui.QLabel(self.exifDataGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.depthValue.setFont(font)
        self.depthValue.setText(_fromUtf8(""))
        self.depthValue.setObjectName(_fromUtf8("depthValue"))
        self.gridLayout.addWidget(self.depthValue, 5, 1, 1, 1)
        self.substrateValue = QtGui.QLabel(self.exifDataGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.substrateValue.setFont(font)
        self.substrateValue.setText(_fromUtf8(""))
        self.substrateValue.setObjectName(_fromUtf8("substrateValue"))
        self.gridLayout.addWidget(self.substrateValue, 8, 1, 1, 1)
        self.temperatureValue = QtGui.QLabel(self.exifDataGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.temperatureValue.setFont(font)
        self.temperatureValue.setText(_fromUtf8(""))
        self.temperatureValue.setObjectName(_fromUtf8("temperatureValue"))
        self.gridLayout.addWidget(self.temperatureValue, 6, 1, 1, 1)
        self.habitatLabel = QtGui.QLabel(self.exifDataGroupBox)
        self.habitatLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.habitatLabel.setObjectName(_fromUtf8("habitatLabel"))
        self.gridLayout.addWidget(self.habitatLabel, 7, 0, 1, 1)
        self.habitatValue = QtGui.QLabel(self.exifDataGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.habitatValue.setFont(font)
        self.habitatValue.setText(_fromUtf8(""))
        self.habitatValue.setObjectName(_fromUtf8("habitatValue"))
        self.gridLayout.addWidget(self.habitatValue, 7, 1, 1, 1)
        self.substrateLabel = QtGui.QLabel(self.exifDataGroupBox)
        self.substrateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.substrateLabel.setObjectName(_fromUtf8("substrateLabel"))
        self.gridLayout.addWidget(self.substrateLabel, 8, 0, 1, 1)
        self.dateValue = QtGui.QLabel(self.exifDataGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateValue.setFont(font)
        self.dateValue.setText(_fromUtf8(""))
        self.dateValue.setObjectName(_fromUtf8("dateValue"))
        self.gridLayout.addWidget(self.dateValue, 0, 1, 1, 1)
        self.timeLabel = QtGui.QLabel(self.exifDataGroupBox)
        self.timeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.gridLayout.addWidget(self.timeLabel, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.exifDataGroupBox, 1, 1, 1, 1)
        self.habAndSubstTabWidget = QtGui.QTabWidget(self.centralwidget)
        self.habAndSubstTabWidget.setMinimumSize(QtCore.QSize(240, 0))
        self.habAndSubstTabWidget.setMaximumSize(QtCore.QSize(240, 16777215))
        self.habAndSubstTabWidget.setObjectName(_fromUtf8("habAndSubstTabWidget"))
        self.habitatTab = QtGui.QWidget()
        self.habitatTab.setObjectName(_fromUtf8("habitatTab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.habitatTab)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.habitatTableWidget = QtGui.QTableWidget(self.habitatTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.habitatTableWidget.sizePolicy().hasHeightForWidth())
        self.habitatTableWidget.setSizePolicy(sizePolicy)
        self.habitatTableWidget.setMaximumSize(QtCore.QSize(130000, 16777215))
        self.habitatTableWidget.setRowCount(0)
        self.habitatTableWidget.setColumnCount(0)
        self.habitatTableWidget.setObjectName(_fromUtf8("habitatTableWidget"))
        self.habitatTableWidget.horizontalHeader().setVisible(False)
        self.habitatTableWidget.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_2.addWidget(self.habitatTableWidget)
        self.habAndSubstTabWidget.addTab(self.habitatTab, _fromUtf8(""))
        self.substTab = QtGui.QWidget()
        self.substTab.setObjectName(_fromUtf8("substTab"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.substTab)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.substrateListWidget = QtGui.QListWidget(self.substTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.substrateListWidget.sizePolicy().hasHeightForWidth())
        self.substrateListWidget.setSizePolicy(sizePolicy)
        self.substrateListWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.substrateListWidget.setObjectName(_fromUtf8("substrateListWidget"))
        self.horizontalLayout_3.addWidget(self.substrateListWidget)
        self.habAndSubstTabWidget.addTab(self.substTab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.habAndSubstTabWidget, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 919, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOutput = QtGui.QMenu(self.menubar)
        self.menuOutput.setObjectName(_fromUtf8("menuOutput"))
        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName(_fromUtf8("menuActions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_GPS_Log = QtGui.QAction(MainWindow)
        self.actionLoad_GPS_Log.setObjectName(_fromUtf8("actionLoad_GPS_Log"))
        self.actionLoad_Depth_Log = QtGui.QAction(MainWindow)
        self.actionLoad_Depth_Log.setObjectName(_fromUtf8("actionLoad_Depth_Log"))
        self.actionLoad_Photo_Directory = QtGui.QAction(MainWindow)
        self.actionLoad_Photo_Directory.setObjectName(_fromUtf8("actionLoad_Photo_Directory"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionExport_Shapefile = QtGui.QAction(MainWindow)
        self.actionExport_Shapefile.setObjectName(_fromUtf8("actionExport_Shapefile"))
        self.actionDepth_Plot = QtGui.QAction(MainWindow)
        self.actionDepth_Plot.setObjectName(_fromUtf8("actionDepth_Plot"))
        self.actionGeo_Tag_All_Photos = QtGui.QAction(MainWindow)
        self.actionGeo_Tag_All_Photos.setObjectName(_fromUtf8("actionGeo_Tag_All_Photos"))
        self.actionDepth_Temp_Tag_All = QtGui.QAction(MainWindow)
        self.actionDepth_Temp_Tag_All.setObjectName(_fromUtf8("actionDepth_Temp_Tag_All"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.menuFile.addAction(self.actionLoad_GPS_Log)
        self.menuFile.addAction(self.actionLoad_Depth_Log)
        self.menuFile.addAction(self.actionLoad_Photo_Directory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuOutput.addAction(self.actionExport_Shapefile)
        self.menuOutput.addAction(self.actionDepth_Plot)
        self.menuActions.addAction(self.actionGeo_Tag_All_Photos)
        self.menuActions.addAction(self.actionDepth_Temp_Tag_All)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuOutput.menuAction())

        self.retranslateUi(MainWindow)
        self.habAndSubstTabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.nextButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.nextPhoto)
        QtCore.QObject.connect(self.previousButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.previousPhoto)
        QtCore.QObject.connect(self.geotagButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.geoTag)
        QtCore.QObject.connect(self.depthTempTagButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.depthTempTag)
        QtCore.QObject.connect(self.actionGeo_Tag_All_Photos, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.geoTagAll)
        QtCore.QObject.connect(self.actionDepth_Temp_Tag_All, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.depthTempTagAll)
        QtCore.QObject.connect(self.actionLoad_Depth_Log, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.loadDepthLog)
        QtCore.QObject.connect(self.actionLoad_GPS_Log, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.loadGpsLog)
        QtCore.QObject.connect(self.actionDepth_Plot, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.depthPlot)
        QtCore.QObject.connect(self.actionExport_Shapefile, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.exportShapefile)
        QtCore.QObject.connect(self.actionLoad_Photo_Directory, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.loadPhotoDirectory)
        QtCore.QObject.connect(self.actionPreferences, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.preferenceDialog)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Benthic Photo Survey", None, QtGui.QApplication.UnicodeUTF8))
        self.photoInfoGroupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Photo Info", None, QtGui.QApplication.UnicodeUTF8))
        self.photoCountValue.setText(QtGui.QApplication.translate("MainWindow", "0 of 0", None, QtGui.QApplication.UnicodeUTF8))
        self.directoryLabel.setText(QtGui.QApplication.translate("MainWindow", "Directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.filenameLabel.setText(QtGui.QApplication.translate("MainWindow", "Filename:", None, QtGui.QApplication.UnicodeUTF8))
        self.previousButton.setText(QtGui.QApplication.translate("MainWindow", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.previousButton.setShortcut(QtGui.QApplication.translate("MainWindow", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.geotagButton.setText(QtGui.QApplication.translate("MainWindow", "Geo Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.depthTempTagButton.setText(QtGui.QApplication.translate("MainWindow", "Depth/Temp Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setShortcut(QtGui.QApplication.translate("MainWindow", "Right", None, QtGui.QApplication.UnicodeUTF8))
        self.exifDataGroupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Exif Data", None, QtGui.QApplication.UnicodeUTF8))
        self.dateLabel.setText(QtGui.QApplication.translate("MainWindow", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.latitudeLabel.setText(QtGui.QApplication.translate("MainWindow", "Latitude", None, QtGui.QApplication.UnicodeUTF8))
        self.temperatureLabel.setText(QtGui.QApplication.translate("MainWindow", "Temperature", None, QtGui.QApplication.UnicodeUTF8))
        self.depthLabel.setText(QtGui.QApplication.translate("MainWindow", "Depth", None, QtGui.QApplication.UnicodeUTF8))
        self.longitudeLabel.setText(QtGui.QApplication.translate("MainWindow", "Longitude", None, QtGui.QApplication.UnicodeUTF8))
        self.directionLabel.setText(QtGui.QApplication.translate("MainWindow", "Direction ", None, QtGui.QApplication.UnicodeUTF8))
        self.habitatLabel.setText(QtGui.QApplication.translate("MainWindow", "Habitat", None, QtGui.QApplication.UnicodeUTF8))
        self.substrateLabel.setText(QtGui.QApplication.translate("MainWindow", "Substrate", None, QtGui.QApplication.UnicodeUTF8))
        self.timeLabel.setText(QtGui.QApplication.translate("MainWindow", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.habitatTableWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Hover and roll mouse wheel to set habitat proportions</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.habAndSubstTabWidget.setTabText(self.habAndSubstTabWidget.indexOf(self.habitatTab), QtGui.QApplication.translate("MainWindow", "Habitat", None, QtGui.QApplication.UnicodeUTF8))
        self.substrateListWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "Double Click to set Substrate", None, QtGui.QApplication.UnicodeUTF8))
        self.habAndSubstTabWidget.setTabText(self.habAndSubstTabWidget.indexOf(self.substTab), QtGui.QApplication.translate("MainWindow", "Substrate", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOutput.setTitle(QtGui.QApplication.translate("MainWindow", "&Output", None, QtGui.QApplication.UnicodeUTF8))
        self.menuActions.setTitle(QtGui.QApplication.translate("MainWindow", "&Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_GPS_Log.setText(QtGui.QApplication.translate("MainWindow", "Load &GPS Log", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_GPS_Log.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+G", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Depth_Log.setText(QtGui.QApplication.translate("MainWindow", "Load &Depth Log", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Depth_Log.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Photo_Directory.setText(QtGui.QApplication.translate("MainWindow", "Load &Photos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Photo_Directory.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_Shapefile.setText(QtGui.QApplication.translate("MainWindow", "Export &Shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDepth_Plot.setText(QtGui.QApplication.translate("MainWindow", "Depth &Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGeo_Tag_All_Photos.setText(QtGui.QApplication.translate("MainWindow", "Geo Tag All Photos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDepth_Temp_Tag_All.setText(QtGui.QApplication.translate("MainWindow", "Depth/Temp Tag All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences...", None, QtGui.QApplication.UnicodeUTF8))

