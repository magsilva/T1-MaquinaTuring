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
        self.tape_list[0].size = len(self.tape_list[0].content)
        while self.step():
            ''' just a empty while function that executes turing machine's steps'''

    def step(self):
        for transition in self.transitions:
            if int(self.current_state) == int(transition[0]) and self.tape_list[0].get_content() == transition[2]:
               
                self.tape_list[0].set_content(transition[3])
                self.current_state = transition[1]
                self.tape_list[0].move_head(transition[4])
               
                  
                return 1
        return 0
