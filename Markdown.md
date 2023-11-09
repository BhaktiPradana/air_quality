# Interactive Air Quality and Temperature Dashboard ✨

## Setup environment
```
conda create --project_akhir main-ds python=3.9
conda activate main-ds
pip install streamlit seaborn matplotlib pandas altair
```

## Run steamlit app
```
streamlit run dashboard_analisis.py
```
## Link for Dashboard
```
https://analysis-air-quality.streamlit.app/
```
```
![image](https://github.com/BhaktiPradana/air_quality/assets/130721271/d120a375-6975-4cdd-a332-35ab508eb29e)
```
### Conclusion
```
1. Analisa tingkat polusi udara, yang diukur dengan PM10, SO2, NO2, dan CO, berhubungan dengan perubahan suhu seiring waktu:
  Dalam analisis data, kita dapat menemukan bahwa hubungan antara tingkat polusi udara (diukur dengan PM10, SO2, NO2, dan CO) dan perubahan suhu seiring waktu cukup kompleks. Ada beberapa hubungan yang dapat diidentifikasi: Terdapat beberapa korelasi positif antara tingkat polusi udara dan suhu, yang berarti ketika polusi meningkat, suhu juga cenderung meningkat.
Beberapa negatif korelasi juga terlihat, yang berarti ketika polusi meningkat, suhu cenderung menurun.
Namun, ada banyak faktor lain yang memengaruhi hubungan ini, seperti musim, cuaca, dan geografi.

2. Korelasi antara kadar O3 dalam udara dengan fluktuasi suhu
Analisis menunjukkan bahwa fluktuasi suhu tidak memiliki korelasi yang jelas dengan kadar O3 dalam udara. Oleh karena itu, tidak ada hubungan kuat antara kedua variabel ini dalam data yang dievaluasi.

3. Pengaruh polutan udara (PM10, SO2, NO2, dan CO) pada suhu harian rata-rata
  Dari analisis data, kita dapat menyimpulkan bahwa polutan udara (PM10, SO2, NO2, dan CO) memiliki pengaruh yang kompleks pada suhu harian rata-rata. Hubungannya tergantung pada faktor-faktor lain seperti musim, cuaca, dan lokasi geografis. Terkadang tingkat polutan udara positif berkorelasi dengan peningkatan suhu, sementara terkadang mereka berkorelasi negatif dengan suhu. Pola ini dapat bervariasi seiring waktu.

Pola polusi udara (PM10, SO2, NO2, dan CO) selama periode tertentu dapat memprediksi fluktuasi suhu di masa depan
  Dalam analisis ini, tidak ditemukan bukti yang kuat bahwa pola polusi udara (SO2, NO2, dan CO) selama periode tertentu secara konsisten dapat memprediksi fluktuasi suhu di masa depan. Fluktuasi suhu tergantung pada banyak faktor, dan polusi udara adalah salah satu faktor yang memengaruhi, tetapi tidak selalu merupakan prediktor yang andal. Prediksi suhu yang lebih akurat memerlukan pertimbangan lebih dari sekadar polusi udara, seperti data cuaca, geografi, dan faktor lingkungan lainnya. Nilai PM10 yang teranalisis adalah sedang hingga tidak sehat ini menandakan partikulat berakibat mulai penurunan pada jarak pandang dan menyebabkan jarak pandang turun secara signifikan, dan terjadi pengotoran debu di mana-mana.
```

