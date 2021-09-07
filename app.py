# # from flask import Flask
# # from flask import render_template

# # app = Flask(__name__)


# # @app.route("/")
# # def hello_world():
# #     return render_template("index.html")

# from flask import Flask, request, abort
# from urllib.parse import parse_qs
# import requests
# import json
# import time
# from flask_cors import CORS
# import threading

# # Functie nodig om de authservice te starten
# def startAuthService(i: str):
#     getAuthJson(i)

# # Authenticatie regelen voor Tribe
# def getAuthJson(i: str):
#     urlToken = "https://auth.tribecrm.nl/oauth2/token/"
#     payload='grant_type=refresh_token&client_id=c4f13121-c90a-4933-9707-1c0c867aa91a&client_secret=Nz7cpRVVB84r4spxZIK9cdp5hnPWqseYQCnDyE89&redirect_uri=https%3A%2F%2Fwww.vvebeheerwijsamen.nl%2F&refresh_token=' + i
#     headers = {
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Cookie': 'INGRESSCOOKIE=54faaf98337d6f7813532188c573aea2; INGRESSCOOKIE=807a6e8eb3c06330d01786a893d6643b; _csrf=B1q_xCLA5I9wzTOYViitnfht; connect.sid=s%3Ax3mhao7dflalABkV6NlMW-4DMlSjo8ld.PsNG8O8iDycnmcWh8UoXWQg7wshu6uoEpOvKsWq6F8U; oauth2_authentication_csrf=MTYyNzkyNTEzNXxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJRFF5T0RKa1pEaGtOR0ppWVRRM09EVmlPR0ZtTmprNVptSXhZalZrWTJKbHzfLLEBKYCmVvrknebFYm7aV-YN-O1aK8CN0slzFtwGHg=='
#     }
    
#     response = requests.request("POST", urlToken, headers=headers, data=payload)
#     print(response.text)
#     global y 
#     y = json.loads(response.text)
#     global url 
#     url = "https://api.tribecrm.nl/v1/mutation?access_token=" + y['access_token']
    
# def runAuth():
#     i = True   
#     while i:
#         startAuthService(y['refresh_token'])
#         time.sleep(30)
        

# headers = {
#     'Content-Type': 'application/json'
    
#     }

# # Keys die aanwezig zijn op de site
# keys_from_tribe = ['420', '421', '422', '423', '424', '425', '426', '427', '428', '429', '431', '432', '433', '434', '435', '436', '437', '438', '440', '442', '443', '444', '445']

# # Data checken op missende key's/value's, en indien toepasselijk standaard values invullen
# def check(data):
#     checked_data: dict = {}
#     keys_from_request = []
    
#     # Alle keys van request toeveogen aan een list
#     for k, v in data.items():
#         keys_from_request.append(str(k))
    
#     # Keys toevoegen aan een dict, als er een key mist wordt er een lege string toegevoegd
#     for i in keys_from_tribe:
#         if i in keys_from_request:
#             checked_data[i] = data[i][0] 
#         else:
#             checked_data[i] = ""

#     # Resultaat terugsturen
#     return checked_data

      
# def send_data_to_tribe(data: dict):
#     i = {
#     "entityType": "Relation.Organization",
#     "fields": {
#         "Name": data['420'],       
#         "EmailAddress": data['438']
#     }
#     }
    
#     createOrganizationinTribe(json.dumps(i), data)
 
# # Organization aanmaken in Tribe en OrganisationID ophalen  
# def createOrganizationinTribe(data, data2):
#     response = requests.request("POST", url, headers=headers, data=data)
#     print(response.text)
    
#     # OrganizationID ophalen en aanpassen
#     y = json.loads(response.text)
#     r = {
#         "entityType": "Relationship.Organization.CommercialRelationship.Prospect",
#         "fields": {
#             "AccountManager": "79cdc883-f25a-4d11-80f7-250f2ca3334c",
#             "Organization": y['data'][0]['entityId'],
#             "Status": "7dca7da5-0e92-4dfc-8aa2-af8c5496d6e2",
#             "Group": "a85e1bdb-00ec-42f0-83e1-c08d8d7a6dff",
#             "6fc4e9b8-c787-4f5f-94ff-918f8643f54d": int(data2['428']),
#             "e3822d01-22db-47f2-bfc5-298a22eb1019": int(data2['426']),
#             "7b13c3c8-851d-4979-847c-9d0ef290fd88": str(data2['425']),
#             "c2270abe-396b-42d3-9966-281fa0cdbaf9": str(data2['444'])
#             }
#     }
    
#     #Prospectaanmaken in Tribe
#     createProspectinTribe(json.dumps(r))
   
# # Prospect aanmaken in Tribe
# def createProspectinTribe(data):
#     response = requests.request("POST", url, headers=headers, data=data)
#     print(response.text)

# app = Flask(__name__)

# @app.route('/webhook', methods=['POST', 'GET'])
# def webhook():
#     if request.method == 'POST':
#         offerteAanvraag = request.get_data(as_text = True)
        
#         #Binnenkomende data converteren naar een dictionary --> key:['value']
#         formatted_data_dict: dict = parse_qs(offerteAanvraag)
        
#         # Data checken op missende key's/value's
#         checked_data_dict: dict = check(formatted_data_dict)
        
#         # Data naar API functies sturen
#         send_data_to_tribe(checked_data_dict)
        
#         return 'success', 200
#     else:
#         abort(400)
   
# @app.route('/')
# def index():
#     return "<h1>Welcome to our server !!</h1>"

