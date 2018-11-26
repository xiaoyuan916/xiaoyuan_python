import numpy as np


def data_matrix(file_name):
    """
    将文本转化为matrix
    :param file_name: 文件名
    :return: 数据矩阵
    """
    fr = open(file_name)
    array_lines = fr.readlines()
    number_lines = len(array_lines)
    return_mat = zeros((number_lines, 3))
    # classLabelVector = []
    index = 0
    for line in array_lines:
        line = line.strip()
        list_line = line.split('\t')
        return_mat[index, :] = list_line[0:3]
        # if(listFromLine[-1].isdigit()):
        #     classLabelVector.append(int(listFromLine[-1]))
        # else:
        #     classLabelVector.append(love_dictionary.get(listFromLine[-1]))
        # index += 1
    return return_mat
