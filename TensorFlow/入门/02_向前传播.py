import tensorflow as tf

# 声明了w1,w2两个变量.
w1 = tf.Variable(tf.random_normal(shape = [2,3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal(shape = [3,1], stddev=1, seed=1))

# w1 = tf.random_normal(shape=[2,3],stddev=1.0,seed=1)
# w2 = tf.random_normal(shape=[3,1],stddev=1.0,seed=1)

# 输入特征
x = tf.constant([[0.7, 0.9]])

# 向前传播算法获得神经网络的输出
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)


sess = tf.Session()
# sess.run(w1.initializer)
# sess.run(w2.initializer)
init_op = tf.global_variables_initializer()
sess.run(init_op)
print(sess.run(w1))
print(sess.run(w2))
print('y =',sess.run(y))
sess.close()