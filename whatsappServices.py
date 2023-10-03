import requests
import json

def SentMessageWhatsApp(data):
    try:
        token = "EAAJaZAQov7jUBOZCiLHNam72lA6xqR7yV7LeUonT8hJolMXhzuFwQ4C6TVusAFEDA7cOnMJW1QC7xKh5Gz44OmwOZCGZBMYHmFs4pk3dsAGyjVaBvB5tgt22jsZCfclRoFSTxosbnqi7DOnrguVnOH1h7pYH0ChJpcZATFhFZAiYeNtrEaz37gHgEaEgeuV5QOM"
        apiUrl = "https://graph.facebook.com/v17.0/131540456707269/messages"
        headers = {"Content-Type" : "application/json", "Authorization" : "Bearer " + token }
        response = requests.post(apiUrl, data=json.dumps(data),headers=headers)
        if response.status_code == 200:
            return True
        return False
    except Exception as exception:
        print (exception)
        return False