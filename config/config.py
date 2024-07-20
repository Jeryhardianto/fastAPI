import pymongo

# connect to mongodb
client = pymongo.MongoClient("mongodb+srv://myuser:mysecret@cluster0.l6crrms.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# create database and collection
db = client.get_database("mydatabase")

def get_db_connection():
  return db