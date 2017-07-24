import requests
import re
import pandas as pd


def getData():
    ''' 获取机器学习的数据集 '''
    r = requests.get(r'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

    with open('iris.data', 'w') as f:
        # 将请到的数据写入文件中
        f.write(r.text)

def main():
    # getData()
    df = pd.read_csv('iris.data', names=['sepal lenght','sepal width','petal lenght','petal width','class'])
    # print(df)
    # print(df.ix[:4, :2]) # df.ix[行(是包含)，列(不包含)]
    # print(df.ix[:10, [x for x in df.columns if 'petal' in x]])  # 选出列名中包含:petal的列
    # print(df['class'].unique)
    # print(df.count())
    # print(df[df['class'] == 'Iris-setosa'].count()) # 统计class为'Iris-setosa'的数量
    # print(df[df['class'] == 'Iris-setosa'])
    print(df[df['sepal width'] <= 2.5]) # 筛选出 sepal width <= 2.5的数据
    # print(df[df['sepal width'] >= 2.5].count())
    # print(df[(df['sepal width'] <= 2.5) & (df['class'] == 'Iris-virginica')])

    # print(df.describe()) # 生成描述性统计数据
    # print(df.describe(percentiles=[.10, .20, .40, .50, .60, .70, .80, .90]))
    # print(df.corr())


if __name__ == '__main__':
    main()