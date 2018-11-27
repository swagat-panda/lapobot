import pymongo
from pymongo import MongoClient
import json

class DatabaseColObject():
    def getDatabaseCon():
        with open('Filelist.json', 'r') as f:
                dic_file_list = json.load(f)
        with open(dic_file_list['filelist']['database_config_file'], 'r') as f:
                dic_database_config = json.load(f)
        client=MongoClient()
        try:
            #two arguments IP and port number of the server where the MongoServer is present
            client=MongoClient(dic_database_config['dbclient']['ip'],dic_database_config['dbclient']['port'])
            db=client[dic_database_config['dbclient']['dbname']]
            collectioncon=db[dic_database_config['dbclient']['dbconn']]
        except Exception as e:
            print(e)
        return collectioncon