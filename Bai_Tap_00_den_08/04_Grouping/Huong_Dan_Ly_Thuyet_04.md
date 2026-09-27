# CẨM NANG HƯỚNG DẪN KIẾN THỨC VÀ LÝ THUYẾT: BÀI 04
## Chủ đề: Gom Nhóm Dữ Liệu - GroupBy (Bài tập Alcohol Consumption)
*Dành cho người mới bắt đầu học Phân tích Dữ liệu với Python*

---

### 1. Mục tiêu bài học
Trong phân tích kinh doanh thực tế, hầu hết các câu hỏi đều xoay quanh việc so sánh giữa các nhóm đối tượng (ví dụ: *Doanh số theo từng vùng miền?*, *Năng suất làm việc theo phòng ban?*, *Lượng tiêu thụ bia theo từng châu lục?*). Thao tác gom nhóm **GroupBy** là vũ khí mạnh nhất trong Pandas để giải quyết dạng bài toán này:
- Nắm vững triết lý kinh điển: **Split - Apply - Combine** (Tách - Áp dụng - Kết hợp).
- Biết cách nhóm theo 1 cột hoặc nhiều cột phân loại.
- Áp dụng các hàm tổng hợp thống kê cơ bản: `.mean()`, `.median()`, `.describe()`.
- Sử dụng hàm tổng hợp nâng cao `.agg()` để tính nhiều chỉ số thống kê cùng lúc trên một hoặc nhiều cột.
- Nắm rõ tham số sống còn `numeric_only=True` trong các phiên bản Pandas hiện đại.

---

### 2. Bảng từ điển các hàm và phương thức cốt lõi (Cheat Sheet)

| Tên hàm / Cú pháp | Thư viện | Ý nghĩa & Chức năng | Tại sao lại dùng? | Cú pháp & Ví dụ minh họa |
| :--- | :--- | :--- | :--- | :--- |
| `df.groupby('by_col')` | Pandas | Gom nhóm dữ liệu dựa trên các giá trị trùng lặp của cột `by_col`. | Tạo đối tượng `DataFrameGroupBy` để sẵn sàng áp dụng các phép tính tổng hợp theo từng nhóm. | `grouped = df.groupby('continent')` |
| `df.groupby('by_col')['target'].mean()` | Pandas | Tính giá trị trung bình của cột mục tiêu `target` theo từng nhóm. | Giúp so sánh nhanh chỉ số hiệu suất giữa các nhóm phân loại. | `drinks.groupby('continent')['beer_servings'].mean()` |
| `df.groupby('by_col').mean(numeric_only=True)` | Pandas | Tính trung bình của **tất cả các cột số** trong bảng theo từng nhóm. | Tiện lợi khi muốn tính toán toàn diện mà không phải gõ từng tên cột một. | `drinks.groupby('continent').mean(numeric_only=True)` |
| `df.groupby('by_col')['target'].describe()` | Pandas | Trả về bảng thống kê 8 chỉ số chi tiết cho từng nhóm riêng biệt. | Nhìn sâu vào phân phối của từng phân khúc mà không cần viết nhiều dòng lệnh thủ công. | `drinks.groupby('continent')['wine_servings'].describe()` |
| `df.groupby('by_col')['target'].agg([...])` | Pandas | **Aggregation**: Áp dụng cùng lúc danh sách nhiều hàm thống kê khác nhau lên nhóm. | Tùy biến linh hoạt cao, xuất ra DataFrame đa chỉ số chỉ trong 1 lần duyệt dữ liệu. | `df.groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max'])` |

---

### 3. Phân tích chi tiết từng Bước (Step-by-step)

#### **Triết lý 3 bước của GroupBy (Split - Apply - Combine):**
1. **Split (Tách)**: Pandas duyệt qua cột `continent` và tách bảng 193 quốc gia thành 6 nhóm con tương ứng 6 châu lục: `AF` (Châu Phi), `AS` (Châu Á), `EU` (Châu Âu), `NA` (Bắc Mỹ), `OC` (Châu Đại Dương), `SA` (Nam Mỹ).
2. **Apply (Áp dụng)**: Trong từng nhóm con, Pandas thực hiện phép tính được yêu cầu (ví dụ: tính trung bình `mean()` của cột `beer_servings`).
3. **Combine (Kết hợp)**: Pandas gom 6 kết quả trung bình vừa tính lại thành 1 Series có Index là tên 6 châu lục.

#### **Step 4: Tìm châu lục tiêu thụ bia nhiều nhất**
```python
beer_by_continent = drinks.groupby('continent')['beer_servings'].mean()
top_continent = beer_by_continent.idxmax()
```
- Kết quả cho thấy châu Âu (`EU`) dẫn đầu với mức trung bình gần 200 phần bia/người/năm.
- `.idxmax()` giúp lấy trực tiếp nhãn `'EU'` mà không cần phải nhìn bằng mắt thường.

#### **Step 6 & 7: Ý nghĩa của tham số `numeric_only=True`**
```python
drinks.groupby('continent').mean(numeric_only=True)
```
- **Tại sao tham số này cực kỳ quan trọng?**:
  - Bảng `drinks` có cột `country` là kiểu chuỗi ký tự (text).
  - Phép tính `mean()` (trung bình) hay `median()` (trung vị) chỉ có ý nghĩa trên số học. Bạn không thể tính "trung bình của tên quốc gia" (`mean(['Vietnam', 'Japan'])` là vô nghĩa).
  - Trong các phiên bản Pandas mới (Pandas 2.0+ và 3.0+), nếu không có `numeric_only=True`, Pandas sẽ báo lỗi `TypeError: Could not convert ... to numeric`.

#### **Step 8: Sức mạnh của phương thức `.agg()`**
```python
drinks.groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max'])
```
- Thay vì phải chạy 3 dòng lệnh riêng biệt:
  - `s_mean = drinks.groupby('continent')['spirit_servings'].mean()`
  - `s_min = drinks.groupby('continent')['spirit_servings'].min()`
  - `s_max = drinks.groupby('continent')['spirit_servings'].max()`
- Phương thức `.agg(['mean', 'min', 'max'])` thực hiện cả 3 phép toán trong 1 lượt duyệt duy nhất và tự động ghép thành một bảng DataFrame 3 cột cực kỳ đẹp mắt và tối ưu tài nguyên tính toán.

---

### 4. Các lỗi phổ biến người mới hay mắc phải (Common Pitfalls)
1. **Quên `numeric_only=True`**: Gây lỗi chương trình khi gọi hàm tính toán trên toàn bộ DataFrame có chứa cột văn bản.
2. **Nhầm lẫn thứ tự gom nhóm**:
   - `df.groupby('A')['B'].sum()`: Gom theo A, tính tổng trên B.
   - Nếu viết ngược `df.groupby('B')['A'].sum()`: Kết quả sẽ gom theo B, tính tổng trên A (hoàn toàn khác biệt về ý nghĩa nghiệp vụ).
3. **Hiểu nhầm giá trị rỗng trong cột nhóm**: Mặc định, nếu giá trị trong cột gom nhóm bị `NaN`, Pandas sẽ bỏ qua nhóm đó trừ khi chỉ định tham số `dropna=False`.

---

### 5. Đối chiếu giáo trình môn học (Slides Reference)
- **Slide Week3-Pandas (Trang 17, 22 - 24)**:
  - *Trang 17*: Các hàm thống kê mô tả cơ bản của DataFrame.
  - *Trang 22 - 24*: Kỹ thuật tổng hợp, thống kê theo nhóm và xử lý dữ liệu với Pandas.
