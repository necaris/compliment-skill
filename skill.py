from mycroft import MycroftSkill, intent_file_handler


class Compliment(MycroftSkill):
    def __init__(self):
        super().__init__()

    @intent_file_handler("compliment.intent")
    def handle_compliment(self, name: str = None):
        if name:
            self.speak_dialog("compliment.named", {"name": name})
        else:
            self.speak_dialog("compliment")
