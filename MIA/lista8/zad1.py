import pymongo

# Replace the following with your MongoDB connection string
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or access a database
mydb = client["mydatabase"]

# Create or access a collection
mycollection = mydb["customers"]

# Insert a document into the collection
my_customer = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "age": 30
}

my_customer2 = {
    "name": "Jacek Placek",
    "email": "jacekplacek@ggg.com",
    "age": 12
}

# Insert the document into the collection
insert_result = mycollection.insert_one(my_customer2)

print(f"Inserted document ID: {insert_result.inserted_id}")

# Query the collection
query_result = mycollection.find_one({"name": "Jacek Placek"})
if query_result:
    print("Found a document:")
    print(query_result)
else:
    print("Document not found.")


# /////////////////////////////////////////////////////////////////////////zad4a
result = mycollection.find().sort('_id', pymongo.ASCENDING).skip(2).limit(2)

print("Documents in the middle (page 2):")
for doc in result:
    print(doc)

#//////////////////////////////////////////////////////////////////////////zad4b
query = {"email": "johndoe@example.com"}
filtered_docs = mycollection.find(query)

print("Filtered Documents:")
for doc in filtered_docs:
    print(doc)

# Close the MongoDB connection
client.close()

