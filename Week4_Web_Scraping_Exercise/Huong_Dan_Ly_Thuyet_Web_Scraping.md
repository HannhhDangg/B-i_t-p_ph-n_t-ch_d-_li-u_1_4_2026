# CẨM NANG HƯỚNG DẪN KIẾN THỨC VÀ LÝ THUYẾT: TUẦN 4
## Chủ đề: Thu Thập Dữ Liệu Web (Web Scraping) & So Sánh BeautifulSoup vs Scrapy
*Môn học: Phân tích Dữ liệu với Python | Giảng viên: Bùi Anh Tuấn*
*Đối chiếu trực tiếp với bài giảng `Files/Week4-Web-scraping.pdf` (Mục 10 - Bài tập)*

---

### 1. Mục tiêu bài học & Bức tranh toàn cảnh

Theo bài giảng Tuần 4 (Slide 3 - 5), **Web Scraping** là quy trình tự động hóa việc truy cập và trích xuất dữ liệu có cấu trúc từ các trang web trên Internet. Trong thực tế phân tích dữ liệu và khoa học máy tính:
- Thay vì nhập liệu thủ công tốn hàng tuần, Web Scraping thu thập hàng chục nghìn dữ liệu chỉ trong vài phút.
- Phục vụ nghiên cứu thị trường, theo dõi giá cả của đối thủ cạnh tranh trên các sàn Thương mại điện tử (E-Commerce).
- Cung cấp dữ liệu huấn luyện (Training Data) cho các mô hình Machine Learning và Trí tuệ nhân tạo (AI).

Bài tập thực hành này giải quyết trọn vẹn 3 yêu cầu trong **Mục 10 (Slide 14)**:
1. **Thu thập danh sách sản phẩm từ trang thương mại điện tử**: Áp dụng thư viện `requests` và `BeautifulSoup` để cào tự động thông tin sách qua nhiều trang.
2. **Lưu dữ liệu vào CSV và làm sạch bằng Pandas**: Loại bỏ ký tự tiền tệ, chuẩn hóa xếp hạng đánh giá, xử lý trạng thái kho hàng và phân tích thống kê mô tả (EDA).
3. **So sánh hai phương pháp Web Scraping hàng đầu**: Phân tích chuyên sâu sự khác biệt giữa `BeautifulSoup` và `Scrapy`.

---

### 2. Bảng từ điển các hàm và phương thức cốt lõi (Cheat Sheet)

#### 2.1. Thư viện `requests` (Giao tiếp HTTP)

| Cú pháp / Thuộc tính | Chức năng & Ý nghĩa | Tại sao lại dùng? | Ví dụ minh họa |
| :--- | :--- | :--- | :--- |
| `requests.get(url, headers)` | Gửi yêu cầu HTTP GET đến máy chủ web để tải nội dung HTML. | Giả lập trình duyệt gửi yêu cầu lấy trang web về máy tính để xử lý. | `res = requests.get(url, headers={'User-Agent': '...'})` |
| `res.status_code` | Mã phản hồi HTTP từ máy chủ (HTTP Status Code). | Kiểm tra xem việc tải trang có thành công không: `200` (OK), `403` (Bị chặn quyền), `404` (Không tìm thấy). | `if res.status_code == 200: ...` |
| `res.text` | Nội dung phản hồi dạng chuỗi văn bản (HTML thô). | Cung cấp mã nguồn HTML để thư viện BeautifulSoup bóc tách dữ liệu. | `soup = BeautifulSoup(res.text, 'html.parser')` |
| `res.encoding = 'utf-8'` | Thiết lập bảng mã giải mã văn bản là UTF-8. | Tránh lỗi font chữ tiếng Việt hoặc các ký hiệu tiền tệ đặc biệt (`£`, `€`, `₫`). | `res.encoding = 'utf-8'` |

#### 2.2. Thư viện `BeautifulSoup` (Bóc tách cú pháp HTML)

