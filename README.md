# 🏘️ Mahalle İhtiyaç Yardım Sistemi

<div align="center">
  <img src="https://img.shields.io/badge/Django-5.2.1-green.svg" alt="Django Version">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</div>

## 📋 Proje Hakkında

**Mahalle İhtiyaç Yardım Sistemi**, 3 kişilik bir takım tarafından geliştirilen, mahalle sakinlerinin birbirlerine yardım etmesini kolaylaştıran, topluluk dayanışmasını güçlendiren modern bir web uygulamasıdır. Bu platform, komşular arasında güvenli ve etkili bir şekilde yardım taleplerinin paylaşılmasını ve karşılanmasını sağlar.

### 🎓 Proje Geçmişi

Bu proje, takım çalışması ve işbirliğinin önemini vurgulayan bir öğrenme deneyimidir. Her takım üyesi kendi uzmanlık alanında katkıda bulunarak, ortak bir hedefe ulaşmıştır.

### 🎯 Projenin Amacı

- **Topluluk Dayanışması**: Mahalle sakinleri arasında güçlü bağlar kurmak
- **Yardımlaşma Kültürü**: Komşuların birbirine yardım etme alışkanlığını teşvik etmek
- **Acil Durum Desteği**: Acil ihtiyaçların hızlıca karşılanmasını sağlamak
- **Güvenli İletişim**: Mahalle sakinleri arasında güvenli mesajlaşma ortamı sunmak
- **Sosyal Sorumluluk**: Toplumsal yardımlaşma bilincini artırmak

### 🌟 Temel Özellikler

#### 👥 Kullanıcı Yönetimi
- **Kayıt ve Giriş Sistemi**: Güvenli kullanıcı kimlik doğrulama
- **Rol Tabanlı Sistem**: "Yardım İsteyen" ve "Yardım Eden" rolleri
- **Profil Yönetimi**: Detaylı kullanıcı profil bilgileri
- **Profil Fotoğrafı**: Kişiselleştirilmiş profil görünümü

#### 📝 Yardım Talebi Sistemi
- **Kategori Bazlı Organizasyon**: Farklı yardım türleri için kategoriler
- **Detaylı Açıklama**: Başlık, açıklama ve konum bilgileri
- **Acil Durum İşaretleme**: Öncelikli yardım talepleri
- **Tarih ve Konum**: Yardım tarihi ve lokasyon bilgisi
- **Durum Takibi**: Yardım taleplerinin durumunu takip etme

#### 💬 İletişim Sistemi
- **Mesajlaşma**: Kullanıcılar arası güvenli mesajlaşma
- **Yorum Sistemi**: Yardım taleplerine yorum yapma
- **Bildirim Sistemi**: Yeni mesaj ve yorum bildirimleri
- **Gelen Kutusu**: Tüm mesajları tek yerden yönetme

#### 🔍 Arama ve Filtreleme
- **Gelişmiş Arama**: Başlık ve açıklama bazlı arama
- **Kategori Filtresi**: Kategoriye göre filtreleme
- **Konum Filtresi**: Yakındaki yardım taleplerini bulma
- **Acil Durum Filtresi**: Acil yardım taleplerini öncelikle gösterme

#### 📊 Yönetim Paneli
- **Admin Dashboard**: Kapsamlı yönetim paneli
- **Kullanıcı Yönetimi**: Kullanıcı hesaplarını yönetme
- **İçerik Moderasyonu**: Yardım taleplerini denetleme
- **İstatistikler**: Platform kullanım istatistikleri
- **Raporlama**: Detaylı kullanım raporları

#### 📱 Modern Arayüz
- **Responsive Tasarım**: Tüm cihazlarda uyumlu görünüm
- **Kullanıcı Dostu**: Sezgisel ve kolay kullanım
- **Modern UI/UX**: Çağdaş tasarım prensipleri
- **Hızlı Yükleme**: Optimize edilmiş performans

## 🚀 Kurulum ve Çalıştırma

### 📋 Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- Git (versiyon kontrolü için)

### 🔧 Adım Adım Kurulum

#### 1. Projeyi İndirin
```bash
# GitHub'dan klonlayın
git clone https://github.com/caprazzz/mahalle_ihtiyac.git
cd mahalle_ihtiyac

# Veya ZIP dosyası olarak indirip açın
```

