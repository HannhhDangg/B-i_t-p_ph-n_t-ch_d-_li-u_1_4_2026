# CẨM NANG HƯỚNG DẪN KIẾN THỨC VÀ LÝ THUYẾT: BÀI 02
## Chủ đề: Lọc và Sắp Xếp Dữ Liệu (Bài tập Euro 2012)
*Dành cho người mới bắt đầu học Phân tích Dữ liệu với Python*

---

### 1. Mục tiêu bài học
Trong thực tế, một bảng dữ liệu có thể có hàng chục nghìn dòng và hàng trăm cột. Kỹ năng **Lọc (Filtering)** và **Sắp xếp (Sorting)** giúp bạn trích xuất đúng phân khúc dữ liệu cần quan tâm để trả lời các câu hỏi kinh doanh cụ thể:
- Phân biệt và sử dụng thành thạo hai công cụ truy xuất dữ liệu mạnh nhất của Pandas: `.loc` (theo nhãn/điều kiện) và `.iloc` (theo vị trí số thứ tự).
- Lọc dữ liệu số bằng điều kiện so sánh logic (`> `, `< `, `==`).
- Lọc dữ liệu chuỗi ký tự bằng nhóm hàm `.str` (ví dụ `.str.startswith()`).
- Lọc theo danh sách giá trị với `.isin()`.
- Sắp xếp bảng dữ liệu theo một hoặc nhiều cột cùng lúc (Multi-level Sorting).
- Kỹ thuật cắt lát (Slicing) cột bằng chỉ số âm trong Python.

---

### 2. Bảng từ điển các hàm và phương thức cốt lõi (Cheat Sheet)

| Tên hàm / Thuộc tính | Thư viện | Ý nghĩa & Chức năng | Tại sao lại dùng? | Cú pháp & Ví dụ minh họa |
| :--- | :--- | :--- | :--- | :--- |
| `df.sort_values(by, ascending)` | Pandas | Sắp xếp các dòng trong DataFrame theo giá trị của một hoặc nhiều cột. | Giúp đưa các giá trị cao nhất/thấp nhất lên đầu, hỗ trợ xếp hạng (Ranking). | `df.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)` |
| `df[df['col'] > value]` | Pandas | Lọc các dòng thỏa mãn điều kiện logic (Boolean Masking). | Thay thế cho vòng lặp `for...if` truyền thống của Python, nhanh hơn gấp hàng trăm lần nhờ tính toán vector hóa. | `euro12[euro12['Goals'] > 6]` |
| `series.str.startswith(prefix)` | Pandas | Kiểm tra xem chuỗi có bắt đầu bằng một tiền tố ký tự hay không. | Lọc các chuỗi ký tự theo quy luật bắt đầu (ví dụ: tìm họ tên, mã vùng, mã sản phẩm). | `euro12['Team'].str.startswith('G')` |
| `series.isin(list_values)` | Pandas | Kiểm tra xem giá trị của mỗi dòng có thuộc một danh sách cho trước hay không. | Trực quan và ngắn gọn hơn rất nhiều so với việc viết nhiều điều kiện `(x == A) | (x == B) | (x == C)`. | `euro12['Team'].isin(['England', 'Italy'])` |
| `df.iloc[row_idx, col_idx]` | Pandas | **Integer-location**: Cắt lát dữ liệu dựa trên chỉ số vị trí số nguyên (0, 1, 2...). | Dùng khi muốn lấy cột theo số thứ tự (ví dụ: lấy 5 cột đầu, bỏ 3 cột cuối) bất kể tên cột là gì. | `df.iloc[:, :7]` (Lấy tất cả hàng, 7 cột đầu) |
| `df.loc[row_condition, col_names]` | Pandas | **Label-location**: Truy xuất dữ liệu dựa trên nhãn tên dòng/cột hoặc điều kiện logic. | Cho phép vừa lọc dòng theo điều kiện, vừa chỉ định chính xác tên các cột muốn hiển thị. | `df.loc[df['Goals'] > 5, ['Team', 'Goals']]` |

---

### 3. Phân tích chi tiết từng Bước (Step-by-step)

