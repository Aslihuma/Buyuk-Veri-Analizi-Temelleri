# ==========================================
# PROJE: Veri Normalizasyonu ve Özellik Mühendisliği
# YAZAR: Aslı Hüma
# AMAÇ: Ham verileri ölçeklendirmek ve yeni analiz değişkenleri üretmek.
# ==========================================

import pandas as pd

# 1. HAM VERİ SETİ (Eğitim ve Performans Verileri)
ham_veri = {
    'Ogrenci_ID': [1, 2, 3, 4, 5],
    'Teorik_Not': [95, 40, 70, 20, 85],
    'Uygulama_Notu': [100, 30, 80, 10, 90],
    'Sistemde_Gecirilen_Dakika': [1200, 150, 600, 50, 900]
}

df = pd.DataFrame(ham_veri)

# 2. ÖZELLİK MÜHENDİSLİĞİ (Feature Engineering)
def analiz_hazirligi(dataframe):
    print("--- Özellik Mühendisliği Süreci Başladı ---\n")
    
    # A. Yeni Sütun Türetme: Başarı Endeksi
    # Teorik notun %40'ı, uygulama notunun %60'ı alınarak karma bir puan oluşturulur.
    dataframe['Basari_Endeksi'] = (dataframe['Teorik_Not'] * 0.4) + (dataframe['Uygulama_Notu'] * 0.6)
    
    # B. Veri Normalizasyonu (Min-Max Scaling)
    # Sistemde geçirilen süreyi 0 ile 1 arasına çekiyoruz (Büyük veri analizinde çok önemlidir)
    min_dakika = dataframe['Sistemde_Gecirilen_Dakika'].min()
    max_dakika = dataframe['Sistemde_Gecirilen_Dakika'].max()
    
    dataframe['Etkilesim_Skoru'] = (dataframe['Sistemde_Gecirilen_Dakika'] - min_dakika) / (max_dakika - min_dakika)
    
    # C. Kategorik Sınıflandırma
    # Endekse göre seviye belirleme
    dataframe['Seviye'] = dataframe['Basari_Endeksi'].apply(
        lambda x: 'Yüksek' if x > 80 else ('Orta' if x > 50 else 'Düşük')
    )
    
    return dataframe

# 3. İŞLENMİŞ VERİYİ GÖSTER
islenmis_df = analiz_hazirligi(df)
print("Normalizasyon Sonrası Tablo:")
print(islenmis_df[['Ogrenci_ID', 'Basari_Endeksi', 'Etkilesim_Skoru', 'Seviye']])

# 4. ÖZET ÇIKTI
print("\nSeviye Bazlı Öğrenci Dağılımı:")
print(islenmis_df['Seviye'].value_counts())