| Phương thức / Thuộc tính | Chức năng & Ý nghĩa | Tại sao lại dùng? | Ví dụ minh họa |
| :--- | :--- | :--- | :--- |
| `soup.find(tag, class_=...)` | Tìm phần tử HTML **đầu tiên** khớp với thẻ và thuộc tính chỉ định. | Dùng khi chỉ cần lấy 1 phần tử duy nhất (ví dụ: tiêu đề chính `<h1>`, thẻ sản phẩm đơn). | `price = book.find('p', class_='price_color').text` |
| `soup.find_all(tag, class_=...)` | Tìm **tất cả** các phần tử HTML khớp với điều kiện, trả về một danh sách (ResultSet). | Dùng khi cần lặp qua danh sách sản phẩm, danh sách bài viết, bảng dữ liệu. | `books = soup.find_all('article', class_='product_pod')` |
| `element.text` / `.get_text(strip=True)` | Trích xuất toàn bộ văn bản bên trong thẻ HTML và loại bỏ các thẻ con. | Loại bỏ các thẻ HTML rườm rà xung quanh để chỉ lấy nội dung chữ có nghĩa. | `title_clean = book.h3.a.text.strip()` |
| `element.get('attribute_name')` | Lấy giá trị của một thuộc tính HTML (ví dụ `href`, `src`, `title`, `class`). | Cực kỳ quan trọng để lấy đường dẫn liên kết (`href`), link ảnh (`src`) hoặc tiêu đề đầy đủ. | `link = book.h3.a.get('href')` |
| `soup.select(css_selector)` | Tìm kiếm phần tử bằng bộ chọn **CSS Selector** (tương tự như trong CSS/JavaScript). | Ngắn gọn và mạnh mẽ khi cần truy vấn lồng nhau phức tạp. | `prices = soup.select('div.product > p.price')` |

---

### 3. Phân tích chi tiết quy trình Web Scraping 4 bước (Step-by-step)

#### **Bước 1: Gửi HTTP Request kèm User-Agent giả lập trình duyệt**
```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers, timeout=10)
```
- **Tại sao cần `User-Agent`?**: Nếu bạn không khai báo `headers`, thư viện `requests` sẽ gửi User-Agent mặc định là `python-requests/2.x.x`. Rất nhiều máy chủ web được cấu hình tự động chặn các yêu cầu có User-Agent này. Khai báo User-Agent trình duyệt thật giúp yêu cầu của bạn trông như một người dùng bình thường đang lướt web.
- **Tại sao cần `timeout`?**: Đảm bảo chương trình không bị treo vô hạn nếu mạng chậm hoặc máy chủ web phản hồi quá lâu.

#### **Bước 2: Phân tích cây DOM HTML với BeautifulSoup**
```python
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
```
- Cấu trúc cây DOM (Document Object Model) của trang web được tổ chức dạng cây phả hệ (Parent - Child - Sibling như mô tả tại Slide 12).
- Thẻ `<article class="product_pod">` là thẻ cha bao bọc toàn bộ thông tin của một cuốn sách (ảnh, tiêu đề, xếp hạng, giá, nút mua hàng).

#### **Bước 3: Thu thập dữ liệu đa trang & nguyên tắc cào dữ liệu văn minh (Polite Scraping)**
```python
for page in range(1, 6):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    # Gửi request và bóc tách dữ liệu...
    time.sleep(0.5)  # Nghỉ 0.5s giữa các lần gửi request
```
- **Nguyên tắc đạo đức (Slide 8)**: Cào web không được phép gây quá tải máy chủ (DDoS). Lệnh `time.sleep(0.5)` giúp tạo khoảng nghỉ tự nhiên, tôn trọng tài nguyên của trang web.

