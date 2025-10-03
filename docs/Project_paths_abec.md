# Project Paths Scripts: cdproject and cdproject_append

## How to set up

1. Copy the **cdproject** and **cdproject_append** files into your **bin** folder
in your home directory. The **bin** folder is where you store your executable scripts.

2. Make sure the two scripts are executable for you. 

```
  # To make them executable:
  chmod +x cdproject*
```
3. Copy the **.project_paths** file into your home folder.

4. Make sure your **bin** folder is on the **PATH**.

```
  # C-Shell. Add this to your ~/.cshrc file:
  setenv PATH ${PATH}:/private/<usr_name>/bin

  # Bash. Add this to your ~/.bashrc file:
  PATH=$PATH:~/bin
```

5. For convenience, add some aliases:

- **cdp**: Filter your **.project_paths** and show a numbered list for selection
- **cda**: Append the current directory path to the **.project_paths** file
- **cde**: Shortcut to edit the **.project_paths** file. Replace **vim** with your favorite editor, e.g. **code** or **gedit**

```
  # C-Shell. Add this to your ~/.cshrc file:

  alias cdp 'cdproject \!* && set sel_path=`cat ~/.selected_path` && cd "$sel_path" && unset sel_path'
  alias cda 'cdproject_append \!*'
  alias cde 'vim ~/.project_paths'  # using vim

  # Bash. Add this to your ~/.bashrc file:

  function cdp () {
      cdproject "$1"
      sel_path=$(cat ~/.selected_path)
      cd "$sel_path"
      unset sel_path
  }

  function cda () {
      cdproject_append "$1"
  }

  alias cde='vim ~/.project_paths'  # using vim
```

## Usage examples

1. List all paths: `cdp`

2. Filter paths on 'snorre': `cdp snorre`

3. Filter paths on 'snorre' and 'vig': `cdp 'snorre|vig'`

4. Add the current directory: `cda`

5. Add a specific directory: `cda /path/to/project`

6. Add multiple directories using wildcards: `cda ~/projects/* /tmp`

## The .project_paths file

The **~/.project_paths** file contains project directory paths. It may contain comment lines 
starting with **#** to structure the file. In addition, tags can be added in each line by
adding a **#** after the path and one or more keywords. The tags are searchable.

**Example .project_paths file:**

---*Start of file*---<br>
\# Snorre Sim2Seis<br>
/project/snorre/reservoirmodels/ff<br>
/project/snorre/reservoirmodels/ff/users/abec<br>
/scratch/coviz_sn/abec   # snorre<br>

\# Vigdis Brent Sim2Seis<br>
/project/pl089/vigdis_area/resmod/brent/ff<br>
/project/pl089/vigdis_area/resmod/brent/ff/users/abec<br>
/scratch/vigdis/vm/users/abec<br>
---*End of file*---

**Author: Andreas Becht, 10/2025**


