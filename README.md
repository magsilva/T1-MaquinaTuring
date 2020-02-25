[![Build Status](https://travis-ci.org/magsilva/fla-runner.svg?branch=master)](https://travis-ci.org/magsilva/fla-runner)

Formal Language Automaton Runner (fla-runner) is a software that executes
automaton specified in a formal language. Currently, we support Turing
machines (with single taple or multiple tapes, always unbounded to both
directions), pushdown automata (with one stack) and finite automata. It
does not matter if it is a deterministic or nondetermistic model: we
support them all!

The formal language specification must be written in [JFLAP](http://www.jflap.org/)
format (which is an XML document). Internally, that format is converted to a
[simpler text-base format](#Text-based FLA format).


# Running instructions

Running fla-runner is rather simple. The main file is `fla/main.py`. It
requires two arguments: the name of the file (either in JFLAP or text-based
format) and the string to be tested. If you are using a multiple-tape
Turing machine, you should use as many strings as tapes required (for empty
tapes, just use "" to specify an empty string).

```sh
PYTHONPATH=. python3 fla/main.py [filename] [string]
```

The application will return `0` if the computation was successful (string
accepted) and `1` otherwise. The content of the automaton memory (if applicable)
will be written to stdout. It can output debug information to stderr.

Sometimes the computation result will be different from JFLAP's one. This
is (probably) not an error from fla-runner, but from JFLAP (its implementation
of non-deterministic models, specially Turing machines, has some issues with
depth-first search instead of using breadth-first search).


# Text-based FLA format

The `fla/jflap2flarunner.py` script can convert software specified using
JFLAP format to text-based format. Actually, there is no need to write the
specification directly in text-based FLA format: fla-runner will automatically
run the conversion script to handle such conversion if required (no file is
generated with text-based format when it is run automatically). If you want to
convert a JFLAP specification to textual format, run `fla/jflap2flarunner.py`
and set the first argument to the JFLAP filename and the second argument to
the filename of the text-based FLA file that will be created.

The first line of the file defines the type of formal language used. Currently,
we support the following:
* DFA: Deterministic Finite Automaton
* NFA: Nondeterministic Finite Automaton
* PDA: Pushdown Automaton
* TM: Turing machine
 
The remaining lines of the file depends upon the formal language defined in the
first line (although some elements, such as input alphabet and states, are
similarly defined for most formal languages).


## Deterministic and Nondeterministic Finite Automaton

* Line 2: input alphabet.
* Line 3: character to be used to represent epsilon or lambda (it should not be
  part of the input alphabet, default is E).
* Line 4: set of states.
* Line 5: initial state (or set of initial states if a nondeterministic finite
  automaton).
* Line 6: set of acceptance states.
* Line 7 onwards: transitions, one per line, in the following format: current
  state, input alphabet symbol or epsilon/lambda symbol, next state.


## Pushdown automaton

* Line 2: input alphabet.
* Line 3: stack alphabet.
* Line 4: character to be used to represent epsilon or lambda (it should not be
  part of the input alphabet, default is E).
* Line 5: initial stack symbol (default is Z).
* Line 6: set of states.
* Line 7: initial state (or set of initial states if a nondeterministic pushdown
  automaton).
* Line 8: set of acceptance states.
* Line 9 onwards: transitions, one per line, in the following format: current
  state, current input alphabet symbol or epsilon/lambda symbol, current symbol
  at the top of the stack or epsilon/lambda symbol, next state, string of 
  symbols to be stacked (top to the left of the string, bottom to the right)
  or epsilon/lambda symbol.


## Turing machine

* Line 2: input alphabet.
* Line 3: tape alphabet.
* Line 4: character to be used to represent blank spaceepsilon or lambda (it should not be
  part of the input alphabet, default is E).
* Line 5: set of states.
* Line 6: initial state.
* Line 7: set of final states.
* Line 8: number of tapes.
* Line 9 onwards: transitions, one per line, in the following format: current
  state, next state, and, for each tape, the current symbol in that tape,
  new symbol for that tape, and direction to move the head on that tape (L for
  left, R to right and S to stay at current position).


