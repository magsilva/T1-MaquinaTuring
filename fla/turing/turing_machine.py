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
import logging

from fla.turing.instance import Instance

class TuringMachine:
	def __init__(self, states, initial_state, final_states, whitespace, transitions):
		self.states = states
		self.initial_state = initial_state
		self.final_states = final_states
		self.transitions = transitions
		self.whitespace = whitespace
		self.current_configurations = []

	def get_initial_configurations(self, tapes):
		return [Instance(self, self.initial_state, tapes)]
	
	def load_configurations(self, configurations):
		self.current_configurations = configurations

	def restart(self):
		self.current_configurations = []

	def verify_status(self, configuration):
		if configuration.acceptance_status != None:
			configuration.acceptance_status
		for final_state in self.final_states:
			if configuration.current_state == final_state:
				configuration.acceptance_status = True
				return True
		valid_transitions = configuration.get_valid_transitions()
		if len(valid_transitions) == 0:
			configuration.acceptance_status = False
			return False

	def is_halted(self):
		if len(self.current_configurations) == 0:
			return True
		for configuration in self.current_configurations:
			if configuration.acceptance_status != None:
				return True 
		return False

	def get_decision(self):
		for configuration in self.current_configurations:
			if configuration.acceptance_status == True:
				print(configuration.get_tapes_as_string())
				return True
		if len(self.current_configurations) == 0 or self.is_halted():
			return False
		return None
		
	def step_forward(self):
		configurations_current_step = copy.copy(self.current_configurations)
		self.current_configurations = []
		for configuration in configurations_current_step:
			logging.debug("Evaluation transitions for configuration " + str(configuration))
			for transition in configuration.get_valid_transitions():
				new_configuration = configuration.apply_transition(transition)
				self.current_configurations.append(new_configuration)
				logging.debug("\tApplying transition " + str(transition) + ": " + str(configuration) + " -> " + str(new_configuration))
			
	def run(self):
		halted_configurations = []
		for configuration in self.current_configurations:
			self.verify_status(configuration)
			if configuration.acceptance_status != None:
				halted_configurations.append(configuration)
			logging.debug("Verifying configuration status for " + str(configuration) + ": " + str(configuration.acceptance_status))
		while self.current_configurations:
			self.step_forward()
			for configuration in self.current_configurations:
				self.verify_status(configuration)
				if configuration.acceptance_status != None:
					halted_configurations.append(configuration)
				logging.debug("Created new configuration: " + str(configuration) + " (" + str(configuration.acceptance_status) + ")")
		self.current_configurations = halted_configurations
		if self.is_halted():
			return True
		
