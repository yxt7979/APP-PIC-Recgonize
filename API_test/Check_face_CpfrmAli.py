import urllib, sys
import ssl
import urllib.request

########################################################
# www.littlefisher.cn
# 阿里云的人脸识别API接口调用（不过我的免费次数都用完了哈哈哈）
########################################################

host = 'https://picbg.market.alicloudapi.com'
path = '/do'
method = 'POST'
appcode = 'f6feec88d0624131bf951592c61b8b27'
querys = ''
bodys = {}
url = host + path

bodys['image'] = 'https://littlefisher.oss-cn-beijing.aliyuncs.com/images/%E9%9B%85%E7%90%AA.jpg'
post_data = urllib.parse.urlencode(bodys).encode('utf-8')
request = urllib.request.Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
# 根据API的要求，定义相对应的Content-Type
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = response.read()

if (content):
    print(content)