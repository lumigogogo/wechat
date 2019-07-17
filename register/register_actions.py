import itchat
from itchat.content import TEXT, MAP, NOTE, CARD, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO, FRIENDS
import requests

import config
import json


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    text = msg.text
    response = requests.get(config.to_chat_with_machine + text)

    if response.status_code == 200:
        text = json.loads(response.content).get('content')
    msg.user.send('%s: %s' % ('[auto reply]', text))


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    text = msg.text
    response = requests.get(config.to_chat_with_machine + text)

    if response.status_code == 200:
        text = json.loads(response.content).get('content')

    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, text))
