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
from string import ascii_uppercase
import sys
from xml.etree import ElementTree


class Transition(object):
	def __init__(self):
		self.currentState = None
		self.newState = None
		self.tapeMovements = []

	def __lt__(self, other):
		if self.currentState < other.currentState:
			return True
		elif self.currentState > other.currentState:
			return False
		elif self.newState < other.newState:
			return True
		elif self.newState > other.newState:
			return False
		else:
			return self.newState < other.newState

class TapeMovement(object):
	def __init__(self):
		self.tape = 1
		self.currentTapeSymbol = None
		self.newTapeSymbol = None
		self.headDirection = None

	def __lt__(self, other):
		if self.currentTapeSymbol < other.currentTapeSymbol:
			return True
		elif self.currentTapeSymbol > other.currentTapeSymbol:
			return False
		elif self.newTapeSymbol < other.newTapeSymbol:
			return True
		elif self.newTapeSymbol > other.newTapeSymbol:
			return False
		else:
			return self.headDirection < other.headDirection

class JflapTmConverter(object):
	def __init__(self):
		self.alphabet = set()
		self.states = set()
		self.tapeSymbols = set()
		self.tapes = 1
		self.initialState = None
		self.finalStates = set()
		self.transitions = set()
		self.singleTape = False

	def convert(self, inputFile, outputFile = None, blankSymbol = 'E', alphabet = None):
		xmldoc = ElementTree.parse(inputFile)
		root = xmldoc.getroot()
		if root.find('tapes') == None:
			self.singleTape = True
			self.tapes = 1
		else:
			self.tapes = int(root.find('tapes').text)

		tm = root.find('automaton')
		if tm == None:  # Old JFLAP format
			tm = root

		stateElementName = 'block'
		if tm.find(stateElementName) == None:
			stateElementName = 'state'

		# Discover states
		for s in tm.findall(stateElementName):
			state = s.attrib['id']
			self.states.add(state)
			if s.find('initial') is not None:
				self.initialState = state
			if s.find('final') is not None:
				self.finalStates.add(state)

		# Discover tape alphabet (and fix blank symbol if required)
		for t in tm.findall('transition'):
			tapeXPath = ''
			for i in range(1, self.tapes + 1):
				if not self.singleTape: # Workaround for handling single and multitape Turing machines
					tapeXPath = "[@tape='" + str(i) + "']"
				if t.find("read" + tapeXPath).text is not None:
					self.tapeSymbols.add(t.find("read" + tapeXPath).text)
				if t.find("write" + tapeXPath).text is not None:
					self.tapeSymbols.add(t.find("write" + tapeXPath).text)
		for s in self.tapeSymbols:
			if s == blankSymbol:
				oldBlankSymbol = blankSymbol
				for c in ascii_uppercase:
					if c not in self.tapeSymbols:
						blankSymbol = c
						break
				logging.debug("Simbolo escolhida para representar branco (" + oldBlankSymbol + ") foi utilizado para outros fins na maquina. Simbolo para branco foi substituido por " + blankSymbol + ".")
		self.blankSymbol = blankSymbol
		self.tapeSymbols.add(self.blankSymbol)

		for t in tm.findall('transition'):
			transition = Transition()
			self.transitions.add(transition)
			transition.currentState = t.find('from').text
			transition.newState = t.find('to').text
			tapeXPath = ''
			for i in range(1, self.tapes + 1):
				movement = TapeMovement()
				transition.tapeMovements.append(movement)
				movement.tape = i
				if not self.singleTape: # Workaround for handling single and multitape Turing machines
					tapeXPath = "[@tape='" + str(i) + "']"
				if t.find("read" + tapeXPath).text is not None:
					movement.currentTapeSymbol = t.find("read" + tapeXPath).text
				else:
					movement.currentTapeSymbol = self.blankSymbol
				if t.find("write" + tapeXPath).text is not None:
					movement.newTapeSymbol = t.find("write" + tapeXPath).text
				else:
					movement.newTapeSymbol = self.blankSymbol
				movement.headDirection = t.find("move" + tapeXPath).text

		if alphabet is None:
			self.alphabet = self.tapeSymbols.copy()
			self.alphabet.remove(self.blankSymbol)
		else:
			self.alphabet = alphabet
	
		csvcontent = ""
		if outputFile == None:
			csvfile = io.StringIO()
		else:
			csvfile = open(outputFile, 'w')
		
		with csvfile:
			writer = csv.writer(csvfile, delimiter=' ', lineterminator='\n')
			writer.writerow("TM")
			writer.writerow(sorted(self.alphabet))
			writer.writerow(sorted(self.tapeSymbols))
			writer.writerow([self.blankSymbol])
			writer.writerow(sorted(self.states))
			writer.writerow([self.initialState])
			writer.writerow(sorted(self.finalStates))
			writer.writerow([self.tapes])
			for transition in sorted(self.transitions):
				transitionDescription = []
				transitionDescription.append(transition.currentState)
				transitionDescription.append(transition.newState)
				for i in range(1, self.tapes+1):
					for movement in sorted(transition.tapeMovements):
						if movement.tape == i:
							transitionDescription.append(movement.currentTapeSymbol)
							transitionDescription.append(movement.newTapeSymbol)
							transitionDescription.append(movement.headDirection)
				writer.writerow(transitionDescription)
			if outputFile == None:
				csvcontent = csvfile.getvalue()
		return csvcontent
