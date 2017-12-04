from instance  import instance
import copy
''' classe que representa uma turing machine '''
class turing_machine:
    def __init__(self,states, final_states, initial_state, transitions, whitespace, tape_list):
        '''
            self.instances: é uma lista de instancias de turing machine, que é iniciada com apenas 
            uma instancia que usa os estados de aceitacao e a lista de fitas da entrada
        '''
        self.instances = [instance(initial_state, final_states, tape_list)]
        self.final_states = final_states
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.whitespace = whitespace
    
    
    '''
        Executa toda a computacao necessaria para turing machine ser processada
    '''
    def run(self):
        # inicia o tamanho das fitas da primeira instancia de acordo com seus conteudos
        for tape in self.instances[0].tape_list:
            tape.size = len(tape.content)

        '''
            Laco de repeticao que executa enquanto existir instancias de maquina de turing
        '''
        while self.instances:
            instances = self.instances # para nao iterar em uma lista que tem possibilidade de nao modificacao
            # iterar sobre a lista de instancias
            for instance in instances:
                # stepResult recebe a lista de transicoes validas
                stepResult = instance.step(self.transitions)   
                # verifica se nao tem transicao valida
                if len(stepResult) == 0:
                    self.instances.remove(instance)
                else:
                # realiza a primeira transicao na instancia que esta iterando
                    instance.doTransition(stepResult[0])
                # deleta a transicao executada
                    del stepResult[0]
                # realiza copias da instancia e executa as transicoes restantes nelas    
                    for result in stepResult:
                        self.instances.append(copy.deepcopy(instance)) 
                        self.instances[-1].doTransition(result)
        print(False)