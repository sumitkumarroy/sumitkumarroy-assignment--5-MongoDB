'''
Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use MongoDB over SQL 
databases?

MongoDB:

    MongoDB is a popular open-source NoSQL document database.
    It stores data in flexible, JSON-like documents, meaning fields can vary from document to document.
    Documents are stored in collections, which are akin to tables in relational databases.
    MongoDB is schema-less, allowing for easy and rapid changes to data structure.
    It is designed for scalability, high availability, and performance.

Non-relational Databases:

    Non-relational databases (NoSQL) are databases that do not follow the tabular structure of relational databases.
    They offer more flexibility in terms of data storage, allowing for semi-structured and unstructured data.
    NoSQL databases are often used for big data and real-time applications where flexibility and scalability are crucial.

Scenarios to use MongoDB over SQL:

    When the data structure is expected to evolve frequently.
    For applications requiring high scalability and performance.
    When dealing with semi-structured or unstructured data.
    Real-time analytics and IoT applications.
'''

'''
Q2. State and Explain the features of MongoDB.

Features of MongoDB:
Flexible Schema: Documents in MongoDB do not require a predefined schema, allowing for dynamic and flexible data models.
High Performance: MongoDB uses indexing, sharding, and replication for high performance and scalability.
Scalability: It is designed to scale out horizontally with sharding, distributing data across multiple servers.
Document-Oriented: Data is stored in JSON-like BSON documents, making it easy to work with.
Rich Query Language: Supports a wide range of queries, including field, range queries, regular expressions, etc.
Aggregation: MongoDB provides aggregation framework for complex analytics and data processing.
Geospatial Indexing: Allows for efficient geospatial queries.
High Availability: Replication and failover mechanisms ensure high availability and data durability.
Security: Provides role-based access control, encryption, and auditing features.
'''

#Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.


from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://sumitttroy56:Nandu@cluster0.wyz7ynw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = client["database_5"]
my_collection = db["first_collection_1"]
'''
Q4. Using the database and the collection created in question number 3, write a code to insert one record, and insert many
records. Use the find() and find_one() methods to print the inserted record.
'''
#insert 1 record
data_5 = {
    "name":"harsh",
    "rollNo":75
}

my_collection.insert_one(data_5)

#insert many record
data_6 = [
    {"name":"prince","rollNo":8},
    {"name":"udit","rollNo":5}
]
my_collection.insert_many(data_6)

print(my_collection.find_one({"name": "varnit"}))

'''
Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to demonstrate this.
find() Method: The find() method is used to query documents in a MongoDB collection.
It returns a cursor object, which can be iterated to retrieve documents.
Filters can be applied to specify criteria for the query.
'''
results = my_collection.find({"rollNo": {"$gt": 24}})  
print("Find method results:")
for result in results:
    print(result)
    
'''
Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.
sort() Method: The sort() method in MongoDB is used to sort the documents in a collection.
It takes one or more fields and their sort order as arguments.
By default, it sorts in ascending order.
'''
# Sorting documents by age in descending order
results = my_collection.find().sort("rollNo", -1)

# Iterating through the sorted results
print("Sorted results:")
for result in results:
    print(result)


'''
Q7. Explain why delete_one(), delete_many(), and drop() are used.
delete_one(): Used to delete a single document that matches the specified criteria.
Example: mycollection.delete_one({"name": "John"})
delete_many(): Used to delete multiple documents that match the specified criteria.
Example: mycollection.delete_many({"age": {"$lt": 30}})
drop(): Used to drop an entire collection from a database.
Example: mycollection.drop()
These methods are used for data management in MongoDB:

delete_one() and delete_many() are used to remove documents from a collection based on specified criteria.
drop() is used to completely remove a collection and its associated documents from the database.
'''
