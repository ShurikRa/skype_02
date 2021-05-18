# -*- coding: utf-8 -*-

import secrets 
import os
import time
from skpy import Skype, SkypeChat, SkypeEventLoop, SkypeNewMessageEvent

#CONSTANTS
USERNAME = 'alexandr.dobruy.@gmail.com'
PASSWORD = 'pas'

GOOD_PPL = ['live:5e9e2404459d2fe1']
BAD_PPL = ['lunarseer']

RESP01 = ['немного занят', 'освобожусь наберу', 'очень занят', 'отстань', 'ну опять', 'еслт срочно набери', 'опять', 'не надо', 'я серезно']

#print(secrets.choice(RESP01))

class SkypeResponder(SkypeEventLoop):

    def __init__(self):
        super(SkypeResponder, self).__init__(USERNAME, PASSWORD)
        print('Listening...')

    def onEvent(self, event):
        try:
            if isinstance(event, SkypeNewMessageEvent):
                content = event.msg.__dict__['content']
                username = event.msg.user.id
                responce = ''
                if username in GOOD_PPL:
                    responce = secrets.choice(RESP01)
                    #responce = "Привет, {} УРААААААА!".format(username)
                    #responce = responce(.encode('utf-8', 'ignore'))
                    #print(type(responce), responce)
                    # responce = responce.encode('ascii', errors='xmlcharrefreplace')
                    # responce = responce.decode('utf-8')

                elif username in BAD_PPL:
                    responce = secrets.choice(RESP01)
                    #responce = "OMG!!! {} Go to hell".format(username)

                if responce:
                    event.msg.chat.sendMsg(responce)
                    print(username, ' sent: {} recieved: {}'.format(
                        content,
                        responce))
                    
                # , not event.msg.userId == self.userId])
            #   and "ping" in event.msg.content:
            #     event.msg.chat.sendMsg("Pong!")
        except Exception as error:
            print(error)

skypesession = Skype(USERNAME, PASSWORD)


if __name__ != 'main':
    os.system('cls')
    responder = SkypeResponder()
    responder.loop()