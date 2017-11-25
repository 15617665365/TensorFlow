import tensorflow as tf
import mysql.connector


m1 = tf.constant([[3, 3]])
m2 = tf.constant([[4],[2]])

with tf.Session() as sess:
    product = tf.matmul(m1,m2)
    restult = sess.run(product)
    print(restult)