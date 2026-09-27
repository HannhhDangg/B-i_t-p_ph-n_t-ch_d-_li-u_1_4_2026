# ==============================================================================
# BÀI TẬP 07: TRỰC QUAN HÓA DỮ LIỆU - VISUALIZATION (THẢM HỌA TITANIC)
# Môn học: Phân tích dữ liệu với Python
# ==============================================================================

# Step 1: Import các thư viện cần thiết
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Thiết lập style thẩm mỹ cho biểu đồ
sns.set_theme(style='whitegrid')

print("--- STEP 1: IMPORT THƯ VIỆN THÀNH CÔNG ---")

# Step 2 & 3: Đọc dữ liệu từ URL và gán vào biến titanic
url = 'https://raw.githubusercontent.com/thieu1995/csv-files/main/data/pandas/titanic_train.csv'
titanic = pd.read_csv(url)
print("\n--- STEP 2 & 3: DỮ LIỆU BAN ĐẦU ---")
print(titanic.head())

# Step 4: Đặt PassengerId làm chỉ số (Index)
titanic.set_index('PassengerId', inplace=True)
print("\n--- STEP 4: SAU KHI ĐẶT PassengerId LÀM INDEX ---")
print(titanic.head())

# Step 5: Tạo biểu đồ tròn (Pie Chart) biểu diễn tỷ lệ Nam / Nữ
gender_counts = titanic['Sex'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=['Nam (Male)', 'Nữ (Female)'], autopct='%1.1f%%',
        colors=['#3498db', '#e74c3c'], startangle=90, explode=(0.05, 0))
plt.title('Tỷ Lệ Hành Khách Nam / Nữ Trên Tàu Titanic', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Step 6: Tạo biểu đồ phân tán (Scatterplot) giữa Giá vé (Fare) và Tuổi (Age), tô màu theo Giới tính (Sex)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=titanic, x='Age', y='Fare', hue='Sex', palette={'male': '#2980b9', 'female': '#e74c3c'}, alpha=0.7)
plt.title('Mối Quan Hệ Giữa Giá Vé Và Độ Tuổi Phân Theo Giới Tính', fontsize=14, fontweight='bold')
plt.xlabel('Độ tuổi (Năm)', fontsize=12)
plt.ylabel('Giá vé ($)', fontsize=12)
plt.tight_layout()
plt.show()

# Step 7: Có bao nhiêu người đã sống sót?
survived_count = titanic['Survived'].sum()
total_passengers = len(titanic)
print(f"\n--- STEP 7: SỐ LƯỢNG NGƯỜI SỐNG SÓT: {survived_count} / {total_passengers} ({survived_count/total_passengers*100:.2f}%) ---")

# Step 8: Tạo biểu đồ tần số (Histogram) biểu diễn phân phối của Giá vé (Fare)
plt.figure(figsize=(10, 6))
plt.hist(titanic['Fare'], bins=40, color='#2ecc71', edgecolor='black', alpha=0.8)
plt.title('Phân Phối Của Giá Vé (Fare Histogram)', fontsize=14, fontweight='bold')
plt.xlabel('Giá vé ($)', fontsize=12)
plt.ylabel('Số lượng hành khách (Tần suất)', fontsize=12)
plt.tight_layout()
plt.show()

# BONUS: Biểu đồ cột (Bar Chart) - Tỷ lệ sống sót theo Hạng vé (Pclass)
plt.figure(figsize=(8, 5))
pclass_survival = titanic.groupby('Pclass')['Survived'].mean() * 100
ax = sns.barplot(x=pclass_survival.index, y=pclass_survival.values, palette='Blues_d')
plt.title('Tỷ Lệ Sống Sót (%) Theo Hạng Vé (Pclass)', fontsize=14, fontweight='bold')
plt.xlabel('Hạng vé (1 = Hạng nhất, 2 = Hạng nhì, 3 = Hạng ba)', fontsize=12)
plt.ylabel('Tỷ lệ sống sót (%)', fontsize=12)

for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 7), textcoords='offset points', fontweight='bold')

plt.tight_layout()
plt.show()

print("\nHoàn thành bài tập 07!")
