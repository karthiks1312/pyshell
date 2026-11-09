# pyshell

A simple Unix-style command line shell written in Python, built for the [Coding Challenges shell challenge](https://codingchallenges.fyi/challenges/challenge-shell).

## Features

- Built-in commands: `cd` (including `cd` with no argument and `~` paths), `pwd` and `exit`
- Runs any external program with its arguments, e.g. `ls -la`
- Quote-aware parsing, so `echo "hello   world"` keeps its spacing
- Clear messages for unknown commands, bad directories and unbalanced quotes
- Ctrl-C clears the line; Ctrl-D exits

## Install and run

Requires Python 3.10 or newer.

```bash
git clone https://github.com/karthiks1312/pyshell.git
cd pyshell
pip install -e .
pyshell
```

```
shell> pwd
/Users/you
shell> cd /tmp
shell> ls -la
shell> exit
```

## Tests

```bash
pip install -e ".[test]"
pytest
```

## Project layout

```
src/pyshell/main.py   # shell loop, built-ins, command execution
tests/test_main.py    # pytest suite
```

## Roadmap

Pipes, redirection, environment variables and command history.
