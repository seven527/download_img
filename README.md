# download_img
给定一批图片链接，批量下载到本地。

需求：有一批商品，每个商品包含多张图片，目标是下载商品图片到相应的文件夹，文件夹以商品ID命名。

需求分析：
如图片链接为
https://gd2.alicdn.com/imgextra/i2/2752294408/TB2085naH1YBuNjSszhXXcUsFXa_!!2752294408.jpg,
https://gd1.alicdn.com/imgextra/i1/2752294408/TB254yCo4PI8KJjSspoXXX6MFXa_!!2752294408.jpg,
https://gd1.alicdn.com/imgextra/i3/285445295/TB2rnC8X6QnBKNjSZSgXXXHGXXa_!!285445295.jpg,
https://gd4.alicdn.com/imgextra/i4/285445295/TB2mh8eeXXXXXadXpXXXXXXXXXX_!!285445295.jpg;

相当于给的图片链接，把图片爬到本地。
需用到urllib.request.urlretrieve()方法，非常方便。
具体见py脚本。