#### 2. Virtual Environment Oluşturun
```bash
# Python virtual environment oluşturun
python -m venv venv

# Virtual environment'ı aktifleştirin
# Linux/Mac için:
source venv/bin/activate

# Windows için:
venv\Scripts\activate
```

#### 3. Bağımlılıkları Yükleyin
```bash
# Gerekli paketleri yükleyin
pip install -r requirements.txt

# Veya manuel olarak:
pip install Django==5.2.1
pip install Pillow==10.4.0
pip install python-decouple==3.8
```

#### 4. Veritabanını Hazırlayın
```bash
# Veritabanı migrasyonlarını çalıştırın
python manage.py migrate

# Örnek kategoriler oluşturun (isteğe bağlı)
python manage.py shell
>>> from yardim.models import Category
>>> Category.objects.create(name="Ev İşleri")
>>> Category.objects.create(name="Bahçe İşleri")
>>> Category.objects.create(name="Teknik Destek")
>>> Category.objects.create(name="Nakliye")
>>> Category.objects.create(name="Eğitim")
>>> exit()
```

#### 5. Süper Kullanıcı Oluşturun
```bash
# Admin paneli için süper kullanıcı oluşturun
python manage.py createsuperuser
# Kullanıcı adı, e-posta ve şifre girin
```

#### 6. Sunucuyu Başlatın
```bash
# Development sunucusunu başlatın
python manage.py runserver

# Veya belirli bir port kullanın
python manage.py runserver 8080
```

### 🌐 Erişim Adresleri

- **Ana Sayfa**: http://127.0.0.1:8000/
- **Admin Paneli**: http://127.0.0.1:8000/admin/
- **Kayıt Sayfası**: http://127.0.0.1:8000/register/
- **Giriş Sayfası**: http://127.0.0.1:8000/login/

### 🎯 İlk Kullanım

1. **Kayıt Olun**: Ana sayfadan "Kayıt Ol" butonuna tıklayın
2. **Profil Oluşturun**: Rolünüzü seçin (Yardım İsteyen/Yardım Eden)
3. **Yardım Talebi Oluşturun**: "Yardım Talebi Oluştur" sayfasından ilan verin
4. **Mesajlaşın**: Diğer kullanıcılarla iletişim kurun
5. **Admin Paneli**: Süper kullanıcı ile admin paneline erişin

## 🏗️ Proje Mimarisi

### 📊 Veritabanı Modelleri

#### 👤 User Modeli
- Django'nun varsayılan kullanıcı modeli
- Kullanıcı kimlik doğrulama ve yetkilendirme
- Kullanıcı adı, e-posta ve şifre yönetimi

#### 👤 Profile Modeli
```python
- user: OneToOneField (User ile ilişki)
- role: CharField (Yardım İsteyen/Yardım Eden)
- bio: TextField (Kullanıcı hakkında bilgi)
- phone_number: CharField (İletişim numarası)
- location: CharField (Konum bilgisi)
- profile_picture: ImageField (Profil fotoğrafı)
```

#### 📂 Category Modeli
```python
- name: CharField (Kategori adı)
- Yardım taleplerinin kategorilere ayrılması
- Örnek kategoriler: Ev İşleri, Bahçe İşleri, Teknik Destek
```

#### 📝 HelpRequest Modeli
```python
- user: ForeignKey (Talep sahibi)
- category: ForeignKey (Kategori)
- title: CharField (Başlık)
- description: TextField (Detaylı açıklama)
- created_at: DateTimeField (Oluşturulma tarihi)
- location: CharField (Konum)
- help_date: DateTimeField (Yardım tarihi)
- is_urgent: BooleanField (Acil durum)
```

#### 💬 Comment Modeli
```python
- help_request: ForeignKey (İlgili yardım talebi)
- user: ForeignKey (Yorum yapan kullanıcı)
- content: TextField (Yorum içeriği)
- created_at: DateTimeField (Yorum tarihi)
```

#### 📨 Message Modeli
```python
- sender: ForeignKey (Gönderen kullanıcı)
- receiver: ForeignKey (Alıcı kullanıcı)
- content: TextField (Mesaj içeriği)
- created_at: DateTimeField (Gönderim tarihi)
- is_read: BooleanField (Okundu durumu)
```

### 🛠️ Teknoloji Stack'i

