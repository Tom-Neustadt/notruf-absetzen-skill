from mycroft import MycroftSkill, intent_file_handler


class NotrufAbsetzen(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('absetzen.notruf.intent')
    def handle_absetzen_notruf(self, message):
        self.speak_dialog('absetzen.notruf')


def create_skill():
    return NotrufAbsetzen()

