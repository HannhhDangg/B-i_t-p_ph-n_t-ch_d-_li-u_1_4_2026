# ==============================================================================
# BÀI TẬP TUẦN 4: WEB SCRAPING - THU THẬP & LÀM SẠCH DỮ LIỆU SẢN PHẨM TMĐT
# Thư viện sử dụng: requests, BeautifulSoup (bs4), pandas, time
# ==============================================================================

import sys
import os
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Đảm bảo hiển thị tiếng Việt UTF-8 chuẩn trên Windows console
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

print("=== BẮT ĐẦU QUÁ TRÌNH WEB SCRAPING VỚI BEAUTIFULSOUP ===")

# ------------------------------------------------------------------------------
# PHẦN 1: THU THẬP DỮ LIỆU SẢN PHẨM TỪ TRANG THƯƠNG MẠI ĐIỆN TỬ
# Website: Books to Scrape (http://books.toscrape.com)
# Trang web TMĐT chuẩn mực quốc tế cho thực hành Web Scraping
# ------------------------------------------------------------------------------

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

products_data = []
num_pages = 5  # Thu thập 5 trang đầu tiên (mỗi trang 20 sản phẩm = 100 sản phẩm)

for page in range(1, num_pages + 1):
    page_url = base_url.format(page)
    print(f"--> Đang gửi HTTP GET Request tới Trang {page}: {page_url}")
    
    response = requests.get(page_url, headers=headers, timeout=10)
    
    # Kiểm tra mã trạng thái HTTP (200 = Thành công)
    if response.status_code != 200:
        print(f"Lỗi truy cập trang {page} (Status: {response.status_code})")
        continue

    # Đặt encoding UTF-8 để xử lý đúng ký tự đặc biệt
    response.encoding = "utf-8"
    
    # Phân tích cú pháp tài liệu HTML với BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Tìm tất cả các thẻ <article class="product_pod"> đại diện cho từng sản phẩm
    book_cards = soup.find_all("article", class_="product_pod")
    
    for book in book_cards:
        # 1. Tên sản phẩm (Title) nằm trong thuộc tính 'title' của thẻ <a> bên trong thẻ <h3>
        title = book.h3.a.get("title", "").strip()
        
        # 2. Giá sản phẩm thô (Raw Price) ví dụ '£51.77' nằm trong thẻ <p class="price_color">
        price_raw = book.find("p", class_="price_color").text.strip()
        
        # 3. Đánh giá xếp hạng sao (Star Rating) nằm trong class của thẻ <p class="star-rating Three">
        rating_classes = book.find("p", class_="star-rating").get("class", [])
        rating_str = [c for c in rating_classes if c != "star-rating"][0] if len(rating_classes) > 1 else "Unknown"
        
        # 4. Tình trạng hàng tồn kho (Availability) ví dụ 'In stock'
        availability = book.find("p", class_="instock availability").text.strip()
        
        # 5. Đường link chi tiết của sản phẩm (Product URL)
        detail_rel_url = book.h3.a.get("href", "")
        detail_full_url = "http://books.toscrape.com/catalogue/" + detail_rel_url
        
        products_data.append({
            "title": title,
            "price_raw": price_raw,
            "rating_str": rating_str,
            "availability_raw": availability,
            "url": detail_full_url
        })
    
    # Nghỉ 0.5 giây giữa các lượt gửi request để tôn trọng tài nguyên máy chủ (Polite Scraping)
    time.sleep(0.5)

print(f"\n=> Đã thu thập thành công {len(products_data)} sản phẩm từ {num_pages} trang web!")

# ------------------------------------------------------------------------------
# PHẦN 2: LƯU DỮ LIỆU THÔ RA FILE CSV
# ------------------------------------------------------------------------------

# Chuyển đổi danh sách dict thành DataFrame
df_raw = pd.DataFrame(products_data)

# Lưu dữ liệu thô ban đầu ra file CSV
raw_csv_path = os.path.join(os.path.dirname(__file__), "products_raw.csv")
df_raw.to_csv(raw_csv_path, index=False, encoding="utf-8-sig")
print(f"Đã lưu dữ liệu thô vào: {raw_csv_path}")
print("\n5 dòng dữ liệu thô đầu tiên:")
print(df_raw.head())

# ------------------------------------------------------------------------------
# PHẦN 3: LÀM SẠCH DỮ LIỆU (DATA CLEANING) VỚI PANDAS
# ------------------------------------------------------------------------------

print("\n--- BẮT ĐẦU QUÁ TRÌNH LÀM SẠCH DỮ LIỆU ---")
df_clean = df_raw.copy()

# 1. Làm sạch cột giá tiền (Price): Trích xuất phần số thực (bỏ mọi ký tự tiền tệ như £, $, ...)
df_clean["price_gbp"] = df_clean["price_raw"].str.extract(r"(\d+\.\d+)")[0].astype(float)

# 2. Làm sạch cột xếp hạng (Star Rating): Ánh xạ từ chữ tiếng Anh sang số nguyên (1 - 5)
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df_clean["rating_stars"] = df_clean["rating_str"].map(rating_map).fillna(0).astype(int)

# 3. Làm sạch cột tình trạng kho (Availability):
# Chuyển chuỗi dài có nhiều khoảng trắng thành trạng thái 'In Stock' ngắn gọn
df_clean["is_in_stock"] = df_clean["availability_raw"].str.contains("In stock", case=False)

# 4. Sắp xếp lại thứ tự cột gọn gàng và xóa các cột thô không cần thiết
df_clean = df_clean[["title", "price_gbp", "rating_stars", "is_in_stock", "url"]]

# Lưu dữ liệu đã làm sạch vào file CSV mới
clean_csv_path = os.path.join(os.path.dirname(__file__), "products_cleaned.csv")
df_clean.to_csv(clean_csv_path, index=False, encoding="utf-8-sig")
print(f"Đã lưu dữ liệu làm sạch vào: {clean_csv_path}")

print("\n5 dòng dữ liệu sau khi làm sạch:")
print(df_clean.head())

# ------------------------------------------------------------------------------
# PHẦN 4: PHÂN TÍCH THỐNG KÊ SƠ BỘ (EDA)
# ------------------------------------------------------------------------------

print("\n=== THỐNG KÊ MÔ TẢ GIÁ TIỀN & XẾP HẠNG ===")
print(df_clean[["price_gbp", "rating_stars"]].describe())

avg_price = df_clean["price_gbp"].mean()
min_price = df_clean["price_gbp"].min()
max_price = df_clean["price_gbp"].max()
print(f"\n- Giá sách trung bình: £{avg_price:.2f}")
print(f"- Giá sách thấp nhất: £{min_price:.2f}")
print(f"- Giá sách cao nhất: £{max_price:.2f}")

print("\n- Phân phối xếp hạng sao (1 - 5 sao):")
print(df_clean["rating_stars"].value_counts().sort_index())

print("\n=== HOÀN THÀNH TOÀN BỘ CHƯƠNG TRÌNH WEB SCRAPING ===")
