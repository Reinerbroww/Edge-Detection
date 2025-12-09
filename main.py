#import libary
import cv2
import os
import numpy as np
import csv

# Setup Folder Dataset & Output
DATASET_FOLDER = "dataset"
OUTPUT_FOLDER = "hasil"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Siapkan file CSV untuk fitur
CSV_FILE = "dataset_edges.csv"
header = [
    "filename",
    "sobel_mean",
    "sobel_edge_pixels",
    "canny_edge_pixels"
]

# Kalau file belum ada, tulis header
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)

# Fungsi PREPROCESSING
def preprocess_image(img):
    # Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Gaussian Blur
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # Histogram Equalization (untuk meningkatkan kontras)
    hist = cv2.equalizeHist(blur)

    return gray, blur, hist

# Fungsi Deteksi Tepi
def sobel_edge(img):
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobelx, sobely)
    # Ubah ke uint8 biar bisa disimpan
    sobel_8u = cv2.convertScaleAbs(sobel)
    return sobel_8u

def canny_edge(img):
    canny = cv2.Canny(img, 100, 200)
    return canny

# Loop Semua Gambar di Folder Dataset
for filename in os.listdir(DATASET_FOLDER):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):

        print(f"Processing: {filename}")
        # MEMBACA GAMBAR
        img_path = os.path.join(DATASET_FOLDER, filename)
        img = cv2.imread(img_path)

        # PREPROCESS
        gray, blur, hist = preprocess_image(img)

        # DETEKSI TEPI
        sobel = sobel_edge(hist)
        canny = canny_edge(hist)

        # ====== HITUNG FITUR NUMERIK ======
        sobel_mean = float(np.mean(sobel))
        sobel_edge_pixels = int(np.sum(sobel > 0))   # pixel tepi sobel
        canny_edge_pixels = int(np.sum(canny > 0))   # pixel tepi canny

        # SIMPAN FITUR KE CSV
        with open(CSV_FILE, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                filename,
                sobel_mean,
                sobel_edge_pixels,
                canny_edge_pixels
            ])

        # SIMPAN SEMUA HASIL GAMBAR
        base = filename.split(".")[0]

        cv2.imwrite(f"{OUTPUT_FOLDER}/{base}_1_original.jpg", img)
        cv2.imwrite(f"{OUTPUT_FOLDER}/{base}_2_gray.jpg", gray)
        cv2.imwrite(f"{OUTPUT_FOLDER}/{base}_3_blur.jpg", blur)
        cv2.imwrite(f"{OUTPUT_FOLDER}/{base}_4_hist.jpg", hist)
        cv2.imwrite(f"{OUTPUT_FOLDER}/{base}_sobel.jpg", sobel)
        cv2.imwrite(f"{OUTPUT_FOLDER}/{base}_canny.jpg", canny)

# NOTIFIKASI
print("\n🔥 Selesai bro! Semua hasil sudah disimpan di folder 'hasil/' dan fitur di 'dataset_edges.csv'!")
