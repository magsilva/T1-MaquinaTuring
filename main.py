from turing_machine import turing_machine
import sys
from tape import tape


if __name__ == "__main__":
    fp = open(sys.argv[1], "r")
    lines = fp.readlines()
    input_alphabet = lines[0].split()
    print("input_alphabet")
    print(input_alphabet)
    whitespace = lines[2]
    states = lines[3].split()
    print("states")
    print(states)
    initial_state = lines[4]
    print("initial_state")
    print(initial_state)
    final_states = lines[5].split()
    print("final_state")
    print(final_states)
    number_of_tapes = lines[6]
    print("number_of_tapes")
    print(number_of_tapes)
    number_of_lines = len(lines)
    print("number_of_lines")
    print(number_of_lines)
    transitions = []
    for i in range(7, number_of_lines):
        print(lines[i].split())
        transitions.append(lines[i].split())

    number_of_args = 2 + int(number_of_tapes)
    tape_list = tape(['a'], 'B')
    for i in range(2, number_of_args):
        tape_list.content.append(sys.argv[i].split())

    tm = turing_machine(states, final_states, initial_state, transitions, whitespace, [tape_list])

    tm.run()
    print(tm.tape_list[0].content)
