import tensorflow as tf
import numpy as np

x_data = np.random.rand(100)
y_data = x_data * 5 + 4

#构建一个模型
b = tf.Variable(9.0)
k = tf.Variable(1.0)
y = k * x_data + b

#二次代价函数
loss = tf.reduce_mean(tf.square(y-y_data))
#定义一个梯度下降法来训练的优化器
optimizer = tf.train.GradientDescentOptimizer(0.2)
#最小代价函数
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    print(y_data)
    for item in range(501):
        sess.run(train)
        if(item%20 == 0):
            print(item,sess.run([b,k]))
