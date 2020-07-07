#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
import time
import zipfile
import os
from glob import glob


def zip_ya(startdir, opath):
    # startdir-要压缩的文件夹路径
    unix_time = str(time.time())
    nameT = unix_time[-4:-1]
    print(opath)
    file_news = opath + nameT + '.zip'  # 压缩后文件夹的名字

    with zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED) as z:
        [z.write(x) for x in glob(startdir + '\*.jpg')]
        print('压缩成功')

    backp = file_news.split('\\')[-1]
    print(backp)
    return backp




#   # 参数一：文件夹名
#
