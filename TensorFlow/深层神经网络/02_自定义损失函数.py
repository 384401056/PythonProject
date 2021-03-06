import tensorflow as tf
from numpy.random import RandomState

# v1 = tf.constant([1.0, 2.0, 3.0, 4.0])
# v2 = tf.constant([4.0, 3.0, 2.0, 1.0])

# with tf.Session() as sess:
    # # 比较两个张量中元素的大小，返回一个True/False的数组
    # condition = tf.greater(v1, v2)
    # print(sess.run(condition))
    # # 根据条件，选择返回哪个张量的元素,为false时返回v2的元素，为true时返回v1的元素
    # c = tf.where(condition, v1, v2)
    # print(sess.run(c))

batch_size = 8

x = tf.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')

w1 = tf.Variable(tf.random_normal([2, 1], stddev=1, seed=1))
y = tf.matmul(x, w1)

# 定义预测多了和预测少了的成本
loss_less = 10
loss_more = 1

loss = tf.reduce_sum(tf.where(tf.greater(y, y_), (y-y_)*loss_more, (y_-y)*loss_less))
train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2) # 返回两个元素的随机数组
Y = [[x1 + x2 + rdm.rand()/10.0-0.05] for (x1, x2) in X]

with tf.Session() as sess:
    init_op = tf.initialize_all_variables()
    sess.run(init_op)
    STEPS = 500
    for i in range(STEPS):
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)
        sess.run(train_step, feed_dict={x:X[start:end], y_:Y[start:end]})
        print(sess.run(w1))

