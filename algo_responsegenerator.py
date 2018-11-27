# Designed by:-
# THIS PYTHON FILE IS A PART OF ALGO FAMILY.
# THIS HAS A SINGLE CLASS ResponseGenerator() with a SINGLE FUNCTION AS get_output_string()
# THIS FUNCTION GENERATES THE BOT output_string WITH RESPECT TO THE VALID TOKENS PROVIDED 
# AND PROCESED BY THE PREVIOUS CLASSES OF ALGO FAMILY




import json
from storedb import Store_Dic
from algo_supportfunction import PriceResponseGenerator
from algo_supportfunction import BrandResponseGenerator
from algo_supportfunction import PurposeResponseGenerator
from algo_supportfunction import ConfigResponseGenerator
from algo_supportfunction import Introduction
from algo_supportfunction import ConvertDic



#THIS CLASS CONTAINS THE FUNCTION get_output_string() which creates the 
#user request to bot response (after tokenising to valid tokens)
class ResponseGenerator():
    def get_output(token, flag_variable_set, priority_set_variable,username,date):
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


        #print("ok-1 entry")
        output_string = ""
        #this if is true only if the user query didn't contain a proper valid token
        #otherwise if the user query have some valid tokens then only the else part will flow
        #else  part is a label structure where the module work is performed as per label 
        #of priority 0 is the least priority and 6 is the maximum priority
        #some module share similar  priority which are differenciated by the flag content of that module
        if flag_variable_set == []:
            output_string = dic_invalidtoken['tokens']['message']['default']
        else:
            #in my model joiner has the maximum priority hence  so as per the level structure the first 
            #checking is done for the joiner
            if (dic_validtoken['tokens']['priority']['joiner'] in priority_set_variable):
                #joiner is a dependent module hence it check for brand,purpose and price module to create the
                #user response

                #we have two joiner i.e["and","or"] we have applied the logic as per the normal corresponding operator works

                #in this if we are doing the or operation and in the else part we are performing the and operation
                if (token[priority_set_variable.index(dic_validtoken['tokens']['priority']['joiner'])] == "or"):
                    #checked for only priority of purpose because purpose,brand and price have the same priority
                    #so no need of checking the other two 
                    if (dic_validtoken['tokens']['priority']['purpose'] in priority_set_variable):
                        #print(1)
                        #computed the purpose keyword family if exists in user query
                        if (dic_validtoken['tokens']['flag']['purpose'] in flag_variable_set):
                            output_string = output_string + "  " + PurposeResponseGenerator.get_purpose(
                                token[flag_variable_set.index(dic_validtoken['tokens']['flag']['purpose'])])
                        #computed the brand keyword family if exists
                        if (dic_validtoken['tokens']['flag']['brandname'] in flag_variable_set):
                            # print(2,token[flag_variable_set.index(2)])
                            output_string = output_string + "  " + BrandResponseGenerator.get_brand(
                                token[flag_variable_set.index(dic_validtoken['tokens']['flag']['brandname'])])
                            #print(output_string)
                        #compute the price keyword family if exists
                        if (dic_validtoken['tokens']['flag']['pricenumber'] in flag_variable_set):
                            if (dic_validtoken['tokens']['flag']['valuetoken'] in flag_variable_set):
                                print(token[flag_variable_set.index(dic_validtoken['tokens']['flag']['pricenumber'])])
                                # check the -ve flow of price keyword
                                if (token[flag_variable_set.index(dic_validtoken['tokens']['flag']['valuetoken'])] 
                                    in list(dic_validtoken['tokens']['valid']['oppovalue'])):
                                    output_string = output_string + "  " + PriceResponseGenerator.get_price(
                                        token[flag_variable_set.index(dic_validtoken['tokens']['flag']['pricenumber'])], -1)
                                else:
                                    #print(token[flag_variable_set.index(9)])

                                    output_string = output_string + "  " + PriceResponseGenerator.get_price(
                                        token[flag_variable_set.index(dic_validtoken['tokens']['flag']['pricenumber'])], 0)
                                    #print(output_string)
                            else:

                                output_string = output_string + "  " + PriceResponseGenerator.get_price(
                                    token[flag_variable_set.index(dic_validtoken['tokens']['flag']['pricenumber'])], 0)
                    #eliminating the duplicate model number that or operator generates
                    list1=output_string.split(" ")
                    print(list1,"got or list")
                    output_string=""
                    for i in list(set(list1)):
                        output_string=output_string+" "+i

                    #print(output_string)
                #in this else part 'and' operation is done a joiner keyword and it is similar to the normal and operation
                #here we are performing the and operation through the list,set intersaction 
                else:
                    if (dic_validtoken['tokens']['priority']['brandname'] in priority_set_variable):
                        #print(1)
                        list1 = []
                        list2 = []
                        joinlist = []
                        #check the brand family tokens if exists and store in a list
                        if (dic_validtoken['tokens']['flag']['brandname'] in flag_variable_set):
                            list1 = BrandResponseGenerator.get_brand(
                                token[flag_variable_set.index(dic_validtoken['tokens']['flag']['brandname'])]).split()
                        #check the purpose family token if exists and store in a list
                        if (dic_validtoken['tokens']['flag']['purpose'] in flag_variable_set):
                            list2 = PurposeResponseGenerator.get_purpose(
                                token[flag_variable_set.index(dic_validtoken['tokens']['flag']['purpose'])]).split()
                            #perform and operation between brand and purpose iff brand list is occupied
                            if (list1 != []):
                                list2 = list(set(list1).intersection(list2))
                                list1 = []
                        #check the price token family if exists and store it in a list
                        if (dic_validtoken['tokens']['flag']['pricenumber'] in flag_variable_set):
                            if(dic_validtoken['tokens']['flag']['valuetoken'] in flag_variable_set):
                                #check for the -ve flow of value token i.e the opposite direction flow of price keyword
                                if (token[flag_variable_set.index(dic_validtoken['tokens']['flag']['valuetoken'])] 
                                    in list(dic_validtoken['tokens']['valid']['oppovalue'])):
                                    joinlist = PriceResponseGenerator.get_price(
                                        token[flag_variable_set.index(
                                            dic_validtoken['tokens']['flag']['pricenumber'])], -1).split()
                                else:
                                    #print(token[flag_variable_set.index(9)])

                                    joinlist =PriceResponseGenerator.get_price(
                                        token[flag_variable_set.index(
                                            dic_validtoken['tokens']['flag']['pricenumber'])], 0).split()
                            else:
                                joinlist = PriceResponseGenerator.get_price(
                                    token[flag_variable_set.index(
                                        dic_validtoken['tokens']['flag']['pricenumber'])], 0).split()
                        # perform the and operation as per list set interaction
                        if (joinlist != []):
                            if (list2 != []):
                                joinlist = list(set(joinlist).intersection(list2))
                            else:
                                joinlist = list(set(joinlist).intersection(list1))
                        else:
                            joinlist = list(set(list1).intersection(list2))

                        for i in joinlist:
                            output_string=output_string+"  "+i
            #here the action is performed as a single model  and are leveled as per the priority value
            #first the priority of purpose is checked i.e  purpose,brand,price have same priority
            elif(dic_validtoken['tokens']['priority']['purpose'] in priority_set_variable):
                #checking the purpose flag for existing of any purpose family keywords
                if (dic_validtoken['tokens']['flag']['purpose'] in flag_variable_set):
                    output_string = output_string + "  " + PurposeResponseGenerator.get_purpose(
                        token[flag_variable_set.index(dic_validtoken['tokens']['flag']['purpose'])])
                #checking the brand flag for existing of any brand family keywords
                if (dic_validtoken['tokens']['flag']['brandname'] in flag_variable_set):
                    # print(2,token[flag_variable_set.index(2)])
                    #checking for any model number with space validation error
                    if(dic_validtoken['tokens']['flag']['pricenumber'] in flag_variable_set):
                        if(len(str(token[flag_variable_set.index(
                            dic_validtoken['tokens']['flag']['pricenumber'])]))==4):
                            st_model=str(token[flag_variable_set.index(
                                dic_validtoken['tokens']['flag']['brandname'])])+str(token[flag_variable_set.index(
                                dic_validtoken['tokens']['flag']['pricenumber'])])
                            output_string=output_string+"  "+ConfigResponseGenerator.config(st_model)
                    else:
                        output_string = output_string + "  " + BrandResponseGenerator.get_brand(
                            token[flag_variable_set.index(dic_validtoken['tokens']['flag']['brandname'])])
                    #print(output_string)
                #check for any price  token if exist and perform the activity
                if (dic_validtoken['tokens']['flag']['pricenumber'] in flag_variable_set):
                    if (dic_validtoken['tokens']['flag']['valuetoken'] in flag_variable_set):
                        #print(dic_validtoken['tokens']['valid']['oppovalue'],"ok got it")
                        #checking for the -ve flow flow of price checker
                        if (token[flag_variable_set.index(dic_validtoken['tokens']['flag']['valuetoken'])] 
                            in list(dic_validtoken['tokens']['valid']['oppovalue'])):
                            output_string = output_string + "  " + PriceResponseGenerator.get_price(
                                token[flag_variable_set.index(dic_validtoken['tokens']['flag']['pricenumber'])], -1)
                        else:
                            #print(token[flag_variable_set.index(9)])

                            output_string = output_string + "  " + PriceResponseGenerator.get_price(
                                token[flag_variable_set.index(dic_validtoken['tokens']['flag']['pricenumber'])], 0)
                            #print(output_string)
                    else:

                        output_string = output_string + "  " + PriceResponseGenerator.get_price(
                            token[flag_variable_set.index(dic_validtoken['tokens']['flag']['pricenumber'])], 0)

                #print(output_string)
                #checking the priority of the model number which is present in lapoconfig.json file
                #and performing the action  to get all the specs of the desired laptop model
            elif(dic_validtoken['tokens']['priority']['modelname'] in priority_set_variable):
                output_string=output_string+" "+ConfigResponseGenerator.config(
                    token[flag_variable_set.index(dic_validtoken['tokens']['flag']['modelname'])])
            #check the priority of validtoken because intro,weltok and validtoken have same level priority
            #but the intro one has slightly greater priority than other two hence it is called first at this level 
            elif(dic_validtoken['tokens']['priority']['validtoken'] in priority_set_variable):
                #checking for intro type token family if exist and getting the static output from the supportfunction.py
                #which describe the details of all brand and price range of different laptops the lapobot deals with
                if(dic_validtoken['tokens']['flag']['intro'] in flag_variable_set):
                    output_string=output_string+"  "+Introduction.introconfig()
                #it deals with the tokens that interact with the user as wetoks
                elif(dic_validtoken['tokens']['flag']['weltok'] in flag_variable_set):
                    output_string=output_string+"  "+dic_validtoken['tokens']['messages']['wellap']
                #it deals with the flag that corresponding hi,hello type tokens
                elif(dic_validtoken['tokens']['flag']['validtoken'] in flag_variable_set):
                    output_string=output_string+"  "+dic_validtoken['tokens']['messages']['welcome']
            #it deals with the termination token i.e thanks
            elif(dic_validtoken['tokens']['priority']['termination'] in priority_set_variable):
                #store in mongodb as flag-3 for generatiing new session

               Store_Dic.store_conversation("thanks",3,username,date)
               output_string="thanks"
               #channelising it to get_dic which return a dictionary which can easly be
               #dumped to json format to move to front end
               return ConvertDic.get_dic(output_string,username,date)


                #output_string=output_string+"  "+dic_validtoken['tokens']['messages']['thanksmsg']
        #storing in mongodb as flag-2 as abot response to the database
        Store_Dic.store_conversation(output_string,2,username,date)
        #channelising it to get_dic which return a dictionary which can easly be
        #dumped to json format to move to front end
        return ConvertDic.get_dic(output_string,username,date)




###### VARIABLE DECLARATION AND ITS FUNCTIONALITY ######

####DICTIONARY:-
# dic_laptop_config->create a dictionary from lapoconfig.json which contain the details 
# configuration of different models of different brands

# dic_validtoken-> create a DICTIONARY from validtokens.json which contain the details of different valid
# tokens and its corresponding flag and priority

# dic_invalidtoken-> create a DICTIONARY from invalidtokens.json which contails the details of different
# invalid  tokens and its corresponding flag and priority 

####LISTS :-
# token->it contains all the valid tokens after filter of the user request query to 
# its corresponding  tokens 

# flag_variable_set->it contains all the valid flag value

# priority_set_variable->it contains all the valid priority value of the corresponding token set.

# list1,list2,joinlist->this are the temporary lists used for the and operation

####normal variable :-
#output_string= it contains the final bot response generated by this engine