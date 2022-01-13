from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage, message
from viberbot.api.messages.text_message import TextMessage
#import logging

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

import funkcijeZaFajlove as funcFajlove

komande = ("!about", "!komande", "!listaObavestenja", "!obavesti", "!listaTermina", "!zakazi")

app = Flask(__name__)
viber = Api(BotConfiguration(
    name=funcFajlove.botName,
    avatar=funcFajlove.avatarUrl,
    auth_token=funcFajlove.authToken
))

@app.route('/', methods=['POST'])
def incoming():
    #logger.debug("received request. post data: {0}".format(request.get_data()))
    # every viber message is signed, you can verify the signature using this method
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request.get_data())

    def decodeCommand(message):
        rawMessage = message.text
        command = recognizeCommand(message)
        if len(command) == len(rawMessage) - rawMessage.count(' '):
            return [command]
        firstArg = rawMessage.split(' ')[1]
        if len(command) + len(firstArg) == len(rawMessage) - rawMessage.count(' '):
            return [command, firstArg]
        secArg = rawMessage.split(' ')[2]
        if len(command) + len(firstArg) + len(secArg) == len(rawMessage) - rawMessage.count(' '):
            return [command, firstArg, secArg]
        thirdArg = rawMessage.split(' ')[3]
        if len(command) + len(firstArg) + len(secArg) + len(thirdArg) == len(rawMessage) - rawMessage.count(' '):
            return [command, firstArg, secArg, thirdArg]
        elif len(rawMessage) - rawMessage.count(' ') > len(command) + len(firstArg) + len(secArg) + len(thirdArg):
            sendMsgFunc("Previse parametra max 3")
            sendMsgFunc("(ノಠ益ಠ)ノ彡┻━┻")
            errorStrg = "Previse parametra"
            return errorStrg     
    
    def recognizeCommand(message):
        rawCommString = message.text
        commandStrg = rawCommString.split(' ')[0]
        return commandStrg

    def isCommand(message):
        if recognizeCommand(message) not in komande:
            return False
        else:
            return True

    def aboutFunc():
        sendMsgFunc("Bot za rano uzbunjivanje i informisanje studenata hemije na viberu/vajberu")
        sendMsgFunc("Autor Yistic(Milan Djokic)")
        sendMsgFunc("Github:github.com/Yistic")
        sendMsgFunc("≋≋≋≋≋̯̫⌧̯̫(ˆ•̮ ̮•ˆ)")
           
    def sendMsgFunc(poruka):
        viber.send_messages(viber_request.sender.id, TextMessage(text=poruka))
    """
    def echoMsgFunc():
        message = viber_request.message
        # lets echo back
        viber.send_messages(viber_request.sender.id, [message])
    """
    def komandeFunc():
        for komanda in komande:
            sendMsgFunc(komanda)
    
    def listaObavTermFunc(fileName, brLinija, getUserId):
        porukeZaSlanje = []
        obavestenja = funcFajlove.readLinesFromBellow(brLinija, fileName)
        for obavestenje in obavestenja:
            porukeZaSlanje.append(TextMessage(text=obavestenje))
        viber.send_messages(getUserId, porukeZaSlanje)

    def listaObavFunc():
        raisedErrVal = 0
        class Error(Exception):
            """Base class for other exceptions"""
            pass
        class nijeOdjereneVrednosti(Error):
            """Raised when the input value is too small"""
            pass
                
        if len(commandList) <= 1 or len(commandList) > 2:
            sendMsgFunc("Komanda prima samo jedan parametar(broj)")
        else:
            try:
                if int(commandList[1]) not in range(1, 100):
                    raise nijeOdjereneVrednosti
                elif raisedErrVal == 1:
                    pass
                else:
                    prvArg = int(commandList[1]) 
                    listaObavTermFunc("Zakazano", prvArg, viber_request.sender.id)
            except nijeOdjereneVrednosti:
                sendMsgFunc("Komanda prima samo jedan broj od 1 do 100")
            except ValueError:
                sendMsgFunc("Broj(parametar) ne sme da sadrzi slova, znakove")
                raisedErrVal = 1
    
    def listaTermFunc():
        raisedErrVal = 0
        class Error(Exception):
            """Base class for other exceptions"""
            pass
        class nijeOdjereneVrednosti(Error):
            """Raised when the input value is too small"""
            pass
                
        if len(commandList) <= 1 or len(commandList) > 2:
            sendMsgFunc("Komanda prima samo jedan parametar(broj)")
        else:
            try:
                if int(commandList[1]) not in range(1, 100):
                    raise nijeOdjereneVrednosti
                elif raisedErrVal == 1:
                    pass
                else:
                    prvArg = int(commandList[1]) 
                    listaObavTermFunc("Obavestenja", prvArg, viber_request.sender.id)
            except nijeOdjereneVrednosti:
                sendMsgFunc("Komanda prima samo jedan broj od 1 do 100")
            except ValueError:
                sendMsgFunc("Broj(parametar) ne sme da sadrzi slova, znakove")
                raisedErrVal = 1
    
    def obavestiFunc():
        pass
    def zakaziFunc():
        pass

    if isinstance(viber_request, ViberMessageRequest):
        if isCommand(viber_request.message) == False:
            sendMsgFunc("Pogresna komanda, za listu komandi ukucajte !komande")
            sendMsgFunc("ಠಿ_ಠ")            
        else:
            """
            Za pajton 3.10+ dodjaj
            match x:
                case 'a':
                    return 1
                case 'b':
                    return 2
                case _:        
                    return 0   # 0 is the default case if x is not found
            """
            # Lose, ali radi :| 
            commandList = decodeCommand(viber_request.message)
            if commandList[0] == "!about":
                aboutFunc()            
            elif commandList[0] == "!komande":
                komandeFunc()            
            elif commandList[0] == "!listaObavestenja":
                listaObavFunc()
            elif commandList[0] == "!listaTermina":
                listaTermFunc() 
            elif commandList[0] == "!obavesti":
                obavestiFunc()                                    
            elif commandList[0] == "!zakazi":
                zakaziFunc() 

    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!")
        ])

    elif isinstance(viber_request, ViberFailedRequest):
        print("Request failed")#logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(status=200)

if __name__ == "__main__":
    #context = ('server.crt', 'server.key')
    app.run(port=1443)
