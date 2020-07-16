# encoding:utf-8

#######################################
# www.littlefisher.cn
# 百度云通用图像场景识别的接口调用（官方代码）
########################################

import requests
import base64

'''
通用物体和场景识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
# 二进制方式打开图片文件
f = open('师哥.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.31690f195354669b52b308bac9a0ab04.2592000.1597382800.282335-21365047'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)

if response:
    total_list = response.json()['result']
    ans1 = total_list[0]['root']
    ans2 = total_list[0]['keyword']
    ans3 = total_list[1]['root']
    ans4 = total_list[1]['keyword']

    print("ans1 : " + ans1)
    print (response.json())