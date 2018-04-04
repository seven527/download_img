# -*-coding:utf8-*-
#!/usr/bin/python3


import os
import urllib.request
import time
from retrying import retry
import random


#定义爬取方法
@retry(stop_max_attempt_number=7,stop_max_delay=10000,wait_fixed=30000)
def save_img(url,name):
    file_path = 'd://img/'+str(name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_suffix= os.path.splitext(url)[1]
    file_name = str(time.time()).replace('.','')
    filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
    urllib.request.urlretrieve(url,filename=filename)

#图片链接池
url_pool =(
['https://gd2.alicdn.com/imgextra/i2/2752294408/TB2085naH1YBuNjSszhXXcUsFXa_!!2752294408.jpg', 2752294408],
['https://gd1.alicdn.com/imgextra/i1/2752294408/TB254yCo4PI8KJjSspoXXX6MFXa_!!2752294408.jpg', 2752294408],
['https://gd1.alicdn.com/imgextra/i3/285445295/TB2rnC8X6QnBKNjSZSgXXXHGXXa_!!285445295.jpg', 285445295],
['https://gd4.alicdn.com/imgextra/i4/285445295/TB2mh8eeXXXXXadXpXXXXXXXXXX_!!285445295.jpg',285445295]
) 

#爬取图片到本地
for url,name in url_pool:
    save_img(url,name)
    time.sleep(0.1)
    print('%s下载成功' % name)