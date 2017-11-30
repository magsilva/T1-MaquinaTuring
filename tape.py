class tape:
    def __init__(self, whitespace, tape_alphabet, content=[]):
        self.position = 0
        self.whitespace_symbol = whitespace
        self.alphabet = tape_alphabet
        self.content = content
        self.size = len(content)


    def move_head(self, movement):
        if movement == 'L':
            self.move_left()
        elif movement == 'R':
            self.move_right()

    def move_left(self):
        if self.position > 0:
            self.position -= 1
        else:
            self.content.insert(0,self.whitespace_symbol)

    def move_right(self):
        if self.position < len(self.content)-1:
            self.position += 1
        else:
            whitespace = self.whitespace_symbol
            self.content.append(whitespace)
            self.position += 1

    def get_content(self):
        return self.content[self.position]

    def set_content(self, symbol):
        self.content[self.position] = symbol 