# getAuthJson('xf7P3h8Jk1vr6dCIRiANDXBLx6SAx1Mslzaum9_P-9E.Ix2xAfeJAvy6h-CNWe-08yQtix3iW21nA5LnAC7buZI')   
# t=threading.Thread(target=runAuth)
# t.start()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=5000)
    
    
    
from flask import Flask, request, abort
from urllib.parse import parse_qs
import requests
import json
import time
from flask_cors import CORS
import threading

# Functie nodig om de authservice te starten
def startAuthService(i: str):
    return getAuthJson(i)

# Authenticatie regelen voor Tribe
def getAuthJson(i: str):
    urlToken = "https://auth.tribecrm.nl/oauth2/token/"
    payload='grant_type=refresh_token&client_id=c4f13121-c90a-4933-9707-1c0c867aa91a&client_secret=Nz7cpRVVB84r4spxZIK9cdp5hnPWqseYQCnDyE89&redirect_uri=https%3A%2F%2Fwww.vvebeheerwijsamen.nl%2F&refresh_token=' + i
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'INGRESSCOOKIE=54faaf98337d6f7813532188c573aea2; INGRESSCOOKIE=807a6e8eb3c06330d01786a893d6643b; _csrf=B1q_xCLA5I9wzTOYViitnfht; connect.sid=s%3Ax3mhao7dflalABkV6NlMW-4DMlSjo8ld.PsNG8O8iDycnmcWh8UoXWQg7wshu6uoEpOvKsWq6F8U; oauth2_authentication_csrf=MTYyNzkyNTEzNXxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJRFF5T0RKa1pEaGtOR0ppWVRRM09EVmlPR0ZtTmprNVptSXhZalZrWTJKbHzfLLEBKYCmVvrknebFYm7aV-YN-O1aK8CN0slzFtwGHg=='
    }
    
    response = requests.request("POST", urlToken, headers=headers, data=payload)
    print(response.text)
    global y 
    y = json.loads(response.text)
    global url 
    url = "https://api.tribecrm.nl/v1/mutation?access_token=" + y['access_token']
    return y
    
# def runAuth():
#     i = True   
#     while i:
#         startAuthService(y['refresh_token'])
#         time.sleep(6)
        

headers = {
    'Content-Type': 'application/json'
    
    }

# Keys die aanwezig zijn op de site
keys_from_tribe = ['420', '421', '422', '423', '424', '425', '426', '427', '428', '429', '431', '432', '433', '434', '435', '436', '437', '438', '440', '442', '443', '444', '445']

# Data checken op missende key's/value's, en indien toepasselijk standaard values invullen
def check(data):
    checked_data: dict = {}
    keys_from_request = []
    
    # Alle keys van request toeveogen aan een list
    for k, v in data.items():
        keys_from_request.append(str(k))
    
    # Keys toevoegen aan een dict, als er een key mist wordt er een lege string toegevoegd
    for i in keys_from_tribe:
        if i in keys_from_request:
            checked_data[i] = data[i][0] 
        else:
            checked_data[i] = ""

    # Resultaat terugsturen
    return checked_data

      
def send_data_to_tribe(data: dict):
    i = {
    "entityType": "Relation.Organization",
    "fields": {
        "Name": data['420'],       
        "EmailAddress": data['438']
    }
    }
    
    createOrganizationinTribe(json.dumps(i), data)
 
# Organization aanmaken in Tribe en OrganisationID ophalen  
def createOrganizationinTribe(data, data2):
    response = requests.request("POST", url, headers=headers, data=data)
    print(response.text)
    
    # OrganizationID ophalen en aanpassen
    y = json.loads(response.text)
    r = {
        "entityType": "Relationship.Organization.CommercialRelationship.Prospect",
        "fields": {
            "AccountManager": "79cdc883-f25a-4d11-80f7-250f2ca3334c",
            "Organization": y['data'][0]['entityId'],
            "Status": "7dca7da5-0e92-4dfc-8aa2-af8c5496d6e2",
            "Group": "a85e1bdb-00ec-42f0-83e1-c08d8d7a6dff",
            "6fc4e9b8-c787-4f5f-94ff-918f8643f54d": int(data2['428']),
            "e3822d01-22db-47f2-bfc5-298a22eb1019": int(data2['426']),
            "7b13c3c8-851d-4979-847c-9d0ef290fd88": str(data2['425']),
            "c2270abe-396b-42d3-9966-281fa0cdbaf9": str(data2['444'])
            }
    }
    
    #Prospectaanmaken in Tribe
    createProspectinTribe(json.dumps(r))
   
# Prospect aanmaken in Tribe
def createProspectinTribe(data):
    response = requests.request("POST", url, headers=headers, data=data)
    print(response.text)

app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        offerteAanvraag = request.get_data(as_text = True)
        
        #Binnenkomende data converteren naar een dictionary --> key:['value']
        formatted_data_dict: dict = parse_qs(offerteAanvraag)
        
        # Data checken op missende key's/value's
        checked_data_dict: dict = check(formatted_data_dict)
        
        # Data naar API functies sturen
        send_data_to_tribe(checked_data_dict)
        
        return 'success', 200
    else:
        abort(400)

   
@app.route('/first', methods=['GET'])
def index():
    return str(getAuthJson('PwNXmiKyi0aDWurbLBuMLPaPYprBM99aUFrvUbZYvhA.gsCBQjUpFqFFIw_Cjs5kV_UCjR48xN_VQQn4LCX97rY')), 200
    
    
@app.route('/second', methods=['GET'])    
def indexThree():
    startAuthService(y['refresh_token'])
    return 'success', 200

@app.route('/', methods=['GET', 'POST'])
def indexdom():
    return "<h1>Welcome to our server mannn !!</h1>"
       
       
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
