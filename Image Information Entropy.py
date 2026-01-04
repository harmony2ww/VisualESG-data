import os
import cv2
import numpy as np
import pandas as pd
import re


IMAGE_ROOT_DIR = r"C:\Your_Project\Images" 

# 输出文件路径
OUTPUT_PAGE_LEVEL = "pages_entropy.xlsx"
OUTPUT_REPORT_LEVEL = "pdfs_entropy.xlsx"
# =========================================

def calculate_hsv_entropy(image_path):
    """
    NFIVI_IE
    """
    try:
        img = cv2.imread(image_path)
        if img is None:
            return None
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    except Exception:
        return None

    #  HSV  (OpenCV: H:0-180, S:0-255, V:0-255)
    color_ranges = {
        'black':  ([0, 0, 0], [180, 255, 46]),
        'gray':   ([0, 0, 46], [180, 43, 220]),
        'white':  ([0, 0, 221], [180, 30, 255]),
        'red1':   ([0, 43, 46], [10, 255, 255]),
        'red2':   ([156, 43, 46], [180, 255, 255]),
        'orange': ([11, 43, 46], [25, 255, 255]),
        'yellow': ([26, 43, 46], [34, 255, 255]),
        'green':  ([35, 43, 46], [77, 255, 255]),
        'cyan':   ([78, 43, 46], [99, 255, 255]),
        'blue':   ([100, 43, 46], [124, 255, 255]),
        'purple': ([125, 43, 46], [155, 255, 255])
    }

    
    counts = []
    
    kernel = np.ones((3, 3), np.uint8) 
    
    
    red_count = 0
    
    for color, (lower, upper) in color_ranges.items():
        lower_np = np.array(lower, dtype="uint8")
        upper_np = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv, lower_np, upper_np)
        mask = cv2.dilate(mask, kernel, iterations=2)
        count = cv2.countNonZero(mask)
        
        if 'red' in color:
            red_count += count
        else:
            counts.append(count)
    
    
    counts.append(red_count)
    
    total_pixels = sum(counts)
    if total_pixels == 0:
        return 0.0
        
    entropy = 0.0
    epsilon = 1e-10
    
    for c in counts:
        if c > 0:
            p = c / total_pixels
            entropy -= p * np.log2(p + epsilon)
            
    return entropy

def parse_filename(filename):
    
    match = re.search(r'(\d{4})_(\d{6})_(\d+)', filename)
    if match:
        return match.group(1), match.group(2), match.group(3)
    return None, None, None

def main():
    results = []
    print("start...")
    
    # 遍历文件夹
    count = 0
    for root, dirs, files in os.walk(IMAGE_ROOT_DIR):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                year, code, page = parse_filename(file)
                
                # 如果文件名不符合格式，跳过（或者你可以修改解析逻辑）
                if not year: 
                    continue
                    
                full_path = os.path.join(root, file)
                entropy = calculate_hsv_entropy(full_path)
                
                if entropy is not None:
                    results.append({
                        'Year': int(year),
                        'Code': code,  
                        'Page': int(page),
                        'NFIVI_IE': entropy
                    })
                
                count += 1
                if count % 100 == 0:
                    print(f" {count} images...")

    # 1. Page-level Excel
    df_page = pd.DataFrame(results)
    # 按 Year, Code, Page 排序
    df_page = df_page.sort_values(by=['Year', 'Code', 'Page'])
    df_page.to_excel(OUTPUT_PAGE_LEVEL, index=False)
    print(f"Page-level save in: {OUTPUT_PAGE_LEVEL}")

    # 2.Report-level Excel (Groupby Mean)
 
    df_report = df_page.groupby(['Year', 'Code'])['NFIVI_IE'].mean().reset_index()
    df_report.rename(columns={'NFIVI_IE': 'Avg_NFIVI_IE'}, inplace=True)
    
    df_counts = df_page.groupby(['Year', 'Code']).size().reset_index(name='Page_Count')
    df_report = pd.merge(df_report, df_counts, on=['Year', 'Code'])
    
    df_report.to_excel(OUTPUT_REPORT_LEVEL, index=False)
    print(f"Report-level save in: {OUTPUT_REPORT_LEVEL}")

if __name__ == "__main__":
    main()