from tape import tape


''' @mod instance: módulo que representa uma instância'''
class instance:

    """@const: construtor do módulo instance que representa uma instância"""
    def __init__(self,first_state,final_states, tape_list=[]):
        self.tape_list = tape_list
        self.current_state = first_state
        self.final_states = final_states
        
    '''
        @func doTransision: realiza uma transição
        @param transition: transição a ser executada pela instância
    '''
    def doTransition(self,transition):
        self.current_state = transition[1]
        # usado para acessar o símbolo da transição para aquela fita
        tapeIndex = 1

        # executa a transição para todas as fitas da instância
        for tape in self.tape_list:
            # modifica o conteúdo da posição atual da fita
            tape.set_content(transition[3*(tapeIndex)])
            # move a cabeça da fita 
            tape.move_head(transition[(3*tapeIndex)+1])
            tapeIndex += 1

        # Verifica se o estado atual está na lista de estados finais
        for final_state in self.final_states:
            # Se o estado atual é igual ao estado final
            if self.current_state == final_state:
            # término da execucao da turing machine
                print(True)
                exit(0)
        return 0

    '''
        @func step: Verifica as transições válidas para a instância da máquina de turing
    '''
    def step(self,transitions):
        validTransitions = []
        for transition in transitions:
            # Verifica se o estado atual da instância  é igual ao estado de partida da transição
            if int(self.current_state) == int(transition[0]): 
                #contador de transições válidas de fitas que aceitam a transição
                validTapeTransitions = 0
                # usado para acessar o símbolo da transicao para aquela fita
                tapeIndex = 1
                # itera sobre a lista de fitas da instância
                for tape in self.tape_list: 
                    # se o conteudo da transicao é igual ao conteúdo atual da fita, conta-se uma fita válida
                    if tape.get_content() == transition[(3*tapeIndex)-1]:
                        validTapeTransitions += 1
                    # caso contrário, pare a iteração sobre a lista de fitas (tem que ser válido para todas as fitas)
                    else:
                        break
                    tapeIndex += 1

                # verifica se o número de fitas que aceitam a transicao seja igual a quantidade de fitas
                if validTapeTransitions == len(self.tape_list):
                # é adicionado a lista de transições válidas
                    validTransitions.append(transition)

        return validTransitions
