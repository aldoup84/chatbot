from flask import Flask, request
import whatsappServices
import util

app = Flask(__name__)
@app.route ('/welcome', methods=['GET'])
def index():
    return "Welcome Developer"

@app.route('/whatsapp', methods = ['GET'])
def VerifyToken():
    try:
        accessToken = "0217113902171139"
        token = request.args.get("hub.verify_token")
        challange = request.args.get("hub.challange")
        if (token != None and challange != None and token == accessToken):
            return challange
        else:
                return "", 400
    except:
         return "", 400

@app.route('/whatsapp', methods = ['POST'])
def ReceivedMessage():
    try:
        body = request.get_json()
        entry = (body['entry'])[0]
        changes = (entry['changes'])[0]
        value = changes['value']
        message = (value['messages'])[0]
        number = message['from']
        number = number.replace("521", "52")
        print("Number: ", number)
        text = util.GetTextUser(message)
        print("Procesando:  ", text)
        GenerateMessage(text, number)
        return "EVENT_RECEIVED"
    except:
        return "EVENT_RECEIVED"

def GenerateMessage(text, number):
    text = text.lower()
    if "text" in text:
        data = util.TextMessage("Text", number)
    if "format" in text:
        data = util.TextFormatMessage(number)
    if "image" in text:
        data = util.ImageMessage(number)
    if "video" in text:
        data = util.VideoMessage(number)
    if "audio" in text:
        data = util.AudioMessage(number)
    if "document" in text:
        data = util.DocumentMessage(number)
    if "location" in text:
        data = util.LocationMessage(number)
    if "button" in text:
        data = util.ButtonMessage(number)
    if "list" in text:
        data = util.ListMessage(number)
    print ("daa", data)
    whatsappServices.SentMessageWhatsApp(data)

if (__name__ == "__main__"):
    app.run()