# -*- coding: utf-8 -*-

# Copyright (c) 2019 Marco Aurélio Graciotto Silva
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from copy import deepcopy


class Tape:
    def __init__(self, whitespace, tape_alphabet, content = None):
        self.position = 0 # posicao atual da fita
        self.whitespace_symbol = whitespace
        self.alphabet = tape_alphabet
        if content == None:
            self.content = []
        else:
            self.content = content

    def move_head(self, movement):
        if movement == 'L': 
            self.move_left()
        elif movement == 'R':
            self.move_right()
        elif movement == 'S':
            pass
        else:
            raise ValueError("Invalid direction")

    def move_left(self):
        if self.position > 0: # se existir espaco pra esquerda, vai para a esquerda
            self.position -= 1
        else: # se nao, coloca um branco no comeco da fita (e mantém a posição 0)
            self.content.insert(0,self.whitespace_symbol)

    def move_right(self): 
        if self.position < len(self.content)-1: # se tiver posicao para a direita, vai para a direita
            self.position += 1
        else: # se nao, coloca um espaco em branco na fita e vai para a direita
            whitespace = self.whitespace_symbol
            self.content.append(whitespace)
            self.position += 1

    def get_content(self):
        if len(self.content) == 0:
            return self.whitespace_symbol
        else:
            return self.content[self.position]

    def set_content(self, symbol):
        if len(self.content) == 0:
            self.content.append(symbol)
        else:
            self.content[self.position] = symbol 

    def replace_content(self, new_content):
        self.content = deepcopy(new_content)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.content == other.content

    def __str__(self):
        result = "(";
        result += str(self.content)
        result += ")@"
        result += str(self.position)
        return result
