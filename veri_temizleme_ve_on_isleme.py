# ==========================================
# PROJE: Büyük Veri Setlerinde Veri Temizleme
# YAZAR: Aslı Hüma
# AMAÇ: Eksik, hatalı ve kirli verileri analiz edilebilir hale getirmek.
# ==========================================

import pandas as pd
import numpy as np

# 1. KİRLİ VERİ SETİ OLUŞTURMA (Gerçek hayattaki hatalı verileri simüle ediyoruz)
data = {
    'Tarih': ['2026-04-01', '2026-04-02', None, '2026-04-04', '2026-04-05'],
    'Satis_Miktari': [150, np.nan, 200, 450, -500], # -500 hatalı bir veri (negatif satış olamaz)
    'Musteri_Bolgesi': ['Istanbul', 'ankara', 'ISTANBUL', 'Izmir', None] # Karışık yazım ve eksik bölge
}

df = pd.DataFrame(data)

# 2. VERİ TEMİZLEME İŞLEMLERİ
def veriyi_pirlanta_yap(dataframe):
    print("--- Veri Temizleme Süreci Başladı ---\n")
    
    # A. Eksik Verileri Doldurma (Satis_Miktari boşsa ortalama ile doldur)
    dataframe['Satis_Miktari'] = dataframe['Satis_Miktari'].fillna(dataframe['Satis_Miktari'].mean())
    
    # B. Hatalı Verileri Düzeltme (Negatif satış miktarını 0 veya mutlak değer yap)
    dataframe['Satis_Miktari'] = dataframe['Satis_Miktari'].apply(lambda x: abs(x))
    
    # C. Metin Verilerini Standartlaştırma (Bölgeleri büyük harf yap ve boşları 'BİLİNMİYOR' yap)
    dataframe['Musteri_Bolgesi'] = dataframe['Musteri_Bolgesi'].str.upper().fillna('BİLİNMİYOR')
    
    # D. Tarih Formatını Düzeltme ve Boşları Silme
    dataframe = dataframe.dropna(subset=['Tarih'])
    
    return dataframe

# 3. TEMİZLENMİŞ VERİYİ GÖSTER
temiz_df = veriyi_pirlanta_yap(df)
print("Temizlenmiş Veri Seti:")
print(temiz_df)

# 4. KÜÇÜK BİR ANALİZ ÇIKTISI
toplam_satis = temiz_df['Satis_Miktari'].sum()
print(f"\nToplam Satış Miktarı: {toplam_satis}")
