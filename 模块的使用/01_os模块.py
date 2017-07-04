import os
import time
import os.path

# 返回当前路径
print(os.getcwd())

# 返回指定文件的创建时间、修改时间、最近访问时间
ctime = time.localtime(os.path.getctime('record.txt'))
mtime = time.localtime(os.path.getmtime('record.txt'))
atime = time.localtime(os.path.getatime('record.txt'))

print(ctime)
print(mtime)
print(atime)

# 将文件重命名
os.renames('test.txt','test000001.txt')
# os.renames('test000001.txt','test.txt')