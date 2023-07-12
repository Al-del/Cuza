from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://Cuza:FvcsS3QJWzhGKRkk@cuza.yuiityt.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
def inser_data(data):
    db = client.sample_guides
    coll = db.comets
    result = coll.insert_many(data)
def read_Data(database_name, collection_name):
    db = client[database_name]
    col = db[collection_name]
    # Collection Name
    x = col.find_one()
def delete_data(database_name, collection_name):
    mydb = client[database_name]
    mycol = mydb[collection_name]

    x = mycol.delete_many({})

    print(x.deleted_count, " documents deleted.")
def clothes():
    try:
        client.admin.command('ping')
        print('Connected successfully!')
        db = client.sample_guides
        coll = db.comets
        inser_data([{"code": 1}] )

    except Exception as e:
        print(e)
def emotions():
    try:
        client.admin.command('ping')
        print('Connected successfully!')
        db = client.sample_guides
        coll = db.comets
        inser_data([{"code": 2}] )

    except Exception as e:
        print(e)
def emotions():
     try:
        client.admin.command('ping')
        print('Connected successfully!')
        inser_data([{"code":2}])
        while True:
            x=read_Data("sample_guides","data")
            if x!=None:
                print(x)
                if x['emotiom']=="Happy":
                    return "be happy"
                    delete_data("sample_guides","data")
                    delete_data("sample_guides","comets")

                elif x['emotiom']=="Angry":
                    return "you are angry"
                    delete_data("sample_guides","data")
                    delete_data("sample_guides","comets")
                elif x['emotiom']=="Sad":
                    return "you are sad"
                    delete_data("sample_guides","data")
                    delete_data("sample_guides","comets")
            else:
                print("BAAU")
     except Exception as e:
        print(e)
