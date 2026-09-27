# ==============================================================================
# BÀI TẬP 00: TẠO SERIES VÀ DATAFRAME (POKEMON)
# Môn học: Phân tích dữ liệu với Python
# ==============================================================================

# Step 1: Import các thư viện cần thiết
# - pandas (pd): Thư viện xử lý và phân tích dữ liệu dạng bảng hàng đầu trong Python.
# - numpy (np): Thư viện tính toán mảng số học đa chiều hiệu năng cao.
import pandas as pd
import numpy as np

print("--- STEP 1: IMPORT THƯ VIỆN THÀNH CÔNG ---")

# Step 2: Tạo một data dictionary chứa thông tin các Pokemon
# Mỗi key là tên cột, mỗi value là danh sách (list) chứa các giá trị của cột đó.
raw_data = {
    'name': ['Bulbasaur', 'Charmander', 'Squirtle', 'Caterpie'],
    'evolution': ['Ivysaur', 'Charmeleon', 'Wartortle', 'Metapod'],
    'type': ['grass', 'fire', 'water', 'bug'],
    'hp': [45, 39, 44, 45],
    'pokedex': ['yes', 'no', 'yes', 'no']
}
print("\n--- STEP 2: DỮ LIỆU GỐC TỪ DICTIONARY ---")
print(raw_data)

# Step 3: Gán dictionary vào một biến tên là pokemon (Chuyển thành DataFrame)
# pd.DataFrame() nhận vào dictionary và biến nó thành bảng 2 chiều có chỉ số hàng (Index)
# và tên cột (Columns).
pokemon = pd.DataFrame(raw_data)
print("\n--- STEP 3: DATAFRAME BAN ĐẦU ---")
print(pokemon)

# Step 4: Sắp xếp lại thứ tự các cột thành: name, type, hp, evolution, pokedex
# Trong Python dictionary cũ hoặc khi tạo, thứ tự có thể theo alphabet hoặc tùy ý.
# Ta dùng danh sách tên cột để sắp xếp lại thứ tự hiển thị mong muốn.
columns_order = ['name', 'type', 'hp', 'evolution', 'pokedex']
pokemon = pokemon[columns_order]
print("\n--- STEP 4: DATAFRAME SAU KHI SẮP XẾP LẠI THỨ TỰ CỘT ---")
print(pokemon)

# Step 5: Thêm một cột mới có tên là 'place' và điền các địa danh tùy ý
# Lưu ý: Độ dài của list thêm vào phải bằng đúng số hàng của DataFrame (ở đây là 4).
pokemon['place'] = ['park', 'mountain', 'lake', 'forest']
print("\n--- STEP 5: DATAFRAME SAU KHI THÊM CỘT 'place' ---")
print(pokemon)

# Step 6: Hiển thị kiểu dữ liệu của từng cột
# .dtypes là thuộc tính (attribute), không phải hàm, trả về Series chứa kiểu dữ liệu của mỗi cột.
print("\n--- STEP 6: KIỂU DỮ LIỆU CỦA TỪNG CỘT (.dtypes) ---")
print(pokemon.dtypes)

# BONUS: Câu hỏi tự tạo và lời giải
# 1. Tìm Pokemon có HP cao nhất
max_hp = pokemon['hp'].max()
strongest_pokemon = pokemon[pokemon['hp'] == max_hp]
print("\n--- BONUS 1: POKEMON CÓ HP CAO NHẤT ---")
print(strongest_pokemon)

# 2. Lọc các Pokemon thuộc hệ cỏ ('grass')
grass_types = pokemon[pokemon['type'] == 'grass']
print("\n--- BONUS 2: CÁC POKEMON HỆ CỎ (GRASS) ---")
print(grass_types)

print("\nHoàn thành bài tập 00!")
