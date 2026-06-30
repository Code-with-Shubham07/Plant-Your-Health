from sqlalchemy.orm import Session

from app.models.activity import Activity


def seed_activities(db: Session):

    existing = db.query(Activity).first()

    if existing:
        return

    activities = activities = [

    # =========================
    # EXERCISE
    # =========================

    {
        "name": "Morning Walk",
        "description": "30 minute brisk walk",
        "type": "EXERCISE",
        "points": 10
    },
    {
        "name": "Running",
        "description": "20 minute running session",
        "type": "EXERCISE",
        "points": 20
    },
    {
        "name": "Cycling",
        "description": "45 minute cycling",
        "type": "EXERCISE",
        "points": 15
    },
    {
        "name": "Push Ups",
        "description": "50 push ups workout",
        "type": "EXERCISE",
        "points": 15
    },
    {
        "name": "Skipping",
        "description": "15 minutes skipping rope",
        "type": "EXERCISE",
        "points": 10
    },
    {
        "name": "Gym Workout",
        "description": "1 hour gym session",
        "type": "EXERCISE",
        "points": 25
    },
    {
        "name": "Stretching",
        "description": "Full body stretching",
        "type": "EXERCISE",
        "points": 8
    },
    {
        "name": "Jogging",
        "description": "Morning jogging session",
        "type": "EXERCISE",
        "points": 12
    },
    {
        "name": "Squats",
        "description": "100 squats challenge",
        "type": "EXERCISE",
        "points": 15
    },
    {
        "name": "Plank",
        "description": "5 minute plank exercise",
        "type": "EXERCISE",
        "points": 10
    },

    # =========================
    # HYDRATION
    # =========================

    {
        "name": "Drink 2L Water",
        "description": "Complete 2 liters water intake",
        "type": "HYDRATION",
        "points": 10
    },
    {
        "name": "Morning Water",
        "description": "Drink warm water after waking up",
        "type": "HYDRATION",
        "points": 5
    },
    {
        "name": "Electrolyte Drink",
        "description": "Drink electrolyte solution",
        "type": "HYDRATION",
        "points": 8
    },
    {
        "name": "Fruit Juice",
        "description": "Fresh fruit juice intake",
        "type": "HYDRATION",
        "points": 7
    },
    {
        "name": "Coconut Water",
        "description": "Drink fresh coconut water",
        "type": "HYDRATION",
        "points": 10
    },
    {
        "name": "Hydration Reminder",
        "description": "Drink water every hour",
        "type": "HYDRATION",
        "points": 12
    },
    {
        "name": "Post Workout Water",
        "description": "Hydrate after workout",
        "type": "HYDRATION",
        "points": 6
    },
    {
        "name": "Green Tea",
        "description": "Drink healthy green tea",
        "type": "HYDRATION",
        "points": 5
    },
    {
        "name": "Detox Water",
        "description": "Drink lemon detox water",
        "type": "HYDRATION",
        "points": 8
    },
    {
        "name": "Water Tracking",
        "description": "Track daily water intake",
        "type": "HYDRATION",
        "points": 10
    },

    # =========================
    # YOGA
    # =========================

    {
        "name": "Morning Yoga",
        "description": "30 minute yoga session",
        "type": "YOGA",
        "points": 20
    },
    {
        "name": "Meditation",
        "description": "15 minute meditation",
        "type": "YOGA",
        "points": 15
    },
    {
        "name": "Surya Namaskar",
        "description": "12 rounds of Surya Namaskar",
        "type": "YOGA",
        "points": 25
    },
    {
        "name": "Breathing Exercise",
        "description": "Deep breathing practice",
        "type": "YOGA",
        "points": 10
    },
    {
        "name": "Pranayama",
        "description": "20 minute pranayama session",
        "type": "YOGA",
        "points": 18
    },
    {
        "name": "Flexibility Yoga",
        "description": "Improve flexibility exercises",
        "type": "YOGA",
        "points": 15
    },
    {
        "name": "Balance Yoga",
        "description": "Balance and posture practice",
        "type": "YOGA",
        "points": 12
    },
    {
        "name": "Evening Yoga",
        "description": "Relaxing evening yoga",
        "type": "YOGA",
        "points": 15
    },
    {
        "name": "Mindfulness Session",
        "description": "Mindfulness meditation practice",
        "type": "YOGA",
        "points": 10
    },
    {
        "name": "Yoga Stretch",
        "description": "Full body yoga stretching",
        "type": "YOGA",
        "points": 14
    },

    # =========================
    # FOOD
    # =========================

    {
        "name": "Healthy Breakfast",
        "description": "Eat nutritious breakfast",
        "type": "FOOD",
        "points": 10
    },
    {
        "name": "Eat Fruits",
        "description": "Consume seasonal fruits",
        "type": "FOOD",
        "points": 8
    },
    {
        "name": "Green Vegetables",
        "description": "Eat green vegetables",
        "type": "FOOD",
        "points": 10
    },
    {
        "name": "Protein Meal",
        "description": "Consume high protein meal",
        "type": "FOOD",
        "points": 15
    },
    {
        "name": "Avoid Junk Food",
        "description": "No junk food for the day",
        "type": "FOOD",
        "points": 20
    },
    {
        "name": "Salad Intake",
        "description": "Eat healthy salad",
        "type": "FOOD",
        "points": 8
    },
    {
        "name": "Balanced Diet",
        "description": "Follow balanced diet plan",
        "type": "FOOD",
        "points": 18
    },
    {
        "name": "Dry Fruits",
        "description": "Consume healthy dry fruits",
        "type": "FOOD",
        "points": 7
    },
    {
        "name": "Homemade Food",
        "description": "Eat homemade healthy food",
        "type": "FOOD",
        "points": 12
    },
    {
        "name": "Low Sugar Diet",
        "description": "Avoid excess sugar intake",
        "type": "FOOD",
        "points": 15
    }

]

    for activity in activities:
        db.add(Activity(**activity))

    db.commit()

    print("Default activities seeded successfully.")