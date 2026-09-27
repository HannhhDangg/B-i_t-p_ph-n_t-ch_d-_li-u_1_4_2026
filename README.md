# B-i_t-p_ph-n_t-ch_d-_li-u_1_4_2026

## 📊 Khóa Học Phân Tích Dữ Liệu Với Python (Data Analysis with Python)

Dự án tổng hợp bài tập thực hành và tài liệu hướng dẫn lý thuyết phân tích dữ liệu với Python, NumPy, Pandas, Matplotlib và Seaborn.

---

### 📁 Cấu Trúc Dự Án

- **`Bai_Tap_00_den_08/`**: Thư mục bài tập chọn lọc từ `00_` đến `08_`. Mỗi thư mục con bao gồm:
  - File bài giải Jupyter Notebook (`.ipynb`) đã chạy hoàn chỉnh, có sẵn output và đồ thị.
  - File script Python (`.py`) chạy trực tiếp.
  - File cẩm nang hướng dẫn lý thuyết (`Huong_Dan_Ly_Thuyet_xx.md`) giải thích chi tiết từng hàm, tại sao dùng, cơ chế hoạt động và các bẫy thường gặp.
- **`Exercises-27-09-2026/`**: Bộ bài tập gốc đã được đồng bộ lời giải.
- **`Files/`**: Slide bài giảng môn học (Intro, NumPy, Pandas).

---

### 📚 Danh Sách 9 Bài Tập Thực Hành

1. **Bài 00: Khởi Tạo Series & DataFrame (Pokemon)** - `00_Creating_Series_and_DataFrames`
   - Tạo DataFrame từ Dictionary, reordering columns, thêm cột mới, kiểm tra `dtypes`.
2. **Bài 01: Khám Phá & Làm Quen Với Dữ Liệu (Chipotle)** - `01_Getting_and_Knowing_Your_Data`
   - Đọc dữ liệu TSV (`sep='\t'`), kiểm tra shape, columns, index, tính toán doanh thu, làm sạch chuỗi `$` với `apply(lambda)`.
3. **Bài 02: Lọc & Sắp Xếp Dữ Liệu (Euro 2012)** - `02_Filtering_and_Sorting`
   - Boolean Indexing, lọc chuỗi `.str.startswith()`, `.isin()`, slicing `.iloc` và `.loc`, sắp xếp đa tiêu chí `sort_values()`.
4. **Bài 03: Thống Kê Dữ Liệu (US Baby Names)** - `03_Stats`
   - Xóa cột thừa (`.drop()`), phân phối tần suất (`.value_counts()`), Mean, Median, Std, Quartiles (`.describe()`), tìm cực trị (`.idxmax()`).
5. **Bài 04: Phân Nhóm Dữ Liệu - GroupBy (Alcohol Consumption)** - `04_Grouping`
   - Mô hình Split - Apply - Combine, tính toán theo nhóm với `numeric_only=True`, tổng hợp đa hàm với `.agg(['mean', 'min', 'max'])`.
6. **Bài 05: Áp Dụng Hàm Số Tùy Biến - Apply (Student Alcohol Consumption)** - `05_Apply`
   - Slicing dải cột `.loc[:, 'A':'B']`, hàm ẩn danh Lambda, áp dụng hàm `.apply()`, tính bất biến (Immutability), tạo biến phân loại mới.
7. **Bài 06: Ghép Nối Dữ Liệu - Concat & Merge (Housing Market)** - `06_Merge`
   - Sinh số ngẫu nhiên với `numpy.random.randint()`, ghép ngang (`axis=1`) vs ghép dọc (`axis=0`), xử lý trùng lặp chỉ số bằng `reset_index(drop=True)`.
8. **Bài 07: Trực Quan Hóa Dữ Liệu - Visualization (Thảm Họa Titanic)** - `07_Visualization`
   - Biểu đồ tròn (`plt.pie`), biểu đồ phân tán 3 chiều (`sns.scatterplot` với `hue='Sex'`), biểu đồ tần số (`plt.hist`), biểu đồ cột (`sns.barplot`).
9. **Bài 08: Xóa & Xử Lý Dữ Liệu Thiếu (Hoa Iris)** - `08_Deleting`
   - Đọc dữ liệu không tiêu đề (`header=None`), phát hiện NaN (`isnull().sum()`), điền khuyết (`.fillna()`), loại bỏ dòng rỗng (`.dropna()`), reset index.

---

### 🚀 Cách Chạy Mã Nguồn

```bash
# Cài đặt các thư viện cần thiết
pip install pandas numpy matplotlib seaborn ipykernel

# Chạy một bài tập bất kỳ
python Bai_Tap_00_den_08/01_Getting_and_Knowing_Your_Data/Bai_Giai_01_Chipotle.py
```
