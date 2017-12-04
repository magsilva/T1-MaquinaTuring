from turing_machine import turing_machine # representa a turing machine
from tape import tape # representa uma unidade de fita
import sys


if __name__ == "__main__":
    fp = open(sys.argv[1], "r") #abre em modo de leitura o arquivo com a definicao da maquina de turing
    lines_cmd = fp.readlines()
    lines = []
    for line in lines_cmd:
        lines.append(line.replace('\n',''))
    number_of_lines  = len(lines)
    '''valores de entrada que representam a turing machine de entrada'''
    input_alphabet   = lines[0].split()
    tape_alphabet    = lines[1]
    whitespace       = lines[2]
    states           = lines[3].split()
    initial_state    = lines[4]
    final_states     = lines[5].split()
    number_of_tapes  = lines[6]
    transitions      = []
    
    '''laco que pegara as transicoes'''
    for i in range(7, number_of_lines):
        transitions.append(lines[i].split())

    tape_list = [] #lista de fitas
    number_of_args = 2 + int(number_of_tapes)
    '''laco de repeticao que construira a lista de fitas'''
    for i in range(2, number_of_args):
        if len(sys.argv) >= i+1: # caso tenha simbolos, ele coloca na fita
            tape_list.append(tape(whitespace, tape_alphabet, list(sys.argv[i])))
        else: # caso nao tenha, coloca simbolos que representam o branco
            tape_list.append(tape(whitespace,tape_alphabet,[whitespace]))

    '''Instancia a turing machine'''
    # @param_1: lista de estados
    # @param_2: lista de estados de aceitacao
    # @param_3: estado inicial
    # @param_4: lista de transicoes
    # @param_5: simbolo que representa o branco
    # @param_6: lista de fitas da turing machine
    
    tm = turing_machine(states, final_states, initial_state, transitions, whitespace, tape_list)

    '''executa a turing machine'''
    tm.run()