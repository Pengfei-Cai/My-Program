#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
import os
from os.path import exists as file_exists
from tkinter import messagebox
from PIL import Image

def imShr(size, inpath, outpath):
    img = Image.open(inpath)
    img_resize = img.resize((int(size), int(size)), Image.ANTIALIAS)  # 调整尺寸
    imgn = str(size) + os.path.basename(inpath)  # 操作文件后保存的名称
    os.path.isdir(outpath) or os.mkdir(outpath)
    opath = os.path.join(outpath, imgn)
    img_resize.save(opath)
    return imgn