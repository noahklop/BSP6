# CPC
Code Plagiarism Checker

## Table of contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Tutorial](#tutorial)
5. [Libraries](#libraries)
    1. [TextDistance](#textdistance)
    2. [Pygments](#pygments)
    3. [PyYAML](#pyyaml)

## Introduction <a name="introduction"></a>
Application that allows teachers to check if within a programming class 
the students were plagiarizing their code from other students or from an 
online source. The application is usable for any programming language.

A configuration is given to the application, via GUI or via configuration 
file. By using the given configuration the application explodes archives 
(as exported by Moodle or by Git) containing the source code, extracts 
relevant source code files and makes them comparable by parsing the files 
and tokenizing them. Through the use of many algorithms for sequence 
comparison, the application will compare the similarity between these 
tokenized files.

The final output for the teacher is a ranking with a number of submissions 
ordered from most likely to be plagiarism to less likely to be plagiarism. 
The ranking will be shown in a window, allowing the teacher to click on the 
desired files and have a visual representation of the similarities and 
differences between them.

A default configuration for the most efficient and effective way to use the 
program is predefined, but the program allows the user to modify it depending 
to his needs.

## Requirements <a name="requirements"></a>
In order to be able to use this application is required to have installed:

- Python3
- pip

## Installation <a name="installation"></a>
After having cloned the repository into your machine you need to go to the Code
Plagiarism Checker directory, where the application is located.

```console
foo@bar:~$ cd Code\ Plagiarism\ Checker
```

Within this repository we can find a script called setup.sh. The user has to
run the script, which will manage the installation of the libraries needed.

```console
foo@bar:~$ ./setup.sh
```

In case that the script can't be run make sure that the file has the right
permissions, which will allow it to be executed.

```console
foo@bar:~$ chmod +x setup.sh
```

If you still find any problem try using the sudo command. Remember if "Python3"
and "pip" are not installed this won't work, so make sure you installed them.

## Tutorial <a name="tutorial"></a>
To run the application we can use three methods.

- Via command line
- Via configuration file
- Via graphical user interface

To use the command line approach we will run the application with some of its
attributes on the command itself.

```console
foo@bar:~$ python3 main.py path_to_the_assignment top specific_extension
```

If we decide to use the configuration file approach we just need to write our 
desired configuration in our configuration file called configuration.yaml and
then run the application.

Otherwise, if we want to use the graphical user interface to fill the configuration's
parameters we can just run the application.

In any case to run the application, whether we want to use the configuration file or the
graphical user interface, we will use the next command.

```console
foo@bar:~$ python3 main.py
```

## Libraries <a name="libraries"></a>
Our application was implemented using the next libraries, which
were key to its development.

### [TextDistance](https://github.com/life4/textdistance) <a name="textdistance"></a>
TextDistance -- python library for comparing distance between two or more sequences by many algorithms.

Features:

- 30+ algorithms
- Pure python implementation
- Simple usage
- More than two sequences comparing
- Some algorithms have more than one implementation in one class.
- Optional numpy usage for maximum speed.

### [Pygments](https://pygments.org) <a name="pygments"></a>
It is a generic syntax highlighter suitable for use in code hosting, forums, wikis or other applications 
that need to prettify source code. Highlights are:

- a wide range of over 500 languages and other text formats is supported
- special attention is paid to details that increase highlighting quality
- support for new languages and formats are added easily; most languages use a simple regex-based lexing mechanism
- a number of output formats is available, among them HTML, RTF, LaTeX and ANSI sequences
- it is usable as a command-line tool and as a library
- … and it highlights even Perl 6!

### [PyYAML](https://pyyaml.org) <a name="pyyaml"></a>
PyYAML is a full-featured YAML framework for the Python programming language.