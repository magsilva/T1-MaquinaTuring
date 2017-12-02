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

    def doTransition(self,transition):
        self.current_state = transition[1]
        tapeIndex = 1
        for tape in self.tape_list:
            tape.set_content(transition[3*(tapeIndex)])
            tape.move_head(transition[(3*tapeIndex)+1])
            tapeIndex += 1
        for final_state in self.final_states:
            if self.current_state == final_state:
                print(True)
                exit(0)
        return 0

    def step(self):
        validTransitions = []
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
                    validTransitions.append(transition)
        if len(validTransitions) >= 1:
            self.doTransition(validTransitions[0])
            return validTransitions
        return []