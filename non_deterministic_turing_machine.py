from turing_machine import turing_machine
import copy

class non_deterministic_turing_machine:
    def __init__(self,states, final_states, initial_state, transitions, whitespace, tape_list):
        self.instances = [turing_machine(states, final_states, initial_state, transitions, whitespace, tape_list)]
        self.final_states = final_states

    def run(self):
        for tape in self.instances[0].tape_list:
            tape.size = len(tape.content)

        while len(self.instances):
            didStep = 0
            stepAmount = 0
            instances = self.instances
            for instance in instances:
                stepResult = instance.step()   
                if len(stepResult) == 0:
                    self.instances.remove(instance)
                elif len(stepResult) >= 2:
                    del stepResult[0]
                    for result in stepResult:
                        self.instances.append(copy.deepcopy(instance)) 
                        self.instances[-1].doTransition(result)