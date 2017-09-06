import tensorflow as tf
from numpy.random import RandomState

# 定义训练数据batch的大小.
batch_size = 8

# 定义神经网络的参数。
w1 = tf.Variable(tf.random_normal(shape = [2,3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal(shape = [3,1], stddev=1, seed=1))


x = tf.placeholder(dtype=tf.float32, shape=(None, 2), name='x-input')
y_ = tf.placeholder(dtype=tf.float32, shape=(None, 1), name='y-input')


a = tf.matmul(x, w1)
y = tf.matmul(a, w2)


'''定义损失函数(交叉熵)的反向传播的算法, 
tf.reduce_mean在某一维度上求平均值。
clip_by_value(t, clip_value_min, clip_value_max, name=None),
基于定义的min与max对tensor数据进行截断操作，目的是为了应对梯度爆发或者梯度消失的情况, 
tf.log() 每一个元素求对数'''
cross_entropy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)))

'''实现了Adam算法的优化器 '''
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)


# 通过一个随机数来生成一个模拟数据集.1为随机数种子.
rdm = RandomState(1)
dataset_size = 128

# 生成128行2列的二维数组.
X = rdm.rand(dataset_size, 2)

# 产生随机的0或者1的128行1列人二维数组.
Y = [[int(x1+x2 < 1)] for (x1, x2) in X]

with tf.Session() as sess:
    init_op = tf.initialize_all_variables()
    sess.run(init_op)
    print('============训练前的w1,w2=========')
    print('w1 = ', sess.run(w1))
    print('w2 = ', sess.run(w2))
    # print('y = ', sess.run(y, feed_dict={x:X}))

    STEPS = 5000
    for i in range(STEPS):
        # 每次选取 batch_size 个样本进行训练。
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)

        # 通过选取的样本训练神经网络并更新参数。
        sess.run(train_step, feed_dict={x:X[start:end], y_:Y[start:end]})

        if i % 1000 == 0:
            total_cross_entropy = sess.run(cross_entropy, feed_dict={x:X, y_:Y})

            # 通过这个结果可以发现随着训练的进行，交叉熵是逐渐变小的。交叉熵越小说明预测的结果和真实的结果差距越小。
            print("After %d training step(s), cross entropy on all data is %g" % (i, total_cross_entropy))

    print('============训练后的w1,w2=========')
    print('w1 = ', sess.run(w1))
    print('w2 = ', sess.run(w2))




