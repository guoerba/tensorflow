
#Thanks for https://blog.csdn.net/newbie_zero/article/details/79164499


from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np

MNIST_DATA = "../data/"

mnist = input_data.read_data_sets(MNIST_DATA,one_hot=True)

  # Create the model
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.matmul(x, W) + b
print("x = %s" % (str(x)))
 # Define loss and optimizer
#y_ = tf.placeholder(tf.int64, [None])#wrong here
y_ = tf.placeholder(tf.float32, [None,10])
print("y = %s" % (str(y)))

  # The raw formulation of cross-entropy,
  #
  #   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
  #                                 reduction_indices=[1]))
  #
  # can be numerically unstable.
  #
  # So here we use tf.losses.sparse_softmax_cross_entropy on the raw
  # outputs of 'y', and then average across the batch.

#cross_entropy = tf.losses.sparse_softmax_cross_entropy(labels=y_, logits=y)#wrong here
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
print("train_step:%s" % (type(train_step)))
print("train_step fininshed!")

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()
print("parameter initialization fininshed!")
  # Train
for _ in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  #print("batch_xs = %s\nbatch_ys = %s" % (str(batch_xs.shape),str(batch_ys.shape)))
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

#correct_prediction = tf.equal(tf.argmax(y, 1), y_)#wrong here
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(
    accuracy, feed_dict={
        x: mnist.test.images,
        y_: mnist.test.labels
    }))