# -*- coding: utf-8 -*-
#
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

import csv
import logging
import io
import sys
from xml.etree import ElementTree


class Transition(object):
	def __init__(self):
		self.currentState = None
		self.currentInputSymbol = None
		self.newState = None

	def __lt__(self, other):
		if self.currentState != other.currentState:
			return self.currentState < other.currentState
		if self.currentInputSymbol != other.currentInputSymbol:
			return self.currentInputSymbol < other.currentInputSymbol
		return self.newState < other.newState 


class JflapFaConverter(object):
	def __init__(self):
		self.state_id_to_name = {}
		self.alphabet = set()
		self.states = set()
		self.initialStates = set()
		self.acceptanceStates = set()
		self.transitions = []
		self.blankSymbol = 'B'

	def convert(self, inputFile, outputFile = None, blankSymbol = 'E', alphabet = None):
		self.blankSymbol = blankSymbol
		if alphabet is not None:
			self.alphabet = alphabet

		xmldoc = ElementTree.parse(inputFile)
		root = xmldoc.getroot()
		tm = root.find('automaton')
		if tm == None:  # Old JFLAP format
			tm = root

		for s in tm.findall('state'):
			state_id = s.attrib['id']
			if 'name' in s.attrib:
				state_name = s.attrib['name']
			else:
				state_name = str(state_id)
			self.state_id_to_name[state_id] = state_name
			self.states.add(state_name)
			if s.find('initial') is not None:
				self.initialStates.add(state_name)
			if s.find('final') is not None:
				self.acceptanceStates.add(state_name)

		for t in tm.findall('transition'):
			transition = Transition()
			self.transitions.append(transition)
			transition.currentState = self.state_id_to_name[t.find('from').text]
			transition.newState = self.state_id_to_name[t.find('to').text]
			if t.find('read').text is not None:
				transition.currentInputSymbol = t.find('read').text
				self.alphabet.add(transition.currentInputSymbol)
			else:
				transition.currentInputSymbol = blankSymbol
			self.transitions.sort()
		
		if self.blankSymbol in self.alphabet:
			for c in ascii_uppercase:
				if c not in self.alphabet:
					self.blankSymbol = c
				break
			print("Simbolo originalmente escolhido para representar branco foi utilizado para outros fins no automato. Simbolo para branco foi substituido por " + self.blankSymbol + ".")

		csvcontent = ""
		if outputFile == None:
			csvfile = io.StringIO()
		else:
			csvfile = open(outputFile, 'w')
		with csvfile:
			writer = csv.writer(csvfile, delimiter = ' ', escapechar = None, quotechar = None, quoting = csv.QUOTE_NONE, skipinitialspace = True)
			writer.writerow("NDFA") # TODO: Check if is DFA or NFA
			writer.writerow(sorted(self.alphabet))
			writer.writerow(self.blankSymbol)
			writer.writerow(sorted(self.states))
			writer.writerow(sorted(self.initialStates))
			writer.writerow(sorted(self.acceptanceStates))
			for t in self.transitions:
				writer.writerow([t.currentState, t.currentInputSymbol, t.newState])
			if outputFile == None:
				csvcontent = csvfile.getvalue()
		return csvcontent
