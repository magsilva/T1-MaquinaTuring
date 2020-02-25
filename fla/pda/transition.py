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


class Transition(object):
    def __init__(self, current_state, current_word_symbol, current_stack_symbols, new_state, new_stack_symbols):
        self.current_state =  current_state
        self.current_word_symbol = current_word_symbol
        self.current_stack_symbols = current_stack_symbols
        self.new_state = new_state
        self.new_stack_symbols = new_stack_symbols
                   
    def __str__(self):
        result = "["
        result += self.current_state + ", "
        if not self.has_empty_word_symbol():
            result += self.current_word_symbol
        result += ", "
        if not self.has_empty_current_stack_symbols():
            result += self.current_stack_symbols
        result += " -> "
        result += self.new_state + ", "
        if not self.has_empty_new_stack_symbols():
            result += self.new_stack_symbols
        result += "]"
        return result
    
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if self.current_state != other.current_state:
            return False
        if self.current_word_symbol != other.current_word_symbol:
            return False
        if self.current_stack_symbols != other.current_stack_symbols:
            return False
        if self.new_state != other.new_state:
            return False
        if self.mew_stack_symbols != other.new_stack_symbols:
            return False
        return True
    
    def has_empty_word_symbol(self):
        return self.current_word_symbol == None

    def has_empty_current_stack_symbols(self):
        return self.current_stack_symbols == None

    def has_empty_new_stack_symbols(self):
        return self.new_stack_symbols == None
      
    def match(self, state, word_symbol, stack):
        if self.current_state == state:
            if self.has_empty_word_symbol() or self.current_word_symbol == word_symbol:
                if self.has_empty_current_stack_symbols() or self.current_stack_symbols[::-1] == "".join(stack[-len(self.current_stack_symbols):]):
                    return True
        return False