#### **Bước 4: Lưu dữ liệu thô và làm sạch bằng Pandas**
```python
# Trích xuất số thực cho giá tiền (loại bỏ ký tự £)
df_clean["price_gbp"] = df_clean["price_raw"].str.extract(r'(\d+\.\d+)')[0].astype(float)

# Ánh xạ đánh giá sao từ chữ sang số
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df_clean["rating_stars"] = df_clean["rating_str"].map(rating_map).fillna(0).astype(int)
```
- **Tại sao phải làm sạch trước khi phân tích?**: Dữ liệu cào từ web luôn ở dạng văn bản thô (`string`). Không thể tính giá trung bình hay độ lệch chuẩn trên chuỗi `"£51.77"`. Việc chuyển đổi sang kiểu số thực (`float`) và số nguyên (`int`) là bắt buộc để áp dụng các thuật toán thống kê mô tả (Mean, Median, Std) và vẽ biểu đồ.

---

### 4. So sánh toàn diện: BeautifulSoup vs Scrapy

Mục 10 của Slide Week 4 yêu cầu: **"So sánh hai phương pháp Web Scraping: BeautifulSoup vs Scrapy"**. Dưới đây là bảng đối chiếu chuyên sâu theo 8 tiêu chí kỹ thuật:

| Tiêu chí | BeautifulSoup (bs4) | Scrapy Framework |
| :--- | :--- | :--- |
| **1. Bản chất kiến trúc** | Là một **thư viện phân tích cú pháp HTML/XML** (Parser). Chỉ có nhiệm vụ bóc tách chuỗi HTML, cần kết hợp với `requests` hoặc `urllib` để tải trang. | Là một **Khung ứng dụng (Framework) thu thập web hoàn chỉnh**. Bao trọn toàn bộ vòng đời từ gửi request, quản lý hàng đợi, phân tích cú pháp, đến pipeline lưu trữ. |
| **2. Tốc độ & Hiệu năng** | **Đơn luồng, chạy tuần tự (Synchronous)**. Mỗi trang web phải đợi tải xong mới tới trang tiếp theo. Chậm khi cào hàng chục nghìn trang. | **Bất đồng bộ, đa luồng cực nhanh (Asynchronous)** dựa trên động cơ *Twisted Event Loop*. Cho phép xử lý đồng thời hàng trăm trang web cùng lúc. |
| **3. Độ phức tạp khi viết code** | **Rất đơn giản, trực quan**. Chỉ cần 10 - 20 dòng code trong 1 file script `.py` hoặc chạy trực tiếp trong Jupyter Notebook. | **Có cấu trúc dự án nghiêm ngặt**. Cần tạo project bằng lệnh `scrapy startproject`, quản lý thư mục: `spiders/`, `items.py`, `middlewares.py`, `pipelines.py`, `settings.py`. |
| **4. Cơ chế trích xuất dữ liệu** | Sử dụng các hàm trực quan của thư viện: `.find()`, `.find_all()`, hoặc CSS Selector cơ bản với `.select()`. | Tích hợp công cụ `parsel` hỗ trợ cả **CSS Selectors** và **XPath** cực kỳ mạnh mẽ, trích xuất dữ liệu sâu trong cây DOM. |
| **5. Thu thập đa trang (Crawling & Following links)** | Người lập trình phải **tự viết code thủ công**: tự tạo vòng lặp URL, tự tìm thẻ `<a href="...">` và tự gọi đệ quy. | **Tự động hóa hoàn toàn**. Sử dụng `response.follow(next_page, callback=self.parse)` hoặc sử dụng lớp `CrawlSpider` tự động quét toàn bộ site theo luật (Rules). |
| **6. Khả năng xuất dữ liệu (Export)** | Phải tự viết code lưu file bằng thư viện `csv`, `json` hoặc chuyển qua `pandas.DataFrame.to_csv()`. | **Tích hợp sẵn (Feed Exports)**. Chỉ cần thêm tham số dòng lệnh: `scrapy runspider spider.py -o output.csv` hoặc `-o output.json`. |
| **7. Cơ chế phòng thủ & bảo vệ (Anti-scraping)** | Không có sẵn. Lập trình viên phải tự quản lý proxy xoay vòng, tự đổi User-Agent, tự xử lý cookie phiên làm việc. | Tích hợp sẵn kiến trúc **Middleware**: AutoThrottle (tự động điều chỉnh tốc độ cào theo tải server), User-Agent rotation, Proxy Middleware, tự động kiểm tra `robots.txt`. |
| **8. Khi nào nên dùng?** | - Phân tích dữ liệu nhanh, bài tập học tập, nghiên cứu khoa học.<br>- Quy mô nhỏ và vừa (< 10.000 trang).<br>- Tích hợp mượt mà trong Jupyter Notebook để vừa cào vừa làm sạch dữ liệu. | - Dự án thu thập dữ liệu công nghiệp quy mô lớn (hàng triệu URL).<br>- Hệ thống crawl định kỳ tự động chạy trên máy chủ (Cronjob/Airflow).<br>- Cần khả năng mở rộng (Scalability) và tối ưu băng thông mạng. |

