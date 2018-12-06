import tensorflow as tf
import os

# 定义cifar的数据等命令行参数
FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string("cifar_dir", "./data/cifar10/cifar-10-batches-bin/", "文件的目录")
tf.app.flags.DEFINE_string("cifar_tfrecords", "./tmp/cifar.tfrecords", "存进tfrecords的文件")


def picread(filelist):
    """
    读取狗图片并转换成张量
    :param filelist: 文件路径+ 名字的列表
    :return: 每张图片的张量
    """
    # 1、构造文件队列
    file_queue = tf.train.string_input_producer(filelist)

    # 2、构造阅读器去读取图片内容（默认读取一张图片）
    reader = tf.WholeFileReader()

    key, value = reader.read(file_queue)

    print(value)

    # 3、对读取的图片数据进行解码
    image = tf.image.decode_jpeg(value)

    print(image)

    # 5、处理图片的大小（统一大小）
    image_resize = tf.image.resize_images(image, [200, 200])

    print(image_resize)

    # 注意：一定要把样本的形状固定 [200, 200, 3],在批处理的时候要求所有数据形状必须定义
    image_resize.set_shape([200, 200, 3])

    print(image_resize)

    # 6、进行批处理
    image_batch = tf.train.batch([image_resize], batch_size=20, num_threads=1, capacity=20)

    print(image_batch)

    return image_batch


class CifarRead(object):

    def __index__(self, filelist):
        self.file_list = filelist


if __name__  == "__main__":
    pass
