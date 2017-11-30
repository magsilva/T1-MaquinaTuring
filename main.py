from turing_machine import turing_machine
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
    tape_list = tape(whitespace, tape_alphabet, [])
    for i in range(2, number_of_args):
        tape_list.content = list(sys.argv[i])

    tm = turing_machine(states, final_states, initial_state, transitions, whitespace, [tape_list])

    tm.run()
    for state in tm.final_states:
        if tm.current_state == state:
            print(True)
            exit(0)
    print(False)