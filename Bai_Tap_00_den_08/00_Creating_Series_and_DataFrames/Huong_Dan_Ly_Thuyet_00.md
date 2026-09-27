# CẨM NANG HƯỚNG DẪN KIẾN THỨC VÀ LÝ THUYẾT: BÀI 00
## Chủ đề: Khởi Tạo Series và DataFrame (Bài tập Pokemon)
*Dành cho người mới bắt đầu học Phân tích Dữ liệu với Python*

---

### 1. Mục tiêu bài học
Bài học này giúp bạn làm quen với hai cấu trúc dữ liệu nền tảng quan trọng nhất trong thư viện Pandas: **Series** (mảng 1 chiều có nhãn) và **DataFrame** (bảng dữ liệu 2 chiều). Bạn sẽ nắm vững:
- Cách chuyển đổi cấu trúc dữ liệu gốc của Python (Dictionary / List) thành một DataFrame chuẩn mực.
- Cách truy xuất, thay đổi thứ tự các cột (Column Reordering).
- Cách thêm một cột mới vào bảng dữ liệu có sẵn.
- Cách kiểm tra kiểu dữ liệu của từng cột để phục vụ cho các bước phân tích sau này.

---

### 2. Bảng từ điển các hàm và thuộc tính cốt lõi (Cheat Sheet)

| Tên hàm / Thuộc tính | Thư viện | Ý nghĩa & Chức năng | Tại sao lại dùng? | Cú pháp & Cách dùng |
| :--- | :--- | :--- | :--- | :--- |
| `import pandas as pd` | Python | Nạp thư viện Pandas và đặt bí danh ngắn gọn là `pd`. | Quy ước chuẩn quốc tế trong cộng đồng khoa học dữ liệu, giúp viết code ngắn gọn hơn. | `import pandas as pd` |
| `pd.DataFrame(data)` | Pandas | Hàm khởi tạo cấu trúc dữ liệu 2 chiều (DataFrame). | Chuyển đổi dữ liệu thô (dictionary, list of lists, numpy array) thành dạng bảng có chỉ số hàng (Index) và tên cột (Columns). | `df = pd.DataFrame(raw_data)` |
| `df[['colA', 'colB']]` | Pandas | Fancy Indexing / Lọc chọn nhiều cột theo thứ tự mong muốn. | Cho phép tạo ra một DataFrame con hoặc định nghĩa lại thứ tự hiển thị của các cột. | `df = df[['name', 'type', 'hp']]` |
| `df['new_col'] = values` | Pandas | Thêm một cột mới vào DataFrame. | Bổ sung biến số hoặc đặc trưng mới (Feature Engineering) cho bảng dữ liệu. | `df['place'] = ['A', 'B', 'C', 'D']` |
| `df.dtypes` | Pandas | Thuộc tính (Attribute) trả về kiểu dữ liệu của mỗi cột. | Giúp kiểm tra nhanh xem cột nào là số (`int64`, `float64`), cột nào là chuỗi ký tự (`object`). | `df.dtypes` *(Không có dấu ngoặc tròn vì là thuộc tính)* |
| `df['col'].max()` | Pandas | Tính giá trị lớn nhất trong một cột số. | Dùng trong thống kê cơ bản để tìm biên cực đại. | `max_val = df['hp'].max()` |
| `df[condition]` | Pandas | Lọc các dòng thỏa mãn điều kiện logic (Boolean Indexing). | Lấy ra các mẫu dữ liệu quan tâm một cách trực quan, tối ưu tốc độ tính toán. | `df[df['hp'] == max_val]` |

---

### 3. Phân tích chi tiết từng Bước (Step-by-step)

#### **Step 1: Import thư viện**
```python
import pandas as pd
import numpy as np
```
- **Tại sao?**: Mọi tác vụ phân tích bảng dữ liệu trong Python đều bắt đầu bằng việc nạp Pandas (`pd`). Thư viện NumPy (`np`) thường đi kèm vì Pandas được xây dựng trực tiếp trên nền tảng mảng của NumPy (được học tại Slide *Week2-Numpy*).

