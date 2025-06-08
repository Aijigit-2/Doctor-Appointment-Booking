import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Укажи путь к JSON-файлу
cred = credentials.Certificate("path/to/your/serviceAccountKey.json")

# Инициализация приложения
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-id.firebaseio.com'
})

# Считывание данных по пути /users
ref = db.reference('/users')
data = ref.get()

print(data)
