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
import os
import sys
import string

from fla.flarunner import FlaRunner
from fla.jflap2flarunner import Jflap2FlaRunner


if __name__ == "__main__":
	logging.basicConfig(format='%(message)s', level=logging.DEBUG)
	inputfile = sys.argv[1]
	fileextension = os.path.splitext(os.path.split(inputfile)[1])[1]
	if fileextension == '.jff':
		logging.debug("Loading file {} (Jflap format) and converting it to text-based format".format(inputfile))
		converter = Jflap2FlaRunner()
		lines_cmd = converter.convert(inputfile)
		lines_cmd = lines_cmd.splitlines()
	else:
		logging.debug("Loading file {} (text-based format".format(inputfile))
		fp = open(inputfile, "r") #abre em modo de leitura o arquivo com a definicao da maquina de turing
		lines_cmd = fp.readlines()

	lines = []
	for line in lines_cmd:
		lines.append(line.rstrip())
	automaton_type = lines[0].replace(' ', '')
	lines = lines[1:]
	flarunner = FlaRunner()
	result = None
	if automaton_type == "TM":
		result = flarunner.turing_machine(lines, sys.argv[2:])
	elif automaton_type == "DFA":
		result = flarunner.dfa(lines, sys.argv[2:])
	elif automaton_type == "NDFA":
		result = flarunner.ndfa(lines, sys.argv[2:])
	elif automaton_type == "PDA":
		result = flarunner.pda(lines, sys.argv[2:])

	logging.debug("Processed program as a {}".format(automaton_type))
	if result == True:
		logging.debug("Computation finished with acceptance of {}".format(", ".join(sys.argv[2:])))
		sys.exit(0)
	elif result == False:
		logging.debug("Computation finished with rejection of {}".format(", ".join(sys.argv[2:])))
		sys.exit(1)
	else:
		logging.debug("Computation did not finished for {}")
		sys.exit(-1)