---

### 5. Nguyên tắc đạo đức và pháp lý trong Web Scraping (Ethics & Legalities)

Theo hướng dẫn tại **Slide 8**:
1. **Luôn kiểm tra tệp `robots.txt`**:
   - Truy cập `https://example.com/robots.txt` để kiểm tra các đường dẫn mà chủ website cho phép (`Allow`) hoặc cấm (`Disallow`) bot thu thập.
2. **Không làm nghẽn máy chủ (Do not DDoS)**:
   - Luôn đặt thời gian trễ hợp lý giữa các yêu cầu (ví dụ: `time.sleep(0.5 - 2s)` trong BeautifulSoup hoặc cấu hình `DOWNLOAD_DELAY = 1` trong Scrapy).
3. **Chỉ thu thập dữ liệu công khai**:
   - Không vượt qua các cơ chế xác thực đăng nhập trái phép, không bẻ khóa bảo mật, không thu thập thông tin định danh cá nhân nhạy cảm (PII: thẻ tín dụng, số điện thoại, mật khẩu).
4. **Tôn trọng bản quyền tác giả và Điều khoản dịch vụ (Terms of Service - ToS)**.

---

### 6. Hướng dẫn chạy và kiểm thử mã nguồn

Mở Terminal trong thư mục dự án và chạy các lệnh sau:

#### Cách 1: Chạy chương trình cào dữ liệu bằng BeautifulSoup & Làm sạch dữ liệu
```powershell
.venv\Scripts\python.exe Week4_Web_Scraping_Exercise\scrape_products_bs4.py
```
*Kết quả:* Tạo ra hai file dữ liệu:
- `products_raw.csv`: Dữ liệu 100 sản phẩm thô ban đầu.
- `products_cleaned.csv`: Dữ liệu 100 sản phẩm đã chuẩn hóa số tiền, xếp hạng sao và tình trạng kho.

#### Cách 2: Chạy Scrapy Spider mẫu
```powershell
cd Week4_Web_Scraping_Exercise
..\.venv\Scripts\scrapy.exe runspider scrapy_spider_example.py -o scrapy_books.csv
cd ..
```
*Kết quả:* Scrapy tự động cào 3 trang sản phẩm trong chưa đầy 2 giây và xuất ra file `scrapy_books.csv`.

#### Cách 3: Mở tương tác trên Jupyter Notebook
Mở file [Bai_Giai_Web_Scraping_ECommerce.ipynb](file:///e:/Phân tích dữ liệu/Week4_Web_Scraping_Exercise/Bai_Giai_Web_Scraping_ECommerce.ipynb) trong VS Code để xem từng bước thực thi kèm biểu đồ trực quan hóa giá tiền và xếp hạng sản phẩm.
