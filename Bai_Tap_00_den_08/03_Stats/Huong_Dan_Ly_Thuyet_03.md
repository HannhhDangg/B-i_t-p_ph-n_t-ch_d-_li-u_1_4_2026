# CẨM NANG HƯỚNG DẪN KIẾN THỨC VÀ LÝ THUYẾT: BÀI 03
## Chủ đề: Thống Kê Mô Tả Dữ Liệu (Bài tập US Baby Names)
*Dành cho người mới bắt đầu học Phân tích Dữ liệu với Python*

---

### 1. Mục tiêu bài học
Thống kê mô tả (**Descriptive Statistics**) là nền tảng cốt lõi của mọi nhà phân tích dữ liệu nhằm tóm tắt, đo lường các đặc trưng định lượng của tập dữ liệu:
- Nắm được cách dọn dẹp các cột thừa (Index cũ, ID trùng lặp) bằng `.drop()`.
- Phân tích phân phối tần suất của biến định tính (Categorical variable) với `.value_counts()`.
- Hiểu sâu bản chất toán học và ý nghĩa thực tế của:
  - **Mean (Trung bình)** và **Median (Trung vị)**: Khi nào nên dùng đại lượng nào?
  - **Standard Deviation (Độ lệch chuẩn)**: Đo lường mức độ biến thiên, rủi ro hay phân tán dữ liệu.
  - **Quartiles (Tứ phân vị 25%, 50%, 75%)**: Hiểu độ trải rộng của dữ liệu.
- Phân biệt giữa việc tìm giá trị cực đại (`.max()`) và tìm chỉ số định danh dòng chứa giá trị đó (`.idxmax()`).

---

### 2. Bảng từ điển các hàm và phương thức cốt lõi (Cheat Sheet)

| Tên hàm / Phương thức | Thư viện | Ý nghĩa & Chức năng | Tại sao lại dùng? | Cú pháp & Ví dụ minh họa |
| :--- | :--- | :--- | :--- | :--- |
| `df.drop(columns=..., inplace=True)` | Pandas | Xóa một hoặc nhiều cột khỏi DataFrame. | Loại bỏ các biến thừa không có giá trị phân tích, giải phóng bộ nhớ RAM. | `df.drop(columns=['Id', 'Unnamed: 0'], inplace=True)` |
| `series.value_counts()` | Pandas | Đếm số lần xuất hiện (tần suất) của từng giá trị độc nhất trong cột. | Thống kê nhanh cơ cấu phân bố của dữ liệu phân loại (ví dụ: tỷ lệ Nam/Nữ, ngành nghề). | `baby_names['Gender'].value_counts()` |
| `series.idxmax()` / `idxmin()` | Pandas | Trả về chỉ số dòng (Index label) chứa giá trị lớn nhất / nhỏ nhất. | Không chỉ biết con số lớn nhất là bao nhiêu, mà còn truy ngược lại được toàn bộ thông tin dòng đó. | `idx = names['Count'].idxmax()`<br>`names.loc[idx]` |
| `series.median()` | Pandas | Tính trung vị (giá trị nằm chính giữa sau khi sắp xếp). | Đại diện cho mức trung tâm đáng tin cậy khi dữ liệu có nhiều giá trị ngoại lai (Outliers) hoặc bị lệch. | `names['Count'].median()` |
| `series.std()` | Pandas | Tính độ lệch chuẩn (Standard Deviation). | Đo lường mức độ phân tán của dữ liệu xung quanh giá trị trung bình. | `names['Count'].std()` |
| `series.describe()` | Pandas | Tạo bảng tổng kết thống kê 8 chỉ số: count, mean, std, min, 25%, 50%, 75%, max. | Nắm trọn bức tranh toàn cảnh về phân phối số học của biến số chỉ bằng một dòng lệnh. | `names['Count'].describe()` |

---

### 3. Phân tích chi tiết từng Bước (Step-by-step)

#### **Step 5: Xóa cột thừa với `df.drop()`**
```python
cols_to_drop = [c for c in ['Unnamed: 0', 'Id'] if c in baby_names.columns]
baby_names.drop(columns=cols_to_drop, inplace=True)
```
- **Tại sao lại có cột `'Unnamed: 0'`?**: Khi xuất file CSV mà không chỉ định `index=False` (ví dụ `df.to_csv('file.csv')`), Pandas sẽ ghi cả chỉ số dòng vào file. Khi đọc lại bằng `read_csv()`, Pandas coi đó là một cột dữ liệu thông thường và tự đặt tên là `'Unnamed: 0'`.
- **`inplace=True` là gì?**: Mặc định, các hàm xử lý trong Pandas trả về một bản sao mới và giữ nguyên dữ liệu gốc. Truyền `inplace=True` giúp sửa đổi trực tiếp lên biến `baby_names` mà không cần viết `baby_names = baby_names.drop(...)`.

