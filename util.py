def GetTextUser(message):
    text = ""
    typeMessage = message["type"]
    if (typeMessage == "text"):
        text = (message["text"])["body"]
    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]
        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print("Sin mensaje")
    else:
        print ("Sin mensaje")
    return text

def TextMessage(text, number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "text" : {
            "body": text
        },
            "type" : "text"
        }
    return data

def TextFormatMessage(number):
    data = {
        "messaging_product": "whatsapp",   
        "to": number,
        "type": "text",
        "text": {     
            "body": "*Bienvenido al servicio de asistente virtual*\n - _Gracaias por su preferencia_ -~Lo invitamos a utilizar nuestro servicio~ - ```Que tengas un excelente dia```"
            }
        }
    return data

def DocumentMessage(number):
    data = {
            "messaging_product": "whatsapp",   
            "to": number,
            "type": "document",
            "document": {
                "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/document_whatsapp.pdf",
                "filename": "Calificaciones 2023"
            }
        }
    return data

def ImageMessage(number):
    data = {
            "messaging_product": "whatsapp",   
            "to": number,
            "type": "image",
            "image": {
                "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/image_whatsapp.png"
            }
        }
    return data

def VideoMessage(number):
    data = {
            "messaging_product": "whatsapp",   
            "to": number,
            "type": "video",
            "video": {
                "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/video_whatsapp.mp4",
                "caption": "Video2023"
            }
        }
    return data

def AudioMessage(number):
    data = {
            "messaging_product": "whatsapp",   
            "to": number,
            "type": "audio",
            "audio": {
                "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/audio_whatsapp.mp3"
            }
        }
    return data

def LocationMessage(number):
    data = {
            "messaging_product": "whatsapp",   
            "to": number,
            "type": "location", 
            "location": {
                "latitude": "24.829753", 
                "longitude": "-107.385361", 
                "name": "Centro de Ciencias de Sinaloa", 
                "address": "Calz de las Americas Nte 2771-Nte, Burócrata, 80010 Culiacán Rosales, Sin."
            }
        }
    return data

def ButtonMessage(number):
    data = {
            "messaging_product": "whatsapp",   
            "to": number,    
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "Confirmas tu registro???"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "btnOk1",
                                "title": "✅ Si  👍"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "btnNo1",
                                "title": " ❌ No"
                            }
                        }
                    ]
                }
            }
        }
    return data

def ListMessage(number):
    data = {
            "messaging_product": "whatsapp",   
            "to": number,    
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {
                    "text": "✅ I have these options"
                },
                "footer": {
                    "text": "Select an option"
                },
                "action": {
                    "button": "See options",
                    "sections": [
                        {
                            "title": "Buy and sell products",
                            "rows": [
                                {
                                    "id": "main-buy",
                                    "title": "Buy",
                                    "description": "Buy the best product your home"
                                },
                                {
                                    "id": "main-sell",
                                    "title": "Sell",
                                    "description": "Sell your products"
                                }
                            ]
                        },
                        {
                            "title": "📍Centro de Atención",
                            "rows": [
                                {
                                    "id": "main-agency",
                                    "title": "Agency",
                                    "description": "Your can visit our agency"
                                },
                                {
                                    "id": "main-contact",
                                    "title": "Contact center",
                                    "description": "One of our agents will assist you"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    return data