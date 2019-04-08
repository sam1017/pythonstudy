#coding=utf-8
import os
#图像读取库
from PIL import Image
#矩阵运算库
import numpy as np
import tensorflow as tf
from cnn_settings import Cnn_settings
from load_data import load_traindata
from tensorflow.python.framework import graph_util

def main():
    print("cnn train begin")
    settings = Cnn_settings()
    datas, labels = load_traindata(settings.date_dir)
    print('Training data shape: ', datas.shape, '     Train labels shape: ', labels.shape)

    # 计算有多少类图片
    num_classes = len(set(labels))
    print("num_classes = " + str(num_classes))

    # 定义Placeholder，存放输入和标签
    datas_placeholder = tf.placeholder(tf.float32, [None, 32, 32, 3])
    labels_placeholder = tf.placeholder(tf.int32, [None])
    # 存放DropOut参数的容器，训练时为0.25，测试时为0
    dropout_placeholdr = tf.placeholder(tf.float32)

    # 定义卷积层, 20个卷积核, 卷积核大小为5，用Relu激活
    conv0 = tf.layers.conv2d(datas_placeholder, 20, 5, activation=tf.nn.relu)
    # 定义max-pooling层，pooling窗口为2x2，步长为2x2
    pool0 = tf.layers.max_pooling2d(conv0, [2, 2], [2, 2])

    # 定义卷积层, 40个卷积核, 卷积核大小为4，用Relu激活
    conv1 = tf.layers.conv2d(pool0, 40, 4, activation=tf.nn.relu)
    # 定义max-pooling层，pooling窗口为2x2，步长为2x2
    pool1 = tf.layers.max_pooling2d(conv1, [2, 2], [2, 2])

    # 将3维特征转换为1维向量
    flatten = tf.layers.flatten(pool1)

    # 全连接层，转换为长度为100的特征向量
    fc = tf.layers.dense(flatten, 400, activation=tf.nn.relu)

    # 加上DropOut，防止过拟合
    dropout_fc = tf.layers.dropout(fc, dropout_placeholdr)

    # 未激活的输出层
    logits = tf.layers.dense(dropout_fc, num_classes)

    predicted_labels = tf.arg_max(logits, 1, name="output")


    # 利用交叉熵定义损失
    losses = tf.nn.softmax_cross_entropy_with_logits(
        labels=tf.one_hot(labels_placeholder, num_classes),
        logits=logits
    )
    # 平均损失
    mean_loss = tf.reduce_mean(losses)

    # 定义优化器，指定要优化的损失函数
    optimizer = tf.train.AdamOptimizer(learning_rate=1e-2).minimize(losses)

    # 用于保存和载入模型
    #saver = tf.train.Saver()
    with tf.Session() as sess:
        print("训练模式")
        # 如果是训练，初始化参数
        sess.run(tf.global_variables_initializer())
        # 定义输入和Label以填充容器，训练时dropout为0.25
        train_feed_dict = {
            datas_placeholder: datas,
            labels_placeholder: labels,
            dropout_placeholdr: 0.25
        }
        for step in range(100):#100
            _, mean_loss_val = sess.run([optimizer, mean_loss], feed_dict=train_feed_dict)

            if step % 10 == 0:
                print("step = {}\tmean loss = {}".format(step, mean_loss_val))

        output_graph_def = graph_util.convert_variables_to_constants(sess, sess.graph_def,output_node_names=['output'])
        with tf.gfile.FastGFile(settings.model_path, mode='wb') as f:#’wb’中w代表写文件，b代表将数据以二进制方式写入文件。
            f.write(output_graph_def.SerializeToString())

    print("cnn train end")


#labels = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

if __name__ == "__main__":
    main()