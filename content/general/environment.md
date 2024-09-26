Title: Labs
date: 2024-01-06
tags: labs, policy, grading
authors: Hazel Victoria Campbell
status: published
summary: Lab Procedure, Lab Assignments, Lab Marking

----

# Standard Environment

Our standard marking for this course is on Ubuntu, with python3.11+ and Firefox.
You should be able to install a recent version of Django (currently 5.1).

## Ubuntu on macOS ARM

This is for M1, M2, M4, etc. "Apple Silicon" ARM computers. We recommend installing Ubuntu in UTM.

Follow these instructions: <https://docs.getutm.app/guides/ubuntu/>

Alternative instructions: <https://jun1okamura.medium.com/install-ubuntu-on-mac-m1-powered-by-utm-499aba3ba7e9>.

After Ubuntu is working, [install virtualenv](#any-ubuntu).

## Ubuntu on macOS Intel

This is for x86 "Intel Core" macs. We recommend installing Ubuntu in VirtualBox.

1. Download VirtualBox: <www.virtualbox.org/wiki/Downloads>
2. Install VirtualBox
3. Download Ubuntu image for x86: <https://ubuntu.com/download/desktop>

You can follow this guide: <https://www.instructables.com/How-to-Create-an-Ubuntu-Virtual-Machine-with-Virtu/>

After Ubuntu is working, [install virtualenv](#any-ubuntu).

## Ubuntu on Windows

We recommend installing Ubuntu in WSL2.

* <https://documentation.ubuntu.com/wsl/en/latest/guides/install-ubuntu-wsl2/>
* <https://learn.microsoft.com/en-us/windows/wsl/install>

After Ubuntu is working, [install virtualenv](#any-ubuntu).

## Any Ubuntu

This includes Ubuntu in a VM like above.

```
sudo apt install python3-virtualenv
# or if that does not work
sudo apt install python3-venv

python --version # should show something recent like 3.12
```

Then you can proceed to [creating your virtual environment](#virtual-environment).

# Running Python Directly on Windows

**This will cause differences for some instructions, because windows doesn't have a Unix shell.**

Installing Python for Windows

## Step 1: Downloading the Python Installer

Go to the official Python download page for Windows.
Find a stable Python 3 release. The latest Python release should be fine.
Click the appropriate link for your system to download the executable file: Windows installer (64-bit) or Windows installer (32-bit).

## Step 2: Running the Executable Installer

1. After the installer is downloaded, double-click the .exe file, for example python-3.10.10-amd64.exe, to run the Python installer.

**Make sure you select customize installation when it shows up**.
   
2. Select the "Install launcher for all users" checkbox, which enables all users of the computer to access the Python launcher application.
   
3. Select the Add python.exe to PATH checkbox, which enables users to launch Python from the command line.

4. If you’re just getting started with Python and you want to install it with default features as described in the dialog, then click Install Now and go to Step 

5. The Optional Features include common tools and resources for Python and you can install all of them, even if you don’t plan to use them.

Select some or all of the following options:

Documentation: recommended

pip: recommended if you want to install other Python packages, such as NumPy or pandas

tcl/tk and IDLE: recommended if you plan to use IDLE or follow tutorials that use it

Python test suite: recommended for testing and learning

py launcher and for all users: recommended to enable users to launch Python from the command line

6. Click Next.
   
7. The Advanced Options dialog displays.

Select the options that suit your requirements:

Install for all users: recommended if you’re not the only user on this computer

Associate files with Python: recommended, because this option associates all the Python file types with the launcher or editor

Create shortcuts for installed applications: recommended to enable shortcuts for Python applications

Add Python to environment variables: recommended to enable launching Python

Precompile standard library: not required, it might down the installation

Download debugging symbols and Download debug binaries: recommended only if you plan to create C or C++ extensions

Make note of the Python installation directory in case you need to reference it later.

8. Click Install to start the installation.
   
9. After the installation is complete, a Setup was successful message displays.

## Step 3: Adding Python to the environment variables

Skip this step if you selected Add Python to environment variables during installation.
If you want to access Python through the command line, but you didn’t add Python to your environment variables during installation, then you can still do it manually.
Before you start, locate the Python installation directory on your system. The following directories are examples of the default directory paths:

`C:\Program Files\Python312`: if you selected "Install for all users" during installation, then the directory will be system-wide. (Assuming you downloaded Python3.12.)

`C:\Users\Sammy\AppData\Local\Programs\Python\Python312`: if you didn’t select Install for all users during installation, then the directory will be in the Windows user path

Note that the folder name will be different if you installed a different version, but will still start with Python.

Go to Start and enter advanced system settings in the search bar.

Click View advanced system settings.

In the System Properties dialog, click the Advanced tab and then click Environment Variables.
Depending on your installation:

If you selected "Install for all users" during installation, select Path from the list of System Variables and click Edit.
If you didn’t select Install for all users during installation, select Path from the list of User Variables and click Edit.
Click New and enter the Python directory path, then click OK until all the dialogs are closed.

## Step 4: Verify Python Installation

You can verify whether the Python installation is successful either through the command line or through the Integrated Development Environment (IDLE) application, if you chose to install it.
Go to Start and enter cmd in the search bar. Click Command Prompt

Enter the following command in the command prompt:

`python --version`

You can also check the version of Python by opening the IDLE application. Go to Start and enter python in the search bar and then click the IDLE app, for example IDLE (Python 3.10 64-bit).

#### PowerShell

In PowerShell, you must allow PowerShell scripts every time you open it for security reasons.

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted
python --version # This should show the python version you installed above!
```

Then you can proceed to [creating your virtual environment](#virtual-environment).


#### Command Prompt

```bat
REM Yes this is how comments are made in a DOS .bat "batch" file...
REM This should show the python version you installed above!
python --version 
```

Then you can proceed to [creating your virtual environment](#virtual-environment).


## Running Python directly on macOS

### Direct Installation

<https://www.python.org/downloads/macos/>

### If you have brew:

1. `brew install git`
2. `brew install python@3`
3. `sudo pip3 install virtualenv`
4. In your repository directory, `virtualenv venv --python=python3`
5. Activate the virtual environment: `source venv/bin/activate`
6. Install requests: `pip3 install requests`


### Check the Python Install

For example, if you installed python3.12:

```sh
python --version
python3 --version
python3.12 --version # If you just installed 3.12 this should work
```

## Ubuntu Lab Computers

We do not recommend using the lab computers because they make the walkthroughs harder, and Wi-Fi can make them super laggy if you're not sitting at them. However, it can be a backup option if your laptop is broken or something like that!

Connect to one of the lab machines at the University if needed. They are rooms CSC105, CSC121, CSC125, CSC129, CSC153, CSC159, CSC219.

They are named like `ub01.cs.ualberta.ca`, `uc02.cs.ualberta.ca`, all the way up to `ui22.cs.ualberta.ca` and `ohaton.cs.ualberta.ca`. There is a full list of them here: <https://www.ualberta.ca/en/computing-science/resources/technical-support/computing-resources/x2go-quick-guide.html#cs-undergrad-lab-hosts>

`ssh yourccid@ohaton.cs.ualberta.ca`

For example:

`ssh hazelcam@ug15.cs.ualberta.ca`

To quit the ssh connection to the lab machine, use the exit command or press control-D on a blank prompt. If that does not work you can force close the connection by pressing enter, then ~, then .

**Want to view stuff in terminal, but it scrolled off the top of the page?**

Try using the more command to scroll page by page. For example, you can pipe the output of curl to more to scroll through the output of curl page by page:

```.sh
curl -s url | more
```

(The `-s` option to curl prevents curl from displaying download progress. You can combine it with other curl options like `-i` and `-L`.)

```sh
python --version # shows python 2, wrong
python3 --version # shows old python 3.8 or something, wrong
python3.11 --version # ah finally a modern python
```

### Remote GUI Connection

If you need to open a web browser on the Ubuntu Lab machine, but you aren't on campus: <https://www.ualberta.ca/en/computing-science/resources/technical-support/computing-resources/x2go-quick-guide.html>

# Create Virtual Environment

You need to create a virtual environment and then activate it.

The command `python -m something` causes python to run the module `something`. The argument to `venv` or `virtualenv`, the last word, `venv` is directory (folder) that `virtualenv` or `venv` will create. You can name the directory something other than `venv` but you have to remember what you called it and add it to your `.gitignore`.


```sh
python3.12 -m venv venv
#               ^   ^
#               |   |
#               |   +---- this is the directory you want to create
#               |
#               +---- this is the python module named venv

python3.12 -m virtualenv venv
#               ^         ^
#               |         |
#               |         +---- this is the directory you want to create
#               |
#               +---- this is the python module named virtualenv
```

Examples of creating and activating a virtual environment:

```sh
python3.12 -m venv venv # if we have python 3.12
source venv/bin/activate # MacOS and Ubuntu
```
or
```sh
python3.12 -m virtualenv venv # if we have python 3.12
source venv/bin/activate # MacOS and Ubuntu
```
or
```sh
python3.11 -m venv venv # we have a different python version
source venv/bin/activate # MacOS and Ubuntu
```
or
```powershell
python -m venv venv # on windows its just python
# if we don't unrestrict powershell scripts, we can't activate
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted 
. venv\Scripts\activate.ps1 # Windows PowerShell
```
or
```bat
REM Windows Command Prompt
python -m venv venv
venv\Scripts\activate.bat
```

After you do this your prompt will change to start with `(venv)` if you've successfully activated the virtual environment.

Example screens:
```txt
hazelcam@Roxanne:~$ source venv/bin/activate
(venv) hazelcam@Roxanne:~$
```
or
```txt
PS C:\Users\hazel> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted
PS C:\Users\hazel> . venv\Scripts\activate.ps1
(venv) PS C:\Users\hazel>
```
or
```txt
C:\Users\hazel>venv\Scripts\activate.bat

(venv) C:\Users\hazel>
```


Then you can check your virtual environment with `pip --version`:

```txt
(venv) hazelcam@Roxanne:~$ pip --version
pip 24.0 from /home/hazelcam/venv/lib/python3.12/site-packages/pip (python 3.12)
```

Notice that it mentions my venv directory (folder), `/home/hazelcam/venv`.

Then you can install packages into the virtual environment with `pip install`.

If you want to install a specific version you can use `"package==version"` or `"package>=version"` but make sure to include the `"quotes"` or you will accidentally create a file named `=version`!

```text
(venv) hazelcam@Roxanne:~$ pip install "django>=5.1"
Collecting django>=5.1
  Downloading Django-5.1.1-py3-none-any.whl.metadata (4.2 kB)
Collecting asgiref<4,>=3.8.1 (from django>=5.1)
  Downloading asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from django>=5.1)
  Downloading sqlparse-0.5.1-py3-none-any.whl.metadata (3.9 kB)
Downloading Django-5.1.1-py3-none-any.whl (8.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 MB 66.6 MB/s eta 0:00:00
Downloading asgiref-3.8.1-py3-none-any.whl (23 kB)
Downloading sqlparse-0.5.1-py3-none-any.whl (44 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.2/44.2 kB 5.2 MB/s eta 0:00:00
Installing collected packages: sqlparse, asgiref, django
Successfully installed asgiref-3.8.1 django-5.1.1 sqlparse-0.5.1
```

# Activate Virtual Environment

**Every time you open a new terminal you must activate:**

```sh
source venv/bin/activate # Ubuntu and macOS
```

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted
. venv\Scripts\activate.ps1 # Windows Powershell
```

```bat
REM Windows Command Prompt
. venv\Scripts\activate.bat
```
