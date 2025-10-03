# Ruff for Python code linting and auto-formatting

[Ruff](https://docs.astral.sh/ruff/) is a very fast linting and code formatting
program for Python. It is included in Komodo. The code formatting is rigorous
with only few options. The defaults are opinionated and set to "good values"
satisfying [PEP8](https://peps.python.org/pep-0008/).

-**Linting:** Identify and flag programming errors, stylistic inconsistencies, and potential bugs
-**Auto-formatting:** Adjust the code's layout and style to adhere to predefined formatting standards, enhancing readability

## Usage examples from the command line

**Linting**
```
ruff check pyfile.py                    - Check file, linter
ruff check --fix pyfile.py              - Check file and fix fixable errors
ruff check                              - Check recursively
ruff check project/path/                - Check recursively
ruff check *.py                         - Check all .py files in current directory
```

**Auto-formatting**
 ```
ruff format pyfile.py                   - Format file
ruff format                             - Format recursively, current directory and subdirectories
ruff format project/path/               - Format recursively, path
ruff format *.py                        - Format all .py files in current directory
```

**Sorting imports**
```
ruff check --select I pyfile.py         - Check imports (isort)
ruff check --select I --fix pyfile.py   - Auto-sort imports (isort)
```

## Configuration and options

[Configuration](https://docs.astral.sh/ruff/configuration/) with **ruff.toml** or **.ruff.toml** file in the folder where you store the Python files.
For example, you may want longer lines, e.g. with 120 characters, when the default 88 characters is too short.

Example **.ruff.toml** file:

---*Start of file*---
line-length = 120
---*End of file*---

You can also exclude lines from linting by appending `# noqa`.
For example, the expression `PRJ = prj` in RMS Python scripts raises an error when linting.
To exclude the line from linting, write `PRJ = prj  # noqa`.
