from pymongo import MongoClient
from urllib.parse import quote_plus
import getpass

#Setting up Mongo Connection
user=input("Username: ") #Get username
pwd=getpass.getpass() #Get the password without prompting the pass
url_pwd=quote_plus(pwd) #Parse especial characters possibly in the password
auth="geral" #Authentication database
database="geral" #Database to connect to

uri=f"mongodb://{user}:{url_pwd}@habeasdata.fearp.usp.br/{database}?authSource={auth}"


#Starting Mongo connection
client=MongoClient(uri)
#Setting database
db=client.<database> #Replace <database> with the desired databese
#Setting collection
collec=db.<collection> #Replace <collection> with the desired collection

del user,pwd,url_pwd,auth,database,uri


#Example
for doc in collec.find():
    print(doc)
