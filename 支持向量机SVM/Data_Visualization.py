from matplotlib import pyplot as plt
import numpy as np

"""
函数说明：
       生成数据集(生成属性矩阵,标签矩阵)
"""
def loadDataSet(filepath):
    attriMat = []                                              # 属性矩阵
    labelMat = []                                              # 标签矩阵
    fs = open(filepath, "r")                                   # 获取文件内容
    for line in fs.readlines():                                # fs为按行生成字符串列表
        line = line.strip().split("\t")                        # 去除首尾换行符\n，并按\t分割生成字符串列表
        attriMat.append([float(line[0]), float(line[1])])      # 将前2列作为属性
        labelMat.append(float(line[2]))                        # 将最后1列作为标签
    return attriMat, labelMat                                  # 将列表转换为numpy数组

"""
函数功能:
       数据可视化
"""
def showDataSet(attriMat, labelMat):
    attriMat_pos = []                                                                                      # 正样本属性矩阵
    attriMat_neg = []                                                                                      # 负样本属性矩阵
    n = len(labelMat)                                                                                      # 样本数量
    for i in range(n):                                                                                     # 将正负样本属性分开,便于绘图
        if labelMat[i] > 0:
            attriMat_pos.append(attriMat[i])
        else:
            attriMat_neg.append(attriMat[i])
    attriMat_pos = np.array(attriMat_pos)                                                                  # 将属性列表,标签列表转换为numpy数组格式，便于后面整体操作
    attriMat_neg = np.array(attriMat_neg)
    fig = plt.figure(figsize = (10, 8), dpi = 90)                                                          # 设置图片大小
    plt.scatter(np.transpose(attriMat_pos)[0], np.transpose(attriMat_pos)[1], label = "Postive Sample")    # np.transpose()将数组进行转置,绘制正样本散点图
    plt.scatter(np.transpose(attriMat_neg)[0], np.transpose(attriMat_neg)[1], label = "Negative Sample")   # np.transpose()将数组进行转置,绘制负样本散点图
    plt.title("Data Visualization")                                                                        # 设置图像标题
    plt.legend(loc = "upper left")                                                                         # 设置图例
    plt.show()

if __name__ == "__main__":
    filepath = "testSet.txt"                                                                               # 文件路径
    attriMat, labelMat = loadDataSet(filepath)
    showDataSet(attriMat, labelMat)
