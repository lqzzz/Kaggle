import tensorflow as tf

def add_layer(inputs,in_size,out_size,keep_prob,activation_function = None):
   Weights = tf.Variable(tf.random_normal([in_size,out_size]))
   biases = tf.Variable(tf.zeros([1,out_size])+0.1)
   Wx_puls_b = tf.matmul(inputs,Weights) + biases 
   Wx_puls_b = tf.nn.dropout(Wx_puls_b,keep_prob)
   if activation_function is None:
       outputs = Wx_puls_b
   else:
       outputs = activation_function(Wx_puls_b)
   return outputs




       
