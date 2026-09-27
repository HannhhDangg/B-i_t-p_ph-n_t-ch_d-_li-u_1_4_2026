# CẨM NANG HƯỚNG DẪN KIẾN THỨC VÀ LÝ THUYẾT: BÀI 07
## Chủ đề: Trực Quan Hóa Dữ Liệu - Data Visualization (Bài tập Titanic)
*Dành cho người mới bắt đầu học Phân tích Dữ liệu với Python*

---

### 1. Mục tiêu bài học
"Một bức tranh có giá trị bằng một nghìn lời nói". Trực quan hóa dữ liệu (**Data Visualization**) là công đoạn biến các bảng số liệu khô khan thành các biểu đồ trực quan, giúp nhà phân tích khám phá các quy luật ẩn giấu và truyền tải thông điệp (Data Storytelling) hiệu quả:
- Nắm được vai trò và cách phối hợp giữa hai thư viện đồ họa trụ cột của Python: **Matplotlib** (thư viện đồ họa nền tảng, kiểm soát chi tiết từng pixel) và **Seaborn** (thư viện thống kê cấp cao, màu sắc tinh tế, cú pháp ngắn gọn).
- Lựa chọn đúng loại biểu đồ cho từng loại bài toán:
  - **Pie Chart (Biểu đồ tròn)**: So sánh tỷ trọng từng phần so với tổng thể (100%).
  - **Scatter Plot (Biểu đồ phân tán)**: Tìm kiếm mối tương quan giữa 2 biến số liên tục (Tuổi vs Giá vé) kết hợp phân tầng màu sắc theo biến thứ 3 (`hue='Sex'`).
  - **Histogram (Biểu đồ tần số)**: Khảo sát hình dạng phân phối của dữ liệu (phân phối chuẩn hay phân phối lệch phải/lệch trái).
  - **Bar Chart (Biểu đồ cột)**: So sánh số liệu định lượng giữa các danh mục khác nhau.
- Tinh chỉnh các thành phần thẩm mỹ của biểu đồ: Kích thước (`figsize`), tiêu đề (`title`), nhãn trục (`xlabel`, `ylabel`), chú thích (`legend`), màu sắc (`palette`).

---

### 2. Bảng từ điển các hàm và phương thức cốt lõi (Cheat Sheet)

| Tên hàm / Thuộc tính | Thư viện | Ý nghĩa & Chức năng | Tại sao lại dùng? | Cú pháp & Ví dụ minh họa |
| :--- | :--- | :--- | :--- | :--- |
| `plt.figure(figsize=(w, h))` | Matplotlib | Khởi tạo khung vẽ với chiều rộng `w` và chiều cao `h` (tính bằng inch). | Đảm bảo kích thước biểu đồ vừa vặn, không bị méo hình hay chữ bị đè lên nhau. | `plt.figure(figsize=(10, 6))` |
| `plt.pie(x, labels, autopct)` | Matplotlib | Vẽ biểu đồ hình quạt tròn (Pie Chart). | Thể hiện cơ cấu tỷ lệ phần trăm trực quan khi số lượng phân loại nhỏ (dưới 5 nhóm). | `plt.pie(gender_counts, labels=['Nam', 'Nữ'], autopct='%1.1f%%')` |
| `sns.scatterplot(x, y, hue)` | Seaborn | Vẽ biểu đồ các điểm phân tán trên hệ tọa độ Descartes 2 chiều. | Khảo sát xu hướng, phát hiện cụm (clustering) và các điểm bất thường (outliers) giữa 2 biến số. | `sns.scatterplot(data=df, x='Age', y='Fare', hue='Sex')` |
| `plt.hist(x, bins=...)` | Matplotlib | Chia dải giá trị liên tục thành các khoảng (bins) và đếm tần suất xuất hiện. | Giúp kiểm tra xem dữ liệu có tập trung ở vùng nào, có bị bất đối xứng không. | `plt.hist(df['Fare'], bins=40, color='green')` |
| `sns.barplot(x, y)` | Seaborn | Vẽ các cột hình chữ nhật có chiều cao tương ứng với giá trị thống kê. | So sánh chỉ số trung bình hoặc tỷ lệ giữa các phân nhóm độc lập. | `sns.barplot(x=pclass.index, y=pclass.values)` |
| `plt.show()` | Matplotlib | Hiển thị đồ họa hoàn chỉnh ra màn hình và giải phóng bộ nhớ đồ họa. | Lệnh chốt để kết thúc quá trình định nghĩa các lớp vẽ của biểu đồ. | `plt.show()` |

