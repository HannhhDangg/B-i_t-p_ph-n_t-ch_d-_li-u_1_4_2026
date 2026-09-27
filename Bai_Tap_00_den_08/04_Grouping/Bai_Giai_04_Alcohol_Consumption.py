# ==============================================================================
# BÀI TẬP 04: GOM NHÓM DỮ LIỆU - GROUPBY (TIÊU THỤ ĐỒ UỐNG CÓ CỒN)
# Môn học: Phân tích dữ liệu với Python
# ==============================================================================

# Step 1: Import các thư viện cần thiết
import pandas as pd
import numpy as np

print("--- STEP 1: IMPORT THƯ VIỆN THÀNH CÔNG ---")

# Step 2 & 3: Đọc dữ liệu từ URL và gán vào biến drinks
url = 'https://raw.githubusercontent.com/thieu1995/csv-files/main/data/pandas/drinks.csv'
drinks = pd.read_csv(url)
print("\n--- STEP 2 & 3: DỮ LIỆU BAN ĐẦU ---")
print(drinks.head())

# Step 4: Châu lục nào tiêu thụ nhiều bia nhất trung bình?
beer_by_cont = drinks.groupby('continent')['beer_servings'].mean()
print("\n--- STEP 4: MỨC TIÊU THỤ BIA TRUNG BÌNH THEO CHÂU LỤC ---")
print(beer_by_cont)
top_beer = beer_by_cont.idxmax()
print(f"=> Châu lục uống nhiều bia nhất: {top_beer} ({beer_by_cont.max():.2f} phần)")

# Step 5: Thống kê mô tả chi tiết lượng rượu vang tiêu thụ theo từng châu lục
print("\n--- STEP 5: THỐNG KÊ RƯỢU VANG THEO CHÂU LỤC (.describe()) ---")
print(drinks.groupby('continent')['wine_servings'].describe())

# Step 6: Mức tiêu thụ trung bình của tất cả các cột số theo từng châu lục
# numeric_only=True giúp tránh lỗi FutureWarning/TypeError trên các phiên bản Pandas mới
print("\n--- STEP 6: MỨC TIÊU THỤ TRUNG BÌNH (MEAN) TẤT CẢ CỘT SỐ ---")
print(drinks.groupby('continent').mean(numeric_only=True))

# Step 7: Mức tiêu thụ trung vị của tất cả các cột số theo từng châu lục
print("\n--- STEP 7: MỨC TIÊU THỤ TRUNG VỊ (MEDIAN) TẤT CẢ CỘT SỐ ---")
print(drinks.groupby('continent').median(numeric_only=True))

# Step 8: In ra mean, min và max của lượng rượu mạnh (spirit_servings) theo từng châu lục
# Phương thức .agg([...]) cho phép tổng hợp nhiều phép tính thống kê cùng một lúc
spirit_stats = drinks.groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max'])
print("\n--- STEP 8: THỐNG KÊ RƯỢU MẠNH (MEAN, MIN, MAX) DƯỚI DẠNG DATAFRAME ---")
print(spirit_stats)

print("\nHoàn thành bài tập 04!")
