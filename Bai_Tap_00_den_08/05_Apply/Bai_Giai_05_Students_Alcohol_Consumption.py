# ==============================================================================
# BÀI TẬP 05: ÁP DỤNG HÀM SỐ TRONG PANDAS - APPLY (HỌC SINH & ĐỒ UỐNG CÓ CỒN)
# Môn học: Phân tích dữ liệu với Python
# ==============================================================================

# Step 1: Import các thư viện cần thiết
import pandas as pd
import numpy as np

print("--- STEP 1: IMPORT THƯ VIỆN THÀNH CÔNG ---")

# Step 2 & 3: Đọc dữ liệu từ URL và gán vào biến df
url = 'https://raw.githubusercontent.com/thieu1995/csv-files/main/data/pandas/student-mat.csv'
df = pd.read_csv(url)
print("\n--- STEP 2 & 3: DỮ LIỆU BAN ĐẦU ---")
print(df.head())

# Step 4: Cắt lát DataFrame từ cột 'school' đến cột 'guardian'
# Cú pháp .loc[:, 'start_col':'end_col'] lấy từ cột bắt đầu đến cột kết thúc (bao gồm cả end_col)
df = df.loc[:, 'school':'guardian']
print("\n--- STEP 4: DỮ LIỆU SAU KHI CẮT LÁT (school -> guardian) ---")
print(df.head())

# Step 5: Tạo một lambda function viết hoa chữ cái đầu (capitalize)
capitalize_func = lambda x: x.capitalize() if isinstance(x, str) else x

# Step 6: Thử áp dụng hàm lên hai cột Mjob và Fjob
print("\n--- STEP 6: KẾT QUẢ APPLY LÊN CỘT Mjob VÀ Fjob (TRẢ VỀ SERIES MỚI) ---")
print("Mjob sau khi apply:")
print(df['Mjob'].apply(capitalize_func).head())

# Step 7: In ra các dòng cuối cùng của DataFrame gốc
print("\n--- STEP 7: CÁC DÒNG CUỐI CỦA DATAFRAME GỐC (VẪN LÀ CHỮ THƯỜNG) ---")
print(df[['Mjob', 'Fjob']].tail())

# Step 8: Giải thích và khắc phục việc DataFrame gốc vẫn là chữ thường
# Giải thích: .apply() không thay đổi trực tiếp (không có inplace=True).
# Khắc phục: Gán đè kết quả trả về vào cột cũ.
df['Mjob'] = df['Mjob'].apply(capitalize_func)
df['Fjob'] = df['Fjob'].apply(capitalize_func)
print("\n--- STEP 8: DATAFRAME SAU KHI ĐÃ GÁN ĐÈ (VIẾT HOA THÀNH CÔNG) ---")
print(df[['Mjob', 'Fjob']].tail())

# Step 9: Tạo hàm majority kiểm tra tuổi hợp pháp (> 17 tuổi) và tạo cột 'legal_drinker'
def majority(age):
    return age > 17

df['legal_drinker'] = df['age'].apply(majority)
print("\n--- STEP 9: THÊM CỘT 'legal_drinker' ---")
print(df[['school', 'age', 'legal_drinker']].head(10))

# Step 10: Nhân tất cả các giá trị số trong bảng với 10 (giữ nguyên chuỗi)
def multiply_10(val):
    # Lưu ý: bool là lớp con của int trong Python nên cần loại trừ kiểu bool
    if isinstance(val, (int, float, np.number)) and not isinstance(val, bool):
        return val * 10
    return val

# Trong Pandas 2.1+, dùng .map() thay thế cho .applymap()
if hasattr(df, 'map'):
    df_multiplied = df.map(multiply_10)
else:
    df_multiplied = df.applymap(multiply_10)

print("\n--- STEP 10: DATAFRAME SAU KHI NHÂN CÁC SỐ VỚI 10 ---")
print(df_multiplied.head())

print("\nHoàn thành bài tập 05!")
