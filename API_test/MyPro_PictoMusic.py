
####################################################
# www.littlefisher.cn
# 这个是mytest_space.py的升级版软件
# 可以通过本地图片识别出图片场景，进而找到对应的歌曲并播放
####################################################

from typing import Union
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from PIL import ImageQt
import sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import requests
import base64
import winsound

class Ui_Form(QWidget):

    def __init__(self,api,keys,parent = None):
        super(Ui_Form,self).__init__(parent =None)
        self.keyword = ""
        self.api = api
        self.keys =keys
        self.setObjectName("Form")
        self.resize(800, 530)
        self.pushButton = QtWidgets.QPushButton("选择",self)

        self.pushButton.setGeometry(QtCore.QRect(50,460,130,40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_file)

        self.pushButton_2 = QtWidgets.QPushButton("识别",self)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 460, 130, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.clicked.connect(self.get_date)

        self.pushButton_3 = QtWidgets.QPushButton("Music", self)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 460, 130, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.clicked.connect(self.get_music)

        self.pushButton_4 = QtWidgets.QPushButton("播放音乐", self)
        self.pushButton_4.setGeometry(QtCore.QRect(620,30,130,50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setStyleSheet("QpushButton{background-color:lightblue}")
        self.pushButton_4.clicked.connect(self.get_sound)

        self.pushButton_5 = QtWidgets.QPushButton("播放停止", self)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 120, 130, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setStyleSheet("QpushButton{background-color:lightblue}")
        self.pushButton_5.clicked.connect(self.stop_music)


        #图片标签；pic
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30,30,540,400))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color:black;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(580, 270, 191, 111))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label_3 = QtWidgets.QLabel("识别",self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)

        self.label_4 = QtWidgets.QLabel("具体",self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(font)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)


        self.label_5 = QtWidgets.QLabel("识别",self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFont(font)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)


        self.label_6 = QtWidgets.QLabel("具体",self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)


    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self,"Open file..","/",'all files:(*.png);;(*.jpg)')



        if file_name[0]:#File exits
            #clear the contend of label;
           self.label.clear()
           self.file_name = file_name[0]
           print("file name: {}".format(str(self.file_name)))
           img = Image.open(self.file_name)
           pixmap = ImageQt.toqpixmap(img)
           self.label.setPixmap(pixmap)
           self.label.setScaledContents(True)
           self.pushButton_2.setEnabled(True)

        else:
            QMessageBox.warning(self,"waring","你不给我图片让我识别个球！")


    def get_token(self):
        get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
            self.api, self.keys)
        try:
            res = requests.get(get_token_url).json()['access_token']
            print("res : " + res)
            return str(res)
        except:
            print("something wrong in get_token")
            return 0


    def get_date(self):
        print("in get data")
        if self.file_name:
            params = {
                'image': str(base64.b64encode(open(self.file_name, 'rb').read()), 'utf-8'),
                'image_type': 'BASE64'
            }

            request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
            # 二进制方式打开图片文件

            access_token = '24.31690f195354669b52b308bac9a0ab04.2592000.1597382800.282335-21365047'
            request_url = request_url + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            res = requests.post(request_url, data=params, headers=headers)

            try:
                total_list = res.json()['result']
                ans1 = total_list[0]['root']
                ans2 = total_list[0]['keyword']
                ans3 = total_list[1]['root']
                ans4 = total_list[1]['keyword']

                # print("ans1 : " + ans1)
                # print(res.json())

                print(ans1)
                self.lineEdit.setText(str(ans1))
                self.lineEdit.setAlignment(Qt.AlignCenter)

                print(ans2)
                self.keyword = ans2
                self.lineEdit_2.setText(str(ans2))
                self.lineEdit_2.setAlignment(Qt.AlignCenter)

                print(ans3)
                self.lineEdit_3.setText(str(ans3))
                self.lineEdit_3.setAlignment(Qt.AlignCenter)

                print(ans4)
                self.lineEdit_4.setText(str(ans4))
                self.lineEdit_4.setAlignment(Qt.AlignCenter)

                self.pushButton_3.setEnabled(True)

            except:
                print("not find")
                # QMessageBox.warning(self,'error','Not Find')

        else:
            QMessageBox.information(self,'info','The file path of pic is not exist!')


    def get_music( self ):
        # winsound.PlaySound('D:\Ytube\Pong\/faded.wav', winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
        # encoding=utf8

        import requests
        from bs4 import BeautifulSoup
        import urllib.request

        headers = {
            'Referer': 'http://music.163.com/',
            'Host': 'music.163.com',
            'User-Agent': 'Littlefisher/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3202.75 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        }
        # play_url = 'http://music.163.com/playlist?id=317113395'
        play_url = 'https://music.163.com/playlist?id=5124358874'

        s = requests.session()
        response = s.get(play_url, headers=headers).content
        s = BeautifulSoup(response, 'lxml')
        main = s.find('ul', {'class': 'f-hide'})

        name = self.keyword
        print(name)
        for music in main.find_all('a'):
            if music.text == name:
                print('{} : {}'.format(music.text, music['href']))
                list = []
                musicUrl = 'https://music.163.com/song/media/outer/url' + music['href'][5:] + '.mp3'
                musicName = music.text
                list.append(musicName)
                list.append(musicUrl)

                print(list)

                url = list[1]
                name = list[0]
                try:
                    print('正在下载', name)
                    QtWidgets.QMessageBox.information(self,"你在干嘛呐","正在下载歌曲:{}".format(name),QtWidgets.QMessageBox.Yes)
                    QtWidgets.QMessageBox.information(self, "听我说", "下载慢等我！好了会提示你！",
                                                      QtWidgets.QMessageBox.Yes)
                    res = requests.get(url)
                    music = res.content
                    with open(r'E:\工作啊\竞赛\API_test\{}.mp3'.format(name), 'ab') as file:  # 保存到本地的文件名
                        file.write(res.content)
                        file.flush()
                    file.close()
                    print('下载成功')

                    QtWidgets.QMessageBox.information(self, "喂", "歌曲:{}下载成功".format(name), QtWidgets.QMessageBox.Yes)

                    self.pushButton_4.setEnabled(True)

                except:
                    print('下载失败')
                    QtWidgets.QMessageBox.information(self, "喂", "歌曲:{}下载失败了".format(name), QtWidgets.QMessageBox.Yes)


    def get_sound( self ):

        music_path = r'{}.mp3'.format(self.keyword)
        self.pushButton_5.setEnabled(True)
        url = QUrl.fromLocalFile(music_path)
        content = QMediaContent(url)
        self.player = QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()


    def stop_music( self ):
        self.player.stop()


if __name__ =='__main__':
    import sys
    api ='MaH9NRPRQDGVmRGViapLe56Z'
    keys ='NPBag1Qgfnfe0auMwrKpC59iIoqWa7Ym'
    app =QtWidgets.QApplication(sys.argv)
    window = Ui_Form(api,keys)
    window.show()
    sys.exit(app.exec_())
