# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:13:53 2024

@author: ice
"""

import pandas as pd
import numpy as np
from scipy.spatial.distance import mahalanobis

# 加载Excel文件
file_path = 'real path.xlsx'  # 请将此处替换为实际的文件路径

df = pd.read_excel(file_path, sheet_name='ESG_pages')  # 如果工作表名称不同，请替换 'Sheet1'

# 去除前6列
df_reduced = df.iloc[:, 6:]

# 计算协方差矩阵的逆矩阵
cov_matrix = np.cov(df_reduced, rowvar=False)
inv_cov_matrix = np.linalg.inv(cov_matrix)

# 计算马氏距离
def compute_mahalanobis(row, data, inv_cov_matrix):
    return mahalanobis(row, data.mean(axis=0), inv_cov_matrix)

# 初始化进度信息
# 初始化进度信息
total_rows = len(df_reduced)
progress_interval = max(1, total_rows // 100)  # 每处理1%的数据输出一次进度
processed_rows = 0

# 对每一行计算马氏距离
mahalanobis_distances = []
for index, row in df_reduced.iterrows():
    distance = compute_mahalanobis(row, df_reduced, inv_cov_matrix)
    mahalanobis_distances.append(distance)
    
    # 更新进度信息
    processed_rows += 1
    if processed_rows % progress_interval == 0 or processed_rows == total_rows:
        print(f"已处理 {processed_rows} 行，共 {total_rows} 行。")

# 将结果添加到DataFrame中
df['Mahalanobis Distance'] = mahalanobis_distances

# 将结果保存为Excel文件
output_path = 'maha_dis.xlsx'
df.to_excel(output_path, index=False)

print(f"马氏距离已计算并保存至 {output_path}")
