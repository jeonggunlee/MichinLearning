import tensorflow as tf
import numpy as np
import random as rn

rows = 4
cols = 4

tfc = tf.Variable(tf.random_normal(shape=[rows,cols], dtype=tf.float32))

sess = tf.Session()

sess.run(tf.global_variables_initializer())
print("[origin value]")
print(sess.run(tfc))

npc = sess.run(tfc)

ran_row = rn.randrange(rows)        #0~3
ran_col = rn.randrange(cols)        #0~3

npc[ran_row, ran_col] = 0

sess.run(tfc.assign(npc))

print("[modified {0},{1}]]".format(ran_row, ran_col))
print(sess.run(tfc))

