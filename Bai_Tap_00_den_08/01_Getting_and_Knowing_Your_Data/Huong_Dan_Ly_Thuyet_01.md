# CẨM NANG HƯỚNG DẪN KIẾN THỨC VÀ LÝ THUYẾT: BÀI 01
## Chủ đề: Khám Phá Và Làm Quen Với Dữ Liệu (Bài tập Chipotle)
*Dành cho người mới bắt đầu học Phân tích Dữ liệu với Python*

---

### 1. Mục tiêu bài học
Giai đoạn đầu tiên và quan trọng nhất của mọi dự án phân tích dữ liệu là **EDA (Exploratory Data Analysis - Khám phá dữ liệu sơ bộ)**:
- Nắm được cách đọc dữ liệu từ tệp văn bản qua đường dẫn URL trực tuyến.
- Phân biệt được các kiểu định dạng file: CSV (ngăn cách bằng dấu phẩy) và TSV (ngăn cách bằng dấu Tab).
- Đo lường kích thước dữ liệu (số dòng, số cột), định danh các biến số (tên cột) và kiểu chỉ số (Index).
- Biết cách nhóm dữ liệu theo từng đối tượng (`groupby`) và tính tổng để tìm ra những món bán chạy nhất.
- Làm sạch chuỗi ký tự (Data Cleaning): Loại bỏ ký tự tiền tệ đặc biệt như `$` và chuyển đổi kiểu dữ liệu thành số thực (`float`) để tính toán doanh thu.

---

### 2. Bảng từ điển các hàm và phương thức cốt lõi (Cheat Sheet)

| Tên hàm / Thuộc tính | Thư viện | Ý nghĩa & Chức năng | Tại sao lại dùng? | Cú pháp & Ví dụ minh họa |
| :--- | :--- | :--- | :--- | :--- |
| `pd.read_csv(filepath, sep=...)` | Pandas | Đọc dữ liệu từ file CSV, TSV, TXT hoặc đường link web URL thành DataFrame. | Tự động phân tích cấu trúc cột, nhận diện kiểu dữ liệu và tối ưu bộ nhớ. | `pd.read_csv('data.tsv', sep='\t')` |
| `df.head(n)` | Pandas | Hiển thị `n` dòng đầu tiên của bảng (mặc định là 5). | Giúp nhà phân tích "nhìn tận mắt" cấu trúc mẫu dữ liệu mà không làm nặng màn hình. | `df.head(10)` |
| `df.shape` | Pandas | Thuộc tính trả về một bộ giá trị `(số_hàng, số_cột)`. | Biết ngay quy mô dữ liệu: `df.shape[0]` là số dòng, `df.shape[1]` là số cột. | `rows, cols = df.shape` *(Không có dấu ngoặc tròn)* |
| `df.columns` | Pandas | Thuộc tính trả về danh sách/Index tên các cột. | Liệt kê nhanh các biến số có trong bảng để chuẩn bị truy vấn. | `list(df.columns)` |
| `df.index` | Pandas | Thuộc tính mô tả cách đánh chỉ số hàng. | Biết dữ liệu đang đánh chỉ số tự động (`RangeIndex(0, n)`) hay theo mã định danh. | `df.index` |
| `df.groupby('col')['target'].sum()` | Pandas | Gom nhóm dữ liệu theo một cột phân loại và tính tổng cột mục tiêu. | Nguyên lý *Split - Apply - Combine* kinh điển để tổng hợp dữ liệu theo từng nhóm. | `chipo.groupby('item_name')['quantity'].sum()` |
| `series.sort_values(ascending=...)` | Pandas | Sắp xếp giá trị của Series hoặc DataFrame. | Tìm giá trị lớn nhất/nhỏ nhất theo thứ tự tăng dần (`True`) hoặc giảm dần (`False`). | `s.sort_values(ascending=False)` |
| `series.apply(func)` | Pandas | Áp dụng một hàm số lên từng phần tử của Series. | Xử lý biến đổi hàng loạt dữ liệu (ví dụ làm sạch chuỗi, ép kiểu). | `s.apply(lambda x: float(x.replace('$', '')))` |
| `series.nunique()` | Pandas | Đếm số lượng giá trị duy nhất (Number of Unique values). | Đếm xem có bao nhiêu khách hàng khác nhau, bao nhiêu đơn hàng, hoặc bao nhiêu món ăn khác biệt. | `chipo['order_id'].nunique()` |

---

### 3. Phân tích chi tiết từng Bước (Step-by-step)

#### **Step 2 & 3: Đọc dữ liệu từ TSV với `sep='\t'`**
```python
url = 'https://raw.githubusercontent.com/thieu1995/csv-files/main/data/pandas/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')
```
- **Tại sao cần `sep='\t'`?**: Hàm `pd.read_csv()` mặc định phân cách các cột bằng dấu phẩy `,` (`sep=','`). Nhưng file này có đuôi `.tsv` (Tab-Separated Values), nghĩa là các cột được phân cách bằng phím Tab `\t`. Nếu không có `sep='\t'`, Pandas sẽ đọc toàn bộ dòng dữ liệu thành một cột duy nhất gây sai lệch hoàn toàn.

