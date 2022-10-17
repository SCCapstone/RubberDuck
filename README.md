
# Project Name

This first paragraph should be a short description of the app. You can add links
to your wiki pages that have more detailed descriptions.

Your audience for the Readme.md are other developers who are joining your team.
Specifically, the file should contain detailed instructions that any developer
can follow to install, compile, run, and test your project. These are not only
useful to new developers, but also to you when you have to re-install everything
because your old laptop crashed. Also, the teachers of this class will be
following your instructions.

## External Requirements

List all the stuff the reader will need to install in order to get you app to 
run in their laptop. For example:

In order to build this project you first have to install:

* [Node.js](https://nodejs.org/en/)
* [MongoDB](https://www.mongodb.com/)

If possible, list the actual commands you used to install these, so the reader
can just cut-n-paste the commands and get everything setup.

You only need to add instructions for the OS you are using.

## Style Guide
We will be PEP8 Style Guide for Python. You can find the style guide here: https://www.python.org/dev/peps/pep-0008/
This can be done by using a command run using autopep8. You can install autopep8 using pip.
''' pip install autopep8 '''
Then you can run the command:
''' autopep8 --in-place --aggressive --aggressive <filename> '''
** Full guide below

## Setup

Here you list all the one-time things the developer needs to do after cloning
your repo. Sometimes there is no need for this section, but some apps require
some first-time configuration from the developer, for example: setting up a
database for running your webapp locally.

## Running

Specify the commands for a developer to run the app from the cloned repo.

# Deployment

Webapps need a deployment section that explains how to get it deployed on the 
Internet. These should be detailed enough so anyone can re-deploy if needed
. Note that you **do not put passwords in git**. 

Mobile apps will also sometimes need some instructions on how to build a
"release" version, maybe how to sign it, and how to run that binary in an
emulator or in a physical phone.

# Testing

In 492 you will write automated tests. When you do you will need to add a 
section that explains how to run them.

The unit tests are in `/test/unit`.

The behavioral tests are in `/test/casper/`.

## Testing Technology

In some cases you need to install test runners, etc. Explain how.

## Running Tests

Explain how to run the automated tests.

# Authors

Your names and emails

# AutoPep8
'''
usage: autopep8 [-h] [--version] [-v] [-d] [-i] [--global-config filename]
                [--ignore-local-config] [-r] [-j n] [-p n] [-a]
                [--experimental] [--exclude globs] [--list-fixes]
                [--ignore errors] [--select errors] [--max-line-length n]
                [--line-range line line] [--hang-closing] [--exit-code]
                [files [files ...]]

Automatically formats Python code to conform to the PEP 8 style guide.

positional arguments:
  files                 files to format or '-' for standard in

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         print verbose messages; multiple -v result in more
                        verbose messages
  -d, --diff            print the diff for the fixed source
  -i, --in-place        make changes to files in place
  --global-config filename
                        path to a global pep8 config file; if this file does
                        not exist then this is ignored (default:
                        ~/.config/pep8)
  --ignore-local-config
                        don't look for and apply local config files; if not
                        passed, defaults are updated with any config files in
                        the project's root directory
  -r, --recursive       run recursively over directories; must be used with
                        --in-place or --diff
  -j n, --jobs n        number of parallel jobs; match CPU count if value is
                        less than 1
  -p n, --pep8-passes n
                        maximum number of additional pep8 passes (default:
                        infinite)
  -a, --aggressive      enable non-whitespace changes; multiple -a result in
                        more aggressive changes
  --experimental        enable experimental fixes
  --exclude globs       exclude file/directory names that match these comma-
                        separated globs
  --list-fixes          list codes for fixes; used by --ignore and --select
  --ignore errors       do not fix these errors/warnings (default:
                        E226,E24,W50,W690)
  --select errors       fix only these errors/warnings (e.g. E4,W)
  --max-line-length n   set maximum allowed line length (default: 79)
  --line-range line line, --range line line
                        only fix errors found within this inclusive range of
                        line numbers (e.g. 1 99); line numbers are indexed at
                        1
  --hang-closing        hang-closing option passed to pycodestyle
  --exit-code           change to behavior of exit code. default behavior of
                        return value, 0 is no differences, 1 is error exit.
                        return 2 when add this option. 2 is exists
                        differences.
'''
