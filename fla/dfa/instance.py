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


from fla.dfa.transition import Transition

class Instance:
    def __init__(self, automaton, state, word, previous_configuration = None):
        self.automaton = automaton
        self.current_state = state
        self.current_word = word
        self.acceptance_status = None
        self.previous_configuration = previous_configuration

    def __is_transition_valid(self, transition):
        return transition.match(self.current_state, self.current_word[0])

    def __str__(self):
        result = "["
        result += self.current_word
        result += "]@S"
        result += self.current_state
        return result
    
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if self.current_state != other.current_state:
            return False
        if self.current_word != other.current_word:
            return False
        return True

    def is_final(self):
        return len(self.current_word) == 0 or self.acceptance_status != None

    def get_valid_transition(self):
        valid_transitions = []
        for transition in self.automaton.transitions:
            if self.__is_transition_valid(transition):
                valid_transitions.append(transition)
        return valid_transitions[0]
        
    def apply_transition(self, transition):
        if not self.__is_transition_valid(transition):
            return None
        new_instance = Instance(self.automaton, transition.new_state, self.current_word[1:], self)
        return new_instance
