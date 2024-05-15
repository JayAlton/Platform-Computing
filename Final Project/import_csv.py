import csv
import pymongo
from pymongo import MongoClient

mongoClient = MongoClient('mongodb+srv://jalton:mtpJrE0zmD7eXzXf@cluster0.bjnrjj9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = mongoClient['Test']
collection = db['Baseline']

# Open the CSV file
with open('metrics.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Insert each row as a document into MongoDB
        collection.insert_one(row)

print("CSV data successfully imported into MongoDB.")



