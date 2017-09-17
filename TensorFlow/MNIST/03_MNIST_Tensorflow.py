import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# MNIST数据集的相关常数
INPUT_NODE = 784  # 输入层的节点数，对于MNIST数据集，这个就等于图片的像素。
OUTPUT_NODE = 10  # 类别的数目(0~9)

LAYER1_NODE = 500 # 隐藏节点数.这里使用只有一个隐藏层的网络结构作为样例

BATCH_SIZE = 100 # 一个训练batch中的训练数据个数。数字越小时，训练过程越接近。

LEARNING_RATE_BASE = 0.8 # 基础的学习率.
LEARNING_RATE_DECAY = 0.99 # 学习率的衰减率.

REGULARIZATION_RATE = 0.0001 # 描述模型复杂的正则化项在损失函数中的系统。
TRAINING_STEPS = 30000 # 训练轮数。
MOVING_AVERAGE_DECAY = 0.99 # 滑动平均衰减率。


def inference(input_tensor, avg_class, weights1, biases1, weights2, biases2):
    # 当没提供滑动平均数时，直接使用参数当前的取值。
    if avg_class is None:
        layer1 = tf.nn.relu(tf.matmul(input_data, weights1) + biases1)
        return tf.matmul(layer1, weights2) + biases2
    else:
        layer1 = tf.nn.relu(tf.matmul(input_data, avg_class.average(weights1))) + avg_class.average(biases1)
        return tf.matmul(layer1, avg_class.average(weights2) + avg_class.average(biases2))


def train(mnist):

    # 定义节点准备接收数据
    x = tf.placeholder(tf.float32, [None, INPUT_NODE], name = 'x-input')
    y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name = 'y-input')

    # 权重
    weights1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
    # 偏置
    biases1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]))

    weights2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, OUTPUT_NODE], stddev=0.1))
    biases2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))


    y = inference(x, None, weights1, biases1, weights2, biases2)

    global_step = tf.Variable(0, trainable=False)

    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    variables_averages_op = variable_averages.apply(tf.trainable_variables())
    average_y = inference(x, variable_averages, weights1, biases1, weights2, biases2)

    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(y, tf.argmax(y_, 1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)

    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    regularization = regularizer(weights1) + regularizer(weights2)

    # 误差公式 loss
    loss = cross_entropy_mean + regularization

    # 设置指数衰减的学习率
    learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE, global_step, mnist.train.num.examples, LEARNING_RATE_DECAY)

    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step = global_step)

    with tf.control_dependencies([train_step, variables_averages_op]):
        train_op = tf.no_op(name='train')

    #
    correct_prediction = tf.equal(tf.argmax(average_y,1), tf.argmax(y_, 1))

    # 这个运算，先将布尔型的数值转换为实数型，然后计算平均值。这个平均值就是模型在这一组数据上的正确率.
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    with tf.Session() as sess:
        tf.initialize_all_variables().run()

        validate_feed = {x: mnist.validation.images, y_:mnist.validation.labels}

        test_feed = {x: mnist.test.images, y_:mnist.test.labels}

        for i in range(TRAINING_STEPS):
            if i % 1000 == 0:
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)
                print("After %d training step(s), validation accuracy on average model is %g" % (i, validate_acc))

            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            sess.run(train_op, feed_dict={x:xs, y_:ys})

            test_acc = sess.run(accuracy, feed_dict=test_feed)
            print("After %d training step(s), test accuracy using average model is %g" % (TRAINING_STEPS, test_acc))


def main(argv= None):
    # 加载训练数据集
    mnist = input_data.read_data_sets('E:\MNIST', one_hot=True)
    train(mnist)

if __name__ == '__main__':
    tf.app.run()


