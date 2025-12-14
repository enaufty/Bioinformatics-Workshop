# 🧬 Genomik Veri Analizi ve Görselleştirme Workshopu

## 🚀 Proje İçeriği

Bu notebook aşağıdaki adımları içermektedir:

1.  **Teorik Giriş:** Genom analizi, Sekanslama, Genom Montajı ve Anotasyon kavramları.
2.  **Veri Hazırlığı:**
    * Ham **GFF3** (General Feature Format) dosyasının okunması.
    * Verinin Pandas DataFrame'ine dönüştürülmesi ve temizlenmesi.
    * **Ekson (Exon)** verilerinin filtrelenmesi.
3.  **İntron Analizi:**
    * `introns.tsv` dosyası üzerinden istatistiksel analizler.
    * İntron boyut dağılımlarının **Histogram** ile görselleştirilmesi.
4.  **İleri Düzey Analiz (Challenge):**
    * Genlerin DNA üzerindeki yönüne (Strand: + veya -) göre intron pozisyonlarının analizi.
    * 5'->3' ve 3'->5' yönelimlerine göre medyan intron boyutlarının karşılaştırmalı **Çizgi Grafiği (Line Plot)** ile gösterilmesi.


## 📂 Veri Setleri

Projede kullanılan veri setleri:
* **GFF3 Dosyası:** *Schistosoma mansoni* genom anotasyonları (WormBase veritabanından).
* **Introns TSV:** İntronların başlangıç, bitiş ve boyut bilgilerini içeren yapılandırılmış veri seti.