#### **Step 6: Đếm phân phối với `value_counts()`**
```python
baby_names['Gender'].value_counts()
```
- Cột `Gender` có 2 giá trị `'F'` (Female) và `'M'` (Male). Hàm này tự động đếm và sắp xếp số lần xuất hiện giảm dần.

#### **Step 7: Gom nhóm theo tên và tính tổng**
```python
names = baby_names.groupby('Name')['Count'].sum().reset_index()
```
- Trong dữ liệu gốc, mỗi tên (ví dụ: `Emma`) xuất hiện ở nhiều năm khác nhau và ở nhiều bang khác nhau.
- `groupby('Name')['Count'].sum()`: Gom toàn bộ các lần xuất hiện của tên `Emma` qua các năm lại và cộng dồn tổng số trẻ em được đặt tên này.
- `.reset_index()`: Chuyển `Name` từ chỉ số (Index) trở lại thành một cột bình thường trong DataFrame kết quả.

#### **Step 9: Tìm tên phổ biến nhất với `.idxmax()`**
```python
idx_max = names['Count'].idxmax()
most_popular_name = names.loc[idx_max]
```
- **Phân biệt `.max()` và `.idxmax()`**:
  - `names['Count'].max()` chỉ trả về một con số: ví dụ `242874`.
  - `names['Count'].idxmax()` trả về vị trí dòng (Index): ví dụ dòng `14120`.
  - Nhờ có vị trí dòng này, ta dùng `names.loc[idx_max]` để in ra được cả tên bé (`Jacob`) cùng số lượt sinh tương ứng!

#### **Step 11 & 12 & 13: Thống kê mô tả (Mean, Median, Std)**
- **Mean (Trung bình) vs Median (Trung vị)**:
  - Nếu Mean rất lệch so với Median, dữ liệu đang bị lệch mạnh (Skewed). Trong bài tập này, có một vài cái tên quá phổ biến (vài trăm nghìn lượt), trong khi hàng nghìn cái tên hiếm chỉ xuất hiện vài chục lần. Do đó, **Median** phản ánh số lần đặt tên phổ biến của một cái tên bình thường tốt hơn nhiều so với **Mean**.
- **Tứ phân vị (Quartiles: 25%, 50%, 75%)**:
  - 25% (Q1): 25% số lượng tên có lượt đặt nhỏ hơn giá trị này.
  - 50% (Q2): Chính là Median.
  - 75% (Q3): 75% số lượng tên có lượt đặt nhỏ hơn giá trị này.

---

### 4. Các lỗi phổ biến người mới hay mắc phải (Common Pitfalls)
1. **Lỗi `KeyError` khi drop cột**: Nếu cột đã bị drop rồi mà chạy lại lệnh `baby_names.drop(['Id'], axis=1)`, Python sẽ báo lỗi vì cột không còn tồn tại. Khắc phục: thêm `errors='ignore'`.
2. **Nhầm lẫn giữa `.max()` và `.idxmax()`**: Cố gắng truy xuất `names.loc[names['Count'].max()]` sẽ gây lỗi `KeyError` nghiêm trọng vì truyền nhầm giá trị lớn nhất vào chỗ chỉ số dòng.
3. **Quên `reset_index()`**: Sau khi `groupby()`, cột nhóm trở thành Index. Nếu muốn lọc hay vẽ biểu đồ dạng cột thông thường, nên dùng `.reset_index()`.

---

### 5. Đối chiếu giáo trình môn học (Slides Reference)
- **Slide Week2-Numpy (Trang 28 - 29)**:
  - Các hàm thống kê trong mảng số học: `np.mean()`, `np.median()`, `np.std()`, `np.min()`, `np.max()`.
- **Slide Week3-Pandas (Trang 17, 25 - 28)**:
  - *Trang 17*: Các hàm thống kê mô tả của DataFrame (`df.describe()`, `df.count()`, `df.sum()`).
  - *Trang 25 - 28*: Kỹ thuật làm sạch dữ liệu: Xóa cột thừa (`df.drop()`), xử lý dữ liệu khuyết.
