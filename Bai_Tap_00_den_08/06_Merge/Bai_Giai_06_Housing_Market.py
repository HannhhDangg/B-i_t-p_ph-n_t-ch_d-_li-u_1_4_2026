# ==============================================================================
# BÀI TẬP 06: GHÉP NỐI DỮ LIỆU - CONCAT & MERGE (THỊ TRƯỜNG NHÀ ĐẤT)
# Môn học: Phân tích dữ liệu với Python
# ==============================================================================

# Step 1: Import các thư viện cần thiết
import pandas as pd
import numpy as np

print("--- STEP 1: IMPORT THƯ VIỆN THÀNH CÔNG ---")

# Step 2: Tạo 3 Series ngẫu nhiên, độ dài 100
# - s1: số phòng ngủ từ 1 đến 4 (lưu ý: randint(1, 5) lấy từ 1 đến 4 vì cận trên bị loại trừ)
# - s2: số phòng tắm từ 1 đến 3 (randint(1, 4))
# - s3: giá tiền mỗi m2 từ 10,000 đến 30,000 (randint(10000, 30001))
np.random.seed(42) # Cố định seed ngẫu nhiên

s1 = pd.Series(np.random.randint(1, 5, size=100))
s2 = pd.Series(np.random.randint(1, 4, size=100))
s3 = pd.Series(np.random.randint(10000, 30001, size=100))

print("\n--- STEP 2: TẠO 3 SERIES THÀNH CÔNG ---")
print(f"Độ dài s1: {len(s1)}, s2: {len(s2)}, s3: {len(s3)}")

# Step 3: Ghép 3 Series theo cột (axis=1) để tạo DataFrame
# pd.concat() ghép các đối tượng Pandas theo một trục chỉ định
house = pd.concat([s1, s2, s3], axis=1)
print("\n--- STEP 3: DATAFRAME GHÉP THEO CỘT (axis=1) ---")
print(house.head())

# Step 4: Đổi tên các cột thành: bedrs, bathrs, price_sqr_meter
house.columns = ['bedrs', 'bathrs', 'price_sqr_meter']
print("\n--- STEP 4: DATAFRAME SAU KHI ĐỔI TÊN CỘT ---")
print(house.head())

# Step 5: Tạo DataFrame 1 cột ghép 3 Series theo chiều dọc (axis=0) gán vào 'bigcolumn'
# .to_frame() chuyển Series kết quả thành DataFrame
bigcolumn = pd.concat([s1, s2, s3], axis=0).to_frame(name='bigcolumn')
print("\n--- STEP 5: DATAFRAME 'bigcolumn' GHÉP DỌC (axis=0) ---")
print(bigcolumn)

# Step 6: Kiểm tra hiện tượng chỉ số chỉ chạy đến 99
# Giải thích: Mặc dù tổng số hàng là 300, nhưng do 3 Series gốc đều có index từ 0..99
# nên khi nối dọc, index cũ được giữ nguyên, dẫn đến có 3 dòng mang index 0, 3 dòng mang index 1...
print("\n--- STEP 6: KIỂM TRA CHỈ SỐ INDEX ---")
print(f"Tổng số dòng: {len(bigcolumn)}")
print(f"Giá trị index lớn nhất: {bigcolumn.index.max()}")
print("Xem các dòng tại vị trí giao thoa giữa s1 và s2 (dòng 98 đến 102):")
print(bigcolumn.iloc[98:103])

# Step 7: Đánh lại chỉ số (Reindex) từ 0 đến 299
# Sử dụng reset_index(drop=True) để bỏ index cũ và thay thế bằng RangeIndex từ 0 đến n-1
bigcolumn.reset_index(drop=True, inplace=True)
print("\n--- STEP 7: SAU KHI RESET INDEX LIÊN TỤC TỪ 0 ĐẾN 299 ---")
print(f"Chỉ số mới: {bigcolumn.index}")
print("Kiểm tra lại dòng 98 đến 102 sau khi reset:")
print(bigcolumn.iloc[98:103])

print("\nHoàn thành bài tập 06!")
