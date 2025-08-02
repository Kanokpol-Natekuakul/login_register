# โปรเจกต์บล็อก Django

เว็บไซต์บล็อกแบบง่ายที่พัฒนาด้วย Django Framework พร้อมระบบจัดการผู้ใช้และการโพสต์บทความ

## ✨ คุณสมบัติ

- 📝 แสดงรายการบทความบล็อก
- 👤 ระบบสมัครสมาชิกและเข้าสู่ระบบ
- 🔐 ระบบรีเซ็ตรหัสผ่าน
- 🛡️ ป้องกันหน้าเว็บด้วย Login Required
- 📧 ส่งอีเมลผ่าน Console Backend
- 💻 Admin Panel สำหรับจัดการข้อมูล

## 🛠️ เทคโนโลยีที่ใช้

- **Django 5.2.4** - Web Framework
- **SQLite** - ฐานข้อมูล
- **HTML/CSS** - Frontend
- **Python** - Backend Language

## 📁 โครงสร้างโปรเจกต์

```
mywebsite/
├── mywebsite/          # การตั้งค่าหลักของโปรเจกต์
│   ├── settings.py     # การตั้งค่า Django
│   ├── urls.py         # URL routing หลัก
│   └── wsgi.py         # WSGI configuration
├── blog/               # แอปพลิเคชัน blog
│   ├── models.py       # โมเดลข้อมูล (Post)
│   ├── views.py        # View functions
│   ├── urls.py         # URL routing ของ blog
│   ├── forms.py        # ฟอร์มสำหรับสมัครสมาชิก
│   ├── admin.py        # การตั้งค่า admin
│   └── templates/      # HTML templates
├── manage.py           # Django management script
└── requirements.txt    # รายการ dependencies
```

## 🚀 การติดตั้งและใช้งาน

### 1. โคลนโปรเจกต์
```bash
git clone <repository-url>
cd mywebsite
```

### 2. สร้าง Virtual Environment
```bash
python -m venv myenv
# Windows
myenv\Scripts\activate
# Linux/Mac
source myenv/bin/activate
```

### 3. ติดตั้ง Dependencies
```bash
pip install django
# หรือติดตั้งจาก requirements.txt
pip install -r requirements.txt
```

### 4. ทำการ Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. สร้าง Superuser (ไม่บังคับ)
```bash
python manage.py createsuperuser
```

### 6. รันเซิร์ฟเวอร์
```bash
python manage.py runserver
```

เปิดเบราว์เซอร์และไปที่ `http://127.0.0.1:8000`

## 📋 คุณสมบัติของแอปพลิเคชัน

### หน้าหลัก (Home)
- แสดงรายการบทความทั้งหมด
- แสดงสถานะการเข้าสู่ระบบ
- ลิงก์ไปยังหน้าสมัครสมาชิก/เข้าสู่ระบบ

### หน้าเกี่ยวกับ (About)
- ต้องเข้าสู่ระบบก่อนถึงจะเข้าได้
- ใช้ `@login_required` decorator

### ระบบผู้ใช้
- **สมัครสมาชิก**: `/register/`
- **เข้าสู่ระบบ**: `/accounts/login/`
- **ออกจากระบบ**: `/accounts/logout/`
- **รีเซ็ตรหัสผ่าน**: `/accounts/password_reset/`

### Admin Panel
- เข้าถึงได้ที่ `/admin/`
- จัดการโมเดล Post
- ต้องมี superuser account

## 🎨 Templates ที่มี

### Blog Templates
- `home.html` - หน้าแสดงบทความ
- `about.html` - หน้าเกี่ยวกับ
- `register.html` - หน้าสมัครสมาชิก

### Authentication Templates
- `login.html` - หน้าเข้าสู่ระบบ
- `logout.html` - หน้าออกจากระบบ
- `password_reset_form.html` - ฟอร์มรีเซ็ตรหัสผ่าน
- `password_reset_done.html` - แจ้งส่งอีเมลแล้ว
- `password_reset_confirm.html` - ตั้งรหัสผ่านใหม่
- `password_reset_complete.html` - รีเซ็ตเสร็จสิ้น

## 📊 โมเดลข้อมูล

### Post Model
```python
class Post(models.Model):
    title = models.CharField(max_length=100)        # หัวเรื่อง
    content = models.TextField()                    # เนื้อหา
    date_posted = models.DateTimeField(default=timezone.now)  # วันที่โพสต์
```

## ⚙️ การตั้งค่าสำคัญ

### Settings.py
- `LOGIN_REDIRECT_URL = 'home'` - หลังเข้าสู่ระบบให้ไปหน้าหลัก
- `LOGOUT_REDIRECT_URL = 'home'` - หลังออกจากระบบให้ไปหน้าหลัก
- `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` - ส่งอีเมลผ่าน console

## 🔧 การพัฒนาต่อ

### เพิ่มฟีเจอร์ใหม่
1. สร้าง view ใน `blog/views.py`
2. เพิ่ม URL pattern ใน `blog/urls.py`
3. สร้าง template ในโฟลเดอร์ `templates/blog/`

### การจัดการไฟล์สถิต
- CSS, JavaScript, Images ควรอยู่ในโฟลเดอร์ `static/`
- ตั้งค่า `STATIC_URL` และ `STATICFILES_DIRS` ใน settings.py

## 📝 การใช้งาน Admin

1. เข้าไปที่ `http://127.0.0.1:8000/admin/`
2. เข้าสู่ระบบด้วย superuser account
3. จัดการ Posts และ Users ได้

## 🔒 ความปลอดภัย

- ใช้ CSRF tokens ในทุกฟอร์ม
- Password validation ตาม Django defaults
- `@login_required` decorator ป้องกันหน้าสำคัญ

## 🐛 การแก้ไขปัญหาทั่วไป

### ปัญหา Migration
```bash
python manage.py makemigrations blog
python manage.py migrate
```

### ปัญหา Static Files
```bash
python manage.py collectstatic
```

### รีเซ็ตฐานข้อมูล
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## 📞 การติดต่อ

หากมีปัญหาหรือข้อสงสัย สามารถสร้าง Issue ได้ที่ GitHub repository

---

*พัฒนาด้วย ❤️ โดยใช้ Django Framework*
