# 🌱 Plant Your Health

A full-stack health and wellness tracking application that helps users build healthy habits through gamification.

Users can:

- Track daily healthy activities
- Maintain streaks
- Earn points
- Grow a virtual plant/tree based on consistency

---

# 🚀 Features

## ✅ Authentication

- User Signup
- User Login

## ✅ Activity Tracking

Track activities in:

- Exercise
- Hydration
- Yoga
- Food

## ✅ Habit Building

- Daily activity completion
- Streak tracking
- Progress monitoring

## ✅ Dashboard

- Visual progress tracking
- Streak display
- Gamified health growth system

## ✅ Auto Database Seeding

Default activities are automatically created when backend starts for the first time.

---

# 🛠️ Tech Stack

## Frontend

- Angular
- TypeScript
- Angular Material

## Backend

- FastAPI
- SQLAlchemy
- SQLite

---

# 📂 Project Structure

```txt
PLANT-YOUR-HEALTH
│
├── Frontend
│   │
│   ├── src
│   │   │
│   │   ├── app
│   │   │   ├── Activities
│   │   │   ├── dashboard
│   │   │   ├── Login_Signup
│   │   │   ├── Profile_setup
│   │   │   ├── service
│   │   │   ├── welcome
│   │   │   ├── app.routes.ts
│   │   │   └── auth.service.ts
│   │   │
│   │   ├── assets
│   │   ├── index.html
│   │   ├── main.ts
│   │   └── styles.css
│   │
│   ├── angular.json
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md
│
└── Backend-fastapi
    │
    ├── app
    │   │
    │   ├── models
    │   │   ├── activity.py
    │   │   ├── activity_log.py
    │   │   ├── streak.py
    │   │   └── user.py
    │   │
    │   ├── routers
    │   │   ├── activity_router.py
    │   │   ├── auth_router.py
    │   │   ├── log_router.py
    │   │   └── streak_router.py
    │   │
    │   ├── schemas
    │   │   ├── activity_schema.py
    │   │   ├── auth_schema.py
    │   │   ├── log_schema.py
    │   │   └── streak_schema.py
    │   │
    │   ├── utils
    │   │   └── seed_data.py
    │   │
    │   ├── database.py
    │   └── main.py
    │
    ├── requirements.txt
    ├── plant_health.db
    └── README.md
```

---

# ⚙️ Frontend Setup

## 1. Navigate to frontend

```bash
cd Frontend
```

## 2. Install dependencies

```bash
npm install
```

## 3. Run Angular app

```bash
ng serve
```

Frontend runs on:

```txt
http://localhost:4200
```

---

# ⚙️ Backend Setup

## 1. Navigate to backend

```bash
cd Backend-fastapi
```

## 2. Create virtual environment

```bash
python -m venv venv
```

## 3. Activate virtual environment

### Windows

```bash
.\venv\Scripts\activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Run FastAPI server

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```txt
http://127.0.0.1:8000
```

Swagger documentation:

```txt
http://127.0.0.1:8000/docs
```

---

# 🗄️ Database

The project uses SQLite.

Database file:

```txt
plant_health.db
```

This file is automatically created when backend starts.

---

# 🌱 Default Activities

The backend automatically seeds:

- Exercise activities
- Hydration activities
- Yoga activities
- Food activities

No manual activity creation is required after setup.

---

# 🔥 API Features

## Authentication

- Signup
- Login

## Activities

- Create activity
- Get activities
- Update activity
- Delete activity

## Logs

- Mark activity completed
- Daily tracking

## Streaks

- Streak calculation
- Longest streak tracking

---

# 📌 Future Improvements

- JWT Authentication
- Password Hashing
- User-specific activities
- Progress charts
- Notifications
- Cloud database deployment
- Mobile responsiveness improvements

---

# 👨‍💻 Author

Shubham Kumar
