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

import csv
import logging
import io
import sys
from xml.etree import ElementTree


class Transition(object):
	def __init__(self):
		self.currentState = None
		self.currentWordSymbol = None
		self.currentStackTopSymbol = None
		self.newState = None
		self.newStackTopSymbol = None

	def __lt__(self, other):
		if self.currentState != other.currentState:
			return self.currentState < other.currentState
		if self.currentWordSymbol != other.currentWordSymbol:
			return self.currentWordSymbol < other.currentWordSymbol
		if self.currentStackTopSymbol != other.currentStackTopSymbol:
			return self.currentStackTopSymbol < other.currentStackTopSymbol
		if self.newState != other.newState:
			return self.newState < other.newState 
		if self.newStackTopSymbol != other.newStackTopSymbol:
			return self.newStackTopSymbol < other.newStackTopSymbol

class JflapPdaConverter(object):
	def __init__(self):
		self.state_id_to_name = {}
		self.inputAlphabet = set()
		self.stackAlphabet = set()
		self.states = set()
		self.initialStates = set()
		self.acceptingStates = set()
		self.transitions = []
		self.blankSymbol = "E"
		self.stackInitialSymbol = "Z"

	def convert(self, inputFile, outputFile = None, blankSymbol = "E", inputAlphabet = None, stackAlphabet = None, states = None):
		self.blankSymbol = blankSymbol
		if inputAlphabet is not None:
			self.inputAlphabet = inputAlphabet
		if stackAlphabet is not None:
			self.stackAlphabet = stackAlphabet
		if states is not None:
			self.states = states

		xmldoc = ElementTree.parse(inputFile)
		root = xmldoc.getroot()
		tm = root.find('automaton')

		for s in tm.findall('state'):
			state_id = s.attrib['id']
			state_name = s.attrib['name']
			self.state_id_to_name[state_id] = state_name
			self.states.add(state_name)
			if s.find('initial') is not None:
				self.initialStates.add(state_name)
			if s.find('final') is not None:
				self.acceptingStates.add(state_name)

		# Discover stack alphabet
		if stackAlphabet is None:
			self.stackAlphabet.add(self.stackInitialSymbol)
			for t in tm.findall('transition'):
				popSymbol = t.find('pop').text
				if popSymbol is not None and len(popSymbol.strip()) > 0:
					self.stackAlphabet.add(popSymbol)
				pushSymbol = t.find('push').text
				if pushSymbol is not None and len(pushSymbol.strip()) > 0:
					self.stackAlphabet.add(pushSymbol)
	
		# Discover input alphabet:
		if inputAlphabet is None:
			for t in tm.findall('transition'):
				if t.find('read').text is not None:
					self.inputAlphabet.add(t.find('read').text)

		# Use a symbol to represent epsilon that is not used by the input or stack alphabets
		fullAlphabet = set()
		fullAlphabet.union(self.inputAlphabet)
		fullAlphabet.union(self.stackAlphabet)
		for s in fullAlphabet:
			if s == blankSymbol:
				oldBlankSymbol = blankSymbol
				for c in ascii_uppercase:
					if c not in fullAlphabet:
						blankSymbol = c
						break
				logging.debug("Simbolo escolhida para representar branco (" + oldBlankSymbol + ") foi utilizado para outros fins no automato. Simbolo para branco foi substituido por " + blankSymbol + ".")
		self.blankSymbol = blankSymbol
		
		for t in tm.findall('transition'):
			transition = Transition()
			self.transitions.append(transition)
			transition.currentState = self.state_id_to_name[t.find('from').text]
			if t.find('read').text is not None:
				transition.currentWordSymbol = t.find('read').text
			else:
				transition.currentWordSymbol = self.blankSymbol
			if t.find('pop').text is not None:
				transition.currentStackTopSymbol = t.find('pop').text
			else:
				transition.currentStackTopSymbol = self.blankSymbol
			transition.newState = self.state_id_to_name[t.find('to').text]
			if t.find('push').text is not None:
				symbols = t.find('push').text
				transition.newStackTopSymbol = symbols
			else:
				transition.newStackTopSymbol = self.blankSymbol

		self.transitions.sort()

		csvcontent = ""
		if outputFile == None:
			csvfile = io.StringIO()
		else:
			csvfile = open(outputFile, 'w')
		with csvfile:
			writer = csv.writer(csvfile, delimiter = ' ', escapechar = None, quotechar = None, quoting = csv.QUOTE_NONE, skipinitialspace = True)
			writer.writerow("PDA")
			writer.writerow(sorted(self.inputAlphabet))
			writer.writerow(sorted(self.stackAlphabet))
			writer.writerow(self.blankSymbol)
			writer.writerow(self.stackInitialSymbol)
			writer.writerow(sorted(self.states))
			writer.writerow(sorted(self.initialStates))
			writer.writerow(sorted(self.acceptingStates))
			for t in self.transitions:
				writer.writerow([t.currentState, t.currentWordSymbol, t.currentStackTopSymbol, t.newState, t.newStackTopSymbol])
			if outputFile == None:
				csvcontent = csvfile.getvalue()
		return csvcontent
