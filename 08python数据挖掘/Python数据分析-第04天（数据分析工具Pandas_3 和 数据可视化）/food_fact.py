# coding = utf-8

# 用来处理压缩文件
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # 数据集的路径
    data_path = "./data"
    # 压缩文件文件名
    zip_filename = "open-food-facts.zip"
    # 组合为完整的文件路径
    zip_filepath = os.path.join(data_path, zip_filename)
    #print(zip_filepath)

    data_filename = ""
    with zipfile.ZipFile(zip_filepath) as zipf:
        # 提取压缩包内所有的文件名，默认返回文件名列表
        data_filename = zipf.namelist()[0]

    # 组合为完整的数据路径
    data_filepath = os.path.join(data_path, data_filename)

    with zipfile.ZipFile(zip_filepath) as zipf:
        # 解压zip_filepath的文件，将压缩包里的文件解压到指定目录下
        zipf.extractall(path = data_path)

    #　读取csv文件里的指定的行的数据
    df_obj = pd.read_csv(data_filepath, usecols = ['countries_en','additives_n'])

    # 数据清洗：
    # 1. 去除缺失的数据
    #df_obj = df_obj.dropna()
    # inplace=True表示在原始数据上进行修改，不创建新的DataFrame对象
    # 默认inplace=False,需要创建新的对象
    df_obj.dropna(inplace=True)

    # 数据统计：
    # 2. 对数据进行分组统计
    data = df_obj['additives_n'].groupby(df_obj['countries_en']).mean()
    # 对data里的数据进行降序排序
    data = data.sort_values(ascending=False)
    #print(data.head(10))
    #print(type(data))

    # 3. 数据可视化
    # bar是展现柱形图
    data[:10].plot.bar()
    #保存可视化图片到本地磁盘文件里
    plt.savefig("food_fact.png")
    # 将可视化的图片展现出来
    plt.show()

    # 4. 数据存储
    #　将数据存储到本地csv文件里
    data.to_csv(data_path + "/newfood.csv")


if __name__ == "__main__":
    main()





