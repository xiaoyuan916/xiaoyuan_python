import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 创建一张图包含了一组op和tensor,上下文环境
# op:只要使用tensorflow的API定义的函数都是OP
# tensor：就指代的是数据

# g = tf.Graph()
#
# print(g)
# with g.as_default():
#     c = tf.constant(11.0)
#     print(c.graph)
#
# # 实现一个加法运算
# a = tf.constant(5.0)
# b = tf.constant(6.0)
#
# sum1 = tf.add(a, b)
#
# # 默认的这张图，相当于是给程序分配一段内存
# graph = tf.get_default_graph()
#
# print(graph)
#
# # 不是op不能运行
# var1 = 2.0
# # var2 = 3
# # sum2 = var1 + var2
#
# # 有重载的机制,默认会给运算符重载成op类型
# sum2 = a + var1
#
# print(sum2)
#
# # s = tf.Session()
# #
# # s.run()
# # s.run()
# # s.close()
#
# # 只能运行一个图， 可以在会话当中指定图去运行
# # 只要有会话的上下文环境，就可以使用方便eval()
#
# # 训练模型
# # 实时的提供数据去进行训练
#
# # placeholder是一个占位符,feed_dict一个字典
# plt = tf.placeholder(tf.float32, [2, 3, 4])
#
# print(plt)
#
# with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
#     # print(sess.run(plt, feed_dict={plt: [[1, 2, 3], [4, 5, 36], [2, 3, 4]]}))
#     # print(sum1.eval())
#     print(a.graph)
#     print("---------")
#     print(a.shape)
#     print(plt.shape)
#     print("-------")
#     print(a.name)
#     print("-------")
#     print(a.op)

# tensorflow:打印出来的形状表示
# 0维：()   1维:(5)  2维：(5,6)   3维：(2,3,4)

# 形状的概念
# 静态形状和动态性状
# 对于静态形状来说，一旦张量形状固定了，不能再次设置静态形状, 不能夸维度修改 1D->1D 2D->2D
# 动态形状可以去创建一个新的张量,改变时候一定要注意元素数量要匹配  1D->2D  1->3D
#
# plt = tf.placeholder(tf.float32, [None, 2])
#
# print(plt)
#
# plt.set_shape([3, 2, 1])
#
# print(plt)
#
# # plt.set_shape([2, 3]) # 不能再次修改
#
# plt_reshape = tf.reshape(plt, [3, 3])
#
# print(plt_reshape)
#
# with tf.Session() as sess:
#     pass


# 变量op
# 1、变量op能够持久化保存，普通张量op是不行的
# 2、当定义一个变量op的时候，一定要在会话当中去运行初始化
# 3、name参数：在tensorboard使用的时候显示名字，可以让相同op名字的进行区分

# a = tf.constant(3.0, name="a")
#
# b = tf.constant(4.0, name="b")
#
# c = tf.add(a, b, name="add")
#
# var = tf.Variable(tf.random_normal([2, 3], mean=0.0, stddev=1.0), name="variable")
#
# print(a, var)
#
# # 必须做一步显示的初始化op
# init_op = tf.global_variables_initializer()
#
# with tf.Session() as sess:
#     # 必须运行初始化op
#     sess.run(init_op)
#
#     # 把程序的图结构写入事件文件, graph:把指定的图写进事件文件当中
#     filewriter = tf.summary.FileWriter("./tmp/summary/test/", graph=sess.graph)
#
#     print(sess.run([c, var]))


