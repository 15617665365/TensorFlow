import tensorflow as tf

a = tf.Variable([[3,4]])
b = tf.Variable([[6],[7]])

c = tf.initialize_all_variables()

with tf.Session() as sess:

    sess.run(c)
    print(sess.run(tf.sub(a,b)))
    print(sess.run(tf.matmul(a, b)))
    print(sess.run(tf.add(a, b)))
