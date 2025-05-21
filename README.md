# 📚 Biblioteca Virtual

**Biblioteca Virtual** is a monolithic web application built using **Flask** and **SQLite**, following a layered architecture pattern (**MVC without external APIs or routes**).
The application allows users to browse books, view detailed descriptions, register accounts, and administrators to manage books through CRUD operations. The frontend data is injected directly into HTML templates rendered by Flask.

---

## 📋 Index

* [Frontend (Jinja2 Templates)](#frontend)
* [Backend (Flask + SQLite)](#backend)
* [Project Structure](#project-structure)
* [Technologies Used](#technologies-used)
* [Setup and Execution](#setup-and-execution)
* [Security Considerations](#security-considerations)
* [Next Steps](#next-steps)
* [License](#license)

---

## 🚀 Technologies Used

### 🔧 Backend

* **Python 3.11**
* **Flask 3.x** (Web framework)
* **SQLite 3** (Database)
* **SQLAlchemy** (ORM)
* **Flask-Migrate** (Database migrations)
* **Flask-WTF** (Form handling and validation)
* **bcrypt** (Password hashing)
* **python-dotenv** (Environment variable management)

### 🎨 Frontend

* **Jinja2** (HTML templating engine)
* **Tailwind CSS** (Styling framework)

---

## 🧩 Project Structure

```
biblioteca-virtual/
│
├── app/
│   ├── controllers/
│   │   ├── libro_controller.py
│   │   └── usuario_controller.py
│   ├── models/
│   │   ├── libro.py
│   │   └── usuario.py
│   ├── services/
│   │   ├── libro_service.py
│   │   └── usuario_service.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── libros.html
│   │   └── usuarios.html
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── views/
│   │   └── inject_data.py
│   └── __init__.py
│
├── migrations/
├── instance/
│   └── biblioteca.sqlite
├── .env
├── requirements.txt
└── README.md
```

---

## 📌 Application Functionality

### **User Features:**

* Register with name, email, password, and ID number.
* Secure login and logout.
* View the complete list of books.
* Filter books by name, author, or category.
* View book details (synopsis, author, year, availability).

### **Admin Features:**

* CRUD management for books.

---

## 🛠️ Setup and Execution

### Prerequisites

* Python 3.11+

### Installation

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Environment Configuration

Create `.env` file:

```env
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///instance/biblioteca.sqlite
```

Initialize Database:

```bash
flask db init
flask db migrate
flask db upgrade
```

Run the server:

```bash
flask run
```

Server available at:

```
http://localhost:5000
```

---

## 🛡️ Security Considerations

* Password hashing using **bcrypt**.
* Environment variables managed via **python-dotenv**.
* Prepared statements via **SQLAlchemy ORM** to prevent SQL injection.

---

## 🔮 Next Steps

* Implement user roles and permissions.
* Advanced search functionality.
* Export book data in CSV or PDF.

---

## 📄 License

This project is licensed under the **MIT License**.
