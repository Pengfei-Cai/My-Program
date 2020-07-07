#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
import time
import zipfile
import os


def zip_ya(startdir, opath):
    # startdir-要压缩的文件夹路径
    unix_time = str(time.time())
    nameT = unix_time[-4:-1]
    file_news = opath + nameT + '.zip'  # 压缩后文件夹的名字
    print(file_news)
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')  # 将当前目录替换为空，即以当前目录为相对目录，如果当前目录下面还存在文件夹，则fpath为 【/子目录】

        # fpath = (fpath + os.sep, '')[fpath != '']
        # fpath = fpath and fpath + os.sep or ''
        # fpath = fpath and fpath + os.sep
        # if fpath:
        #     fpath += os.sep
        # else:
        #     fpath = ''
        # fpath = fpath or ''
        fpath += os.sep if fpath else ''# 实现当前文件夹以及包含的所有文件的压缩


        for filename in filenames:
            dfpath = os.path.join(dirpath, filename)
            ffpath = os.path.join(fpath, filename)
            z.write(dfpath,ffpath)
            print('压缩成功')

    backp = file_news.split('\\')[-1]
    return backp
    z.close()



