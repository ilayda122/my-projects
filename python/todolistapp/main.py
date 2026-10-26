import tkinter as tk
from tkinter import messagebox

# Başlangıç görevleri
gorevler = ["Ders çalış", "Spor yap", "Kitap oku"]

# Görev ekleme fonksiyonu
def gorev_ekle():
    yeni_gorev = entry.get()
    if yeni_gorev:
        listbox.insert(tk.END, yeni_gorev)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev girin.")

# Görev silme fonksiyonu
def gorev_sil():
    secilen = listbox.curselection()
    if secilen:
        listbox.delete(secilen)
    else:
        messagebox.showwarning("Uyarı", "Lütfen silinecek görevi seçin.")

# Pencereyi oluştur
pencere = tk.Tk()
pencere.title("Yapılacaklar Listesi")
pencere.geometry("300x400")
pencere.configure(bg="#f0f0f0")

# Başlık etiketi
etiket = tk.Label(pencere, text="📝 Görev Listesi", font=("Helvetica", 16), bg="#f0f0f0")
etiket.pack(pady=10)

# Liste kutusu
listbox = tk.Listbox(pencere, width=35, height=10, font=("Arial", 12))
listbox.pack(pady=10)

# Başlangıç görevlerini ekle
for g in gorevler:
    listbox.insert(tk.END, g)

# Giriş kutusu
entry = tk.Entry(pencere, width=25, font=("Arial", 12))
entry.pack(pady=5)

# Butonlar
ekle_buton = tk.Button(pencere, text="Görev Ekle", width=15, command=gorev_ekle, bg="#a0d6b4")
ekle_buton.pack(pady=5)

sil_buton = tk.Button(pencere, text="Görev Sil", width=15, command=gorev_sil, bg="#f5a9a9")
sil_buton.pack(pady=5)

# Ana döngü
pencere.mainloop()
