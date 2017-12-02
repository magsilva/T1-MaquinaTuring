from instance  import instance
import copy

class turing_machine:
    def __init__(self,states, final_states, initial_state, transitions, whitespace, tape_list):
        self.instances = [instance(initial_state, final_states, tape_list)]
        self.final_states = final_states
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.whitespace = whitespace

    def run(self):
        for tape in self.instances[0].tape_list:
            tape.size = len(tape.content)

        while self.instances:
            instances = self.instances
            for instance in instances:
                stepResult = instance.step(self.transitions)   
                if len(stepResult) == 0:
                    self.instances.remove(instance)
                elif len(stepResult) >= 1:
                    instance.doTransition(stepResult[0])
                    del stepResult[0]
                    for result in stepResult:
                        self.instances.append(copy.deepcopy(instance)) 
                        self.instances[-1].doTransition(result)
        print(False)