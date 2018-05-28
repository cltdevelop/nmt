# coding=utf-8

# tensorflow中实现变量共享:
#       tf.get_variable()
#       tf.variable_scope()


import tensorflow as tf
from tensorflow.python.framework import ops


def conv_relu(input, kernel_shape, bias_shape):
    weights = tf.get_variable('weights', shape=kernel_shape, initializer=tf.random_normal_initializer())

if __name__ == '__main__':
    with tf.variable_scope('cltdevelop', reuse=tf.AUTO_REUSE):
        weights = tf.get_variable('weights', shape=(10, 10), dtype=tf.float32,
                                  initializer=tf.random_normal_initializer())
        print(weights.name)

        scope = ops.get_collection(("__varscope",))
    print 1

