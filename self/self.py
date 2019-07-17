import itchat

from auth import auth


class Self(object):

    def __init__(self):
        auth.login_self()

    def run(self):
        itchat.run()