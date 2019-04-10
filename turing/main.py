#!/usr/bin/python
# -*- coding: utf-8 -*-

from turing_machine import TuringMachine # representa a turing machine
from tape import Tape # representa uma unidade de fita
from transition import Transition
import sys


if __name__ == "__main__":
    fp = open(sys.argv[1], "r") #abre em modo de leitura o arquivo com a definicao da maquina de turing
    lines_cmd = fp.readlines()
    lines = []
    for line in lines_cmd:
        lines.append(line.rstrip())
    number_of_lines  = len(lines)
    '''valores de entrada que representam a turing machine de entrada'''
    input_alphabet   = lines[0].split()
    tape_alphabet    = lines[1]
    whitespace       = lines[2]
    states           = lines[3].split()
    initial_state    = lines[4]
    final_states     = lines[5].split()
    number_of_tapes  = lines[6]
    transitions_description  = []
    for i in range(7, number_of_lines):
        transitions_description.append(lines[i])

    transitions = []
    for description in transitions_description:
        splited_description = description.split()
        transition = Transition(splited_description[0], splited_description[1])
        for tape_part in zip(*(splited_description[2:][i::3] for i in range(3))):
            transition.add_tape_part(tape_part[0], tape_part[1], tape_part[2])
        transitions.append(transition)
    
    tapes = []
    for i in range(2, 2 + int(number_of_tapes)):
        tapes.append(Tape(whitespace, tape_alphabet, list(sys.argv[i])))
    
    '''Instancia a turing machine'''
    tm = TuringMachine(states, initial_state, final_states, whitespace, transitions, tapes)

    '''executa a turing machine'''
    result = tm.run()
    if result == True:
        if tm.get_decision() == "Accept":
            print("Aceitou")
        else:
            print("Rejeitou")
    else:
        print("Never halted")

