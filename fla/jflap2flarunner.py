#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Copyright (c) 2019 Marco Aurélio Graciotto Silva
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import sys
from xml.etree import ElementTree

from fla.jflap_fa_converter import JflapFaConverter
from fla.jflap_pda_converter import JflapPdaConverter
from fla.jflap_turing_converter import JflapTmConverter


class Jflap2FlaRunner(object):

	def convert(self, inputFile, outputFile = None):
		xmldoc = ElementTree.parse(inputFile)
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
		else:
			raise Exception('Could not identify automaton type {}.'.format(automata_type))
		txt = converter.convert(inputFile, outputFile)
		return txt
		

if __name__ == "__main__":
	logging.basicConfig(format='%(message)s', level=logging.DEBUG)
	if len(sys.argv) != 3:
		print("Parametros insuficientes. Informe o nome de arquivo de entrada e o nome do arquivo de saida")
		sys.exit(1)
	converter = Jflap2FlaRunner()
	converter.convert(sys.argv[1], sys.argv[2])
