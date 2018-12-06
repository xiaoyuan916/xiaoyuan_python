import tensorflow as tf

# # 创建两个常量节点
# node1 = tf.constant(3.2)
# node2 = tf.constant(4.8)
# # 创建一个 adder 节点，对上面两个节点执行 + 操作
# adder = node1 + node2
# # 打印一下 adder 节点
# print(adder)
# # 打印 adder 运行后的结果
# sess = tf.Session()
# print(sess.run(adder))
# 创建两个占位 Tensor 节点
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
# 创建一个 adder 节点，对上面两个节点执行 + 操作
adder = a + b
# 打印三个节点
print(a)
print(b)
print(adder)
# 运行一下，后面的 dict 参数是为占位 Tensor 提供输入数据
sess = tf.Session()
print(sess.run(adder, {a: 3, b: 4.5}))
print(sess.run(adder, {a: [1, 3], b: [2, 4]}))
