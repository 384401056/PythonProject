import tensorflow as tf

# 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
# 加到默认图中.
#
# 构造器的返回值代表该常量 op 的返回值.
matrix1 = tf.constant([[12., 42.], [36.,31.]])

# 创建另外一个常量 op, 产生一个 2x1 矩阵.
matrix2 = tf.constant([[2.],[3.]])

# 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# 返回值 'product' 代表矩阵乘法的结果.
product1 = tf.matmul(matrix1, matrix2)

# 返回矩阵的平均值,每二个参数为0则按列求平均，为1则按行求平均。
product2 = tf.reduce_mean(matrix1, 1)

# 返回矩阵的最大值。每二个参数为0则按列求最大值，为1则按行求最大值
product3 = tf.reduce_max(matrix1, 1)


with tf.Session() as sess:
    print(sess.run(product3))

# g1 = tf.Graph()
# with g1.as_default():
#     # 初始化为0
#     init = tf.zeros(shape=[1])
#     v = tf.get_variable("v", initializer=init)
#
# g2 = tf.Graph()
# with g2.as_default():
#     # 初始化为1
#     init = tf.ones(shape=[1])
#     v = tf.get_variable("v", initializer=init)
#
# with tf.Session(graph=g1) as sess:
#     tf.initialize_all_variables().run()
#     with tf.variable_scope("", reuse=True):
#         print(sess.run(tf.get_variable("v")))
#
#
# with tf.Session(graph=g2) as sess:
#     tf.initialize_all_variables().run()
#     with tf.variable_scope("", reuse=True):
#         print(sess.run(tf.get_variable("v")))

