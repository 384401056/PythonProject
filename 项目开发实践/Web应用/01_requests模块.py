import requests

results = None

def getMarketList():
    ''' 获取全部农贸市场的基本信息 '''
    res = requests.get('http://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip=46201')
    # 对全局变量进行赋值
    global results
    # 将返回的数据进转为json
    results = res.json()
    for result in results['results']:
        print(result)


def getMaketDetails():
    '''循环获取每个农贸市场的具体信息'''
    for result in results['results']:
        id = result['id']
        res = requests.get('http://search.ams.usda.gov/farmersmarkets/v1/data.svc/mktDetail?id='+id)
        print(res.json())



def main():
    getMarketList()
    getMaketDetails()


if __name__ == '__main__':
    main()
