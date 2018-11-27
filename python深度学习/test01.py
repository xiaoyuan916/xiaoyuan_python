import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
g = tf.Graph()

print(g)
with g.as_default():
    c = tf.constant(11.0)
    print(c.graph)

# 实现一个加法运算
a = tf.constant(5.0)
b = tf.constant(6.0)

sum1 = tf.add(a, b)

# 默认的这张图，相当于是给程序分配一段内存
graph = tf.get_default_graph()

print(graph)

# 不是op不能运行
var1 = 2.0
# var2 = 3
# sum2 = var1 + var2

# 有重载的机制,默认会给运算符重载成op类型
sum2 = a + var1

print(sum2)

# s = tf.Session()
#
# s.run()
# s.run()
# s.close()

# 只能运行一个图， 可以在会话当中指定图去运行
# 只要有会话的上下文环境，就可以使用方便eval()

# 训练模型
# 实时的提供数据去进行训练

# placeholder是一个占位符,feed_dict一个字典
plt = tf.placeholder(tf.float32, [2, 3, 4])

print(plt)

with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    # print(sess.run(plt, feed_dict={plt: [[1, 2, 3], [4, 5, 36], [2, 3, 4]]}))
    # print(sum1.eval())
    print(a.graph)
    print("---------")
    print(a.shape)
    print(plt.shape)
    print("-------")
    print(a.name)
    print("-------")
    print(a.op)
