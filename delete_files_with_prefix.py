import os

def delete_files_with_prefix(directory, prefix=""):
    # Duyệt qua tất cả các tệp trong thư mục
    for filename in os.listdir(directory):
        # Kiểm tra nếu tệp bắt đầu bằng tiền tố đã chỉ định
        if '_aug' in filename:
            file_path = os.path.join(directory, filename)
            # Kiểm tra nếu đường dẫn là một tệp và xóa
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Đã xóa: {file_path}")

# Thay thế đường dẫn thư mục dưới đây bằng thư mục của bạn
directory_path = r'D:\BKAI\nighttime_aug_v1\train\image'
delete_files_with_prefix(directory_path)

directory_path = r'D:\BKAI\nighttime_aug_v1\train\label'
delete_files_with_prefix(directory_path)
