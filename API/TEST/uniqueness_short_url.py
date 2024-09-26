# import datetime   # This will be needed later
import os

from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)

# List all the databases in the cluster:
for db_info in client.list_database_names():
    print(db_info)

# Указываем базу данных и коллекцию
db = client['TestCompany']
collection = db['TestCollection']

# Строим запрос для получения документа
query = {'testKey': 'testValue'}  # Замените ключ и значение на нужные

# Ищем документ
document = collection.find_one(query)

if document:
    # Получаем значение поля
    value = document.get('testKey')  # Замените 'имя_поля' на нужное
    print(value)
else:
    print('Документ не найден')
