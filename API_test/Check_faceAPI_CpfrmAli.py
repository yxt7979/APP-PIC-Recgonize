# encoding:utf-8

#################################
# www.littlefisher.cn
# 阿里云官网提供的人脸检测实例代码
# 在2020.08.15后需要更换token
#################################

import requests

'''
人脸检测与属性分析
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

params = "{\"image\":\"027d8308a2ec665acb1bdf63e513bcb9\",\"image_type\":\"FACE_TOKEN\",\"face_field\":\"faceshape,facetype\"}"
access_token = '24.ef559d5b80107d290d1f2e91bfb10f22.2592000.1597383709.282335-21367748'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())