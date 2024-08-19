# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowilUUJB.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QToolButton,
    QVBoxLayout, QWidget)
from Resources import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(869, 1148)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.open_button = QPushButton(self.centralwidget)
        self.open_button.setObjectName(u"open_button")

        self.verticalLayout_2.addWidget(self.open_button)

        self.song_info_layout = QVBoxLayout()
        self.song_info_layout.setObjectName(u"song_info_layout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.song_cover = QLabel(self.centralwidget)
        self.song_cover.setObjectName(u"song_cover")
        self.song_cover.setPixmap(QPixmap(u":/Icons/Album.png"))
        self.song_cover.setScaledContents(False)
        self.song_cover.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.song_cover)

        self.song_name_label = QLabel(self.centralwidget)
        self.song_name_label.setObjectName(u"song_name_label")
        self.song_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.song_name_label)

        self.song_album_label = QLabel(self.centralwidget)
        self.song_album_label.setObjectName(u"song_album_label")
        self.song_album_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.song_album_label)

        self.song_quality_label = QLabel(self.centralwidget)
        self.song_quality_label.setObjectName(u"song_quality_label")
        self.song_quality_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.song_quality_label)


        self.song_info_layout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.song_info_layout)

        self.song_controls_layout = QHBoxLayout()
        self.song_controls_layout.setObjectName(u"song_controls_layout")
        self.song_mini_cover = QLabel(self.centralwidget)
        self.song_mini_cover.setObjectName(u"song_mini_cover")
        self.song_mini_cover.setPixmap(QPixmap(u":/Icons/Album.png").scaled(100, 100))
        self.song_mini_cover.setScaledContents(False)

        self.song_controls_layout.addWidget(self.song_mini_cover)

        self.song_name_controls_label = QLabel(self.centralwidget)
        self.song_name_controls_label.setObjectName(u"song_name_controls_label")
        self.song_name_controls_label.setWordWrap(True)
        self.song_name_controls_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.song_controls_layout.addWidget(self.song_name_controls_label)

        self.previous_button = QToolButton(self.centralwidget)
        self.previous_button.setObjectName(u"previous_button")
        icon = QIcon()
        icon.addFile(u":/Icons/Previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previous_button.setIcon(icon)
        self.previous_button.setIconSize(QSize(35, 35))
        self.song_controls_layout.addWidget(self.previous_button)

        self.play_button = QToolButton(self.centralwidget)
        self.play_button.setObjectName(u"play_button")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_button.setIcon(icon1)
        self.play_button.setIconSize(QSize(50, 50))

        self.song_controls_layout.addWidget(self.play_button)

        self.next_button = QToolButton(self.centralwidget)
        self.next_button.setObjectName(u"next_button")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_button.setIcon(icon2)
        self.next_button.setIconSize(QSize(35, 35))

        self.song_controls_layout.addWidget(self.next_button)

        self.mute_button = QToolButton(self.centralwidget)
        self.mute_button.setObjectName(u"mute_button")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Mute.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mute_button.setIcon(icon3)
        self.mute_button.setIconSize(QSize(35, 35))

        self.song_controls_layout.addWidget(self.mute_button)

        self.volume_slider = QSlider(self.centralwidget)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.song_controls_layout.addWidget(self.volume_slider)

        self.song_length_label = QLabel(self.centralwidget)
        self.song_length_label.setObjectName(u"song_length_label")

        self.song_controls_layout.addWidget(self.song_length_label)

        self.song_progress = QSlider(self.centralwidget)
        self.song_progress.setObjectName(u"song_progress")
        self.song_progress.setOrientation(Qt.Orientation.Horizontal)

        self.song_controls_layout.addWidget(self.song_progress)

        self.song_progress_label = QLabel(self.centralwidget)
        self.song_progress_label.setObjectName(u"song_progress_label")

        self.song_controls_layout.addWidget(self.song_progress_label)


        self.verticalLayout_2.addLayout(self.song_controls_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Music Player", None))
        self.open_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.song_cover.setText("")
        self.song_name_label.setText(QCoreApplication.translate("MainWindow", u"Song Name", None))
        self.song_album_label.setText(QCoreApplication.translate("MainWindow", u"Song Album", None))
        self.song_quality_label.setText(QCoreApplication.translate("MainWindow", u"Song Quality", None))
        self.song_mini_cover.setText("")
        self.song_name_controls_label.setText(QCoreApplication.translate("MainWindow", u"Song Name", None))
        self.previous_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.play_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.mute_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.song_length_label.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.song_progress_label.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
    # retranslateUi

