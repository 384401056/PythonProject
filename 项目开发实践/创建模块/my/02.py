import sys
sys.path.append('..') # 当要引用上一级的包和模块时
import mymodule as mo
import my.mod as mo2

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