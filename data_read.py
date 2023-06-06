# 导入pickle模块
import pickle
# 导入numpy模块
import numpy as np


# # 以二进制读模式打开pickle文件
# file = open('./pdb_files/input1/fingerprint_dict.pickle', 'rb')
#
# # 从文件中读取数据并转换为Python的类型
# data = pickle.load(file)
# print(data)
# # 关闭文件
# file.close()


# 从npy文件中读取一个数组
examples = np.load('./pdb_files/input1/train_examples_one_five.npy')
print(examples)
