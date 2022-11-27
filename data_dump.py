import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017")

DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"
data_file_path = "/config/workspace/aps_failure_training_set1.csv"
if __name__ =="__main__":
    df = pd.read_csv(data_file_path)
    print(f"rows and columns : {df.shape}")

    ## we have to convert the data in the format of json and insert to mongodb
    ## convert datafram to json 
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    ##insert converted json to mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    print("records inserted succesfully")




