#Importing the MongoClient for mongoDB
#import pymongo
#from pymongo import MongoClient

#Importing the datetime for recieving current time
import datetime

#To create session id using uuid4(version 4)
import uuid

from dbconnect import DatabaseColObject

#Class Store_Dic to basically interact with the MongoDB and create the session id
class Store_Dic():
    newValues={}#For storing the new values that are going to be updated
    myQuery={}#For storing the query that is to be given as argument to the update function
    convodicttt={}#To store an object of the chat
    convodicttt['_id']=''#Assigning the first key of the dictionary as '_id' 
    #whose values acts as root element in the mongoDB
    convodicttt['convo']=[]#Initializing the convo key of the dictionary as a empty list

    #Here it clears all the content of the variables and gets ready for the new object to be stored
    def makeEmpty():
        Store_Dic.newValues.clear()
        Store_Dic.myQuery.clear()
        Store_Dic.convodicttt.clear()
        Store_Dic.convodicttt['_id']=''
        Store_Dic.convodicttt['convo']=[]

    #This method interacts with the mongoDb and creates the session_id. 
    #This method takes 4 arguments that is token-'message',
    #flag-'user or bot'
    #username-'name of the sender of the message'
    #date1-'date and time of the message'
    def store_conversation(token,flag,username,date1):
        #print(token,flag,"db==>")

        #Connecting to the MongoClient server, creating the database and a collection under it
        collectioncon=DatabaseColObject.getDatabaseCon()

        #Message is from USER
        if flag==1 or flag==3 :
            #local dictionary 'user'(to avoid overwriting of each new data) to store the 
            #name,message and date and lastly to append it to the list 'convo'
            user={}
            user['name']=username
            user['msg']=token
            user['time']=date1
            Store_Dic.convodicttt['convo'].append(user)
        else:#Message is from BOT
            #local dictionary 'bot'(to avoid overwriting of each new data) to store the 
            #name,message and date and lastly to append it to the list 'convo'
            bot={}
            bot['name']='bot'
            bot['msg']=token
            bot['time']=date1
            Store_Dic.convodicttt['convo'].append(bot)

        #Here whether the conversation object is new or not is checked by checking the '_id' key as empty
        if Store_Dic.convodicttt['_id']=='':
            Store_Dic.convodicttt['_id']=uuid.uuid4()#session id creation by uuid4()
            Store_Dic.convodicttt['date']=datetime.datetime.now()#generating current time by now()
            x=collectioncon.insert_one(Store_Dic.convodicttt)#inserting the first element of the object
            #print("lklk")
            #print(Store_Dic.convodicttt['_id'],"==>uid")
        else:#If '_id' has a value then the element are stored under the same session-id
            #Generating the query that is to be matched with the session-id in the mongoDB
            Store_Dic.myQuery['_id']=Store_Dic.convodicttt['_id']
            #Assigning the new values that is to be replaced with the previous values of the matched session-id
            Store_Dic.newValues['$set']=Store_Dic.convodicttt
            #updating the object by taking the 2 arguments that are query and new values
            collectioncon.update_one(Store_Dic.myQuery,Store_Dic.newValues)
            #print("llll")
            
        #Here if the message is thanks,that is checked and the makeEmpty() is called which clears the content 
        #of the varibales so that the next object can be stored without overwriting
        if flag==3:
            Store_Dic.makeEmpty()