# ==============================================================================
# VÍ DỤ SCRAIPY SPIDER: CÀO DỮ LIỆU SẢN PHẨM TMĐT VỚI FRAMEWORK SCRAPY
# Cách chạy:
#   scrapy runspider scrapy_spider_example.py -o scrapy_books.csv
# ==============================================================================

import scrapy

class BookSpider(scrapy.Spider):
    name = "books_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/catalogue/page-1.html"]
    
    # Cấu hình thiết lập Spider (tuân thủ đạo đức & rate limiting)
    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,        # Nghỉ 0.5s giữa các request (tránh làm quá tải server)
        'ROBOTSTXT_OBEY': True,       # Tuân thủ robots.txt của website
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'CLOSESPIDER_PAGECOUNT': 3,   # Giới hạn cào 3 trang mẫu để kiểm thử nhanh
        'FEEDS': {
            'scrapy_books.csv': {
                'format': 'csv',
                'encoding': 'utf8',
                'overwrite': True
            }
        }
    }

    def parse(self, response):
        """
        Hàm callback chính được gọi khi nhận được HTTP Response từ trang web.
        Sử dụng CSS Selector hoặc XPath để bóc tách thông tin từng cuốn sách.
        """
        # Duyệt qua từng thẻ <article class="product_pod">
        for book in response.css("article.product_pod"):
            title = book.css("h3 a::attr(title)").get()
            price = book.css("p.price_color::text").get()
            
            # Trích xuất class sao đánh giá (ví dụ: 'star-rating Four')
            rating_classes = book.css("p.star-rating::attr(class)").get()
            rating = rating_classes.replace("star-rating", "").strip() if rating_classes else ""
            
            # Trích xuất link chi tiết sản phẩm và tạo URL tuyệt đối
            rel_url = book.css("h3 a::attr(href)").get()
            full_url = response.urljoin(rel_url)
            
            # Trích xuất tình trạng tồn kho
            availability = "".join(book.css("p.instock.availability::text").getall()).strip()

            # Trả về từng dòng bản ghi dữ liệu (Scrapy tự động chuyển thành CSV/JSON)
            yield {
                "title": title,
                "price": price,
                "rating": rating,
                "availability": availability,
                "url": full_url
            }

        # ----------------------------------------------------------------------
        # CƠ CHẾ TỰ ĐỘNG THU THẬP PHÂN TRANG (CRAWLING & FOLLOWING LINKS)
        # ----------------------------------------------------------------------
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            # response.follow tự động kết hợp URL tương đối và gọi lại hàm parse
            yield response.follow(next_page, callback=self.parse)
