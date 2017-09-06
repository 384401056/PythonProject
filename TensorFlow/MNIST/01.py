import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 加载训练数据集
mnist = input_data.read_data_sets('E:\MNIST', one_hot=True)

# 打印训练数据集大小
print('Tranning data size:', mnist.train.num_examples)
# 打印验证数据集大小
print('Validating data size:', mnist.validation.num_examples)
# 打印测试数据集大小
print('Testing data size:', mnist.test.num_examples)
# 打印示例图片
print('Example training data:', mnist.train.images[0])
# 打印图片的答案
print('Example training data:', mnist.train.labels[0])