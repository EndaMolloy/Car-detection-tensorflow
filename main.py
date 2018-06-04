import tensorflow as tf

hello = tf.constant('TEST')
sess = tf.Session()

print(sess.run(hello).decode())
