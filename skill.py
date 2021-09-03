from mycroft import MycroftSkill, intent_file_handler
from mycroft.messagebus import Message


class Compliment(MycroftSkill):
    def __init__(self):
        super().__init__()

    @intent_file_handler("compliment.intent")
    def handle_compliment(self, message: Message):
        if message.data.get("name"):
            self.speak_dialog("compliment.named", message.data)
        else:
            self.speak_dialog("compliment")
