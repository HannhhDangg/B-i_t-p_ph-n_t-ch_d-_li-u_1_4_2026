# CẨM NANG HƯỚNG DẪN KIẾN THỨC VÀ LÝ THUYẾT: BÀI 05
## Chủ đề: Áp Dụng Hàm Tùy Biến - Apply (Bài tập Student Alcohol Consumption)
*Dành cho người mới bắt đầu học Phân tích Dữ liệu với Python*

---

### 1. Mục tiêu bài học
Trong thực tế, không phải lúc nào các hàm tích hợp sẵn của Pandas cũng đáp ứng được mọi yêu cầu nghiệp vụ phức tạp. Phương thức `.apply()` là cánh cửa giúp bạn tự do áp dụng bất kỳ hàm tự viết nào của Python (từ xử lý chuỗi, phân nhánh `if-else` đến các công thức toán học riêng) lên dữ liệu:
- Nắm vững cú pháp cắt lát nhãn cột bằng `.loc[:, 'cột_đầu':'cột_cuối']`.
- Hiểu rõ bản chất của **Hàm ẩn danh (Lambda Function)** và cách phối hợp với `.apply()`.
- Hiểu tại sao `.apply()` không tự động thay đổi dữ liệu gốc (Immutability) và cách gán đè.
- Thực hành tạo đặc trưng mới (Feature Engineering) dựa trên điều kiện logic.
- Phân biệt giữa `.apply()` (áp dụng trên từng cột hoặc hàng) và `.map()` / `.applymap()` (áp dụng trên từng ô dữ liệu đơn lẻ - Element-wise).

---

### 2. Bảng từ điển các hàm và phương thức cốt lõi (Cheat Sheet)

| Tên hàm / Cú pháp | Thư viện | Ý nghĩa & Chức năng | Tại sao lại dùng? | Cú pháp & Ví dụ minh họa |
| :--- | :--- | :--- | :--- | :--- |
| `df.loc[:, 'A':'B']` | Pandas | Trích xuất dải cột từ cột `A` đến cột `B`. | Tiện lợi khi cần lấy một cụm cột liên tiếp nhau mà không cần gõ hết danh sách tên cột. | `df.loc[:, 'school':'guardian']` |
| `lambda x: <biểu_thức>` | Python | Khai báo hàm ẩn danh ngắn gọn trong 1 dòng lệnh. | Viết nhanh các phép biến đổi đơn giản mà không cần đặt tên hàm bằng từ khóa `def`. | `cap = lambda x: x.capitalize()` |
| `series.apply(func)` | Pandas | Chuyền từng phần tử của Series qua hàm `func` và gom các giá trị trả về thành một Series mới. | Tối ưu hóa việc biến đổi dữ liệu cột dựa trên logic Python tự tạo. | `df['Mjob'] = df['Mjob'].apply(cap)` |
| `df.map(func)` | Pandas | Áp dụng hàm `func` lên **từng ô giá trị đơn lẻ** trong toàn bộ bảng DataFrame. | Thao tác trên mọi phần tử của bảng 2 chiều (trước phiên bản Pandas 2.1 gọi là `applymap`). | `df.map(multiply_10)` |
| `isinstance(object, type)` | Python | Kiểm tra kiểu dữ liệu của một biến. | Đảm bảo tính toán an toàn, tránh lỗi khi bảng dữ liệu có cả chữ lẫn số. | `isinstance(x, (int, float))` |

---

### 3. Phân tích chi tiết từng Bước (Step-by-step)

#### **Step 4: Cắt lát dải cột với `.loc`**
```python
df = df.loc[:, 'school':'guardian']
```
- **Điểm đặc biệt của `.loc`**:
  - Khi cắt lát theo nhãn (`'school':'guardian'`), Pandas **lấy bao gồm cả cột kết thúc** (`'guardian'`).
  - Điều này khác hoàn toàn với cắt lát theo vị trí số nguyên (`0:5` chỉ lấy từ 0 đến 4, loại trừ 5).

