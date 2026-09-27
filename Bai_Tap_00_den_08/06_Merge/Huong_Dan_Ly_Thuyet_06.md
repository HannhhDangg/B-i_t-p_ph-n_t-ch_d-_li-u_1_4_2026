# CẨM NANG HƯỚNG DẪN KIẾN THỨC VÀ LÝ THUYẾT: BÀI 06
## Chủ đề: Ghép Nối Dữ Liệu - Concat & Merge (Bài tập Housing Market)
*Dành cho người mới bắt đầu học Phân tích Dữ liệu với Python*

---

### 1. Mục tiêu bài học
Trong thực tế, dữ liệu kinh doanh thường nằm rải rác ở nhiều bảng khác nhau (ví dụ: bảng thông tin khách hàng, bảng đơn hàng, bảng chi tiết sản phẩm). Kỹ năng **Hợp nhất (Merging)** và **Ghép nối (Concatenation)** dữ liệu là bắt buộc đối với mọi chuyên viên phân tích:
- Sinh dữ liệu số ngẫu nhiên phục vụ mô phỏng và kiểm thử mô hình bằng `numpy.random`.
- Hiểu thấu đáo bản chất trục tính toán trong Pandas: **Trục dọc (`axis=0`)** và **Trục ngang (`axis=1`)**.
- Nắm vững cách hoạt động của hàm ghép nối đa năng `pd.concat()`.
- Nhận biết và xử lý triệt để lỗi trùng lặp chỉ số (Duplicate Index) gây sai lệch khi truy vấn dữ liệu.
- Phân biệt giữa `pd.concat()`, `pd.merge()` và `df.join()`.

---

### 2. Bảng từ điển các hàm và phương thức cốt lõi (Cheat Sheet)

| Tên hàm / Cú pháp | Thư viện | Ý nghĩa & Chức năng | Tại sao lại dùng? | Cú pháp & Ví dụ minh họa |
| :--- | :--- | :--- | :--- | :--- |
| `np.random.randint(low, high, size)` | NumPy | Sinh mảng số nguyên ngẫu nhiên trong khoảng nửa mở `[low, high)`. | Tạo dữ liệu mẫu nhanh chóng để thử nghiệm thuật toán và kiểm thử code. | `np.random.randint(1, 5, size=100)` *(Sinh 100 số từ 1 đến 4)* |
| `pd.concat(objs, axis=...)` | Pandas | Ghép nối danh sách các Series hoặc DataFrame lại với nhau. | Công cụ mạnh mẽ nhất để dán các bảng dữ liệu lại với nhau theo hàng hoặc theo cột. | `pd.concat([s1, s2, s3], axis=1)` |
| `axis=0` vs `axis=1` | Pandas | Hướng của thao tác: `0` là chiều dọc (hàng), `1` là chiều ngang (cột). | Quy chuẩn xuyên suốt cả NumPy và Pandas để định hướng mọi phép toán. | Nối dọc: `axis=0`<br>Nối ngang: `axis=1` |
| `series.to_frame(name=...)` | Pandas | Chuyển đổi cấu trúc 1 chiều (Series) thành bảng 2 chiều (DataFrame). | Chuẩn hóa định dạng khi cần lưu trữ hoặc áp dụng các thao tác riêng của DataFrame. | `s.to_frame(name='col_name')` |
| `df.reset_index(drop=True)` | Pandas | Đánh lại chỉ số hàng từ `0, 1, 2... n-1`. | Xóa bỏ chỉ số cũ bị phân mảnh hoặc trùng lặp, đưa bảng về trạng thái chỉ số tuần tự chuẩn. | `df.reset_index(drop=True, inplace=True)` |

---

### 3. Phân tích chi tiết từng Bước (Step-by-step)

#### **Step 2: Quy tắc nửa mở `[low, high)` của `np.random.randint()`**
```python
s1 = pd.Series(np.random.randint(1, 5, size=100))
```
- **Tại sao đề bài yêu cầu từ 1 đến 4 mà code lại viết `1, 5`?**:
  - Giống như hàm `range()` trong Python, `np.random.randint(a, b)` lấy các số nguyên $x$ sao cho $a \le x < b$ (chặn dưới lấy, chặn trên bỏ qua).
  - Do đó, để sinh các số từ 1 đến 4, ta phải đặt cận trên là `5`.
  - Tương tự: từ 1 đến 3 thì cận trên là `4`; từ 10,000 đến 30,000 thì cận trên là `30001`.

#### **Step 3 & 5: So sánh bản chất `axis=1` vs `axis=0`**
- **Nối ngang (`axis=1`)**:
  - `pd.concat([s1, s2, s3], axis=1)`
  - Pandas đặt 3 Series nằm cạnh nhau: Cột 0 là `s1`, Cột 1 là `s2`, Cột 2 là `s3`.
  - Kết quả: Bảng có **100 hàng và 3 cột**.
- **Nối dọc (`axis=0`)**:
  - `pd.concat([s1, s2, s3], axis=0)`
  - Pandas xếp chồng các Series lên nhau: 100 dòng của `s1`, tiếp đến 100 dòng của `s2`, rồi 100 dòng của `s3`.
  - Kết quả: Bảng có **300 hàng và 1 cột**.

#### **Step 6 & 7: Vấn đề chỉ số trùng lặp (Duplicate Index)**
- Khi nối dọc 3 Series (mỗi Series có index từ `0` đến `99`), mặc định Pandas giữ nguyên index gốc của từng Series:
  - Dòng 0 đến 99: mang index 0 .. 99 (thuộc s1).
  - Dòng 100 đến 199: lại mang index 0 .. 99 (thuộc s2).
  - Dòng 200 đến 299: lại mang index 0 .. 99 (thuộc s3).
- **Hậu quả**: Nếu bạn truy vấn `bigcolumn.loc[0]`, Pandas sẽ trả về cả **3 dòng** thay vì 1 dòng duy nhất!
- **Giải pháp**:
  - Cách 1: Dùng `bigcolumn.reset_index(drop=True, inplace=True)`. Tham số `drop=True` giúp vứt bỏ cột index cũ, không để nó biến thành một cột dữ liệu thừa.
  - Cách 2: Ngay từ lúc concat, truyền thêm tham số `ignore_index=True`: `pd.concat([s1, s2, s3], axis=0, ignore_index=True)`.

---

### 4. Mở rộng: So sánh `pd.concat()` vs `pd.merge()` vs `df.join()`
- **`pd.concat()`**: Dán các bảng vào nhau đơn thuần theo vị trí hoặc theo index (như xếp các viên gạch cạnh nhau hoặc chồng lên nhau).
- **`pd.merge()`**: Hợp nhất dựa trên **giá trị chung** của một hoặc nhiều cột khóa (tương tự câu lệnh `JOIN` trong cơ sở dữ liệu SQL: `inner join`, `left join`, `right join`, `outer join`).
- **`df.join()`**: Một dạng viết tắt của merge nhưng dựa chủ yếu trên Index của hai bảng.

---

### 5. Đối chiếu giáo trình môn học (Slides Reference)
- **Slide Week2-Numpy (Trang 21 - 26, 44)**:
  - *Trang 21 - 26*: Thao túng mảng: Ghép mảng với `np.concatenate()`, `np.vstack()`, `np.hstack()`.
  - *Trang 44*: Module ngẫu nhiên `numpy.random` (`randint`, `rand`, `randn`).
- **Slide Week3-Pandas (Trang 8 - 14, 22)**:
  - *Trang 8 - 14*: Tạo Series, DataFrame và quản lý hệ thống chỉ mục (Index & Columns).
