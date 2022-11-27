import pymongo
import pandas as pd
import json
import os,sys
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.config import mongo_client

# Provide the mongodb localhost url to connect python to mongodb.


def get_collection_as_dataframe(database_name,collection_name)->pd.DataFrame:
    """
     Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        ##since id column is present from mongodb collection we dont need that column so we are dropping 
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e, sys)