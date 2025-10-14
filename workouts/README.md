# 🏋️‍♂️ FitTrack

FitTrack is a simple Django web app that helps users log and track their workouts.  
Each user can register, log in, add, edit, and delete their workouts securely.

## 🚀 Features
- User registration, login, and logout  
- Add, edit, and delete workouts (CRUD)  
- Optional workout images  
- Delete account option  
- Clean, consistent design with success messages  

## 🛠️ Built With
- Django (Python)
- HTML & CSS (Django Templates)
- SQLite (default database)

## ⚙️ How to Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
