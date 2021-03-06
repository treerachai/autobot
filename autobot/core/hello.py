import autobot


class HelloPlugin(autobot.Plugin):
    '''
    A simple example plugin to demonstrate multiple matchers and storage
    '''

    def __init__(self, factory):
        super().__init__(factory)
        if 'hello_replies' not in self.storage or (
                not isinstance(self.storage['hello_replies'], set)):
            self.storage['hello_replies'] = set()

    @autobot.respond_to('^(H|h)i')
    @autobot.respond_to('^(H|h)i,? ({mention_name})')
    @autobot.respond_to('^(H|h)ello,? ({mention_name})')
    def hi(self, message):
        message.reply('Hi, %s!', message.author)
        self.storage['hello_replies'].add(message.author)

    @autobot.eavesdrop(always=True)
    def listen(self, message):
        pass

    @autobot.scheduled(minutes='*/1')
    def be_obnoxious(self):
        self.default_room.say('Echo on a clock!')
