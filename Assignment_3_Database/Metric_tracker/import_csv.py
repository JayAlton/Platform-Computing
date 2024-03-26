import csv
import pymongo
from pymongo import MongoClient

mongoClient = MongoClient('mongodb+srv://jmalton77:YYy28T6gphplGkFU@cluster0.bhxdsrj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = mongoClient['metric_data']
collection = db['metrics']

# Open the CSV file
with open('metrics.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Insert each row as a document into MongoDB
        collection.insert_one(row)

print("CSV data successfully imported into MongoDB.")


