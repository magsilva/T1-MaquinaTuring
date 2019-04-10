#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy
from transition import Transition

''' @mod instance: módulo que representa uma instância'''
class Instance:

    """@const: construtor do módulo instance que representa uma instância"""
    def __init__(self, state, tapes = [], previous_configuration = None):
        self.current_state = state
        self.tapes = copy.deepcopy(tapes)
        self.previous_configuration = previous_configuration
        self.acceptance_status = None
        
    '''
        @func doTransision: realiza uma transição
        @param transition: transição a ser executada pela instância
    '''
    def apply_transition(self, transition):
        if self.acceptance_status != None:
            # raise RuntimeError("Cannot apply transition")
            return self
        
        if not self.is_transition_valid(transition):
            return None
        
        new_instance = Instance(transition.get_new_state(), self.tapes, self)
        for tape in zip(new_instance.tapes, transition.get_new_tape_data()):
            tape[0].set_content(tape[1][0])
            tape[0].move_head(tape[1][1])
        return new_instance

    def is_transition_valid(self, transition):
        current_tape_symbols = []
        for tape in self.tapes:
            current_tape_symbols.append(tape.get_content())
        if transition.match(self.current_state, current_tape_symbols):
            return True
        else:
            return False

    '''
        @func step: Verifica as transições válidas para a instância da máquina de turing
    '''
    def get_valid_transitions(self, transitions):
        valid_transitions = []
        for transition in transitions:
            if self.is_transition_valid(transition):
                valid_transitions.append(transition)
        return valid_transitions

    def __str__(self):
        result = "["
        for tape in self.tapes:
            result += str(tape)
            result += ","
        result += "]@S"
        result += self.current_state
        return result
    
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        
        if self.current_state != other.current_state:
            return False
        
        if self.tapes != other.tapes:
            return False
