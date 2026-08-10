## 🧊 فارسی

**icepick** یک ابزار قدرتمند و سبک برای تست نفوذ است که توسط **iceSEC | Cyber Intelligence Operations** ساخته شده است. این ابزار برای ارزیابی‌های امنیتی دقیق طراحی شده است.

> *"یخ را بشکن، یک ضربه در هر بار."*
---

### ✨ قابلیت‌ها

| دسته | قابلیت‌ها |
|------|-----------|
| 🚀 **موتور اصلی** | اسکنر چندنخی پورت (۲۳+ پورت)، تشخیص هوشمند آسیب‌پذیری (SQLi، XSS، پنل‌های مدیریت)، شناسایی زیردامنه، امتیازدهی امنیتی (۰ تا ۱۰۰) |
| 🖥️ **رابط گرافیکی حرفه‌ای** | تم تاریک، موس هکری (حلقه نئونی + کراس‌هیر + دنباله ذرات)، پس‌زمینه‌ی ماتریکس، لاگ‌های رنگی زنده، خروجی JSON با یک کلیک |
| 📊 **گزارش‌دهی** | فرمت JSON، امتیاز امنیتی، ارزیابی ریسک (کم/متوسط/بالا/بحرانی)، جزئیات آسیب‌پذیری با مکان دقیق |
| 🔗 **ادغام برند** | لندینگ پیج iceSEC، کانال تلگرام، گیت‌هاب، حمایت مالی (Buy Me a Coffee) |

---

### 🚀 شروع سریع

#### نصب

```bash
# کلون کردن ریپازیتوری
git clone https://github.com/iceSEC-Operations/icepick.git
cd icepick

# نصب وابستگی‌ها (هیچ وابستگی خارجی لازم نیست!)
pip install -r requirements.txt

# اجرای رابط گرافیکی
python gui_standalone.py
```

#### دانلود EXE (ویندوز)

آخرین نسخه را از صفحه‌ی [Releases](https://github.com/iceSEC-Operations/icepick/releases) دانلود کنید.

۱. فایل `icepick-gui.zip` را دانلود کنید
۲. پوشه را اکسترکت کنید
۳. فایل `icepick-gui.exe` را اجرا کنید

---

### 📥 دانلود

| نسخه | پلتفرم | دانلود |
|------|--------|--------|
| **v1.0.0** | ویندوز GUI | [icepick-gui.zip](https://github.com/iceSEC-Operations/icepick/releases/download/v1.0.0/icepick-gui.zip) |

**نیازی به نصب نیست!** فقط اکسترکت کنید و اجرا کنید.

---

### 🛠️ توسعه

```bash
# کلون کردن ریپازیتوری
git clone https://github.com/iceSEC-Operations/icepick.git
cd icepick

# ساخت EXE با PyInstaller
pyinstaller --onedir --windowed --name icepick-gui --hidden-import=tkinter --hidden-import=socket --hidden-import=json --hidden-import=threading --hidden-import=urllib --hidden-import=concurrent.futures gui_standalone.py
```

---

### 🤝 مشارکت

ما از بازخورد و پیشنهادات شما استقبال می‌کنیم! راه‌های کمک:

- 🐛 **گزارش باگ** از طریق [Issues](https://github.com/iceSEC-Operations/icepick/issues)
- 💡 **پیشنهاد ویژگی** از طریق [Issues](https://github.com/iceSEC-Operations/icepick/issues)
- 💬 **پرسش سوال** از طریق [Discussions](https://github.com/iceSEC-Operations/icepick/discussions)

> **توجه:** در حال حاضر Pull Request قبول نمی‌کنیم.

---

### ⚠️ سلب مسئولیت

> **این ابزار فقط برای اهداف آموزشی و اخلاقی طراحی شده است.**  
> فقط روی سیستم‌هایی که مالک آن هستید یا اجازه‌ی تست دارید استفاده کنید.  
> iceSEC مسئولیتی در قبال سوءاستفاده یا آسیب‌های ناشی از این ابزار ندارد.

---

<p align="center">
  <strong>🧊 iceSEC | Cyber Intelligence Operations</strong><br>
  <em>Precision strikes. Every time.</em>
</p>
```
