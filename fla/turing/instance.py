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


import copy

from fla.turing.transition import Transition


class Instance:
	def __init__(self, automaton, state, tapes = [], previous_configuration = None):
		self.automaton = automaton
		self.current_state = state
		self.tapes = copy.deepcopy(tapes)
		self.previous_configuration = previous_configuration
		self.acceptance_status = None

	def is_transition_valid(self, transition):
		current_tape_symbols = []
		for tape in self.tapes:
			current_tape_symbols.append(tape.get_content())
		return transition.match(self.current_state, current_tape_symbols)
		
	def get_valid_transitions(self):
		valid_transitions = []
		for transition in self.automaton.transitions:
			if self.is_transition_valid(transition):
				valid_transitions.append(transition)
		return valid_transitions

	def apply_transition(self, transition):
		if self.acceptance_status != None:
			return self
		if not self.is_transition_valid(transition):
			return None
		new_instance = Instance(self.automaton, transition.get_new_state(), self.tapes, self)
		for tape in zip(new_instance.tapes, transition.get_new_tape_data()):
			tape[0].set_content(tape[1][0])
			tape[0].move_head(tape[1][1])
		return new_instance

	def get_tapes_as_string(self, symbol_separator = ''):
		result = ""
		for tape in self.tapes:
			current_tape_string = ""
			for value in tape.content:
				current_tape_string += value
				current_tape_string += symbol_separator
			current_tape_stringt = result.rstrip(symbol_separator)
			current_tape_string = current_tape_string.strip(tape.whitespace_symbol)
			result += current_tape_string
			result += "\n"
		result = result.rstrip()
		return result

	def __str__(self):
		result = "["
		for tape in self.tapes:
			result += str(tape)
			result += ","
		result += "]@S"
		result += self.current_state
		return result
	
	def __eq__(self, other):
		if self.__class__ != other.__class__:
			return False
		
		if self.current_state != other.current_state:
			return False
		
		if self.tapes != other.tapes:
			return False
