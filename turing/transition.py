#!/usr/bin/python
# -*- coding: utf-8 -*-

class TransitionTapePart(object):
    def __init__(self, current_tape_symbol, new_tape_symbol, direction):
        self.current_tape_symbol = current_tape_symbol
        self.new_tape_symbol = new_tape_symbol
        self.direction = direction

'''
@author: magsilva
'''
class Transition(object):
    '''
    Transition of Turing machine
    '''

    def __init__(self, current_state, new_state):
        self.current_state =  current_state
        self.new_state = new_state
        self.tape_data = []
       
    def add_tape_part(self, current_tape_symbol, new_tape_symbol, direction, tape_number = -1):
        tape_part = TransitionTapePart(current_tape_symbol, new_tape_symbol, direction)
        if tape_number == -1:
            self.tape_data.append(tape_part)
        else:
            try:
                self.tape_data.pop(tape_number)
            except IndexError:
                pass
            self.tape_data.insert(tape_number, tape_part)
    
    def match_state(self, state):
        """
        Check if the transition can be activated with the given state. For a trivial Turing machine,
        this method will just check if the state is the same.
        """
        if self.current_state == state:
            return True
        else:
            return False
      
    def match_tape_symbol(self, tape_symbol, tape_number = 0):
        """
        Check if the transition can be activated with the given tape symbol.
        """      
        return self.tape_data[tape_number].current_tape_symbol == tape_symbol
    
    def match(self, state, tape_symbols):
        if self.match_state(state):
            tapes_match = True
            for tapes_data in zip(self.tape_data, tape_symbols):
                tapes_match &= tapes_data[0].current_tape_symbol == tapes_data[1]
            if tapes_match:
                return True
        return False    
            
    def get_new_state(self):
        """
        Return the new state for the current transition.
        """
        return self.new_state
        
        
    def get_new_tape_symbol(self, tape_number = 0):
        """
        Return the new tape symbol for the current transition.
        """
        return self.tape_data[tape_number].new_tape_symbol
                
    def get_direction(self, tape_number = 0):
        return self.tape_data[tape_number].direction
    
    def get_new_tape_data(self):
        new_tape_data = []
        for data in self.tape_data:
            new_tape_data.append([data.new_tape_symbol, data.direction])
        return new_tape_data
    
    def __str__(self):
        result = "[" + self.current_state + ", " + self.new_state
        for tape_part in self.tape_data:
            result += ", " + tape_part.current_tape_symbol
            result += ", " + tape_part.new_tape_symbol
            result += ", " + tape_part.direction
        result += "]"
        return result
        
        
