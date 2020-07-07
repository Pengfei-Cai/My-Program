#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
import os
import time
import tempfile

from PIL import Image
from Imge.Function1 import imShr
from flask import Flask, jsonify, request
from flask import send_from_directory, abort
from werkzeug.utils import secure_filename
from Imge.ZFunction1 import zip_ya


#设置路径以及上传文件后缀
app = Flask(__name__)
tpath = tempfile.mktemp()#临时文件的路径
UPLOAD_FOLDER = tpath
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))#当前文件路径
frontdir = os.path.abspath(os.path.join(os.getcwd(), ".."))#截取当前目录上级文件路径
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF'])


# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



#下载文件
@app.route("/api/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == "GET":
        if os.path.isfile(os.path.join(frontdir,filename)):#filename压缩后的名字，frontdir保存的路径
            return send_from_directory(frontdir, filename, as_attachment=True) #最后的参数是改变名称的开关
    abort(404)


# 上传文件
@app.route('/api/upload', methods=['POST'], strict_slashes=False)# 对URL最后的 / 符号是否严格要求
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])#上传文件目的路径

    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值

    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname = secure_filename(f.filename)
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = str(unix_time) + '.' + ext  # 修改了上传的文件名

        f.save(os.path.join(file_dir, new_filename))  # 保存文件到临时文件目录
        ipath = file_dir + '\\' + new_filename#获取上传目的文件路径

        img = Image.open(ipath)
        oriH = img.size[0]#获取图片原高
        oriW = img.size[1]#获取图片原宽

        dict = {'Ip6': 180, 'Ip7': 120}
        for x in dict:
            size = dict[x]
            if size > oriH or size > oriW:
                return '<script>alert("图片太小")</script>'
            imShr(size,ipath, file_dir)#执行更改size的方法

        zipdp = "/api/download/" + zip_ya(file_dir,basedir) #zip_ya()返回的是压缩后的文件名称
        return '<br><a href=' + zipdp + '>下载</a>'
    else:
        return jsonify({"code": 1001, "errmsg": "上传失败","he": request.form('pheight')})

if __name__ == '__main__':
    app.run(debug=True)
