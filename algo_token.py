# Designed by:-
# THIS PYTHON FILE IS A PART OF ALGO FAMILY.
# THIS HAS A SINGLE CLASS TokenGenerator() with a SINGLE FUNCTION AS get_tokens()
# THIS FUNCTION GENERATES THE TOKENS from the Request object(message) that is 
# to be sent to the get_validtokens() of algo_validtoken file for further manipulation

#For reading the json data from the json file
import json
#To send the tokens to get_validtokens() for further manipulation
from algo_validtoken import ValidateTokens
#To store the user message into the MongoDB
from storedb import Store_Dic

# Tokenise the usertext to get the valid tokens and map it
class TokenGenerator():
    #To generate tokens and takes 3 arguments:
    #userText- message or the request
    #username- name of the user
    #date- time of the query generated
    def get_tokens(userText,username,date):
        with open('Filelist.json', 'r') as f:
            dic_file_list = json.load(f)

        #open the laptop configuration file which is a json file
        #and it contain all the configuration of various laptops
        with open(dic_file_list['filelist']['config_file'], 'r') as f:
            dic_laptop_config = json.load(f)

        #open the valid-token file which is a json file
        #and it contain all the valid tokens with its
        #priority and flag value respectively
        with open(dic_file_list['filelist']['valid_tokens_file'], 'r') as f:
            dic_validtoken = json.load(f)

        #open the invalid-token file which is a json file
        #and it contain all the invalid token with its
        #priority and flag value respectively
        with open(dic_file_list['filelist']['invalid_tokens_file'], 'r') as f:
            dic_invalidtoken = json.load(f)

        #Change the message to lowercase and split it for retriving each words individually as a list
        userText=userText.lower()
        tokens = userText.split("+")
        # user.append(userText)

        #print(userText,"usere===>")
        #If the message is not 'thanks' then it sends the message to the store_conversation() of 
        #storedb.py and has a flag value 1 to indicate that the user text is not thanks
        if(userText!="thanks"):
            Store_Dic.store_conversation(userText.replace("+"," "),1,username,date)
        # print("ok1")

        #Stores the validtoken as a list in a list named 'valid'
        valid = list(dic_validtoken['tokens']['valid']['validtoken'])

        #Stores all the brands in a list named 'branditem'
        branditem = {}
        for i in list(dic_laptop_config['lapo'].keys()):
            branditem[dic_laptop_config['lapo'][i]['brand']] = 1
        branditem = list(branditem.keys())
        #branditem.append("mac")

        #Stores all the purpose in a list named 'purposeitem'
        purposeitem = {}
        for i in list(dic_laptop_config['lapo'].keys()):
            purposeitem[dic_laptop_config['lapo'][i]['purpose']] = 1
        purposeitem = list(purposeitem.keys())

        #Stores the data from the dictionary according to the intents that are retrieved from the json file 
        valuetokens = list(dic_validtoken['tokens']['valid']['value'])
        # invalid = dic_invalidtoken['tokens']['message']['default']
        welcome = dic_validtoken['tokens']['messages']['welcome']
        wellap = dic_validtoken['tokens']['messages']['wellap']
        weltok = list(dic_validtoken['tokens']['valid']['weltok'])
        invalidtokens = list(dic_invalidtoken['tokens']['invalid']['token'])
        joinertoken = list(dic_validtoken['tokens']['valid']['joiner'])
        lapolist = list(dic_laptop_config['lapo'].keys())
        introtoken = list(dic_validtoken['tokens']['valid']['intro'])

        #Declaring 3 lists thats will hold the words, their respective flags and 
        #their respective priority according to the storing sequence in the 'token' list
        token = []
        flag_variable_set = []
        priority_variable_set = []

        #Outerloop that iterates through the words present in the tokens
        for outerloop in tokens:
            
            #Innerloop which iterates through the valid list
            for innerloop in valid:
                #If the word and the validtoken match then the token,its flag and 
                #its priority are retrieved from the dictionary and appended to their respective lists
                if outerloop == innerloop:
                    flag_variable_set.append(dic_validtoken['tokens']['flag']['validtoken'])
                    token.append(outerloop)
                    priority_variable_set.append(dic_validtoken['tokens']['priority']['validtoken'])
            
            #Innerloop which iterates through the purposeitem list
            for innerloop in purposeitem:
                #If the word and the purpose match then the token,its flag and its 
                #priority are retrieved from the dictionary and appended to their respective lists
                if outerloop == innerloop:
                    flag_variable_set.append(dic_validtoken['tokens']['flag']['purpose'])
                    token.append(outerloop)
                    priority_variable_set.append(dic_validtoken['tokens']['priority']['purpose'])
            
            #Innerloop which iterates through the branditem list
            for innerloop in branditem:
                #If the word and the brand match then the token,its flag and its 
                #priority are retrieved from the dictionary and appended to their respective lists
                if outerloop == innerloop:
                    flag_variable_set.append(dic_validtoken['tokens']['flag']['brandname'])
                    token.append(outerloop)
                    priority_variable_set.append(dic_validtoken['tokens']['priority']['brandname'])
            
            #Innerloop which iterates through the valuetokens list
            for innerloop in valuetokens:
                #If the word and the valuetokens match then the token,its flag and its 
                #priority are retrieved from the dictionary and appended to their respective lists
                if outerloop == innerloop:
                    flag_variable_set.append(dic_validtoken['tokens']['flag']['valuetoken'])
                    priority_variable_set.append(dic_validtoken['tokens']['priority']['valuetoken'])
                    token.append(outerloop)
            
            #Innerloop which iterates through the weltok list
            for innerloop in weltok:
                #If the word and the welcome token match then the token,its flag and its 
                #priority are retrieved from the dictionary and appended to their respective lists
                if outerloop == innerloop:
                    flag_variable_set.append(dic_validtoken['tokens']['flag']['weltok'])
                    token.append(outerloop)
                    priority_variable_set.append(dic_validtoken['tokens']['priority']['weltok'])
            
            #Innerloop which iterates through the joinertoken list
            for innerloop in joinertoken:
                #If the word and the joiner token match then the token,its flag and its 
                #priority are retrieved from the dictionary and appended to their respective lists
                if outerloop == innerloop:
                    flag_variable_set.append(dic_validtoken['tokens']['flag']['joiner'])
                    token.append(outerloop)
                    priority_variable_set.append(dic_validtoken['tokens']['priority']['joiner'])
            
            #Innerloop which iterates through the invalidtokens list
            for innerloop in invalidtokens:
                #If the word and the invalid token match then the token,its flag and its 
                #priority are retrieved from the dictionary and appended to their respective lists
                if outerloop == innerloop:
                    flag_variable_set.append(dic_invalidtoken['tokens']['flag']['invalidtoken'])
                    token.append(outerloop)
                    priority_variable_set.append(dic_invalidtoken['tokens']['priority']['invalidtoken'])
            
            #Innerloop which iterates through the introtoken list
            for innerloop in introtoken:
                #If the word and the intro token match then the token,its flag and its 
                #priority are retrieved from the dictionary and appended to their respective lists
                if outerloop == innerloop:
                    flag_variable_set.append(dic_validtoken['tokens']['flag']['intro'])
                    token.append(outerloop)
                    priority_variable_set.append(dic_validtoken['tokens']['priority']['intro'])

            #If the word is a number that describes the price range then this try block works and its 
            #respective flag and priority are set, and if not then the error is handled by except block
            try:
                int(outerloop)
                flag_variable_set.append(dic_validtoken['tokens']['flag']['pricenumber'])
                priority_variable_set.append(dic_validtoken['tokens']['priority']['pricenumber'])
                token.append(int(outerloop))
            except Exception:
                k = 0

            #Innerloop which iterates through the lapo(laptops) list
            for innerloop in lapolist:
                #If the word and the laptop token match then the token,its flag and its 
                #priority are retrieved from the dictionary and appended to their respective lists
                if innerloop == outerloop:
                    flag_variable_set.append(dic_validtoken['tokens']['flag']['modelname'])
                    priority_variable_set.append(dic_validtoken['tokens']['priority']['modelname'])
                    token.append(outerloop)

            #If the word match with termination token then the token,its flag and its 
            #priority are retrieved from the dictionary and appended to their respective lists
            if outerloop in dic_validtoken['tokens']['valid']['termination']:
                flag_variable_set.append((dic_validtoken['tokens']['flag']['termination']))
                priority_variable_set.append(dic_validtoken['tokens']['priority']['termination'])
                token.append(outerloop)

        #print(token)
        #print(flag_variable_set, "==>flag")
        #print(priority_variable_set, "==>priority_variable_set")

        #It calls the get_validtokens() which takes the 3 lists that we 
        #have been appending in this class and with that the name of the user 
        #and the time of the message and returns the result to the main.py
        return ValidateTokens.get_validtokens(token, flag_variable_set, priority_variable_set,username,date)





