# Vẽ số lượng classes trong tập label


import os
from collections import Counter

import matplotlib.pyplot as plt

# Đường dẫn đến thư mục chứa các file .txt
bbox_dir = r'D:\BKAI\main_datasets\nighttime\nighttime_fold_0_YOLO\train\label'

# Khởi tạo Counter để đếm số lượng của mỗi class
class_counts = {
    0: 0,
    1: 0,
    2: 0,
    3: 0
}

# Lặp qua tất cả các file .txt trong thư mục
for filename in os.listdir(bbox_dir):
    if filename.lower().endswith('.txt'):
        file_path = os.path.join(bbox_dir, filename)
        # Mở file và đếm từng class trong đó
        with open(file_path, 'r') as file:
            for line in file:
                class_id = int(line.strip().split()[0])  # Lấy class_id từ dòng
                class_counts[class_id] += 1  # Tăng bộ đếm cho class_id

for i in range(4):
    print(class_counts[i])

# Trực quan hóa kết quả bằng biểu đồ cột
class_labels, counts = zip(*class_counts.items())
plt.bar(class_labels, counts, color='skyblue')
plt.xlabel('Class ID')
plt.ylabel('Số lượng')
plt.title('Số lượng từng Class trong các file .txt')
plt.xticks(rotation=45)
plt.show()