# ==============================================================================
# BÀI TẬP 03: THỐNG KÊ DỮ LIỆU (US BABY NAMES)
# Môn học: Phân tích dữ liệu với Python
# ==============================================================================

# Step 1: Import các thư viện cần thiết
import pandas as pd
import numpy as np

print("--- STEP 1: IMPORT THƯ VIỆN THÀNH CÔNG ---")

# Step 2 & 3: Đọc dữ liệu từ URL và gán vào biến baby_names
url = 'https://raw.githubusercontent.com/thieu1995/csv-files/main/data/pandas/US_Baby_Names_right.csv'
baby_names = pd.read_csv(url)
print("\n--- STEP 2 & 3: DỮ LIỆU BAN ĐẦU ---")
print(baby_names.head())

# Step 4: Xem 10 dòng đầu tiên
print("\n--- STEP 4: 10 DÒNG ĐẦU TIÊN ---")
print(baby_names.head(10))

# Step 5: Xóa các cột thừa 'Unnamed: 0' và 'Id'
# Dùng drop(columns=...) với inplace=True để sửa đổi trực tiếp DataFrame
cols_to_drop = [c for c in ['Unnamed: 0', 'Id'] if c in baby_names.columns]
baby_names.drop(columns=cols_to_drop, inplace=True)
print("\n--- STEP 5: DỮ LIỆU SAU KHI XÓA CỘT THỪA ---")
print(baby_names.head())

# Step 6: Trong tập dữ liệu, số lượng tên cho Bé gái (F) hay Bé trai (M) nhiều hơn?
gender_counts = baby_names['Gender'].value_counts()
print("\n--- STEP 6: PHÂN PHỐI THEO GIỚI TÍNH ---")
print(gender_counts)
if gender_counts['F'] > gender_counts['M']:
    print("=> Kết luận: Số lượng tên Bé gái (F) nhiều hơn số lượng tên Bé trai (M).")
else:
    print("=> Kết luận: Số lượng tên Bé trai (M) nhiều hơn số lượng tên Bé gái (F).")

# Step 7: Nhóm theo tên (Name) và tính tổng số lượng sinh (Count), gán vào biến names
names = baby_names.groupby('Name')['Count'].sum().reset_index()
print("\n--- STEP 7: DỮ LIỆU TỔNG SỐ LƯỢNG THEO TÊN (names) ---")
print(names.head())

# Step 8: Có bao nhiêu tên khác nhau tồn tại trong tập dữ liệu?
num_names = len(names)
print(f"\n--- STEP 8: SỐ LƯỢNG TÊN KHÁC NHAU: {num_names} ---")

# Step 9: Tên nào xuất hiện nhiều nhất (được đặt nhiều nhất)?
# Dùng .idxmax() để tìm chỉ số dòng có giá trị Count lớn nhất
idx_max = names['Count'].idxmax()
most_popular_name = names.loc[idx_max]
print("\n--- STEP 9: TÊN ĐƯỢC ĐẶT NHIỀU NHẤT ---")
print(most_popular_name)

# Step 10: Có bao nhiêu tên khác nhau có số lần xuất hiện ít nhất?
min_val = names['Count'].min()
num_least_popular = (names['Count'] == min_val).sum()
print(f"\n--- STEP 10: SỐ LƯỢNG TÊN CÓ LƯỢT ĐẶT ÍT NHẤT ({min_val} lần): {num_least_popular} ---")

# Step 11: Giá trị trung vị (Median) của số lần xuất hiện tên
median_count = names['Count'].median()
print(f"\n--- STEP 11: TRUNG VỊ (MEDIAN): {median_count} ---")

# Step 12: Độ lệch chuẩn (Standard Deviation)
std_count = names['Count'].std()
print(f"\n--- STEP 12: ĐỘ LỆCH CHUẨN (STD): {std_count:.2f} ---")

# Step 13: Bảng tóm tắt thống kê mô tả (Mean, Min, Max, Std, Phân vị)
print("\n--- STEP 13: TỔNG KẾT THỐNG KÊ MÔ TẢ (.describe()) ---")
print(names['Count'].describe())

print("\nHoàn thành bài tập 03!")
