# TỔNG QUAN KHÓA HỌC VÀ LỘ TRÌNH 9 BÀI TẬP PHÂN TÍCH DỮ LIỆU
## Hướng Dẫn Dành Riêng Cho Người Mới Bắt Đầu Với Python, NumPy và Pandas
*Tài liệu đối chiếu trực tiếp với bài giảng của Giảng viên: Bùi Anh Tuấn (`Files/Week1-Intro.pdf`, `Week2-Numpy.pdf`, `Week3-Pandas.pdf`)*

---

## 1. Cấu Trúc Tổ Chức Thư Mục Bài Tập & Hướng Dẫn

Toàn bộ hệ thống bài tập và tài liệu học tập được chia thành 9 thư mục độc lập từ `00_` đến `08_` trong thư mục `Bai_Tap_00_den_08/`. Trong mỗi thư mục, bạn sẽ tìm thấy:
1. **File Bài Giải Jupyter Notebook (`.ipynb`)**: Chứa toàn bộ câu hỏi, code giải, comment chi tiết và **đặc biệt đã được chạy thực tế, lưu đầy đủ kết quả hiển thị (Bảng số liệu và Biểu đồ màu sắc)**.
2. **File Bài Giải Python Script (`.py`)**: File mã nguồn Python độc lập, có thể chạy trực tiếp bằng dòng lệnh `python ten_file.py` trên bất kỳ môi trường nào.
3. **File Hướng Dẫn Kiến Thức & Lý Thuyết (`Huong_Dan_Ly_Thuyet_xx.md`)**: Đóng vai trò như một bài giảng chuyên sâu:
   - *Mục tiêu bài học* và ý nghĩa thực tế trong ngành dữ liệu.
   - *Bảng từ điển các hàm (Cheat Sheet)*: Tên hàm, thư viện, chức năng, tại sao lại dùng hàm đó và cú pháp chuẩn.
   - *Giải thích chi tiết từng bước (Step-by-step)*: Cơ chế hoạt động ngầm (*Under the hood*), tại sao dùng cú pháp này mà không dùng cách khác.
   - *Các cạm bẫy & lỗi sai thường gặp (Common Pitfalls)* giúp bạn tránh mất hàng giờ gỡ lỗi.
   - *Liên hệ trực tiếp với Slide bài giảng tuần 1, tuần 2 và tuần 3*.

---

## 2. Bản Đồ Lộ Trình 9 Bài Học (Data Analysis Roadmap)

```
[BƯỚC 1: XÂY DỰNG NỀN TẢNG]
├── Bài 00: Khởi tạo Series & DataFrame (Pokemon)
│   └── Hiểu cấu trúc 1 chiều (Series), 2 chiều (DataFrame), tạo từ Dictionary, thêm cột, kiểm tra dtypes.
│
[BƯỚC 2: KHÁM PHÁ & THẤU HIỂU DỮ LIỆU - EDA]
├── Bài 01: Làm quen với tập dữ liệu thực tế (Chipotle)
│   └── Đọc file TSV (sep='\t'), đo lường shape, kiểm tra columns, index, làm sạch chuỗi tiền tệ ($) sang float.
├── Bài 02: Lọc và sắp xếp dữ liệu (Euro 2012)
│   └── Boolean Indexing, lọc chuỗi (.str.startswith), lọc danh sách (.isin), slicing với .iloc và .loc, sắp xếp đa cột.
├── Bài 03: Thống kê mô tả (US Baby Names)
│   └── Mean vs Median, Std, Quartiles, xóa cột (.drop), đếm tần suất (.value_counts), tìm giá trị cực trị (.idxmax).
│
[BƯỚC 3: PHÂN TÍCH NÂNG CAO & ĐA CHIỀU]
├── Bài 04: Gom nhóm dữ liệu - GroupBy (Tiêu thụ đồ uống có cồn)
│   └── Mô hình Split - Apply - Combine, so sánh hiệu suất giữa các nhóm, tính toán an toàn với numeric_only=True, hàm .agg().
├── Bài 05: Áp dụng hàm tùy biến - Apply (Học sinh & Đồ uống có cồn)
│   └── Viết hàm ẩn danh Lambda, áp dụng hàm .apply(), hiểu tính bất biến (Immutability), tạo đặc trưng mới (Feature Engineering).
├── Bài 06: Ghép nối dữ liệu - Concat & Merge (Thị trường nhà đất)
│   └── Mô phỏng dữ liệu với numpy.random, ghép ngang (axis=1) vs ghép dọc (axis=0), xử lý trùng lặp chỉ số (Reset Index).
│
[BƯỚC 4: KẾT NỐI VÀ TRÌNH BÀY THÔNG TIN]
├── Bài 07: Trực quan hóa dữ liệu - Data Visualization (Thảm họa Titanic)
│   └── Kỹ năng kể chuyện qua dữ liệu (Data Storytelling) với Matplotlib & Seaborn: Pie Chart, Scatter Plot (với hue), Histogram, Bar Chart.
├── Bài 08: Làm sạch dữ liệu khuyết thiếu - Deleting & Missing Data (Hoa Iris)
│   └── Xử lý file không tiêu đề (header=None), bản chất np.nan, điền khuyết (.fillna), loại bỏ dòng thiếu (.dropna), reset index.
```

