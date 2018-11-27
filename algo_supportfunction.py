# Designed by:-
# THIS PYTHON FILE IS A PART OF ALGO FAMILY.
# THIS PYTHON FILE ACTS AS A SUPPORT TO THE RESPONSE GENERATOR 
# THIS PYTHON FILE CONSISTS OF 6 DIFFERENT CLASSES i.e
# PriceResponseGenerator(),BrandResponseGenerator()
# PurposeResponseGenerator(),ConfigResponseGenerator()
# Introduction(),ConvertDic()
# THEY PERFORM  THE FOLLOWING TASKS:
#########
# PriceResponseGenerator() THIS CLASS HAVE A SINGLE FUNCTION
# get_price()->THIS FUNCTION HAS 2 PARAMETER TOKEN AND FLAG
# TOKEN CONTAINS THE VALID NUMBER OF THE PRICE WHICH HELP US TO SELECT
# THE LAPTOP AS PER ITS RANGE
# FLAG ACTS LIKE A CONTROLLER IT HAS TWO VALUE [-1,0] -1 FOR -VE FLOW
# AND 0 IS FOR +VE FLOW
#########
# BrandResponseGenerator() THIS CLASS HAVE A SINGLE FUNCTION
# get_brand()-> THIS FUNCTION HAS 1 PARAMETER TOKEN WHICH CORRESPONDING TO THE
# VALID BRAND NAME WHICH  RETURN  THE CORRESPONDING SET OF MODELS REFERED TO IT
#########
# PurposeResponseGenerator() THIS CLASS HAVE A SINGLE FUNCTION
# get_purpose()-> THIS FUNCTION HAS ONE PARAMETER TOKEN WHICH CORRESPONDING TO
# VALID PURPOSE OF THE LAPTOPS ARE RETURN THAT TYPE OF LAPTOPS
#########
# ConfigResponseGenerator() THIS CLASS HAVE A SINGLE FUNCTION
# config() -> THIS FUNCTION HAS ONE PARAMETER TOKEN WHICH CORRESPONDING TO THE 
# VALID MODEL NAME  OF THE LAPTOPS ARE RETURNS THEIR CORRESPONDUING FULL SPECS
# OF THAT MODEL
#########
# Introduction() THIS CLASS HAVE A SINGLE FUNCTION
# introconfig() -> THIS FUNCTION TAKES NO INPUT BUT RETURNS A STATIC OUTPUT STRING
# CORRESPONDING TO THE AVAILABLE TYPES OF LAPTOP IN LAPOCONFIG.JSON FILE
# i.e THE TYPE OF BRAND AND FROM LOWEST TO HIGHEST PRICE RANGE OF LAPTOPS
# ########
# ConvertDic() THIS CLASS HAVE A SINGLE FUNCTION
# get_dic() -> THIS FUNCTION TAKES OUTPUT_STRING AS A INPUT
# AND CONVERT TO A DICTIONARY SO THAT IT COULD BE EASILY DUMPED TO JSON FORMAT
# SO THAT IT CAN EASLY HANDELED BY THE FRONT END JAVASCRIPT PART
#####################################################################################




import json
from storedb import Store_Dic
import pymongo
from pymongo import MongoClient

# get the price token and get the desired laptop according
class PriceResponseGenerator():
    def get_price(token, flag):
        with open('Filelist.json', 'r') as f:
                dic_file_list = json.load(f)
        with open(dic_file_list['filelist']['config_file'], 'r') as f:
                dic_laptop_config = json.load(f)

        with open(dic_file_list['filelist']['valid_tokens_file'], 'r') as f:
                dic_validtoken = json.load(f)

        with open(dic_file_list['filelist']['invalid_tokens_file'], 'r') as f:
                dic_invalidtoken = json.load(f)

        price_output_string = ""
        # keyword.append(token)
        if (flag == -1):
            for outerloop in list(dic_laptop_config['lapo'].keys()):
                if dic_laptop_config['lapo'][outerloop]['price'] >= int(token):
                    price_output_string = price_output_string + "  " + str(outerloop)
        else:
            for outerloop in list(dic_laptop_config['lapo'].keys()):
                if dic_laptop_config['lapo'][outerloop]['price'] <= int(token):
                    price_output_string = price_output_string + "  " + str(outerloop)
        return price_output_string

# class DatabaseColObject():
#     def getDatabaseCon():
#         with open('Filelist.json', 'r') as f:
#                 dic_file_list = json.load(f)
#         with open(dic_file_list['filelist']['database_config_file'], 'r') as f:
#                 dic_database_config = json.load(f)
#         client=MongoClient()
#         try:
#             #two arguments IP and port number of the server where the MongoServer is present
#             client=MongoClient(dic_database_config['dbclient']['ip'],dic_database_config['dbclient']['port'])
#             db=client[dic_database_config['dbclient']['dbname']]
#             collectioncon=db[dic_database_config['dbclient']['dbconn']]
#         except Exception as e:
#             print(e)
#         return collectioncon

# get the brand token and get the desired laptop according to it
class BrandResponseGenerator():
    def get_brand(token):
        with open('Filelist.json', 'r') as f:
                dic_file_list = json.load(f)
        with open(dic_file_list['filelist']['config_file'], 'r') as f:
                dic_laptop_config = json.load(f)

        with open(dic_file_list['filelist']['valid_tokens_file'], 'r') as f:
                dic_validtoken = json.load(f)

        with open(dic_file_list['filelist']['invalid_tokens_file'], 'r') as f:
                dic_invalidtoken = json.load(f)
        brand_output_string = ""
        # bestbrand.append(token)
        for outerloop in list(dic_laptop_config['lapo'].keys()):
            if dic_laptop_config['lapo'][outerloop]['brand'] == token:
                brand_output_string = brand_output_string + "  " + str(outerloop)
        return brand_output_string


