
##################################
# www.littlefisher.cn
# 单独通过Url将音乐保存到本地的代码
##################################

import requests
res = requests.get('https://music.163.com/song/media/outer/url?id=305414.mp3')
music = res.content

with open(r'E:\工作啊\竞赛\API_test\music2.mp3', 'ab') as file: #保存到本地的文件名
    file.write(res.content)
    file.flush()

