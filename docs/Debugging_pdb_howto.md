# Debugging with pde

## Breaking into the debugger

Pdb is part of Python's standard library and always available.

Insert the following code where you want to break into the debugger:

```
import pdb
pdb.set_trace()
# ...code continues...

# Or as one-liner
import pdb; pdb.set_trace()
```

Since Python 3.7 you can also set a breakpoint for debugging simply like this:

```
# No import of pdb required
breakpoint()
# ...code continues...

# Disable all breakpoints by setting environment variable:
setenv PYTHONBREAKPOINT 0  # C-Shell
export PYTHONBREAKPOINT=0  # Bash

# Enable all breakpoints:
unsetenv PYTHONBREAKPOINT  # C-Shell
unset PYTHONBREAKPOINT  # Bash
```

Running Python from the command-line, you can also break into the debuggger
without using `pdb.set_trace()` or `breakpoint()` in the Python file. This will
enter pdb and stop execution immediately at the beginning of the script:

```
python -m pdb script.py
```

Then type c to continue execution until the error occurs.


## Commands in Pdb

Pdb commands can conflict with normal Python code. For example: the **a** pdb
command and an **a** Python variable in the code. You can print the variable **a**
with `print a`. Also, you can force pdb to understand something as Python code
by starting with **!**: `!a` will show the variable **a** in Pdb.

- **l, list** : List source code, default 11 lines
- **l.** : List source code centered around current line
- **ll, longlist** : List the whole source code for current function / frame
- **p <expr>** : Print an expression
- **pp <expr>** : Pretty print an expression
- **whatis <expr>** : Print the type of expression
- **a, args** : Print arguments list of current function

- **b, break <lineno>** : Set breakpoint at line number<\br>
                        b <file:lineno> in another file<\br>
                        b <module.func> by function name
- **b <lineno>, [condition]** : Set breakpoint only if condition is true<\br>
                        b <lineno>, a > 3<\br>
                        Note: using lineno, the variable 'a' can be local to the function<\br>
                        b <module.func>, not filename.startswith("/")<\br>
                        Note: using the function to define the breakpoint, the variable<\br>
                        'filename' must be a function argument<\br>
                        condition <bpnumber> [condition] sets a new condition for the breakpoint<\br>
- **b** : List all breakpoints showing also the bpnumber
- **tbreak <lineno>** : Temporary breakpoint which is removed when first hit
- **disable <bpnumber>** : Disable breakpoint
- **enable <bpnumber>** : Enable breakpoint
- **cl, clear <bpnumber>** : Delete breakpoint

- **c, continue** : Continue execution to the next breakpoint
- **n, next** : Continue execution until next line staying in current function
- **s, step** : Execute current line and stop at first possible occasion
                either inside current function or a function that is called (step inside)
- **r, return** : Continue execution until the current function returns
- **unt, until** : Continue execution until the line with greater lineno is reached
- **unt <lineno>** : Continue execution until lineno is reached
- **r, return** : Continue execution until the current function returns
- **j, jump <lineno>** : Set the next line to be executed, let's you jump back or forward to skip code
- **<CR>** : Repeat last command

- **display <expression>** : Display the value of expression if changed, each time execution stops
- **undisplay <expression>** : Do not display expression any more
- **display** : List all display expressions for current frame
- **undisplay** : Clear all display expressions for current frame

- **w, where** : Print a stack trace to find out who the caller of a function is.<\br>
                        The most recent frame is at the bottom.
- **u, up <count>** : Move current frame count levels up in the stack trace to an older frame.<\br>
                        This moves to the caller of a function.
- **d, down <count>** : Move current frame count levels down in the stack trace to a newer frame.<\br>
                        This moves back from the caller to the function.

- **h, help <cmd>** : Get help for a command or topic
- **h pdb** : Show the full pdb documentation
- **q, quit** : Quit the debugger and exit

- **alias <name> <command>** :  Create alias for command, can also be placed in a .pdbrc file in your home directory.<\br>
                        alias le len(var)  # Print length of variable var<\br>
                        alias dir import glob; print(glob.glob("%1"))  # List files and directories matching pattern<\br>
                        alias who pp list(locals().keys())  # List local namespace<\br>

- **unalias <name>** : Delete specified alias name
                        

# IPdb - enhanced debugger

While pdb is included in Python, ipdb needs to be installed with pip into your
environment. It is also not included in Komodo. However, the debugger commands
listed above are the same.

Advantages of ipdb are:

- syntax highlighting (as in IPython)
- command auto-completion

To set a breakpoint, insert the following code:

```
import ipdb; ipdb.set_trace()
```