#### **Step 5: Hàm ẩn danh Lambda là gì?**
```python
capitalize_func = lambda x: x.capitalize() if isinstance(x, str) else x
```
- Thay vì viết:
  ```python
  def capitalize_func(x):
      if isinstance(x, str):
          return x.capitalize()
      return x
  ```
- Cú pháp `lambda` giúp gom toàn bộ logic thành 1 biểu thức duy nhất, rất tiện để truyền trực tiếp vào `.apply()`.

#### **Step 8: Tại sao DataFrame gốc không đổi và cách khắc phục?**
```python
df['Mjob'].apply(capitalize_func)      # DataFrame gốc VẪN KHÔNG ĐỔI!
df['Mjob'] = df['Mjob'].apply(capitalize_func) # ĐÃ ĐỔI THÀNH CÔNG
```
- **Nguyên lý quan trọng trong Pandas**: Đa số các hàm xử lý dữ liệu đều tuân theo nguyên tắc **Bất biến (Immutability)** để bảo vệ tính toàn vẹn của dữ liệu gốc. Hàm `.apply()` tạo ra một Series kết quả mới và đưa ra màn hình.
- Để lưu lại kết quả, bạn **bắt buộc phải dùng phép gán `=`** để ghi đè Series mới này vào vị trí cột cũ.

#### **Step 9: Tạo biến phân loại nhị phân (Feature Engineering)**
```python
def majority(age):
    return age > 17

df['legal_drinker'] = df['age'].apply(majority)
```
- Hàm nhận vào tuổi học sinh (`age`), kiểm tra điều kiện `> 17`.
- Kết quả tạo ra cột mới `legal_drinker` chứa giá trị `True` (nếu từ 18 tuổi trở lên) hoặc `False` (nếu từ 17 tuổi trở xuống). Đây là bước tiền xử lý dữ liệu cực kỳ phổ biến trong Học máy (Machine Learning).

#### **Step 10: Xử lý từng phần tử trên toàn bộ DataFrame**
```python
def multiply_10(val):
    if isinstance(val, (int, float, np.number)) and not isinstance(val, bool):
        return val * 10
    return val

df_multiplied = df.map(multiply_10)
```
- **Lưu ý chuyên sâu**: Trong Python, kiểu `bool` (`True`/`False`) thực chất là một lớp con kế thừa từ kiểu số nguyên `int` (`isinstance(True, int)` trả về `True`). Vì vậy, nếu chỉ kiểm tra `isinstance(val, int)`, giá trị `True` sẽ bị nhân thành `10`. Ta cần thêm điều kiện `and not isinstance(val, bool)` để bảo toàn các cột Boolean!

---

### 4. Các lỗi phổ biến người mới hay mắc phải (Common Pitfalls)
1. **Quên gán lại cột sau khi apply**: Nghĩ rằng `.apply()` tự động lưu thay đổi vào DataFrame gốc.
2. **Lỗi khi gọi `.str.capitalize()` trên cột có chứa dữ liệu thiếu (NaN) hoặc kiểu số**: Dùng `apply` với kiểm tra `isinstance(x, str)` là giải pháp an toàn nhất.
3. **Lạm dụng `.apply()` khi đã có phép toán vector hóa**:
   - Nếu muốn nhân một cột số với 10: Hãy dùng `df['age'] * 10` (nhanh hơn gấp nhiều lần so với `df['age'].apply(lambda x: x * 10)`).
   - Chỉ nên dùng `.apply()` khi logic phức tạp, có phân nhánh `if-else` hoặc xử lý chuỗi chuyên biệt.

---

### 5. Đối chiếu giáo trình môn học (Slides Reference)
- **Slide Week1-Intro (Trang 15 - 17)**: Quy trình tiền xử lý và làm sạch dữ liệu trong phân tích dữ liệu thực tế.
- **Slide Week3-Pandas (Trang 22 - 28)**:
  - *Trang 22 - 24*: Thao tác với DataFrame, truy xuất `.loc[]`.
  - *Trang 25 - 28*: Kỹ thuật làm sạch và biến đổi dữ liệu (Data Cleaning & Transformation).
