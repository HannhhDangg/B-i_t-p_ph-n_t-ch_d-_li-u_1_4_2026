# ==============================================================================
# BÀI TẬP 01: KHÁM PHÁ VÀ LÀM QUEN VỚI DỮ LIỆU (CHIPOTLE)
# Môn học: Phân tích dữ liệu với Python
# ==============================================================================

# Step 1: Import các thư viện cần thiết
import pandas as pd
import numpy as np

print("--- STEP 1: IMPORT THƯ VIỆN THÀNH CÔNG ---")

# Step 2 & 3: Đọc dữ liệu từ URL và gán vào biến chipo
# Tệp chipotle.tsv là tệp phân cách bằng dấu tab (\t) thay vì dấu phẩy (,).
# Do đó ta bắt buộc phải truyền tham số sep='\t'.
url = 'https://raw.githubusercontent.com/thieu1995/csv-files/main/data/pandas/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')
print("\n--- STEP 2 & 3: ĐỌC DỮ LIỆU THÀNH CÔNG ---")
print(chipo.head())

# Step 4: Xem 10 dòng đầu tiên của tập dữ liệu
print("\n--- STEP 4: 10 DÒNG ĐẦU TIÊN (head(10)) ---")
print(chipo.head(10))

# Step 5: Số lượng quan sát (số dòng) trong tập dữ liệu
# .shape trả về tuple (số_dòng, số_cột) -> .shape[0] là số dòng
num_rows = chipo.shape[0]
print(f"\n--- STEP 5: SỐ LƯỢNG QUAN SÁT (DÒNG): {num_rows} ---")

# Step 6: Số lượng cột trong tập dữ liệu
num_cols = chipo.shape[1]
print(f"\n--- STEP 6: SỐ LƯỢNG CỘT: {num_cols} ---")

# Step 7: In ra tên của tất cả các cột
print("\n--- STEP 7: DANH SÁCH CÁC CỘT ---")
print(list(chipo.columns))

# Step 8: Tập dữ liệu được đánh chỉ số (index) như thế nào?
print("\n--- STEP 8: CHỈ SỐ (INDEX) CỦA DATAFRAME ---")
print(chipo.index)

# Step 9: Món ăn nào được đặt nhiều nhất?
# Nhóm theo 'item_name', tính tổng cột 'quantity', sau đó sắp xếp giảm dần
item_quants = chipo.groupby('item_name')['quantity'].sum().sort_values(ascending=False)
most_ordered_item = item_quants.index[0]
print(f"\n--- STEP 9: MÓN ĐƯỢC ĐẶT NHIỀU NHẤT: {most_ordered_item} ---")

# Step 10: Số lượng đã đặt của món đó là bao nhiêu?
most_ordered_qty = item_quants.iloc[0]
print(f"\n--- STEP 10: TỔNG SỐ LƯỢNG ĐÃ ĐẶT CỦA {most_ordered_item}: {most_ordered_qty} ---")

# Step 11: Món mô tả kèm theo (choice_description) nào được đặt nhiều nhất?
choice_quants = chipo.groupby('choice_description')['quantity'].sum().sort_values(ascending=False)
most_ordered_choice = choice_quants.index[0]
print(f"\n--- STEP 11: MÔ TẢ KÈM THEO ĐƯỢC ĐẶT NHIỀU NHẤT: {most_ordered_choice} ({choice_quants.iloc[0]} phần) ---")

# Step 12: Tổng số lượng tất cả các món đã được đặt
total_items = chipo['quantity'].sum()
print(f"\n--- STEP 12: TỔNG SỐ LƯỢNG MÓN ĐÃ ĐẶT: {total_items} ---")

# Step 13: Chuyển đổi cột item_price thành số thực (float)
# 13.a. Kiểm tra kiểu ban đầu
print(f"\n--- STEP 13.a: KIỂU DỮ LIỆU BAN ĐẦU CỦA item_price: {chipo['item_price'].dtype} ---")

# 13.b. Áp dụng lambda function để xóa ký tự '$' và ép kiểu float
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x.strip().replace('$', '')))

# 13.c. Kiểm tra lại kiểu dữ liệu
print(f"--- STEP 13.c: KIỂU DỮ LIỆU SAU KHI CHUYỂN ĐỔI: {chipo['item_price'].dtype} ---")
print(chipo['item_price'].head())

# Step 14: Tổng doanh thu trong toàn bộ thời gian của tập dữ liệu
# Trong dữ liệu Chipotle, giá trị trong cột 'item_price' là tổng giá tiền của dòng đó
revenue = chipo['item_price'].sum()
print(f"\n--- STEP 14: TỔNG DOANH THU: ${revenue:,.2f} ---")

# Step 15: Có bao nhiêu đơn hàng (orders) đã được thực hiện?
# Dùng .nunique() để đếm số lượng order_id duy nhất không trùng lặp
num_orders = chipo['order_id'].nunique()
print(f"\n--- STEP 15: TỔNG SỐ ĐƠN HÀNG: {num_orders} ---")

# Step 16: Doanh thu trung bình trên mỗi đơn hàng là bao nhiêu?
avg_revenue = chipo.groupby('order_id')['item_price'].sum().mean()
print(f"\n--- STEP 16: DOANH THU TRUNG BÌNH MỖI ĐƠN HÀNG: ${avg_revenue:.2f} ---")

# Step 17: Có bao nhiêu món ăn khác nhau được bán?
num_unique_items = chipo['item_name'].nunique()
print(f"\n--- STEP 17: SỐ LƯỢNG MÓN ĂN KHÁC NHAU: {num_unique_items} ---")

print("\nHoàn thành bài tập 01!")
