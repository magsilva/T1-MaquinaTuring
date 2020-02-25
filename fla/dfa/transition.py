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
    def __init__(self, current_state, current_symbol, new_state):
        self.current_state =  current_state
        self.current_symbol = current_symbol
        self.new_state = new_state
                   
    def __str__(self):
        result = "["
        result += self.current_state + ", " + self.current_symbol + " -> "
        result += self.new_state
        result += "]"
        return result
    
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if self.current_state != other.current_state:
            return False
        if self.current_symbol != other.current_symbol:
            return False
        if self.new_state != other.new_state:
            return False
        return True
    
    def match_state(self, state):
        return self.current_state == state
      
    def match_symbol(self, symbol):
        return self.current_symbol == symbol
      
    def match(self, state, symbol):
        return self.match_state(state) and self.match_symbol(symbol)
