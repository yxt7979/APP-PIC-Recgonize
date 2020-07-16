import urllib, sys
import ssl
import urllib.request

###########################################
# www.littlefisher.cn
# 第一次用API测试IP地址识别好不好用（阿里云API）
###########################################

host = 'https://api01.aliyun.venuscn.com'
path = '/ip'
method = 'GET'
appcode = 'f6feec88d0624131bf951592c61b8b27'
querys = 'ip=218.18.228.178'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)