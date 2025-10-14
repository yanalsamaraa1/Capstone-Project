🏋️‍♀️ **Project Title:** FitTrack – Personal Fitness & Workout Tracker

---

### 🧠 Concept  
A web app that helps users track their workouts and exercises.  
Each user can log different workouts (like “Leg Day” or “Morning Cardio”) and record exercises under them (e.g., “Squats – 3 sets – 12 reps”).  
The app keeps a history so users can see what they’ve done and how they’re progressing.

---

### 🎯 Core Features  
✅ Authentication (register, login, logout)  
✅ CRUD for Workouts (name, date, type)  
✅ CRUD for Exercises under each workout  
✅ Track sets, reps, and weight  
✅ Display workout history for each user  

---

### 🧱 Database Models (ERD)

The database structure for **FitTrack** consists of three main tables — `User`, `Workout`, and `Exercise` — representing the one-to-many relationships between them.

![FitTrack ERD](static/images/fittrack-erd.png)

> **Relationship Summary:**  
> • One user can have many workouts  
> • Each workout can have many exercises  

#### dbdiagram.io Code
```dbml
Table users {
  id integer [pk, increment]
  username varchar
  password varchar
}

Table workouts {
  id integer [pk, increment]
  user_id integer [ref: > users.id]
  name varchar
  weight float
  reps integer
  date date
  image varchar [null]
}

Table exercises {
  id integer [pk, increment]
  workout_id integer [ref: > workouts.id]
  name varchar
  sets integer
  reps integer
  weight float [null]
  notes text [null]
}

Ref: users.id < workouts.user_id
Ref: workouts.id < exercises.workout_id
