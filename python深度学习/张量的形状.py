import tensorflow as tf

# 形状的概念
# 静态形状和动态性状
# 对于静态形状来说，一旦张量形状固定了，不能再次设置静态形状, 不能夸维度修改 1D->1D 2D->2D
# 动态形状可以去创建一个新的张量,改变时候一定要注意元素数量要匹配  1D->2D  1->3D

plt = tf.placeholder(tf.float32, [None, 2])

print(plt)

plt.set_shape([3, 2])

print(plt)

# 不能再次修改
# plt.set_shape([2, 3])

# plt_reshape = tf.reshape(plt, [3, 3])

# print(plt_reshape)

with tf.Session() as sess:
    pass