---

## 3. Bảng Tổng Hợp 9 Bài Tập Chi Tiết

| Bài | Thư mục | Tên bài tập | Dữ liệu áp dụng | Kỹ năng & Hàm trọng tâm |
| :---: | :--- | :--- | :--- | :--- |
| **00** | `00_Creating_Series_and_DataFrames` | Pokemon | Tự khởi tạo từ Python Dict | `pd.DataFrame()`, `df.dtypes`, thêm cột mới, reordering columns. |
| **01** | `01_Getting_and_Knowing_Your_Data` | Chipotle Orders | 4,622 đơn hàng Chipotle | `pd.read_csv(sep='\t')`, `head()`, `shape`, `columns`, `nunique()`, `.apply(lambda)`. |
| **02** | `02_Filtering_and_Sorting` | Euro 2012 Teams | Thống kê bóng đá Euro 2012 | `sort_values()`, Boolean Masking, `.str.startswith()`, `.isin()`, `.iloc`, `.loc`. |
| **03** | `03_Stats` | US Baby Names | 1 triệu bản ghi tên trẻ em Mỹ | `.drop()`, `.value_counts()`, `mean()`, `median()`, `std()`, `describe()`, `.idxmax()`. |
| **04** | `04_Grouping` | Alcohol Consumption | Tiêu thụ đồ uống 193 quốc gia | `groupby()`, `numeric_only=True`, `describe()`, đa hàm `.agg(['mean', 'min', 'max'])`. |
| **05** | `05_Apply` | Student Alcohol | 395 học sinh trường trung học | `.loc[:, 'colA':'colB']`, `lambda`, `Series.apply()`, `df.map()`, kiểm tra kiểu dữ liệu. |
| **06** | `06_Merge` | Housing Market | 100 căn hộ mô phỏng bằng NumPy | `np.random.randint()`, `pd.concat(axis=1)`, `pd.concat(axis=0)`, `reset_index(drop=True)`. |
| **07** | `07_Visualization` | Titanic Disaster | 891 hành khách thảm họa Titanic | `plt.pie()`, `sns.scatterplot(hue=...)`, `plt.hist()`, `sns.barplot()`, `set_index()`. |
| **08** | `08_Deleting` | Iris Flowers | 150 mẫu hoa Iris Fisher | `read_csv(header=None)`, `isnull().sum()`, `np.nan`, `fillna()`, `del`, `dropna()`, `reset_index()`. |

---

## 4. Hướng Dẫn Cách Chạy Và Thực Hành

### Cách 1: Sử dụng Visual Studio Code (Khuyên Dùng)
1. Mở thư mục dự án `e:\Phân tích dữ liệu` trong VS Code.
2. Mở bất kỳ file notebook nào (ví dụ: `Bai_Tap_00_den_08/00_Creating_Series_and_DataFrames/Bai_Giai_00_Pokemon.ipynb`).
3. Chọn Kernel Python: Nhấp vào **"Select Kernel"** ở góc trên bên phải màn hình và chọn môi trường ảo `.venv` (Python 3.14 / `.venv\Scripts\python.exe`).
4. Nhấn **"Run All"** để chạy lại toàn bộ hoặc nhấn nút Play ở từng ô để chạy từng bước một.

### Cách 2: Chạy trực tiếp file mã nguồn Python trên Terminal
Mở PowerShell hoặc Command Prompt tại thư mục dự án và chạy:
```powershell
# Chạy bài 00:
.venv\Scripts\python.exe Bai_Tap_00_den_08\00_Creating_Series_and_DataFrames\Bai_Giai_00_Pokemon.py

# Chạy bài 01:
.venv\Scripts\python.exe Bai_Tap_00_den_08\01_Getting_and_Knowing_Your_Data\Bai_Giai_01_Chipotle.py

# Chạy bài 07 (Hiển thị các cửa sổ biểu đồ đồ họa):
.venv\Scripts\python.exe Bai_Tap_00_den_08\07_Visualization\Bai_Giai_07_Titanic_Desaster.py
```

---

## 5. Lời Khuyên Dành Cho Người Mới Học Phân Tích Dữ Liệu
1. **Đừng chỉ đọc code, hãy tự tay gõ lại**: Việc tự gõ lại giúp hình thành phản xạ ngón tay và nhớ tên hàm nhanh gấp 5 lần so với việc chỉ copy-paste.
2. **Luôn kiểm tra kiểu dữ liệu (`.dtypes`) và kích thước (`.shape`)**: Đây là 2 thao tác đầu tiên bạn nên làm bất cứ khi nào nạp một bảng dữ liệu mới.
3. **Phân biệt rạch ròi giữa nhãn (`.loc`) và vị trí (`.iloc`)**: Đây là nguồn cơn của 80% các lỗi của người mới học Pandas.
4. **Đối chiếu thường xuyên với 3 file tài liệu bài giảng trong thư mục `Files/`**:
   - `Week1-Intro.pdf`: Khái niệm loại dữ liệu và tư duy tiếp cận bài toán.
   - `Week2-Numpy.pdf`: Hiểu bản chất mảng số học ndarray và các phép tính vector hóa.
   - `Week3-Pandas.pdf`: Làm chủ Series, DataFrame, GroupBy và Data Cleaning.
