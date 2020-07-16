#################################################
# www.littlefisher.cn
# 这个是百度智能云的官方文档，如何获取token（30天一换）
#################################################

# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=MaH9NRPRQDGVmRGViapLe56Z&client_secret=NPBag1Qgfnfe0auMwrKpC59iIoqWa7Ym'
response = requests.get(host)

if response:
    print(response.json()['access_token'])

