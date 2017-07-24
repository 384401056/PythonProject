import mymodule as mo # 导入了自定义mymodule模块
import my.mod as mo2 # 导入了自定义的包

def main():
    mo.first()
    mo.last()
    print(mo.num)
    print(mo.ls)

    mo2.add()
    mo2.delete()
    print(mo2.num)
    print(mo2.ls)

if __name__ == '__main__':
    main()
