import tensorflow as tf

# 交叉熵的公式, y_代表正确结果，y代表预测结果。这个交叉熵的计算包含了4个不同的tensorflow运算.
# reduce_mean:求平均值
# log:求对数
# clip_by_value:将一个张量中的数值限制在一个范围以内
'''cross_entropy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)))'''



with tf.Session() as sess:
    '''clip_by_value'''
    # v1 = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    # 小于1.9的变为1.9，大于4.5的变为4.5
    # print(tf.clip_by_value(v, 1.9, 4.5).eval())

    # log,对张量中所有元素求对数。
    # v1 = tf.constant([1.0, 2.0, 3.0])
    # print(tf.log(v1).eval())

    # 张量的乘法运算，是元素之前直接相乘。而不是矩阵乘法
    # v1 = tf.constant([[1.0,2.0], [3.0, 4.0]])
    # v2 = tf.constant([[5.0,6.0], [7.0, 8.0]])
    # print((v2*v3).eval())

    # 矩阵乘法
    v1 = tf.constant([[1.0,2.0], [3.0, 4.0]])
    v2 = tf.constant([[5.0,6.0], [7.0, 8.0]])
    print(tf.matmul(v1, v2).eval())

