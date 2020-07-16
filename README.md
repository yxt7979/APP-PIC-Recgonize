# APP-PIC-Recgonize

## 说明
**Pic To Text** & **Pic To Music**
无数不足点emmmmmm
API_Test中的文件请看文档描述，这样不至于头大...

## Pic To Text

2020.07.15  

I write a very very very simple application that recognizes picture scenes using Baidu API.    

Here's a video of the run time

[vplayer url="https:\/\/littlefisher.oss-cn-beijing.aliyuncs.com\/%E5%9C%BA%E6%99%AF%E8%AF%86%E5%88%ABAPI%E5%BA%94%E7%94%A8.mp4"  /]
（Forgive me that I can't tell the rhino from the hippopotamus)

### About
It can help you Identify the content and scene of the images.     

### Attention
1.The size of the picture that you wanna to choose **can not be larger than 4M**.     
2.I have put my own API keys and the Secret Keys here as nobody is going to see this simple project, but it is also very nice of you to use your own key!

## Pic To Music

2020.07.16

Here's the vedio of the run time.
[vplayer url="https:\/\/littlefisher.oss-cn-beijing.aliyuncs.com\/Pic_Music%20%281%29.mp4"  /]

### About 
Based on the App I write yesterday. I update it to find a music and play it through a picture.

### Attention
1.The music library I crawled is one of my playlist of WangYi which only has 6 songs.....hhhhhhahhhhh    
2.I use the exact same name and the exact same scene to determine whether or not to download music (A VERY WRONG IDEA) so it is better for you to only use the pictures in the "测试图片"Package.....

### 其他
待改进：
1.建立庞大的音乐歌单数据库
2.这里判断图片的场景仅仅根据第一可能性的答案，需要一个合适的加权算法来诠释一张图片
3.得到图片的文字信息后，需要一个算法来匹配歌曲（这里只是找名字一字不差的了），正确的应该是结合名字，情绪，风格，评论等等的匹配算法。（可是我还不会）   
4.丑陋的界面
5.凌乱的代码

Finally...Welcome to [Littlefisher's Blog][1]


  [1]: https://www.littltfisher.cn
