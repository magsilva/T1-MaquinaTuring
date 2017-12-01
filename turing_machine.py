from tape import tape

class turing_machine:

    """A class to represent a turing machine."""
    def __init__(self, state_list, final_state_list, first_state, transition_list, whitespace_symbol, tape_list=[]):
        self.tape_list = tape_list
        self.states = state_list
        self.initial_state = first_state
        self.final_states = final_state_list
        self.transitions = transition_list
        self.whitespace = whitespace_symbol
        self.current_state = first_state


    def run(self):
        for tape in self.tape_list:
            tape.size = len(tape.content)
        while self.step():
            ''' just a empty while function that executes turing machine's steps'''

    def step(self):
        for transition in self.transitions:
            if int(self.current_state) == int(transition[0]):
                validTapeTransitions = 0
                tapeIndex = 1

                for tape in self.tape_list:
                    if tape.get_content() == transition[(3*tapeIndex)-1]:
                        validTapeTransitions += 1
                    else:
                        break
                    tapeIndex +=1

                if validTapeTransitions == len(self.tape_list):
                    self.current_state = transition[1]
                    tapeIndex = 1
                    for tape in self.tape_list:
                        tape.set_content(transition[3*(tapeIndex)])
                        tape.move_head(transition[(3*tapeIndex)+1])
                        tapeIndex += 1
                    return 1
        return 0
