# IPython - interactive Python

IPython is an interactive shell for Python. Some main features are:

* Numbered prompts
  - E.g. **In [2]**, **Out[2]**
  - Output accessible with **Out[2]** or **_2**
  - Last objects in output history:  **\_**, **\_\_**, **\_\_\_** for last, second, and third last, respecively

* Magic commands for efficient work, e.g.
  - **%cd**, **%pwd**, **%ls**
  - **%load**, **%run**, **%debug**
  - **%whos**

* Execute shell commands from IPython
  - Prepend **!** such as **!ls -ltr**
  - Assign to a variable **directory = !ls**

* Access the code history within the shell
  - Show numbered code history: **%history -n**
  - Export code to .py file: **%save draft.py**

* Object introspection, code documentation
  - Use **?** or **??** to get help about an object or magic function
  - Allows **?** with wildcard matching, e.g.
    + ***Error?** lists all types of Python errors
    + **str.*find*?** lists all string methods with 'find' in its name
  - Use **help(function)** for Python's own help system

* Tab completion
  - Tab to select, **Ctrl-Up** and **Ctrl-Down** to scroll suggestions
  - Accept also with **Ctrl-e**, **Ctrl-f**, **Right**, **Ctrl-Right** (token only)
  - **Ctrl-n**, **Ctrl-p** or **Up**, **Down** arrow keys to select suggestion or scroll through command history

* Multi-line input
  - Type **Ctrl-o** to enter several lines of code
  - To execute, press **Enter** or try **Alt-Enter**, **Ctrl-Enter** or **Shift-Enter**
  - **%edit newfile.py** opens the default editor


## Use cases

* Learn and test Python
* Write draft code and export to .py files
* Debug .py files
* Test .py files
* Running workflows/functions interactively from .py files


## Write code drafts

Write some draft code in the IPython shell. Save it to a .py file with:

```
%save script.py             # Save code history to a .py file
%save script.py 4 5 6 8     # Save only input prompts 4, 5, 6 and 8 to a .py file
```

## Debug .py files

Run your .py file in IPython with
```
%run file   (.py extension can be omitted)
```
If an exception occurs, you can go into the ipdb debugger with:
```
%debug
```
To activate automatic calling of the pdb debugger when an exception occurs:
```
%pdb on
```
You can also start a debugging session like this:
```
%run -d file.py                 # breakpoint in first line
%run -d -b14 file.py            # breakpoint in line 14
%run -d -b foo.py:42 file.py    # breakpoint in foo.py on line 42, run file.py
```
The last example is useful when a bug is hidden in one of the imported modules
and you don't want to step through the code manually.

If the program runs successfully, the variables and functions at module level
are available in the IPython namespace. They can further be used in IPython for
inspection or testing. To list the IPython namespace:
```
%whos
```

## Embed IPython in scripts

Embed IPython in an existing Python script which allows an interactive session
within the script, e.g. for debugging:

```
# script.py

import IPython

a = 2
b = 3
IPython.embed()  # Start IPython session at this point
print("Script continues here")
```

## Loading/running scripts in IPython

Load a script into IPython with the option to modify it before execution.
Modify by arrow up/down and type your changes. Execute with <CR> after the last
code line. After execution, all variables and functions are available in the
IPython namespace.
```
%load script.py                         # Load enire script, .py can be omitted
%load -r 1-10 script.py                 # Load line range
%load -s my_function,MyClass script.py
%load URL
```
Edit a script in default editor ($EDITOR environment variable) and execute it
upon closing the editor.
```
%edit script.py
```
Edit a script without executing it after closing the editor:

```
!vim script.py
```

Run a script in the IPython shell. After execution, all variables and functions
are available in the IPython namespace.
```
%run script.py
```
If an exception occurs, you can call the pdb debugger with:
```
%debug
```

## Test modules/functions

You can import a module/function and interactively test it with several arguments:

```
import numpy as np
import my_module
data = np.random.normal(0, 1, 1000)
my_module.analyze_data(data)
```

If you modify my_module.py, you can reload it automatically with these settings:
```
%load_ext autoreload    # Load the autoreload extension
%autoreload 2           # 0: Disable auto-reload, 1: only modules imported with %aimport, 2: auto-reload all
```

## Run workflows

Suppose you have a Python module 'data_analysis_wf.py' with several functions
for data loading, analysis, and plotting.

```
# data_analysis_wf.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    return pd.DataFrame({'A': np.random.rand(10), 'B': np.random.rand(10)})

def calculate_stats(df):
    print(df.describe())

def plot_data(df):
    df.plot(kind='bar')
    plt.show()
```

