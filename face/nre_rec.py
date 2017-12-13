import tensorflow as tf
import file 
import pandas as pd
import numpy as np

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

xs = tf.placeholder('float', shape=[None, image_size])
ys = tf.placeholder('float', shape=[None, labels_count])

W_fc1 = weight_variable([784, 1024])
b_fc1 = bias_variable([1024])

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

h_fc1 = tf.nn.relu(tf.matmul(xs, W_fc1) + b_fc1)

keep_prob = tf.placeholder('float')
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

y = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
real_ = 