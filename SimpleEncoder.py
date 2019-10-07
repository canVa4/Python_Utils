import os
import codecs
import chardet
import io

"""
Author: ZX
Ref:    CSDN
Date:   19-10-7
"""


def convertFile(file, in_enc="GB2312", out_enc="UTF-8"):
    """
    用于将file装换从in_enc编码转换至out_enc编码，默认的是GB2312转到utf-8
    param 1 file:    文件路径
    param 2 in_enc:  输入文件格式
    param 3 out_enc: 输出文件格式
    return: none
    """
    in_enc = in_enc.upper()
    out_enc = out_enc.upper()  # 转换到大写字母
    try:
        print("convert [ " + file.split('\\')[-1] + " ].....From " + in_enc + " --> " + out_enc)
        f = codecs.open(file, 'r', encoding=in_enc)  # 以in_enc的编码方式读取
        new_content = f.read()  # 这里可能会爆炸，read不管多大都读，可能内存会炸
        # codecs.open(file, 'w', out_enc).write(new_content)    # 如果是python 2.x 用这一行，把下面一行注掉
        io.open(file, 'w', encoding=out_enc).write(new_content)  # 以out_enc的编码方式写入
        f.close()
    # print (f.read())
    except IOError as err:
        print("I/O error: {0}".format(err))


def listFoldersAndFiles(path):
    """
    返回 文件夹 和 文件 的名字

    param 1 path: "文件夹"和"文件"所在的路径
    return:  (list_folders, list_files)
            :list_folders: 文件夹
            :list_files: 文件
    """
    list_folders = []
    list_files = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            list_folders.append(file)
        else:
            list_files.append(file)
    return list_folders, list_files


if __name__ == "__main__":
    """
    !!! 将需要转换的文件所在的文件夹写到PATH里即可
    """
    path = 'D:\\RoboconCode\\ok\\chassis\\SrcCopy'
    (list_folders, list_files) = listFoldersAndFiles(path)

    print("Path: " + path)
    for fileName in list_files:
        filePath = path + '\\' + fileName
        with open(filePath, "rb") as f:  # rb:以二进制打开
            data = f.read()
            codeType = chardet.detect(data)['encoding']
            # print(codeType)
            convertFile(filePath, codeType, 'UTF-8')
