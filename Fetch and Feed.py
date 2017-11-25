import tensorflow as tf

intput1 = tf.constant(3)
intput2 = tf.constant(4)
intput3 = tf.constant(5)

add = tf.add(intput1,intput2)

mul = tf.sub(add,intput3)

with tf.Session() as sess:
    result = sess.run([add,mul])
    print(result)


intput3 = tf.placeholder(tf.int32)
intput4 = tf.placeholder(tf.int32)

out = tf.add(intput3,intput4)

with tf.Session() as sess:
    result = sess.run(out,feed_dict={intput3:[2],intput4:[3]})

    print(result)