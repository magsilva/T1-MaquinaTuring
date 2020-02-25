#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.etree import ElementTree as ET

from fla.jflap_fa_converter import JflapFaConverter
from fla.jflap_pda_converter import JflapPdaConverter
from fla.jflap_turing_converter import JflapTmConverter


class Jflap2FlaRunner(object):

    def convert(self, inputFile, outputFile = None):
	    xmldoc = ET.parse(inputfile)
		root = xmldoc.getroot()
	    mainnode = root.find('type')
		automata_type = mainnode.text
		txt = None
		if automata_type == "fa":
			converter = JflapFaConverter()
		elif automata_type == "pda":
			converter = JflapPdaConverter()
	    elif automata_type == "turing":
			converter = JflapTmConverter()
		else
			raise Exception('Could not identify automaton type {}.'.format(automata_type)

		txt = converter.convert(inputfile)
		return txt
		

if __name__ == "__main__":
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    if len(sys.argv) != 3:
        print("Parametros insuficientes. Informe o nome de arquivo de entrada e o nome do arquivo de saida")
        sys.exit(1)
    converter = Jflap2FlaRunner()
	converter.convert(sys.argv[1], sys.argv[2])
