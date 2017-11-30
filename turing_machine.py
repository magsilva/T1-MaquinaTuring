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

    def move_head(self, tape_number, movement):
        if movement == -1:
            self.tape_list[tape_number].move_left()
        elif movement == 1:
            self.tape_list[tape_number].move_right()

    def run(self):
        while self.step():
            print("")

    def step(self):
        for transition in self.transitions:
            print("resultado de tape_list")
            print(self.tape_list[0].content)
            head = int(self.tape_list[0].position)
            print(self.tape_list[0].content)
            print(transition[2])
            print("head = " + str(head))
            if int(self.current_state) == int(transition[0]) and self.tape_list[0].content[head] == transition[2]:
                self.current_state = transition[1]
                print("maoi")
                print(transition[3])
                self.tape_list[0].content[head] = transition[3]
                if transition[4] == 'L':
                    self.tape_list[0].move_left()
                elif transition[4] == 'R':
                    self.tape_list[0].move_right()
                return 1
        return 0
