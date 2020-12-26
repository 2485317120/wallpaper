import requests
import os.path
import ctypes
current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep)
URL = 'https://area.sinaapp.com/bingImg/'
res = requests.get(URL)
# 发出请求，并把返回的结果放在变量res中
photo = open(father_path+"\\wall.jpg",'wb')
# 新建了一个文件wall.jpg，这里的文件没加路径，会被保存在程序运行的当前目录下。
photo.write(res.content)
# 将 Reponse 对象的内容以 [二进制数据] 的形式写入文件
photo.close()
# 关闭文档

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep)
#print(father_path)
ctypes.windll.user32.SystemParametersInfoW(20, 0, father_path+"\\wall.jpg", 0)
#print(father_path + "\\wall.jpg")