import tensorflow as tf
import AddLayer
import file 
import pandas as pd
import numpy as np

add_layer = AddLayer.add_layer

next_train_data = file.NextTrainData())
test_data = pd.read_csv('test.csv').values

xs = tf.placeholder(tf.float32,[None,784])
ys = tf.placeholder(tf.float32,[None,10])

def compute_accuracy(v_xs,v_ys):
    global prediction
    y_pre = sess.run(prediction,feed_dict={xs:v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result = sess.run(accuracy)
    return result

prediction = add_layer(xs,784,10,activation_function = tf.nn.softmax)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),
        reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in next_train_data:
        batch_xs,batch_ys = i
        sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys})
        print(sess.run(compute_accuracy(batch_xs,batch_ys)))
        
        
        
