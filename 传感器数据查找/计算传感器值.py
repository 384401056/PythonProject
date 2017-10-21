class CountSensroValue:

    def countPH(self, value):
        '''计算PH值传感器'''
        num = value
        result = 0
        if ((num/121.905) >= 5.0) and ((num/121.905) <=9.5):
            result = num/121.905-1.5
        print('PH值:',result)


    def countTuHum(self, value):
        '''计算土壤湿度值'''
        num = value
        result = 0
        if num <= 2282:
            result = 3.447*num/121.905-14.108
        elif num > 2282:
            result = 35.71*num/121.905-614.25
        print('土壤湿度值:',result)


    def countAirHum(self, value):
        '''计算大气湿度'''
        num = value
        result = 0
        result = 125*(num/2**16)-6
        print('大气湿度:',result)


def main():
    csv = CountSensroValue()
    csv.countAirHum(40000)



if __name__ == '__main__':
    main()




# 计算PH值传感器
# try:
#     while True:
#         num = int(input("请入PH值传感器："))
#         result = 0
#         if ((num/121.905) >= 5.0) and ((num/121.905) <=9.5):
#             result = num/121.905-1.5
#         print(result)
# except:
#     print("退出")

# 土壤湿度值
# try:
#     while True:
#         num = int(input("请入土壤湿度传感器："))
#         result = 0
#
#         if num <= 2282:
#             result = 3.447*num/121.905-14.108
#         elif num > 2282:
#             result = 35.71*num/121.905-614.25
#         print(result)
# except:
#     print("退出")

# 大气湿度
# try:
#     while True:
#         num = int(input("请入大气湿度传感器值："))
#         result = 0
#         result = 125*(num/2**16)-6
#         print(result)
# except:
#     print("退出")