#### **Step 7 & 8: Trích chọn cột và sắp xếp đa tiêu chí**
```python
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)
```
- **Sắp xếp đa tiêu chí hoạt động thế nào?**:
  - Tiêu chí 1: Sắp xếp theo `Red Cards` giảm dần (`ascending=False`). Đội nào nhiều thẻ đỏ nhất sẽ ở trên cùng.
  - Tiêu chí 2: Nếu có hai hay nhiều đội bằng nhau về số thẻ đỏ, Pandas sẽ tự động dùng cột thứ hai là `Yellow Cards` để phân định thứ bậc (đội nào nhiều thẻ vàng hơn sẽ xếp trên).

#### **Step 10: Lọc các đội ghi trên 6 bàn thắng (Boolean Indexing)**
```python
euro12[euro12['Goals'] > 6]
```
- **Cơ chế ngầm**:
  - `euro12['Goals'] > 6` tạo ra một Series chứa các giá trị Boolean `True` hoặc `False` cho từng đội bóng.
  - Khi truyền Series Boolean này vào `euro12[...]`, Pandas chỉ giữ lại các dòng có giá trị là `True`.

#### **Step 11: Lọc chuỗi bắt đầu bằng chữ 'G'**
```python
euro12[euro12['Team'].str.startswith('G')]
```
- **Tại sao cần `.str`?**: Trong Pandas, các phương thức xử lý chuỗi chuẩn của Python (như `startswith`, `endswith`, `lower`, `upper`) không thể gọi trực tiếp lên Series mà phải truy cập qua bộ điều phối `.str` để áp dụng vector hóa cho toàn bộ các phần tử.

#### **Step 12 & 13: Cắt lát với `.iloc`**
```python
euro12.iloc[:, :7]    # 7 cột đầu tiên (chỉ số 0 đến 6)
euro12.iloc[:, :-3]   # Tất cả các cột trừ 3 cột cuối cùng
```
- **Cú pháp Python Slicing**:
  - Dấu `:` trước dấu phẩy nghĩa là lấy toàn bộ các hàng.
  - Dấu `:` sau dấu phẩy là chỉ số cột: `:7` lấy từ cột 0 đến cột 6 (không lấy cột 7).
  - `:-3` nghĩa là chạy từ đầu cho đến vị trí cách cuối cùng 3 cột (bỏ qua 3 cột cuối).

#### **Step 14: Kết hợp `.loc` với `.isin()`**
```python
euro12.loc[euro12['Team'].isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']]
```
- **Tại sao đây là cú pháp tối ưu nhất?**:
  - Cú pháp chuẩn của `.loc`: `df.loc[điều_kiện_hàng, danh_sách_cột]`.
  - Thay vì phải lọc 2 bước: lấy hàng trước rồi lấy cột sau (gây cảnh báo *Chained Indexing*), `.loc` thực hiện cả 2 việc trong 1 bước duy nhất, vừa tối ưu tốc độ vừa an toàn tuyệt đối.

---

### 4. Các lỗi phổ biến người mới hay mắc phải (Common Pitfalls)
1. **Dùng nhầm `and` / `or` thay vì `&` / `|`**:
   - SAI: `euro12[(euro12['Goals'] > 2) and (euro12['Red Cards'] == 0)]` -> Báo lỗi `ValueError`.
   - ĐÚNG: `euro12[(euro12['Goals'] > 2) & (euro12['Red Cards'] == 0)]`.
   - **Bắt buộc**: Trong Pandas, phải dùng toán tử bitwise `&` (AND), `|` (OR) và **luôn bao bọc mỗi điều kiện con trong cặp ngoặc đơn `(...)`**.
2. **Nhầm lẫn giữa `.loc` và `.iloc`**:
   - `.iloc` chỉ nhận số nguyên vị trí (`0, 1, 2...`). Viết `.iloc[:, 'Goals']` sẽ báo lỗi ngay.
   - `.loc` nhận nhãn tên (`'Goals'`, `'Team'`) hoặc mảng Boolean (`True/False`).

---

### 5. Đối chiếu giáo trình môn học (Slides Reference)
- **Slide Week2-Numpy (Trang 14 - 18)**:
  - *Trang 14 - 17*: Chỉ mục và lát cắt trong array (Slicing 1D và 2D với bước nhảy âm `:-3`).
  - *Trang 32 - 36*: Sắp xếp `np.sort()` và tìm kiếm điều kiện `np.where()`.
- **Slide Week3-Pandas (Trang 22 - 24)**:
  - *Trang 22 - 24*: Truy xuất và lọc dữ liệu với cú pháp Boolean Indexing, `.loc[]` và `.iloc[]`.
