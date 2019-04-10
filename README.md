[![Build Status](https://travis-ci.org/magsilva/T1-MaquinaTuring.svg?branch=master)](https://travis-ci.org/magsilva/T1-MaquinaTuring)

Este programa simula a execução de uma máquina de Turing (MT). Por enquanto, são suportadas as seguintes características:
* Determinismo e não determinismo
* Uma ou mais fitas
* Fita infinita para ambos os lados
* Movimento da cabeça para a esquerda (L), a direita (R) ou permanecer na posição atual (S).

A execução do programa é por linha de comando. São necessários no mínimo parâmetros: o nome de um arquivo texto, contendo a descrição da MT, e os conteúdos das fitas. O primeiro parâmetro sempre é o nome do arquivo e os demais parâmetros são os conteúdos das fitas.

Para cada entrada, ao concluir ou interromper a computação da simulação, o programa informa a configuração instantânea da máquina de Turing e, se concluída a computação, informada a decisão.

O arquivo texto para descrição da MT pode ser gerado automaticamente a partir da conversão de uma MT descrita com o JFLAP (arquivo no formato .jff), utilizando o programa jflap-turing2utfpr.py. Nesse caso, o primeiro parâmetro é o nome do arquivo no formato JFLAP e o segundo parâmetro é o nome do arquivo texto a ser gerado. O formato do arquivo texto suportado pela ferramenta é o seguinte:

* Linha 1: alfabeto de entrada
* Linha 2: alfabeto da fita
* Linha 3: simbolo que representa o espaço em branco (padrão: B)
* Lista 4: conjunto de estados
* Linha 5: estado inicial
* Linha 6: conjunto de estados finais
* Linha 7: quantidade de fitas
* Linhas 8 em diante: transições, uma por linha, cada qual no seguinte formato: estado atual, estado destino e, para cada fita, o simbolo da posição atual da fita, novo símbolo da posição atual da fita e a indicação da movimentação da cabeça para a fita (L para esquerda da posição atual, R para direita da posição atual e S para manter a posição atual).
