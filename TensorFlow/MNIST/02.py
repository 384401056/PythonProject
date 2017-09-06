import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 加载训练数据集
mnist = input_data.read_data_sets('E:\MNIST', one_hot=True)

batch_size = 100
xs, ys = mnist.train.next_batch(batch_size)

print(xs.shape,ys.shape)

