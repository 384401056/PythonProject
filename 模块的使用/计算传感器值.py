
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

