class tape:
    def __init__(self, whitespace, tape_alphabet, content=[]):
        self.position = 0
        self.whitespace_symbol = [whitespace]
        self.alphabet = tape_alphabet
        self.content = content
        self.size = len(content)

    def move_left(self):
        if self.position > 0:
            self.position -= 1
        else:
            self.content.insert(0,self.whitespace_symbol)

    def move_right(self):
        if self.position < len(self.content):
            self.position += 1
        else:
            whitespace = self.whitespace_symbol
            self.content.append(whitespace)
            self.position += 1
