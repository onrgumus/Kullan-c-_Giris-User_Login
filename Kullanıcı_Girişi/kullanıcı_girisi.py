import tkinter as tk

# Giriş komutu fonksiyonu
def giris_komut():
    # Kullanıcı adı ve şifre alınıyor
    kullanici_adi = kullanici_adi_girisi.get()
    sifre = sifre_girisi.get()
    
    # Doğru kullanıcı adı ve şifre
    dogru_kullanici = "onur"
    dogru_sifre = "1234"
    
    # Sonuç penceresi oluşturuluyor
    sonuc_penceresi = tk.Toplevel(arayuz)
    sonuc_penceresi.title("Giriş Sonucu")
    sonuc_penceresi.geometry("200x100")
    
    # Giriş bilgileri kontrol ediliyor
    if kullanici_adi == dogru_kullanici and sifre == dogru_sifre:
        dogru_label = tk.Label(sonuc_penceresi, text="Doğru giriş!", fg="green", font="Verdana 10 bold")
        dogru_label.pack(pady=20)
    else:
        yanlis_label = tk.Label(sonuc_penceresi, text="Yanlış giriş!", fg="red", font="Verdana 10 bold")
        yanlis_label.pack(pady=20)

# Yeni kullanıcı oluşturma fonksiyonu
def yeni_kullanici_olustur():
    # Yeni kullanıcı adı ve şifre alınıyor
    kullanici_adi = yeni_kullanici_adi.get()
    yeni_sifre = yeni_sifre_girisi.get()
    
    # Burada yeni kullanıcı adı ve şifre sisteme kaydedilebilir veya başka bir işlem yapılabilir
    print(f"Yeni kullanıcı adı: {kullanici_adi}, Yeni şifre: {yeni_sifre}")
    
    # Yeni kullanıcı oluşturma sonucu penceresi
    sonuc_penceresi = tk.Toplevel(arayuz)
    sonuc_penceresi.title("Yeni Kullanıcı Oluşturma Sonucu")
    sonuc_penceresi.geometry("200x100")
    
    # Başarılı oluşturma mesajı
    basarili_label = tk.Label(sonuc_penceresi, text="Yeni kullanıcı oluşturuldu!", fg="green", font="Verdana 10 bold")
    basarili_label.pack(pady=20)

# Ana pencere oluşturuluyor
arayuz = tk.Tk()
arayuz.title("Kullanıcı Girişi")
arayuz.geometry("400x300")

# Giriş bileşenleri
kullanici_adi_label = tk.Label(text="Kullanıcı Adı:")
kullanici_adi_label.place(x=20, y=50)

kullanici_adi_girisi = tk.Entry()
kullanici_adi_girisi.place(x=150, y=50)

sifre_label = tk.Label(text="Şifre:")
sifre_label.place(x=20, y=80)

sifre_girisi = tk.Entry(show="*")
sifre_girisi.place(x=150, y=80)

giris = tk.Button(text="Giriş", command=giris_komut)
giris.place(x=150, y=110)

# Yeni kullanıcı oluşturma bileşenleri
yeni_kullanici_adi_label = tk.Label(text="Yeni Kullanıcı Adı:")
yeni_kullanici_adi_label.place(x=20, y=140)

yeni_kullanici_adi = tk.StringVar()
yeni_kullanici_adi_girisi = tk.Entry(textvariable=yeni_kullanici_adi)
yeni_kullanici_adi_girisi.place(x=150, y=140)

yeni_sifre_label = tk.Label(text="Yeni Şifre:")
yeni_sifre_label.place(x=20, y=170)

yeni_sifre = tk.StringVar()
yeni_sifre_girisi = tk.Entry(textvariable=yeni_sifre, show="*")
yeni_sifre_girisi.place(x=150, y=170)

yeni_kullanici_olustur = tk.Button(text="Yeni Kullanıcı Oluştur", command=yeni_kullanici_olustur)
yeni_kullanici_olustur.place(x=150, y=200)

arayuz.mainloop()

