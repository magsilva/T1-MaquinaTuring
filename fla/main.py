#!/usr/bin/python
# -*- coding: utf-8 -*-

from fla.flarunner import FlaRunner
from fla.jflap2flarunner import Jflap2FlaRunner

import sys
import string
import logging
import os

if __name__ == "__main__":
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
	inputfile = sys.argv[1]
	fileextension = os.path.splitext(inputfile)
	if fileextension == '.jff':
		converter = Jflap2FlaRunner()
		lines_cmd = string.splitlines(converter.convert(inputfile))
	else:
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

	if result == True:
		print "Accept"
		sys.exit(0)
	elif result == False:
		print "Reject"
		sys.exit(1)
	else
		print "No reasonable result (did not finish computation?)"
		sys.exit(-1)


