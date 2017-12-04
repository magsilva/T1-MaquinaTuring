from tape import tape

class instance:

    """A class to represent a turing machine."""
    def __init__(self,first_state,final_states, tape_list=[]):
        self.tape_list = tape_list
        self.current_state = first_state
        self.final_states = final_states
        
    '''
        @param: transicao a ser executada pela instancia
    '''
    def doTransition(self,transition):
        self.current_state = transition[1]
        # usado para acessar o simbolo da transicao para aquela fita
        tapeIndex = 1

        # executa a transicao para todas as fitas da instancia
        for tape in self.tape_list:
            # modifica o conteudo da posicao atual da fita
            tape.set_content(transition[3*(tapeIndex)])
            # move a cabeca da fita 
            tape.move_head(transition[(3*tapeIndex)+1])
            tapeIndex += 1

        # Verifica se o estado atual esta na lista de estados finais
        for final_state in self.final_states:
            # Se o estado atual eh igual ao estado final
            if self.current_state == final_state:
            # termino da execucao da turing machine
                print(True)
                exit(0)
        return 0

    '''
        Verifica as transicoes validas para a instancia da maquina de turing
    '''
    def step(self,transitions):
        validTransitions = []
        for transition in transitions:
            # Checa se o estado atual da instancia  eh igual ao estado de partida da transicao
            if int(self.current_state) == int(transition[0]): 
                #contador de transicoes validas de fitas que aceitam a transicao
                validTapeTransitions = 0
                # usado para acessar o simbolo da transicao para aquela fita
                tapeIndex = 1
                # itero sobre a lista de fitas da instancia
                for tape in self.tape_list: 
                    # se o conteudo da transicao eh igual ao conteudo atual da fita, conta-se uma fita valida
                    if tape.get_content() == transition[(3*tapeIndex)-1]:
                        validTapeTransitions += 1
                    # caso contrario, pare a iteracao sobre a lista de fitas (tem que ser valido para todas as fitas)
                    else:
                        break
                    tapeIndex += 1

                # checa se o numero de fitas que aceitam a transicao seja igual a quantidade de fitas
                if validTapeTransitions == len(self.tape_list):
                # eh adicionado a lista de transicoes validas
                    validTransitions.append(transition)

        return validTransitions
