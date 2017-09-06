import tensorflow as tf

# 声明了w1,w2两个变量.
w1 = tf.Variable(tf.random_normal(shape = [2,3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal(shape = [3,1], stddev=1, seed=1))

# w1 = tf.random_normal(shape=[2,3],stddev=1.0,seed=1)
# w2 = tf.random_normal(shape=[3,1],stddev=1.0,seed=1)

# 特征值只是定义了维度、类型和名称.
x = tf.placeholder(tf.float32, shape = (3, 2), name = 'input')

# 向前传播算法获得神经网络的输出
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)





sess = tf.Session()
init_op = tf.global_variables_initializer()
sess.run(init_op)

# feed_dict 就是特征值
print('y =',sess.run(y, feed_dict={x:[[0.7, 0.9], [0.1, 0.4], [0.5, 0.8]]}))
sess.close()