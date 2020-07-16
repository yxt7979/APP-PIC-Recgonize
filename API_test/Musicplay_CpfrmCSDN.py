# -*- coding: utf-8 -*-
# @Time : 2020/4/17 19:06
# @Author : Zhao HL
# @File : 12_musicPlay.py

#############################################
# 上面是代码的作者
#############################################
# www.littlefisher.cn
# 这是在网上找的另一个，单独的音乐播放器，放10s..
#############################################

import sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

music_path = r'气球.mp3'


class Example(QWidget):
    def __init__ ( self ):
        super(Example, self).__init__()

        self.init_UI()

    def init_UI ( self ):
        btn = QPushButton('play', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(self.music_play)

        self.show()

    def music_play ( self ):
        url = QUrl.fromLocalFile(music_path)
        content = QMediaContent(url)
        self.player = QMediaPlayer()
        self.player.setMedia(content)
        # self.player.setVolume(100)
        self.player.play()
        time.sleep(10)
        self.player.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())