---

### 3. Phân tích chi tiết từng Bước (Step-by-step)

#### **Step 4: Tại sao nên đặt `PassengerId` làm Index?**
```python
titanic.set_index('PassengerId', inplace=True)
```
- Cột `PassengerId` chỉ là số thứ tự định danh duy nhất của hành khách. Nếu để nó làm cột dữ liệu thông thường, khi bạn chạy `df.describe()`, Pandas sẽ tính cả trung bình, min, max của số ID (điều này hoàn toàn vô nghĩa trong phân tích kinh doanh). Đặt làm Index giúp loại bỏ nó khỏi vùng tính toán tự động.

#### **Step 5: Giải mã biểu đồ tròn (Pie Chart)**
```python
plt.pie(gender_counts, labels=['Nam', 'Nữ'], autopct='%1.1f%%', colors=['#3498db', '#e74c3c'], startangle=90, explode=(0.05, 0))
```
- `autopct='%1.1f%%'`: Tự động tính toán tỷ lệ phần trăm từ số liệu đếm và định dạng hiển thị với 1 chữ số thập phân kèm ký tự `%`.
- `explode=(0.05, 0)`: Tách nhẹ miếng bánh phần 'Nam' ra khỏi tâm 0.05 đơn vị để tạo điểm nhấn thị giác.
- `startangle=90`: Xoay góc bắt đầu của lát cắt đầu tiên thẳng đứng ở hướng 12 giờ.

#### **Step 6: Kỹ thuật biểu diễn 3 chiều trên mặt phẳng 2D với `hue`**
```python
sns.scatterplot(data=titanic, x='Age', y='Fare', hue='Sex', palette={'male': '#2980b9', 'female': '#e74c3c'}, alpha=0.7)
```
- **Tại sao lại dùng tham số `hue`?**:
  - Trục hoành ($X$): Độ tuổi (`Age`).
  - Trục tung ($Y$): Giá vé (`Fare`).
  - Màu sắc (`hue='Sex'`): Tự động gán màu xanh cho Nam và màu đỏ cho Nữ.
  - Tham số `alpha=0.7`: Độ trong suốt 70% giúp nhìn rõ những vùng có nhiều điểm dữ liệu bị đè chồng lên nhau.
  - **Insight từ biểu đồ**: Phần lớn hành khách mua vé giá rẻ dưới $50 nằm ở độ tuổi 18 - 40; các vé đắt tiền đột biến (trên $200 - $500) đa phần là Nữ giới thuộc giới thượng lưu.

#### **Step 8: Phân tích biểu đồ tần số Giá vé (Histogram)**
```python
plt.hist(titanic['Fare'], bins=40, color='#2ecc71', edgecolor='black', alpha=0.8)
```
- Biểu đồ cho thấy hình dáng **Phân phối lệch phải cực mạnh (Right-skewed / Positively skewed distribution)**: Hơn 80% hành khách mua vé giá rẻ ở vùng sát 0 đến 30$, trong khi chỉ có một số ít mua vé rất cao kéo dài về phía bên phải.

---

### 4. Các lỗi phổ biến người mới hay mắc phải (Common Pitfalls)
1. **Lạm dụng Biểu đồ tròn khi có quá nhiều danh mục**: Biểu đồ tròn chỉ hiệu quả khi có 2 đến 4 nhóm (như Nam/Nữ). Nếu có 15 nhóm, các miếng bánh sẽ bị nén lại bé tí và mắt người không thể so sánh được góc nghiêng. Khi đó, biểu đồ cột (`Bar Chart`) là lựa chọn vượt trội.
2. **Không đặt nhãn trục và tiêu đề**: Vẽ biểu đồ nhưng không có `xlabel`, `ylabel`, `title` khiến người xem không hiểu biểu đồ đang đo lường cái gì và bằng đơn vị gì.
3. **Quên gọi `plt.show()` hoặc `plt.figure()`**: Vẽ nhiều biểu đồ liên tiếp mà không có `plt.figure()` riêng sẽ khiến hình vẽ sau bị đè lên hình vẽ trước.

---

### 5. Đối chiếu giáo trình môn học (Slides Reference)
- **Slide Week1-Intro (Trang 15 - 17, 26)**: Quy trình phân tích dữ liệu và vai trò của việc trực quan hóa truyền tải thông tin.
- **Slide Week3-Pandas (Trang 15, 23)**: Thao tác đặt Index (`set_index`) và tích hợp vẽ biểu đồ nhanh từ Series / DataFrame.
