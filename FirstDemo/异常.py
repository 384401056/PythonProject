try:
    f = open("test02.txt",'a',-1,"UTF-8")
    print(f.write("我是一个文件!!!\n"))
    b = int("abc")
except Exception as e:
    print("发生错误啦！！！！："+ str(e))
finally:
    f.close()