#### Backend
- **Django 5.2.1**: Modern Python web framework
- **Python 3.8+**: Programlama dili
- **SQLite**: Development veritabanı
- **Pillow**: Resim işleme kütüphanesi
- **python-decouple**: Environment variables yönetimi

#### Frontend
- **HTML5**: Semantik markup
- **CSS3**: Modern styling
- **JavaScript**: İnteraktif özellikler
- **Bootstrap**: Responsive tasarım framework'ü
- **Font Awesome**: İkonlar

#### Development Tools
- **Git**: Versiyon kontrolü
- **Virtual Environment**: İzole Python ortamı
- **Django Admin**: Yönetim paneli
- **Django Debug Toolbar**: Geliştirme araçları

### 🔧 Proje Yapısı

```
mahalle_ihtiyac_clean/
├── 📁 mahalle_ihtiyac/          # Ana proje klasörü
│   ├── 📄 settings.py          # Proje ayarları
│   ├── 📄 urls.py              # Ana URL yapılandırması
│   ├── 📄 wsgi.py              # WSGI konfigürasyonu
│   └── 📁 static/              # Static dosyalar
├── 📁 yardim/                   # Ana uygulama
│   ├── 📄 models.py            # Veritabanı modelleri
│   ├── 📄 views.py             # View fonksiyonları
│   ├── 📄 forms.py             # Form sınıfları
│   ├── 📄 urls.py              # URL routing
│   ├── 📄 admin.py             # Admin panel konfigürasyonu
│   ├── 📁 templates/           # HTML şablonları
│   └── 📁 migrations/          # Veritabanı migrasyonları
├── 📁 media/                    # Kullanıcı yüklenen dosyalar
├── 📄 manage.py                # Django yönetim scripti
├── 📄 requirements.txt         # Python bağımlılıkları
└── 📄 README.md               # Proje dokümantasyonu
```

## 🚀 Deployment (Yayınlama)

### Development Ortamı
```bash
# Geliştirme sunucusu
python manage.py runserver
```

### Production Ortamı
```bash
# Static dosyaları topla
python manage.py collectstatic

# Production ayarları için
# DEBUG = False
# ALLOWED_HOSTS = ['yourdomain.com']
# SECRET_KEY = 'your-secret-key'
```

### Docker ile Deployment
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 🤝 Katkıda Bulunma

Bu proje takım çalışması ile geliştirilmiştir. Yeni katkılar için:

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

### 📋 Takım İçi Çalışma Süreci

- **Git Workflow**: Feature branch'ler ile çalışma
- **Code Review**: Her değişiklik takım üyeleri tarafından incelenir
- **Testing**: Yeni özellikler test edilir
- **Documentation**: Kod değişiklikleri dokümante edilir

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👥 Takım Üyeleri

Bu proje, 3 kişilik bir takım tarafından geliştirilmiştir:

### 🧑‍💻 Takım Üyesi 1
- **İsim**: [Esma Zeynep Uysal]
- **GitHub**: [@Esmazuysal](https://github.com/Esmazuysal)

### 🧑‍💻 Takım Üyesi 2
- **İsim**: [Sudenaz Kobilay]
- **GitHub**: [@Sudekobilay](https://github.com/Sudekobilay)

### 🧑‍💻 Takım Üyesi 3
- **İsim**: [Hilal Nur Turan]
- **GitHub**: [@kullaniciadi3](https://github.com/kullaniciadi3)

## 🤝 Takım Çalışması

Bu proje, takım çalışmasının gücünü gösteren bir örnektir:

- **İş Bölümü**: Her takım üyesi kendi uzmanlık alanında çalıştı
- **Kod İnceleme**: Tüm kodlar takım üyeleri tarafından incelendi
- **Fikir Alışverişi**: Sürekli beyin fırtınası ve fikir paylaşımı
- **Kalite Kontrol**: Çoklu gözle kalite kontrolü
- **Öğrenme**: Birbirinden öğrenme ve deneyim paylaşımı

## 🙏 Teşekkürler

### 👥 Takım Üyelerine
- **Takım Arkadaşlarıma**: Bu projeyi birlikte geliştirdiğimiz için
- **İşbirliği**: Sürekli destek ve motivasyon için
- **Öğrenme**: Birbirimizden öğrendiğimiz değerli deneyimler için

---

<div align="center">
  <p>⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!</p>
  <p>🐛 Hata bulduysanız issue açın</p>
  <p>💡 Öneriniz varsa pull request gönderin</p>
</div>
