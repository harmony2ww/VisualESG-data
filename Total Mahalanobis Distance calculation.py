# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:52:07 2024

@author: ice
"""


import pandas as pd
import numpy as np

# 重新加载数据集
file_path ='real path.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1')
# 简化的数据集
data_reduced = data[['Year', 'code', 'pages', 'Mahalanobis Distance']]

# 定义改进的马氏距离计算函数
def calculate_total_mahalanobis_distance_optimized(group):
    if len(group) < 2:
        return 0
    
    # 构建多维特征空间
    multivariate_data = group[['pages', 'Mahalanobis Distance']].values
    
    # 计算协方差矩阵
    cov_matrix = np.cov(multivariate_data, rowvar=False)
    
    # 添加一个小的常数到协方差矩阵的对角线上，以确保矩阵是可逆的
    cov_matrix += np.eye(cov_matrix.shape[0]) * 1e-10
    
    # 计算协方差矩阵的逆矩阵
    inv_cov_matrix = np.linalg.inv(cov_matrix)
    
    # 计算每对页面之间的马氏距离
    total_distance = 0
    for i in range(len(multivariate_data)):
        diff = multivariate_data - multivariate_data[i]
        mahalanobis_distances = np.sqrt(np.sum(np.dot(diff, inv_cov_matrix) * diff, axis=1))
        total_distance += np.sum(mahalanobis_distances)
    
    return total_distance / 2  # 每对距离计算了两次，除以2

# 计算所有年份和代码的总马氏距离
results = data_reduced.groupby(['Year', 'code']).apply(calculate_total_mahalanobis_distance_optimized).reset_index()
results.columns = ['Year', 'code', 'Total Mahalanobis Distance']



# 保存结果到Excel文件
output_file_path = 'Total_Mahalanobis_Distances_Parallel-new.xlsx'

results.to_excel(output_file_path, index=False)

print("结果已保存到:", output_file_path)