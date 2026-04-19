# ==========================================
# PROJE: Keşifçi Veri Analizi (EDA) Uygulaması
# YAZAR: Aslı Hüma
# AMAÇ: Büyük veri setlerinde trend analizi ve grup bazlı istatistikler.
# ==========================================

import pandas as pd

# 1. BÜYÜK VERİ SİMÜLASYU (Satış Verileri)
# Gerçek dünyada bu veri 100.000+ satırlık bir CSV dosyası olurdu.
satis_verisi = {
    'Urun_Kategorisi': ['Elektronik', 'Moda', 'Elektronik', 'Ev-Yaşam', 'Moda', 'Elektronik', 'Ev-Yaşam'],
    'Satis_Adedi': [120, 450, 300, 150, 600, 210, 80],
    'Birim_Fiyat': [5000, 450, 5200, 1200, 400, 4800, 1500],
    'Satis_Bolgesi': ['Marmara', 'Ege', 'Marmara', 'İç Anadolu', 'Ege', 'Akdeniz', 'İç Anadolu']
}

df = pd.DataFrame(satis_verisi)

# 2. TOPLAM GELİR HESAPLAMA (Veri Manipülasyonu)
df['Toplam_Gelir'] = df['Satis_Adedi'] * df['Birim_Fiyat']

def istatistiksel_ozet_getir(dataframe):
    print("--- VERİ SETİ GENEL ÖZETİ ---\n")
    
    # A. Kategorilere Göre Toplam Gelir (Hangi kategori daha çok kazandırıyor?)
    kategori_ozet = dataframe.groupby('Urun_Kategorisi')['Toplam_Gelir'].sum().sort_values(ascending=False)
    
    # B. Bölgelere Göre Ortalama Satış Adedi (Hangi bölge daha çok ürün tüketiyor?)
    bolge_ozet = dataframe.groupby('Satis_Bolgesi')['Satis_Adedi'].mean()
    
    # C. Veri Setinin Temel İstatistikleri (Max, Min, Std Sapma)
    genel_istatistik = dataframe['Toplam_Gelir'].describe()
    
    return kategori_ozet, bolge_ozet, genel_istatistik

# 3. SONUÇLARI RAPORLA
kat_rapor, bolge_rapor, genel_rapor = istatistiksel_ozet_getir(df)

print("Kategori Bazlı Toplam Gelir Sıralaması:")
print(kat_rapor)

print("\nBölge Bazlı Ortalama Satış Adetleri:")
print(bolge_rapor)

print("\nGenel Gelir İstatistikleri (Max/Min/Ortalama):")
print(genel_rapor)

# 4. KRİTİK EŞİK ANALİZİ
# 1 Milyon TL üzeri gelir getiren kategorileri filtrele
yuksek_gelirli = df[df['Toplam_Gelir'] > 1000000]
print("\n--- Yüksek Performanslı Satışlar (1M+ TL) ---")
print(yuksek_gelirli[['Urun_Kategorisi', 'Toplam_Gelir']])
