from mycroft import MycroftSkill, intent_file_handler


class Compliment(MycroftSkill):
    def __init__(self):
        super().__init__()

    @intent_file_handler("compliment.intent")
    def handle_compliment(self, message: dict = None):
        if message and message.get("name"):
            self.speak_dialog("compliment.named", message)
        else:
            self.speak_dialog("compliment")
