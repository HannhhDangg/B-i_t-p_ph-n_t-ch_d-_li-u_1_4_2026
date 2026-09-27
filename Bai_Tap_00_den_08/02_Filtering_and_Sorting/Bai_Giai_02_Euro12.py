# ==============================================================================
# BÀI TẬP 02: LỌC VÀ SẮP XẾP DỮ LIỆU (EURO 2012)
# Môn học: Phân tích dữ liệu với Python
# ==============================================================================

# Step 1: Import các thư viện cần thiết
import pandas as pd
import numpy as np

print("--- STEP 1: IMPORT THƯ VIỆN THÀNH CÔNG ---")

# Step 2 & 3: Đọc dữ liệu từ URL và gán vào biến euro12
url = 'https://raw.githubusercontent.com/thieu1995/csv-files/main/data/pandas/Euro_2012_stats_TEAM.csv'
euro12 = pd.read_csv(url)
print("\n--- STEP 2 & 3: DỮ LIỆU BAN ĐẦU ---")
print(euro12.head())

# Step 4: Chỉ chọn cột Goals (Bàn thắng)
print("\n--- STEP 4: CỘT BÀN THẮNG (Goals) ---")
print(euro12['Goals'])

# Step 5: Có bao nhiêu đội tham gia Euro 2012?
num_teams = euro12['Team'].nunique()
print(f"\n--- STEP 5: SỐ LƯỢNG ĐỘI BÓNG THAM GIA: {num_teams} ---")

# Step 6: Số lượng cột trong tập dữ liệu
num_cols = euro12.shape[1]
print(f"\n--- STEP 6: SỐ LƯỢNG CỘT: {num_cols} ---")

# Step 7: Chỉ chọn các cột Team, Yellow Cards và Red Cards gán vào DataFrame tên là discipline
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print("\n--- STEP 7: BẢNG KỶ LUẬT (discipline) ---")
print(discipline)

# Step 8: Sắp xếp các đội bóng theo Red Cards trước, sau đó đến Yellow Cards (giảm dần)
# Truyền danh sách cột và ascending=False để ưu tiên đội nhiều thẻ phạt nhất lên đầu
discipline_sorted = discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)
print("\n--- STEP 8: BẢNG KỶ LUẬT ĐÃ SẮP XẾP (GIẢM DẦN) ---")
print(discipline_sorted)

# Step 9: Tính số thẻ vàng trung bình mỗi đội nhận được
mean_yellow = discipline['Yellow Cards'].mean()
print(f"\n--- STEP 9: SỐ THẺ VÀNG TRUNG BÌNH MỖI ĐỘI: {mean_yellow:.2f} ---")

# Step 10: Lọc các đội ghi nhiều hơn 6 bàn thắng
high_scoring_teams = euro12[euro12['Goals'] > 6]
print("\n--- STEP 10: CÁC ĐỘI GHI NHIỀU HƠN 6 BÀN THẮNG ---")
print(high_scoring_teams[['Team', 'Goals']])

# Step 11: Chọn các đội bóng có tên bắt đầu bằng chữ 'G'
# Sử dụng phương thức xử lý chuỗi .str.startswith('G')
g_teams = euro12[euro12['Team'].str.startswith('G')]
print("\n--- STEP 11: CÁC ĐỘI BÓNG BẮT ĐẦU BẰNG CHỮ 'G' ---")
print(g_teams[['Team', 'Goals']])

# Step 12: Chọn 7 cột đầu tiên của tập dữ liệu
# Sử dụng .iloc[:, :7] (slicing theo chỉ số vị trí số nguyên)
first_7_cols = euro12.iloc[:, :7]
print("\n--- STEP 12: 7 CỘT ĐẦU TIÊN (iloc[:, :7]) ---")
print(first_7_cols.head())

# Step 13: Chọn tất cả các cột trừ 3 cột cuối cùng
# Dùng bước nhảy âm trong Python: :-3
all_except_last_3 = euro12.iloc[:, :-3]
print("\n--- STEP 13: TẤT CẢ CỘT TRỪ 3 CỘT CUỐI (iloc[:, :-3]) ---")
print(f"Tổng số cột ban đầu: {euro12.shape[1]}, số cột sau khi trừ 3 cột cuối: {all_except_last_3.shape[1]}")

# Step 14: Hiển thị độ chính xác sút bóng (Shooting Accuracy) của England, Italy và Russia
# Kết hợp .loc với điều kiện lọc bằng .isin()
selected_teams_accuracy = euro12.loc[euro12['Team'].isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']]
print("\n--- STEP 14: ĐỘ CHÍNH XÁC SÚT BÓNG CỦA ENGLAND, ITALY, RUSSIA ---")
print(selected_teams_accuracy)

print("\nHoàn thành bài tập 02!")