#### **Step 2 & Step 3: Tạo Dictionary và chuyển thành DataFrame**
```python
raw_data = {
    'name': ['Bulbasaur', 'Charmander', 'Squirtle', 'Caterpie'],
    'evolution': ['Ivysaur', 'Charmeleon', 'Wartortle', 'Metapod'],
    'type': ['grass', 'fire', 'water', 'bug'],
    'hp': [45, 39, 44, 45],
    'pokedex': ['yes', 'no', 'yes', 'no']
}
pokemon = pd.DataFrame(raw_data)
```
- **Cơ chế hoạt động**:
  - Mỗi `key` trong Dictionary đại diện cho **Tên một cột** (Column Name).
  - `value` tương ứng là một `list` đại diện cho **Các giá trị trong cột đó** theo từng hàng.
  - Khi đưa vào `pd.DataFrame()`, Pandas tự động tạo chỉ số hàng mặc định bắt đầu từ `0` đến `n-1` (ở đây là `0, 1, 2, 3`).
- **So sánh**: Bạn có thể dùng list of lists hoặc list of dicts, nhưng dict of lists là cách khởi tạo trực quan và phổ biến nhất.

#### **Step 4: Đổi thứ tự các cột**
```python
pokemon = pokemon[['name', 'type', 'hp', 'evolution', 'pokedex']]
```
- **Tại sao lại dùng 2 dấu ngoặc vuông `[[ ... ]]`?**:
  - Dấu ngoặc ngoài `pokemon[...]` là cú pháp lấy phần tử trong DataFrame.
  - Dấu ngoặc trong `[...]` định nghĩa một danh sách (Python list) gồm các tên cột: `['name', 'type', 'hp', ...]`.
  - Nếu chỉ dùng 1 ngoặc vuông `pokemon['name']`, kết quả trả về là một **Series** (1 cột). Khi dùng 2 ngoặc vuông, kết quả trả về luôn là một **DataFrame** (dù chỉ có 1 cột).

#### **Step 5: Thêm cột mới `place`**
```python
pokemon['place'] = ['park', 'mountain', 'lake', 'forest']
```
- **Quy tắc quan trọng**: Số phần tử trong danh sách thêm vào phải **bằng chính xác** số hàng hiện có của DataFrame (ở đây có 4 Pokemon thì danh sách phải có đúng 4 địa danh). Nếu thiếu hoặc thừa, Python sẽ báo lỗi `ValueError: Length of values does not match length of index`.

#### **Step 6: Hiển thị kiểu dữ liệu của các cột**
```python
pokemon.dtypes
```
- **Kết quả hiển thị**:
  - `name`: `object` (kiểu chuỗi / text trong Pandas).
  - `type`: `object`.
  - `hp`: `int64` (kiểu số nguyên 64-bit).
  - `evolution`: `object`.
  - `pokedex`: `object`.
  - `place`: `object`.
- **Lưu ý**: `.dtypes` là thuộc tính (Property), không được viết `pokemon.dtypes()`.

---

### 4. Các lỗi phổ biến người mới hay mắc phải (Common Pitfalls)
1. **Lẫn lộn giữa Series và DataFrame**:
   - `pokemon['hp']` -> Trả về 1 Series (mảng 1 chiều có nhãn).
   - `pokemon[['hp']]` -> Trả về 1 DataFrame (bảng 2 chiều có 1 cột).
2. **Lỗi `KeyError`**: Xảy ra khi gõ sai tên cột (ví dụ viết `'Name'` thay vì `'name'`). Python phân biệt chữ hoa, chữ thường!
3. **Thêm cột lệch số lượng dòng**: Gán một list có 3 phần tử vào DataFrame có 4 dòng sẽ gây lỗi ngay lập tức.

---

### 5. Đối chiếu giáo trình môn học (Slides Reference)
- **Slide Week2-Numpy (Trang 3 - 14)**: Nền tảng về mảng số học ndarray, indexing từ 0 và các phép tính vector hóa.
- **Slide Week3-Pandas (Trang 4 - 15)**:
  - *Trang 4*: Định nghĩa Series và DataFrame.
  - *Trang 8 - 14*: Các cách khởi tạo Series và DataFrame từ Dictionary, List, Tuple.
  - *Trang 15 - 16*: Các thuộc tính cơ bản của DataFrame: `df.shape`, `df.columns`, `df.index`, `df.dtypes`.
