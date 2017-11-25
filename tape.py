class tape:
    def __init__(self, whitespace, tape_alphabet, content=[]):
        self.position = 0
        self.whitespace_simbol = [whitespace]
        self.alphabet = tape_alphabet
        self.content = content

    def move_left(self):
        if self.position > 0:
            self.position -= 1
        else:
            self.content = self.whitespace_simbol + self.content

    def move_right(self):
        if self.position < len(self.content):
            self.position += 1
        else:
            whitespace = self.whitespace_simbol
            self.content.append(whitespace)
            self.position += 1
