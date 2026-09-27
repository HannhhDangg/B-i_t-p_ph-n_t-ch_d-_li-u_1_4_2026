# CẨM NANG HƯỚNG DẪN KIẾN THỨC VÀ LÝ THUYẾT: BÀI 08
## Chủ đề: Xóa Và Xử Lý Dữ Liệu Khuyết Thiếu - Deleting & Missing Values (Bài tập Hoa Iris)
*Dành cho người mới bắt đầu học Phân tích Dữ liệu với Python*

---

### 1. Mục tiêu bài học
Trong thực tế, dữ liệu thu thập từ các hệ thống, cảm biến hay người dùng khảo sát hầu như không bao giờ hoàn hảo mà luôn chứa các giá trị rỗng, lỗi đo đạc hay bị khuyết thiếu (**Missing Data / NaN**). Bài học này trang bị kỹ năng làm sạch dữ liệu quan trọng nhất:
- Xử lý các tệp dữ liệu không có sẵn dòng tiêu đề cột (`header=None`) và tự đặt tên cột chuẩn hóa.
- Phát hiện, đếm và định vị các giá trị bị khuyết (`.isnull()` / `.isna()`).
- Hiểu bản chất số học kỳ lạ của `np.nan` trong NumPy và Pandas.
- Hai chiến lược xử lý dữ liệu thiếu hàng đầu trong Khoa học Dữ liệu:
  1. **Điền khuyết (Imputation)** với `.fillna()`.
  2. **Loại bỏ (Deletion)** với `.dropna()`.
- Xóa bỏ biến số/cột phân loại bằng lệnh `del` hoặc `.drop()`.
- Khôi phục chỉ số dòng tuần tự bằng `.reset_index(drop=True)`.

---

### 2. Bảng từ điển các hàm và phương thức cốt lõi (Cheat Sheet)

| Tên hàm / Cú pháp | Thư viện | Ý nghĩa & Chức năng | Tại sao lại dùng? | Cú pháp & Ví dụ minh họa |
| :--- | :--- | :--- | :--- | :--- |
| `pd.read_csv(..., header=None)` | Pandas | Đọc dữ liệu không có dòng tiêu đề cột. | Ngăn Pandas lấy nhầm dòng dữ liệu đầu tiên làm tên cột. | `df = pd.read_csv('iris.data', header=None)` |
| `df.isnull().sum()` | Pandas | Kiểm tra ô nào là NaN và đếm tổng số lượng ô rỗng ở từng cột. | Thao tác kiểm tra chất lượng dữ liệu (Data Quality Check) bắt buộc trong mọi dự án. | `iris.isnull().sum()` |
| `np.nan` | NumPy | Đối tượng biểu diễn "Not a Number" (giá trị rỗng, thiếu). | Chuẩn số học IEEE 754 dùng trong Pandas/NumPy để đánh dấu dữ liệu bị khuyết. | `df.iloc[0, 0] = np.nan` |
| `series.fillna(val)` | Pandas | Thay thế tất cả các vị trí NaN bằng một giá trị thay thế `val`. | Giữ lại các mẫu dữ liệu quý giá thay vì xóa bỏ chúng (có thể điền 0, trung bình, hoặc trung vị). | `df['petal_length'] = df['petal_length'].fillna(1.0)` |
| `del df['col']` | Python | Xóa vĩnh viễn một cột khỏi DataFrame. | Cú pháp Python thuần ngắn gọn để loại bỏ cột thừa. | `del df['class']` |
| `df.dropna(axis=0, how='any')` | Pandas | Loại bỏ các dòng (hoặc cột) chứa giá trị NaN. | Dọn sạch hoàn toàn các bản ghi lỗi hoặc thiếu sót trước khi đưa vào mô hình phân tích. | `df.dropna(axis=0, inplace=True)` |
| `df.reset_index(drop=True)` | Pandas | Tái lập chỉ số hàng bắt đầu từ 0 đến n-1. | Khắc phục hiện tượng "thủng chỉ số" sau khi một số dòng bị xóa bỏ. | `df.reset_index(drop=True, inplace=True)` |

---

### 3. Phân tích chi tiết từng Bước (Step-by-step)

#### **Step 2 & 4: Tại sao cần `header=None`?**
```python
iris = pd.read_csv(url, header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
```
- Mặc định, `pd.read_csv()` coi dòng số 1 trong file là tên các cột (`header=0`). Nếu tệp `iris.data` không có tên cột mà chỉ có số liệu (`5.1, 3.5, 1.4, 0.2, Iris-setosa`), Pandas sẽ lấy luôn số `5.1` làm tên cột 1!
- Do đó, bắt buộc phải khai báo `header=None` để Pandas đánh tên cột tạm thời là `0, 1, 2, 3, 4`, sau đó ta gán lại danh sách tên cột có nghĩa.

