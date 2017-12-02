from non_deterministic_turing_machine import non_deterministic_turing_machine
import sys
from tape import tape


if __name__ == "__main__":
    fp = open(sys.argv[1], "r")
    lines_cmd = fp.readlines()
    lines = []
    for line in lines_cmd:
        lines.append(line.replace('\n',''))

    input_alphabet = lines[0].split()
    tape_alphabet = lines[1]
    whitespace = lines[2].replace('\n','')
    states = lines[3].split()
    initial_state = lines[4]
    final_states = lines[5].split()
    number_of_tapes = lines[6]
    number_of_lines = len(lines)
    transitions = []
    for i in range(7, number_of_lines):
        transitions.append(lines[i].split())

    number_of_args = 2 + int(number_of_tapes)
    tape_list = []
    temp = []
    for i in range(2, number_of_args):
        if len(sys.argv) >= i+1:
            tape_list.append(tape(whitespace, tape_alphabet, list(sys.argv[i])))
        else:
            tape_list.append(tape(whitespace,tape_alphabet,[whitespace]))

    tm = non_deterministic_turing_machine(states, final_states, initial_state, transitions, whitespace, tape_list)

    tm.run()
    print(False)