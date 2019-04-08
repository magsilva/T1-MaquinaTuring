#!/usr/bin/python
# -*- coding: utf-8 -*-

from instance  import Instance
import copy
from __builtin__ import True

''' @mod turing_machine: módulo que representa uma turing machine '''
class TuringMachine:
    '''
        @const: construtor do módulo (classe) turing machine
        @param states: lista de estados
        @param final_states: lista de estados de aceitacao
        @param initial_state: estado inicial
        @param transitions: lista de transicoes
        @param whitespace: simbolo que representa o branco
        @param tape_list: lista de fitas da turing machine
    '''
    def __init__(self, states, initial_state, final_states, whitespace, transitions, tapes):
        '''
            @var self.instances: é uma lista de instâncias de turing machine, que é iniciada com apenas 
            uma instância que usa os estados de aceitação e a lista de fitas da entrada
        '''
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.whitespace = whitespace
        self.current_configurations = [Instance(self.initial_state, tapes)]
 

    def restart(self, tapes):
        self.current_configurations = [Instance(self.initial_state, tapes)]


    def verify_status(self, configuration):
        # Verifica aceitacao por estado final
        if configuration.acceptance_status != None:
            configuration.acceptance_status
        for final_state in self.final_states:
            if configuration.current_state == final_state:
                configuration.acceptance_status = True
                return True
        valid_transitions = configuration.get_valid_transitions(self.transitions)
        if len(valid_transitions) == 0:
            configuration.acceptance_status = False
            return False


    def is_halted(self):
        if len(self.current_configurations) == 0:
            return True
        
        for configuration in self.current_configurations:
            if configuration.acceptance_status != None:
                return True
        
        return False

            
    def get_decision(self):
        for configuration in self.current_configurations:
            if configuration.acceptance_status == True:
                return "Accept"
        
        if len(self.current_configurations) == 0:
            return "Reject"
        
        return "Undefined"
        
            
    '''
        @func run: Executa toda a computação necessária para máquina de turing ser processada
    '''
    def step_forward(self):
        configurations_current_step = copy.copy(self.current_configurations)
        self.current_configurations = []
        for configuration in configurations_current_step:
            valid_transitions = configuration.get_valid_transitions(self.transitions)
            for transition in valid_transitions:
                new_configuration = configuration.apply_transition(transition)
                self.current_configurations.append(new_configuration)
#                print(str(configuration) + " -> " + str(new_configuration))
            
    '''
        @func run: Executa toda a computação necessária para máquina de turing ser processada
    '''
    def run(self):
        halted_configurations = []
        while self.current_configurations:
            self.step_forward()
            for configuration in self.current_configurations:
                self.verify_status(configuration)
                if configuration.acceptance_status != None:
                    halted_configurations.append(configuration)
#                print(str(configuration) + " (" + str(configuration.acceptance_status) + ")")
        self.current_configurations = halted_configurations
        if self.is_halted():
            return True
        