#### **Step 5: Bản chất kỳ lạ của `np.nan`**
```python
iris.isnull().sum()
```
- **Lưu ý cực kỳ quan trọng**: Trong Python, `np.nan` là một số thực đặc biệt và **không bằng chính nó**:
  ```python
  np.nan == np.nan  # Trả về FALSE!
  ```
- Vì vậy, bạn **KHÔNG THỂ** lọc ô rỗng bằng lệnh `df[df['col'] == np.nan]`. Cách duy nhất là dùng các hàm chuyên dụng: `df['col'].isnull()` hoặc `df['col'].isna()`.

#### **Step 6 & 7: Điền khuyết (Imputation) với `.fillna()`**
```python
iris.iloc[10:30, 2] = np.nan
iris['petal_length'] = iris['petal_length'].fillna(1.0)
```
- Khi dữ liệu bị thiếu, xóa bỏ dòng không phải lúc nào cũng là giải pháp tối ưu (vì làm mất thông tin ở các cột khác của dòng đó).
- Kỹ thuật `.fillna(1.0)` thay thế toàn bộ các ô rỗng bằng con số `1.0`. Trong thực tế, các chuyên gia thường điền bằng giá trị trung bình (`df['col'].mean()`) hoặc giá trị trung vị (`df['col'].median()`).

#### **Step 8: Xóa cột với `del` vs `.drop()`**
```python
del iris['class']
# Hoặc: iris.drop(columns=['class'], inplace=True)
```
- Cả hai cách đều xóa cột `class`.
  - `del df['class']`: Làm thay đổi trực tiếp DataFrame ngay lập tức, cú pháp rất ngắn.
  - `df.drop(columns=['class'])`: Linh hoạt hơn vì có thể xóa nhiều cột cùng lúc `df.drop(columns=['A', 'B'])` và hỗ trợ tham số `inplace`.

#### **Step 9, 10 & 11: Xóa dòng thiếu và Tái lập chỉ số (Reset Index)**
```python
iris.iloc[0:3, :] = np.nan
iris.dropna(axis=0, inplace=True)
iris.reset_index(drop=True, inplace=True)
```
- **Hiện tượng "thủng chỉ số"**:
  - Ban đầu, bảng có index: `0, 1, 2, 3, 4, ...`
  - Sau khi xóa 3 dòng đầu (dòng 0, 1, 2), dòng đầu tiên của bảng bây giờ có index là **3**!
  - Nếu một lập trình viên khác gọi `iris.loc[0]`, chương trình sẽ báo lỗi `KeyError: 0`.
  - Vì vậy, sau các thao tác xóa dòng (`dropna`, `drop`), ta **luôn luôn phải gọi `.reset_index(drop=True, inplace=True)`** để đưa chỉ số về lại `0, 1, 2, 3, ...` chuẩn mực.

---

### 4. Các lỗi phổ biến người mới hay mắc phải (Common Pitfalls)
1. **Dùng toán tử so sánh `== np.nan`**: Như đã giải thích ở trên, biểu thức này luôn trả về `False` và không tìm được bất kỳ ô rỗng nào.
2. **Quên tham số `drop=True` khi `reset_index()`**: Nếu chỉ viết `df.reset_index()`, cột index cũ sẽ bị đẩy vào làm một cột dữ liệu mới có tên là `'index'`. Thêm `drop=True` sẽ xóa bỏ hoàn toàn cột index cũ này.
3. **Nhầm lẫn giữa `axis=0` và `axis=1` trong `dropna()`**:
   - `dropna(axis=0)`: Xóa các **hàng** có chứa ô rỗng.
   - `dropna(axis=1)`: Xóa cả **cột** nếu cột đó có chứa ô rỗng (rất nguy hiểm vì có thể làm mất sạch các cột trong bảng).

---

### 5. Đối chiếu giáo trình môn học (Slides Reference)
- **Slide Week1-Intro (Trang 15 - 16)**: Bước tiền xử lý và làm sạch dữ liệu trong quy trình phân tích.
- **Slide Week3-Pandas (Trang 25 - 38)**:
  - *Trang 25 - 28*: Kỹ thuật Data Cleaning với Pandas: Kiểm tra `isna()`, xóa dữ liệu thiếu với `dropna()`, điền dữ liệu khuyết với `fillna()`.
  - *Trang 29 - 38*: Xóa cột, xóa dòng và định hình lại cấu trúc DataFrame.