#### **Step 5 & 6: Kích thước tập dữ liệu với `df.shape`**
```python
chipo.shape       # Trả về: (4622, 5)
chipo.shape[0]    # Số dòng: 4622 quan sát
chipo.shape[1]    # Số cột: 5 cột
```
- **Lưu ý**: Đây là tuple kế thừa từ NumPy array (học ở *Slide Week2-Numpy*). Truy cập phần tử bằng chỉ số `[0]` và `[1]`.

#### **Step 9 & 10: Tìm món được đặt nhiều nhất**
```python
most_ordered = chipo.groupby('item_name')['quantity'].sum().sort_values(ascending=False)
```
- **Cơ chế hoạt động**:
  1. `chipo.groupby('item_name')`: Chia bảng thành 50 nhóm nhỏ theo từng món ăn riêng biệt.
  2. `['quantity']`: Chọn cột số lượng của mỗi nhóm.
  3. `.sum()`: Cộng dồn số lượng đặt của từng món ăn trong toàn bộ thời gian.
  4. `.sort_values(ascending=False)`: Sắp xếp món có tổng số lượng từ cao xuống thấp.
  5. `most_ordered.index[0]`: Lấy tên món đứng đầu (`Chicken Bowl`).
  6. `most_ordered.iloc[0]`: Lấy số lượng tương ứng (`761` phần).

#### **Step 13: Xử lý làm sạch chuỗi và chuyển đổi kiểu giá tiền**
```python
# Cột ban đầu có dạng: "$2.39 ", "$3.39 ", kiểu dữ liệu là object (chuỗi)
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x.strip().replace('$', '')))
```
- **Tại sao phải làm sạch?**: Python không thể làm tính cộng, trừ, nhân, chia trên chuỗi ký tự chứa dấu `$`. Nếu tính `sum()`, Python sẽ ghép các chuỗi lại với nhau thay vì tính tổng tiền!
- **Giải mã Lambda Function**:
  - `lambda x:`: Với mỗi phần tử `x` trong cột (ví dụ `"$10.98 "`):
  - `.strip()`: Cắt bỏ khoảng trắng thừa ở hai đầu.
  - `.replace('$', '')`: Bỏ ký tự đô la `$`, chuỗi trở thành `"10.98"`.
  - `float(...)`: Ép chuỗi chữ số thành số thực `10.98`.

#### **Step 15 & 16: Tính số đơn hàng và doanh thu trung bình mỗi đơn**
```python
num_orders = chipo['order_id'].nunique()
avg_revenue_per_order = chipo.groupby('order_id')['item_price'].sum().mean()
```
- **`nunique()` vs `count()`**:
  - `count()` đếm tổng số dòng (4622). Nhưng một đơn hàng có thể mua 3 món (tương ứng 3 dòng cùng chung 1 `order_id`).
  - `nunique()` chỉ đếm các `order_id` độc nhất (1834 đơn hàng).
- **Tính doanh thu trung bình mỗi đơn**:
  - Trước tiên tính tổng tiền của từng hóa đơn: `chipo.groupby('order_id')['item_price'].sum()`.
  - Sau đó lấy trung bình (`.mean()`) của tất cả các hóa đơn đó.

---

### 4. Các lỗi phổ biến người mới hay mắc phải (Common Pitfalls)
1. **Quên `sep='\t'` khi đọc file TSV**: Dẫn đến bảng chỉ có 1 cột kỳ lạ chứa toàn bộ dữ liệu.
2. **Cộng nhầm chuỗi ký tự**: Thực hiện `.sum()` khi cột chưa chuyển sang số thực khiến kết quả bị nối chuỗi khổng lồ (`$2.39 $3.39 $5.50 ...`).
3. **Nhầm giữa `unique()` và `nunique()`**:
   - `df['col'].unique()` trả về mảng các giá trị (ví dụ: `array(['Chicken Bowl', ...])`).
   - `df['col'].nunique()` trả về **một con số nguyên** là số lượng các giá trị khác nhau (ví dụ: `50`).

---

### 5. Đối chiếu giáo trình môn học (Slides Reference)
- **Slide Week1-Intro (Trang 15 - 22)**:
  - *Trang 15*: Quy trình phân tích dữ liệu: Thu thập -> Tiền xử lý -> Phân tích -> Trực quan hóa.
  - *Trang 18 - 22*: Phân loại dữ liệu: Dữ liệu định tính (Categorical/Nominal: `item_name`, `choice_description`) và Dữ liệu định lượng (Numerical/Ratio: `quantity`, `item_price`).
- **Slide Week3-Pandas (Trang 15 - 24)**:
  - *Trang 18*: Đọc dữ liệu từ file ngoài bằng `read_csv()`.
  - *Trang 15 - 17*: Thuộc tính `shape`, `columns`, `index` và các hàm xem nhanh `head()`, `tail()`.
