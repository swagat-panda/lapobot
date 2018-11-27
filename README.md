# lapobot
a simple chatbot which helps customer to buy a ideal laptop using (brand,price and purpose)



type this in cmd or terminal:- /note/ run these two commands in the folder path should be ------botfalcon_application_final$ or where the Dockerfile is present. /*******************/ //For building the image of the docker component command--- docker build -t image_name . (windows) (ubuntu or similar)--> sudo docker build -t image_name .

//For running the docker image with a specified port number //Here 4000 is the port on which gunicorn will run and for the default port of localhost we are giving 80 which is mentioned in the docker file. docker run -it -p4000:80 image_name (windows) (ubuntu or similar)--> sudo docker run -it -p4000:80 image_name

when you the gunicorn is running go to browser and type localhost:4000/lapobot and the bot will appear

/note/ please give your mongodb url in the dbconfig.json app folder-->dbconfig.json other wise response will not come /**********/

/note/ except localhost the voice input will not work due lack of ssl certificate i.e https /***********/

Mandatory information
Project title
Theme

