try:
    # 当文件没有open成功，则finally中的close()就会出错了。
    # f = open('test03.txt','r',-1,'UTF-8')

    # 当使用with时，会自动关闭打开的文件，就不用手动close()了
    with open('test.txt','r',-1,'UTF-8') as f:
        print(f.read())
except Exception as e:
    print(str(e))
# finally:
#     f.close()

