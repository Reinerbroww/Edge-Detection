

## 🧠 Deskripsi Project
Project ini merupakan bagian dari **mata kuliah Pengolahan Citra Digital (PCD)** yang bertujuan untuk menerapkan proses **preprocessing citra** dan **deteksi tepi (edge detection)** menggunakan **Python dan OpenCV**.

Program akan membaca seluruh gambar dalam folder dataset, memprosesnya secara otomatis tahap demi tahap, lalu menyimpan setiap hasil pengolahan ke dalam folder output.

---

## 📌 Fitur Utama
✅ Grayscale Conversion  
✅ Gaussian Blur  
✅ Histogram Equalization  
✅ Sobel Edge Detection  
✅ Canny Edge Detection  
✅ Pemrosesan batch (banyak gambar sekaligus)  
✅ Output tersimpan otomatis  

---

## 📁 Struktur Folder
```

Deteksi_Tepi_PCD/
├── main.py              # source code utama
├── dataset/             # input gambar
├── hasil/               # output hasil pengolahan
├── .gitignore
└── README.md

```

---

## 📂 Dataset
Dataset gambar dapat diunduh melalui Google Drive berikut:

🔗 **Link Dataset:**  
https://drive.google.com/drive/folders/1fAUHUyCcsGcwbI1eVmj5B4DMAImzweKA?usp=drive_link

📌 Setelah download, masukkan seluruh file gambar ke dalam:
```

dataset/

```

---

## 🛠 Software & Tools
Pastikan perangkat sudah terinstall:

- **Python 3.10**  
  https://www.python.org/downloads/release/python-31011/
- **Visual Studio Code**  
  https://code.visualstudio.com/

---

## 📦 Library yang Digunakan
```

numpy==1.26.4
opencv-python==4.7.0.72

````

---

## 🚀 Cara Menjalankan Project
Ikuti langkah berikut dengan urut:

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Reinerbroww/Deteksi_Tepi_PCD.git
cd Deteksi_Tepi_PCD
````

### 2️⃣ Buat Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Aktifkan Virtual Environment (Windows)

```bash
.venv\Scripts\activate
```

### 4️⃣ Install Library

```bash
pip install numpy==1.26.4
pip install opencv-python==4.7.0.72
```

### 5️⃣ Siapkan Dataset

Masukkan gambar dengan format `.jpg`, `.png`, atau `.jpeg` ke folder:

```
dataset/
```

### 6️⃣ Jalankan Program

```bash
python main.py
```

### 7️⃣ Lihat Hasil Output

Semua hasil preprocessing dan deteksi tepi akan otomatis tersimpan di:

```
hasil/
```

---

## 🔍 Metode Pengolahan Citra

* Grayscale Conversion
* Gaussian Blur
* Histogram Equalization
* Sobel Edge Detection
* Canny Edge Detection

---

## ✨ Author

**Reinnher Sakunab**
F55124110
Program Studi Teknik Informatika
Universitas Tadulako

---

<p align="center">
  <i>Project ini dibuat untuk keperluan akademik dan pembelajaran.</i>
</p>