You can import the module and execute the functions interactively in the IPython shell:

```
# IPython shell:

from data_analysis_wf import load_data, calculate_stats, plot_data
df = load_data()
calculate_stats(df)
plot_data(df)
```


## Magic commands

A selection of magic commands is listed below.

Note if **%automagic on** (default) you can run magic commands without having to
type the initial **%**. However, magic functions have lowest priority, so if
there is a variable whose name that collides with that of a magic function,
automagic won't work for that function. You get the variable instead.

```
%pwd                                Current working directory
%ls                                 List directory with same options as unix
%cd                                 Change directory

%bookmark MyPath /path/to/project   Bookmark working directory
%cd -b MyPath                       Change to MyPath bookmarked directory
%bookmark -l                        List bookmarks
%bookmark -d MyPath                 Delete bookmark

%load script.py                     Load script into IPython shell and execute
%edit script.py                     Edit script with default editor ($EDITOR environment variable) and execute
%run script.py                      Run script in IPython shell
%save script.py                     Save code history to a .py file
%save script.py 4 5 6 8             Save only input prompts 4, 5, 6 and 8 to a .py file
%notebook script.ipynb              Exports current IPython history to a notebook file
%paste                              Paste code from clipboard into IPython shell removing marked-up characters

%who                                List variables in workspace
%whos                               List variables with extra information
%who_ls                             Return a sorted list of all interactive variables
%reset -f                           Reset namespace, empty all, without asking for confirmation
%reset_selective var                Clear the 'var' name from the namespace

%history -n                         Display command history
%history 7                          Display command number 7 in the history
%history -opf session.txt           Write history to session.txt with outputs and '>>>' before inputs
%recall 15, %rep 15                 Recall command number 15 and place in next input prompt for editing
%recall, %rep                       Place a string version of last output result to the next input prompt
%rerun                              Rerun last input line
%rerun 15                           Rerun command number 15 in the history
%rerun -l 3                         Rerun the last 3 lines of input
%rerun -g foo                       Rerun the most recent line which contains foo
%macro name 4-6 8                   Define a macro for later re-execution using commands 4-6 and 8

%store var1 var2                    Store variables before exiting IPython
%store -r                           Restore variables from a stored session
%store -d var1                      Delete a variable from storage
%logstart                           Start logging the session
%logoff                             Temporarily stop logging
%logon                              Restart logging
%logstop                            Stop logging and close log file

?object or object?                  Provide detailed information about an object
??object or object??                Provide extra detailed information
%magic                              Print information about magic function system
%lsmagic                            List available magic functions
%quickref                           Show a quick reference sheet
help(function)                      Show help with Python's own help system
%automagic on/off                   Make magic function callable without prepending %

%matplotlib                         Set up matplotlib to work interactively, you don't need plt.show()
%pylab                              Load numpy and matplotlib to work interactively
%time, %%time                       Basic timing (1 execution) of a Python statement/expression in line or cell mode
%timeit, %%timeit                   Time repeated executions of a Python statement/expression in line or cell mode
%prun statement, %%prun ...         Profile a statement
```


## Editing the command history

Sometimes, you may want to delete commands from the history, e.g. after typing
a commond with errors, to avoid suggesting them for auto-completion. For
example, when you typed 'quite' or 'qut' instead of 'quit'.

The IPython history is normally stored in **~/.ipython/profile_default/history.sqlite**.
You can also display the location with ```ipython locate profile default``` in the terminal.

Manage the history with SQLite: ```sqlite3 ~/.ipython/profile_default/history.sqlite```

Execute SQL commands within the SQLite prompt:

```
DELETE FROM history;                                Delete all history

SELECT * FROM history;                              List sessions and commands
DELETE FROM history WHERE session=XXX;              Delete session XXX
                                                    Also <, >, <=, >=, or !=
                                                    E.g. session>100

SELECT * FROM history WHERE source LIKE '%foo%';    List commands containing 'foo'
                                                    '%' matches zero or more characters
                                                    '_' matches exactly one character
                                                    The LIKE operator is case-insensitive
DELETE FROM history WHERE source LIKE '%foo%';      Delete commands containing 'foo'
... source LIKE '%foo%' OR source LIKE '%bar%';     Combination with OR or AND
DELETE FROM history WHERE source GLOB 'foo[0-9]*';  Unix file-globbing, case-sensitive

.quit                                               Exit the SQLite prompt
```


