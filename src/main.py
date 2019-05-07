#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication

from src.calculator import CalculatorWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import  * #QMediaContent, QMediaPlayer, QMediaList
app = QApplication(sys.argv)

calculator = CalculatorWindow()
playlist = QMediaPlaylist()
url = QUrl.fromLocalFile("voice.wav")
playlist.addMedia(QMediaContent(url))
playlist.setPlaybackMode(QMediaPlaylist.Loop)

player = QMediaPlayer()
player.setPlaylist(playlist)
player.setMedia(QMediaContent(url))
player.setVolume(60)
player.play()
sys.exit(app.exec_())


