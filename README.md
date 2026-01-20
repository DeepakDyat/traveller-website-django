# Traveller Website (Django)

A full-stack **Traveller Website** built using **Django (Python backend)** that allows users to explore travel-related content, manage accounts, and authenticate securely.

---

## 🚀 Features

* User authentication (Login / Logout / Signup)
* Google OAuth login integration (securely handled)
* Dynamic travel content management
* Media upload support
* Django Admin Panel
* Responsive templates
* Clean and secure project structure

---

## 🛠 Tech Stack

**Backend:**

* Python
* Django 3.2.9

**Frontend:**

* HTML
* CSS
* Bootstrap

**Database:**

* SQLite (development)

**Authentication:**

* Django AllAuth
* Google OAuth

---

## 📂 Project Structure

```
project_new/
├── manage.py
├── project_new/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── myapp/
├── templates/
├── media-file/
└── db.sqlite3 (ignored in GitHub)
```

---

## ⚙️ Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/DeepakDyat/traveller-website-django.git
cd traveller-website-django
```

2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run migrations

```bash
python manage.py migrate
```

5. Start development server

```bash
python manage.py runserver
```

---

## 🔐 Security Notes

* Sensitive information like **API keys, email credentials, and OAuth secrets** are **not stored in GitHub**
* Secrets should be managed using environment variables (`.env` file)
* Project follows GitHub Push Protection best practices

---

## 📸 Screenshots

<img width="1379" height="690" alt="1" src="https://github.com/user-attachments/assets/02d39159-00f9-4435-86fc-3f9f8234191a" />
<img width="1281" height="748" alt="2" src="https://github.com/user-attachments/assets/870daf9b-1287-4edc-b270-25e8679e8b9c" />
<img width="1379" height="711" alt="3" src="https://github.com/user-attachments/assets/054c0055-bfe0-4783-8052-ccc1c8c7fa07" />
<img width="1379" height="711" alt="3" src="https://github.com/user-attachments/assets/4d753f7d-4168-471c-86cf-df17a898e2ae" />
<img width="1283" height="734" alt="5" src="https://github.com/user-attachments/assets/67a8d7c0-ae85-4789-8a91-94d795f406b0" />
<img width="1377" height="690" alt="6" src="https://github.com/user-attachments/assets/7e96c2a1-f8f0-445f-81bb-5bffd1ff2284" />
<img width="1500" height="740" alt="7" src="https://github.com/user-attachments/assets/0a035552-7171-45a9-9d0f-e3b3ea8dbb31" />
<img width="1167" height="730" alt="8" src="https://github.com/user-attachments/assets/22238ed6-4c85-465a-96be-40e6c1015105" />
<img width="1252" height="271" alt="9" src="https://github.com/user-attachments/assets/35c934e1-706f-4e60-87d9-26d194cacdd0" />
<img width="1378" height="572" alt="10" src="https://github.com/user-attachments/assets/f15d249a-6253-42c0-a761-9305a47a09cd" />


---

## 👨‍💻 Author

**Deepak Dyat**

* GitHub: [DeepakDyat](https://github.com/DeepakDyat)

---

## 📄 License

This project is for educational and learning purposes.
