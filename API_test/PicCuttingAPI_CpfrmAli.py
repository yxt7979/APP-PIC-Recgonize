
##############################################
# www.littlefisher.cn
# 这个是阿里云抠图API调用并把结果写到content.txt中
##############################################

import urllib, sys
import ssl
import urllib.request
import base64

host = 'http://ntread.market.alicloudapi.com'
path = '/imgdect'
method = 'POST'
appcode = 'f6feec88d0624131bf951592c61b8b27'
querys = ''
bodys = {}
url = host + path

#
f = open(r'师哥.jpg','rb')
contents = base64.b64encode(f.read())
f.close()
bodys['src'] = contents
print(contents)

post_data = urllib.parse.urlencode(bodys).encode(encoding='UTF8')
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
    fi = open(r'content.txt', 'w+')
    print(content, file=fi)
    fi.close()
    print(content)