# get the purpose token and derive the theme out of it
class PurposeResponseGenerator():
    def get_purpose(token):
        with open('Filelist.json', 'r') as f:
                dic_file_list = json.load(f)
        with open(dic_file_list['filelist']['config_file'], 'r') as f:
                dic_laptop_config = json.load(f)

        with open(dic_file_list['filelist']['valid_tokens_file'], 'r') as f:
                dic_validtoken = json.load(f)

        with open(dic_file_list['filelist']['invalid_tokens_file'], 'r') as f:
                dic_invalidtoken = json.load(f)

        purpose_output_string = ""
        # purposemeet.append(token)
        for outerloop in list(dic_laptop_config['lapo'].keys()):
            if dic_laptop_config['lapo'][outerloop]['purpose'] == token:
                purpose_output_string = purpose_output_string + "  " + str(outerloop)
        return purpose_output_string


# get the model keyword and retrive all the details of that model
class ConfigResponseGenerator():
    def config(token):
        with open('Filelist.json', 'r') as f:
                dic_file_list = json.load(f)
        with open(dic_file_list['filelist']['config_file'], 'r') as f:
                dic_laptop_config = json.load(f)

        with open(dic_file_list['filelist']['valid_tokens_file'], 'r') as f:
                dic_validtoken = json.load(f)

        with open(dic_file_list['filelist']['invalid_tokens_file'], 'r') as f:
                dic_invalidtoken = json.load(f)

        config_output_string = "The selected laptop has the following specs\n\n"
        for outerloop in list(dic_laptop_config['lapo'][token].keys()):
            config_output_string = config_output_string + outerloop + "::" + str(dic_laptop_config['lapo'][token][outerloop]) + "\n"
        return config_output_string

# generates a static output of a brief details of laptops present in lapoconfig.json
class Introduction():
    def introconfig():
        with open('Filelist.json', 'r') as f:
                dic_file_list = json.load(f)
        with open(dic_file_list['filelist']['config_file'], 'r') as f:
                dic_laptop_config = json.load(f)

        with open(dic_file_list['filelist']['valid_tokens_file'], 'r') as f:
                dic_validtoken = json.load(f)

        with open(dic_file_list['filelist']['invalid_tokens_file'], 'r') as f:
                dic_invalidtoken = json.load(f)

        intro_output_string = "we deal with various kind of laptop like in brand we have "
        branditem = {}
        for outerloop in list(dic_laptop_config['lapo'].keys()):
            branditem[dic_laptop_config['lapo'][outerloop]['brand']] = 1
        for outerloop in list(branditem.keys()):
            intro_output_string = intro_output_string + "," + outerloop
        intro_output_string = intro_output_string + " and we have laptops price range from  "
        price_list = []
        for outerloop in list(dic_laptop_config['lapo'].keys()):
            price_list.append(dic_laptop_config['lapo'][outerloop]['price'])
        intro_output_string = intro_output_string + str(min(price_list)) + "to" + str(max(price_list))
        return intro_output_string
# this only generates a simple dictionary that with bot key the output string is appended
class ConvertDic():
    def get_dic(output_string,username,date):
        with open('Filelist.json', 'r') as f:
                dic_file_list = json.load(f)
        # with open(dic_file_list['filelist']['config_file'], 'r') as f:
        #         dic_laptop_config = json.load(f)

        # with open(dic_file_list['filelist']['valid_tokens_file'], 'r') as f:
        #         dic_validtoken = json.load(f)

        with open(dic_file_list['filelist']['invalid_tokens_file'], 'r') as f:
                dic_invalidtoken = json.load(f)

        dic={}
        print(output_string)
        if(output_string!="thanks"):
            if(output_string==""  or  output_string=="  "):
                dic['bot']=dic_invalidtoken["tokens"]["message"]["empty"]
                Store_Dic.store_conversation(dic_invalidtoken["tokens"]["message"]["empty"],2,username,date)
            else:
                dic['bot']=output_string

            
        # else:
        #     dic['bot']="hi new user"
        return dic

###### VARIABLE DECLARATION AND ITS FUNCTIONALITY ######
####DICTIONARY:-
# dic_laptop_config->create a dictionary from lapoconfig.json which contain the details 
# configuration of different models of different brands

# dic_validtoken-> create a DICTIONARY from validtokens.json which contain the details of different valid
# tokens and its corresponding flag and priority

# dic_invalidtoken-> create a DICTIONARY from invalidtokens.json which contails the details of different
# invalid  tokens and its corresponding flag and priority 

#dic-> it is just a simple dictionary which have OUTPUT_STRING as a bot key

##### output variables
# price_output_string-> generated by the get_price() function about the models related to the that price range

# purpose_output_string-> generated by the get_purpose() function about the models related to the that purpose TYPES

# brand_output_string ->generated by the get_brand() function about the models related to the that brand TYPES

# config_output_string -> generated by the config() function about the models specs

# intro_output_string -> generated by the introconfig() function about the total details of the laptop brand
# and upto what price range the laptop present in lapoconfig.json FILE