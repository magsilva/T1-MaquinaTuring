from tape import tape

class turing_machine:

    """A class to represent a turing machine."""
    def __init__(self, state_list, final_state_list, first_state, transition_list, whitespace_symbol):
        self.tape_list = []
        self.states = state_list
        self.initial_state = first_state
        self.final_states = final_state_list
        self.transitions = transition_list
        self.whitespace = whitespace_symbol

    def move_head(self, tape_number, movement):
        if movement == -1:
            self.tape_list[tape_number].move_left()
        elif movement == 1:
            self.tape_list[tape_number].move_right()
