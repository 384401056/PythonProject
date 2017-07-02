#字符的格式化
mystr = "{0} Love {1}.{2}".format("I","Gyb","com")

mystr = "{a} Love {b}.{c}".format(a="I",b="Gyb",c="com")

mystr = "{0} Love {b},{c}".format("I",b="Gyb",c="com")

mystr = "{{0}}".format("不打印")

#{0:.2f} .2代表保留2位小数,f代表打印定点数
mystr = "{0:.2f}{1}".format(27.356,"GB")


mystr = "%#o" % 123

mystr = "%#x" % 123

mystr = "%010d" % 1000

mystr = "%05d" % 23

print(mystr)