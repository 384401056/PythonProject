from urllib import request
from numpy import genfromtxt, zeros
from pylab import plot, show, figure, subplot, hist, xlim



def getData():
    ''' 伯克利大学网站鸢尾花（iris）数据集,
        这是一个包含了三种鸢(yuān)尾花（山鸢尾、维吉尼亚鸢尾和变色鸢尾）
        的各50个数据样本的多元数据集，每个样本都有四个特征（或者说变量），
        即花萼（sepal）和花瓣（petal）的长度和宽度。以厘米为单位。 '''
    url = 'http://aima.cs.berkeley.edu/data/iris.csv'
    f = request.urlopen(url)
    with open('iris.csv','w') as localFile:
        localFile.write(f.read().decode())


def main():
    ''' 创建了一个包含特征值的矩阵以及一个包含样本类型的向量。
            我们可以通过查看我们加载的数据结构的shape值来确认数据集的大小：'''
    # 读取前4列数据
    data = genfromtxt('iris.csv', delimiter=',', usecols=(0, 1, 2, 3))
    # 读取第5列数据
    target = genfromtxt('iris.csv', delimiter=',', usecols=(4), dtype=str)
    # print(data.shape)
    # print(target.shape)
    # # 查看我们有多少种样本类型以及它们的名字
    # print(set(target))

    ''' 使用第一和第三维度（花萼的长和宽） '''
    # plot(data[target=='setosa',0],data[target=='setosa',2],'bo')
    # plot(data[target=='versicolor',0],data[target=='versicolor',2],'ro')
    # plot(data[target=='virginica',0],data[target=='virginica',2],'go')
    # show()

    xmin = min(data[:,0])
    xmax = max(data[:,0])
    figure()
    subplot(411) # distribution of the setosa class (1st, on the top)
    hist(data[target=='setosa',0],color='b',alpha=.7)
    xlim(xmin,xmax)
    subplot(412) # distribution of the versicolor class (2nd)
    hist(data[target=='versicolor',0],color='r',alpha=.7)
    xlim(xmin,xmax)
    subplot(413) # distribution of the virginica class (3rd)
    hist(data[target=='virginica',0],color='g',alpha=.7)
    xlim(xmin,xmax)
    subplot(414) # global histogram (4th, on the bottom)
    hist(data[:,0],color='y',alpha=.7)
    xlim(xmin,xmax)
    show()


if __name__ == '__main__':
    main()