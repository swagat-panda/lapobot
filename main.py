import falcon
import json
from algo_token import TokenGenerator


# open the static html page
class StaticResource(object):
    def on_get(self, req, resp):
        #To check the status code is ok
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        #Read the html file and store it in the resp.body which will be loaded at the frontend
        with open('new_page.html', 'r') as f:
            resp.body = f.read()

#post function(request and response) stuffs
class get_bot_response(object):
            """docstrinss get_bot_responseame"""
            def on_post(self, req, resp):
                #print(req.context)
                #Read the REQUEST and decoding it using utf-8 format
                raw_json=req.bounded_stream.read()
                #print(raw_json,type(raw_json))
                raw_json=raw_json.decode("utf-8")
                #print(raw_json)

                #Spliting the Request to get the name,message and time separately
                raw_json=raw_json.split("&")
                value=raw_json[0].split("=")
                username=raw_json[1].split("=")
                date=raw_json[2].split("=")
                #print(value[1],username[1],date[1].replace("%3A",":"))
                #print(str(raw_json).split("=")[1].split("'")[0].strip("%0A"))

                #Defining a dictionary to store the response of the bot according to the request
                dic={}
                if (str(value[1])==""):#checking the request is blank
                    dic['bot']="PLEASE enter something!!!!"
                else:#sending the messsage, name,and time to the get_tokens() of algo_token 
                #file for further manipulation
                    dic=TokenGenerator.get_tokens(value[1],username[1],date[1].replace("%3A",":"))
                
                #stores in resp.body and using dumps() method change it to 
                #json format and the response is sent back to the frontend
                resp.body=dic
                #print(resp.body)
                resp.body=json.dumps(resp.body)
                return resp.body
                

                   
              
#Creates the Falcon api and stores the object in the app(variable name)        
app = falcon.API()
app.add_route('/lapobot', StaticResource())#Adding lapobot to the url, the 
#html file is being loaded by calling the StaticResource class

app.add_route('/post', get_bot_response())#When a request comes through the 
#post method the get_bot_response class is called