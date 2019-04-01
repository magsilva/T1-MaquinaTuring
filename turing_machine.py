#!/usr/bin/python
# -*- coding: utf-8 -*-

from instance  import instance
import copy
''' @mod turing_machine: módulo que representa uma turing machine '''
class turing_machine:
    '''
        @const: construtor do módulo (classe) turing machine
        @param states: lista de estados
        @param final_states: lista de estados de aceitacao
        @param initial_state: estado inicial
        @param transitions: lista de transicoes
        @param whitespace: simbolo que representa o branco
        @param tape_list: lista de fitas da turing machine
    '''
    def __init__(self,states, final_states, initial_state, transitions, whitespace, tape_list):
        '''
            @var self.instances: é uma lista de instâncias de turing machine, que é iniciada com apenas 
            uma instância que usa os estados de aceitação e a lista de fitas da entrada
        '''
        self.instances = [instance(initial_state, final_states, tape_list)]
        self.final_states = final_states
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.whitespace = whitespace
    
    
    '''
        @func run: Executa toda a computação necessária para máquina de turing ser processada
    '''
    def run(self):
        # inicia o tamanho das fitas da primeira instancia de acordo com seus conteudos
        for tape in self.instances[0].tape_list:
            tape.size = len(tape.content)

        
        # Laço de repeticao que executa enquanto existir instancias de maquina de turing
        while self.instances:
            instances = self.instances # para nao iterar em uma lista que tem possibilidade de nao modificacao

            # Realiza transicoes
            for instance in instances:
                # Verifica aceitacao por estado final
                for final_state in self.final_states:
                    # Se o estado atual é igual ao estado final
                    if instance.current_state == final_state:
                        # término da execucao da turing machine
                        return [1, instance]

                # stepResult recebe a lista de transições válidas
                stepResult = instance.step(self.transitions) 

                # verifica se não tem transição válida
                if len(stepResult) == 0:
                    self.instances.remove(instance)
                else:
                    # realiza a primeira transição na instância que esta iterando
                    instance.doTransition(stepResult[0])

                    # deleta a transição executada
                    del stepResult[0]

                    # realiza cópias da instância e executa as transições restantes nelas    
                    for result in stepResult:
                        self.instances.append(copy.deepcopy(instance)) 
                        self.instances[-1].doTransition(result)
        return [0, None]
