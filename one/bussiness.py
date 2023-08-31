import json
from random_word import RandomWords

class Domain:

    def __init__(self):
        self.R = RandomWords()

    def do(self, count):
        word = str(count) + ': ' + self.R.get_random_word()
        return json.dumps({"message": word})

