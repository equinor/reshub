# GIT AND GITHUB SETUP

**Date:** 19-June-2024

## Contents
- [Setting Up SSH Connection for Git](#setting-up-ssh-connection-for-git)
  - [General](#general)
  - [LINUX RGS Nodes](#linux-rgs-nodes)
  - [Win10 PC (Standard User Profile, Not Developer)](#win10-pc-standard-user-profile-not-developer)
    - [Introduction](#introduction)
    - [Create SSH Keys](#create-ssh-keys)
    - [SSH-Agent for SSH Keys with Passphrases](#ssh-agent-for-ssh-keys-with-passphrases)
- [General Tips for Working with GitHub Repositories](#general-tips-for-working-with-github-repositories)
  - [GIT Config](#git-config)
  - [Recommended Workflow for Setting Up a New Repository](#recommended-workflow-for-setting-up-a-new-repository)

---

## Setting Up SSH Connection for Git

### General
As of June 2024, proxy servers are no longer required.

### LINUX RGS Nodes
1. In the terminal window, generate SSH keys with:
   ```bash
   ssh-keygen -t ed25519
   ```
   This will create SSH keys in your `/private/<user>/.ssh` directory. Use the default file name and leave the passphrase empty by pressing return each time.

2. Print the public key and copy it to the clipboard:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

3. On GitHub, go to your account settings and add the public SSH key under `Settings > SSH and GPG keys`. Name it sensibly for easy recognition.

4. Configure SSO and authorize the key.

5. Test the SSH connection:
   ```bash
   ssh -T git@github.com
   ```

6. To clone a repository with SSH:
   ```bash
   git clone git@github.com:equinor/MamasKitchen
   ```
   Alternatively:
   ```bash
   git clone ssh://git@ssh.github.com:443/equinor/MamasKitchen.git
   ```
   The shorter version is usually preferred.

7. Note: On RGS Linux machines, cloning via HTTPS may fail, so it’s recommended to use SSH.

### Win10 PC (Standard User Profile, Not Developer)

#### Introduction
- SSH keys used by Git are stored in your home directory (`.ssh` folder). Depending on your setup, this could be `C:\Users\<user>` or the root folder on the F-drive.

- The home directory location can change based on your internet connection, user profile, and IT updates, which can cause issues if SSH keys are not in the current home directory.

- If your home directory changes, you may need to generate new SSH keys and add them to your GitHub settings.

- If you work from both office and home with VPN, it’s safest to generate SSH keys in both `C:\Users\<user>\.ssh` and `F:\.ssh` and authorize both on GitHub.

#### Create SSH Keys
1. Check the current home directory using the `set` command in Git Bash:
   ```bash
   set | grep HOME
   ```
   Alternatively, use `printenv HOME` or `echo $HOME`.

2. Generate SSH keys using the `ssh-keygen` command in Git Bash:
   ```bash
   ssh-keygen -t ed25519
   ```
   This creates an SSH key pair in your `<home>/.ssh` directory. Overwrite existing keys and use the default file name.

3. To show the SSH paths, try connecting to GitHub:
   ```bash
   ssh -v git@github.com
   ```

4. Print the public key:
   ```bash
   cat /c/Users/<user>/.ssh/id_ed25519.pub
   ```
   Then, copy it to the clipboard.

5. Add the public key to your GitHub account under `Settings > SSH and GPG keys`. Name it for easy recognition, then configure SSO and authorize the key.

6. Test the connection:
   ```bash
   ssh -T git@github.com
   ```

7. Test cloning a repository:
   ```bash
   git clone git@github.com:equinor/MamasKitchen
   ```

#### SSH-Agent for SSH Keys with Passphrases
1. If your SSH keys have a passphrase, you’ll need to start the ssh-agent:
   ```bash
   eval "$(ssh-agent -s)"
   ```

2. Add the SSH key to the ssh-agent:
   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```

3. To streamline starting the ssh-agent, create an alias in your `<home>/.bashrc` file:
   ```bash
   alias gitssh='eval `ssh-agent -s` && ssh-add ~/.ssh/id_ed25519'
   ```

4. To check for running ssh-agents:
   ```bash
   ps -ef | grep ssh-agent
   ```

5. To kill running ssh-agents:
   ```bash
   kill <pid1> <pid2>
   ```

6. You can also add a cleanup alias:
   ```bash
   alias killssh='ps -ef | grep ssh-agent | grep -v grep | awk '\''{print $2}'\'' | xargs kill'
   ```

7. If using Windows PowerShell or Command Prompt, start the ssh-agent with:
   ```powershell
   start-ssh-agent
   ```

8. For a better terminal experience, consider using the Windows Terminal application.

## General Tips for Working with GitHub Repositories

### GIT Config
- Setting up `git config` is not essential, but you may want to set a name, email, default editor, and default branch. The `git config` is stored in your home directory in the `.gitconfig` file and can be edited there.

### Recommended Workflow for Setting Up a New Repository
1. Set up a new repository on GitHub:
   - Include at least a README file, so the repository is not empty.
   - Select a suitable LICENSE.
   - Setting up a `.gitignore` file can be a good idea (e.g., with Python profile) to exclude some file name patterns from syncing with GitHub in the future when you push your local updates to the GitHub repository.
2. Clone the new repository onto your local file system. See above under Linux and WIN10 for details.
3. Add files and use Git commands in the Linux terminal or Windows Git Bash.
