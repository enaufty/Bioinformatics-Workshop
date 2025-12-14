import pandas as pd
import matplotlib.pyplot as plt
introns_df = pd.read_table('introns (1).tsv')
first_100 = introns_df.head(100)
last_100 = introns_df.tail(100)
positive_genes = introns_df[introns_df['Strand'] == '+']['Gene'].unique()
negative_genes = introns_df[introns_df['Strand'] == '-']['Gene'].unique()
print(f"Positive: {len(positive_genes)}")
print(f"Negative: {len(negative_genes)}")

print("Biggest Intron:", introns_df['Size'].max())
print("Smallest Intron:", introns_df['Size'].min())
print("Average Size:", introns_df['Size'].mean())

# 1. Boyutu 1000'den küçük veya eşit olanları seç
# "small_introns" adında yeni bir tablo yapıyoruz.
small_introns = introns_df[introns_df['Size'] <= 1000]

# 2. Çizim Alanı Oluştur
plt.figure(figsize=(10, 6))

# 3. Histogramı Çiz
# bins=1000: Veriyi 1000 çubuğa böler.
plt.hist(small_introns['Size'], bins=1000, color='hotpink')

# 4. Sınırları Belirle
plt.ylim(0, 2000) # Y ekseni sınırı
plt.xlim(0, 1000) # X ekseni sınırı

plt.xlabel("Intron Size")
plt.ylabel("Frequency")
plt.title("Schistosoma Mansoni Intron Size Distrubition")



plt.show()