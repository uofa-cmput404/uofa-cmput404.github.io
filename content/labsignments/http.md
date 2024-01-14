title: HTTP Lab
date: 2024-01-06
tags: curl, http
authors: Hazel Victoria Campbell
status: published

----

[TOC]

# Submission Instructions

Submit a link to your repo in the form `https://github.com/uofa-cmput404/f23-assignment-ajax-hazelcam` on eClass. **Do not** submit a link to a branch, a file, or the clone url.

Your submission needs to pass the free tests (included) and the secret tests (you don't have these).


# Tips

## Ubuntu on Windows

Install Ubuntu on Windows using WSL2. 

Installing Ubuntu on Windows

Step 1-  Search for Windows PowerShell in your Windows search bar, then select Run as administrator.

At the command prompt type:
wsl --install
And wait for the process to complete.
For WSL to be properly activated, you will now need to restart your computer.

Step 2- WSL supports a variety of Linux distributions, including the latest Ubuntu release, Ubuntu 20.04 LTS and Ubuntu 18.04 LTS. You can find them by opening the Microsoft store app and searching for Ubuntu.

Choose the distribution you prefer and then click on Get.

Ubuntu will then install on your machine.

The one line install!

There is a single command that will install both WSL and Ubuntu at the same time.

When opening PowerShell for the first time, simply modify the initial instruction to:

wsl --install -d ubuntu

This will install both WSL and Ubuntu! Don’t forget to restart your machine before continuing.

Once installed, you can either launch the application directly from the store or search for Ubuntu in your Windows search bar.

 Step-3 Configure Ubuntu
 
Congratulations, you now have an Ubuntu terminal running on your Windows machine!

If Ubuntu returns an error during this initial installation, then the most common issue is that virtualisation is disabled in your device’s BIOS menu. You will need to turn this on during your device’s boot sequence. The location of this option varies by manufacturer, so you will need to refer to their documentation to find it.
Once Ubuntu has finished its initial setup you will need to create a username and password (this does not need to match your Windows user credentials).

Finally, it’s always good practice to install the latest updates with the following commands, entering your password when prompted.

sudo apt update

Then

sudo apt upgrade

Press Y when prompted.

Step - 4 Install your first package

Installing packages on Ubuntu is as easy as using a single command. Below, you will see how to install bpython, a simple python interpreter for trying out ideas, featuring some nice usability features like expected parameters and autocompletion.
To check that you have the latest package lists, type:

sudo apt update

Then install bpython:

sudo apt install bpython

To run the application type:

bpython

And you’re ready to go!

Step- 5 Customizing your terminal with Windows Terminal Preview

Since you’re likely to be using your Ubuntu terminal a fair bit, it’s always nice to do some customisation. We recommend installing Windows Terminal Preview to get the most user-friendly setup. You can find it in the Microsoft Store. 

Windows Terminal allows you to open multiple Terminal instances as tabs, so you can have PowerShell running alongside Ubuntu. It also includes a number of customisation options. In the below screenshot, we’ve changed the tab name and color, and configured the terminal appearance to use the Tango Dark theme and the Ubuntu font!


These customisations can be applied universally using the Appearance menu in Settings or to individual profiles which each have their own Appearance menu. Try it yourself to find something you feel comfortable with!




## Ubuntu on macOS ARM:
1. Install UTM for macOS: https://mac.getutm.app/
2. Download Ubuntu image for ARM: https://ubuntu.com/download/server/arm
3. Open the UTM app and Select "Create a New Virtual Machine"
4. Select "Virtualize" followed by "Linux"
5. Browse for the Ubuntu iso file you downloaded
6. Select your desired VM memory and CPU configs
7. Give your VM a name and select "Save"
8. Run the VM
9. Follow the onscreen prompts, default options are sufficient
10. Once the configuration is complete, shutdown the VM and dismount the iso file
11. Start and log into your VM
12. Run: `sudo apt install ubuntu-desktop` and `reboot`
You should now have access to Ubuntu desktop.

For more details, you can read [this](https://jun1okamura.medium.com/install-ubuntu-on-mac-m1-powered-by-utm-499aba3ba7e9).

## For macOS with homebrew:

1. `brew install git`
2. `brew install python@3`
3. `sudo pip3 install virtualenv`
4. In your repository directory, `virtualenv venv --python=python3`
5. Activate the virtual environment: `source venv/bin/activate`
6. Install requests: `pip3 install requests`


## For Windows 10 with pip:
Installing Python for Windows

Step 1- Downloading the Python Installer

Go to the official Python download page for Windows.
Find a stable Python 3 release. This tutorial was tested with Python version 3.10.10.
Click the appropriate link for your system to download the executable file: Windows installer (64-bit) or Windows installer (32-bit).

Step 2- Running the Executable Installer

1. After the installer is downloaded, double-click the .exe file, for example python-3.10.10-amd64.exe, to run the Python installer.
   
2. Select the Install launcher for all users checkbox, which enables all users of the computer to access the Python launcher application.
   
3. Select the Add python.exe to PATH checkbox, which enables users to launch Python from the command line.


4. If you’re just getting started with Python and you want to install it with default features as described in the dialog, then click Install Now and go to Step 4 - Verify the Python Installation. To install other optional and advanced features, click Customize installation and continue.

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

Step 3- Adding Python to the environment variables.

Skip this step if you selected Add Python to environment variables during installation.
If you want to access Python through the command line but you didn’t add Python to your environment variables during installation, then you can still do it manually.
Before you start, locate the Python installation directory on your system. The following directories are examples of the default directory paths:

C:\Program Files\Python310: if you selected Install for all users during installation, then the directory will be system wide

C:\Users\Sammy\AppData\Local\Programs\Python\Python310: if you didn’t select Install for all users during installation, then the directory will be in the Windows user path

Note that the folder name will be different if you installed a different version, but will still start with Python.

Go to Start and enter advanced system settings in the search bar.

Click View advanced system settings.

In the System Properties dialog, click the Advanced tab and then click Environment Variables.
Depending on your installation:

If you selected Install for all users during installation, select Path from the list of System Variables and click Edit.
If you didn’t select Install for all users during installation, select Path from the list of User Variables and click Edit.
Click New and enter the Python directory path, then click OK until all the dialogs are closed.

Step-4 Verify Python Installation

You can verify whether the Python installation is successful either through the command line or through the Integrated Development Environment (IDLE) application, if you chose to install it.
Go to Start and enter cmd in the search bar. Click Command Prompt

Enter the following command in the command prompt:

python --version



You can also check the version of Python by opening the IDLE application. Go to Start and enter python in the search bar and then click the IDLE app, for example IDLE (Python 3.10 64-bit).

You’ve successfully installed Python on your Windows system.








In cmd (not powershell):

1. pip install requests
2. pip install virtualenv
3. In your repository directory, `virtualenv venv --python=python3`
    * if you get the error "virtualenv not found" try forcing a reinstall with pip install virtualenv --force-reinstall
4 To activate: venv\Scripts\activate

As of 2018 all Windows 10 machines come pre-installed with curl, so you should have it already.  

## Ubuntu Lab Computers

Connect to one of the lab machines at the University if needed. 

They are named like `ug01.cs.ualberta.ca`, `ug02.cs.ualberta.ca`, all the way up to `ug34.cs.ualberta.ca`:

`ssh yourccid@ugXX.cs.ualberta.ca``

For example:

`ssh hazelcam@ug15.cs.ualberta.ca`

To quit the ssh connection to the lab machine, use the exit command or press control-D on a blank prompt. If that does not work you can force close the connection by pressing enter, then ~, then .

**Want to view stuff in terminal but it scrolled off the top of the page?**

Try using the more command to scroll page by page. For example, you can pipe the output of curl to more to scroll through the output of curl page by page:

curl -s url | more

(The -s option to curl prevents curl from displaying download progress. You can combine it with other curl options like -i and -L.)

