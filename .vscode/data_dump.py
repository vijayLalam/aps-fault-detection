
import pymongo
import pandas as pd
import json
#provide the mongodb localhost url to connect python to mongodb.
client=pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"


if __name__=="__main__":
    df= pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns:{df.shape}")
    #convert data frame into json format so that we can dump these records into mongo DB
    #df.reset_index(drop=True) drops the current index of the DataFrame and replaces it with an index of increasing integers. It never drops columns.
    #When you use inplace=False the new object is created and changed instead of the original data frame. If you wanted to update the original data frame to reflect the dropped rows you would have to reassign the result to the original data frame as shown in the code below.#df_2 = df_2.dropna(inplace=False)
    #inplace=True ..changes the original data frame directly

    df.reset_index(drop=True,inplace=True)
    #df.T.to_json() will transpose and convert dataframe into json format
    #json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary. It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.
    json_record=list(json.loads(df.T.to_json()).values())
    #print(list(json.loads(df.T.to_json()).values()))
   
    #using client we will insert json data into mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)