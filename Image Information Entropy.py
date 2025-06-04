import os
from PIL import Image
import numpy as np


def calculate_entropy(image_path):
    """计算图像的熵值"""
    image = Image.open(image_path).convert('L')  
    histogram = np.histogram(np.array(image).flatten(), bins=256, range=(0, 256))[0]
    histogram = histogram / histogram.sum()  
    entropy = -np.sum(histogram * np.log2(histogram + 1e-10))  
    return entropy

def calculate_color_entropy(image_path, color_channel):
    """计算指定颜色通道的熵值"""
    image = Image.open(image_path).convert('RGB')
    if color_channel == 'red':
        channel_data = np.array(image)[:, :, 0]
    elif color_channel == 'green':
        channel_data = np.array(image)[:, :, 1]
    elif color_channel == 'blue':
        channel_data = np.array(image)[:, :, 2]
    else:
        raise ValueError("color_channel must be 'red', 'green', or 'blue'")

    histogram = np.histogram(channel_data.flatten(), bins=256, range=(0, 256))[0]
    histogram = histogram / histogram.sum() 
    entropy = -np.sum(histogram * np.log2(histogram + 1e-10)) 
    return entropy