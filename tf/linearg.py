
import tensorflow as tf

X = tf.placeholder("float")
Y = tf.placeholder("float")

W = tf.Varialbe(tf.random_normal([1]), name="weight")
b = tf.Varialbe(tf.zeros([1]), name="bias")

z = tf.multiply(X, W) + b