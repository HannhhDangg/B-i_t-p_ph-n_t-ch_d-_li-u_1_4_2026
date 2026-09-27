# ==============================================================================
# BÀI TẬP 08: XÓA VÀ XỬ LÝ DỮ LIỆU THIẾU - DELETING & MISSING DATA (HOA IRIS)
# Môn học: Phân tích dữ liệu với Python
# ==============================================================================

# Step 1: Import các thư viện cần thiết
import pandas as pd
import numpy as np

print("--- STEP 1: IMPORT THƯ VIỆN THÀNH CÔNG ---")

# Step 2 & 3: Đọc dữ liệu từ URL và gán vào biến iris
# Tệp iris.data là dữ liệu thuần túy, không có dòng tiêu đề cột
# Do đó ta bắt buộc phải dùng header=None
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None)
print("\n--- STEP 2 & 3: DỮ LIỆU BAN ĐẦU (CHƯA CÓ TÊN CỘT) ---")
print(iris.head())

# Step 4: Đặt tên cột cho tập dữ liệu
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
print("\n--- STEP 4: DỮ LIỆU SAU KHI ĐẶT TÊN CỘT ---")
print(iris.head())

# Step 5: Kiểm tra xem có giá trị thiếu (NaN / Missing value) nào không
# .isnull().sum() đếm số ô bị rỗng ở từng cột
missing_count = iris.isnull().sum()
print("\n--- STEP 5: SỐ LƯỢNG GIÁ TRỊ THIẾU BAN ĐẦU ---")
print(missing_count)

# Step 6: Gán các giá trị từ dòng 10 đến 29 của cột 'petal_length' thành NaN
# Dùng .iloc[10:30, 2] = np.nan (chỉ số 10 đến 29, cột thứ 3 mang index 2)
iris.iloc[10:30, 2] = np.nan
print("\n--- STEP 6: KIỂM TRA SAU KHI GÁN NaN VÀO CỘT petal_length (DÒNG 10-14) ---")
print(iris.loc[10:14, ['sepal_length', 'petal_length']])

# Step 7: Thay thế các giá trị NaN vừa tạo bằng số 1.0 (Điền khuyết)
iris['petal_length'] = iris['petal_length'].fillna(1.0)
print("\n--- STEP 7: SAU KHI ĐIỀN 1.0 VÀO CÁC Ô NaN (DÒNG 10-14) ---")
print(iris.loc[10:14, ['sepal_length', 'petal_length']])

# Step 8: Xóa cột 'class' khỏi DataFrame
del iris['class']
# Hoặc: iris.drop(columns=['class'], inplace=True)
print("\n--- STEP 8: DỮ LIỆU SAU KHI XÓA CỘT 'class' ---")
print(iris.head())

# Step 9: Gán 3 dòng đầu tiên của DataFrame thành NaN
iris.iloc[0:3, :] = np.nan
print("\n--- STEP 9: 3 DÒNG ĐẦU TIÊN BỊ GÁN THÀNH NaN ---")
print(iris.head(5))

# Step 10: Xóa các dòng có chứa giá trị NaN
# dropna(axis=0) loại bỏ bất kỳ dòng nào có ít nhất một giá trị NaN
iris.dropna(axis=0, inplace=True)
print("\n--- STEP 10: DỮ LIỆU SAU KHI XÓA CÁC DÒNG CHỨA NaN ---")
print(iris.head(5))

# Step 11: Đặt lại chỉ số (Reset Index) để chỉ số chạy lại từ 0
# Do 3 dòng đầu bị xóa, index hiện tại đang bắt đầu từ 3 -> cần reset
iris.reset_index(drop=True, inplace=True)
print("\n--- STEP 11: SAU KHI RESET INDEX BẮT ĐẦU TỪ 0 ---")
print(iris.head(5))

# BONUS: Kích thước cuối cùng và thống kê mô tả
print(f"\n--- BONUS: KÍCH THƯỚC CUỐI CÙNG: {iris.shape} (ĐÃ MẤT 3 HÀNG VÀ 1 CỘT) ---")
print("\nBảng thống kê mô tả sau khi làm sạch:")
print(iris.describe())

print("\nHoàn thành bài tập 08!")
