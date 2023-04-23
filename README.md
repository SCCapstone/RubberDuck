
# Ducks in Space

Ducks in Space is a desktop application featuring an arcade style video game with modern design features. The game will have high replay value by providing an enjoyable and quick gameplay expereince that is unique each time. 

## Wiki Pages
[Team Organization](https://github.com/SCCapstone/RubberDuck/wiki/Team-Organization) <br>
[Project Description](https://github.com/SCCapstone/RubberDuck/wiki/Project-Description)  <br>
[Persona 1 - Timmy Fields](https://github.com/SCCapstone/RubberDuck/wiki/Persona-1---Timmy-Fields) <br>
[Persona 2 - Janet Booth](https://github.com/SCCapstone/RubberDuck/wiki/Persona-2---Janet-Booth) <br>
[Persona 3 - Jay (Fish) Carter](https://github.com/SCCapstone/RubberDuck/wiki/Persona-3-Jay-%22Fish%22-Carter) <br>
[User Stories](https://github.com/SCCapstone/RubberDuck/wiki/User-Stories) <br>
[Design](https://github.com/SCCapstone/RubberDuck/wiki/Design)<br>
[Requirements](https://github.com/SCCapstone/RubberDuck/wiki/Requirements)<br>
[Architecture](https://github.com/SCCapstone/RubberDuck/wiki/Architecture)

## Ethical, Legal, and Security Considerations
[Ethical Issues](https://github.com/SCCapstone/RubberDuck/wiki/Ethical-Issues) <br>
[Legal Issues](https://github.com/SCCapstone/RubberDuck/wiki/Legal-Issues) <br>
[Security Issues](https://github.com/SCCapstone/RubberDuck/wiki/Security-Issues) <br>

## External Requirements

Using Python 3.6.5, Pygame 1.9.3, and Pyinstaller 3.3.1
Install Python 3.6.5 from https://www.python.org/downloads/release/python-365/ <br>
Install Pygame using
```
pip install pygame
```
Install Pyinstaller using
```
pip install pyinstaller
```

Other Packages used (most likely already installed with Python 3.6.5):

* os `pip install os`
* sys `pip install sys`
* random `pip install random`
* math `pip install math`
* time `pip install time`
* pygame_menu `pip install pygame_menu`
* pandas `pip install pandas`
* datetime `pip install datetime`
* json `pip install json`
* shutil `pip install shutil`
* easygui `pip install easygui`
* enum `pip install enum`
* tkinter `pip install tk`
* (TESTING ONLY) pytest `pip install pytest`
* (TESTING ONLY) pytest bdd `pip install pytest-bdd`

## Style Guide
We will be PEP8 Style Guide for Python. You can find the style guide here: https://www.python.org/dev/peps/pep-0008/
This can be done by using a command run using yapf. You can install autopep8 using pip.

```` 
pip install yapf
````

Then you can run the command for individual files:

```` 
Python -m yapf --in-place --recursive --style="{indent_width: 4}" 
````

To run autopep8 on all files in a directory, you can use the following command to run batch script:

````
format.cmd
````


** Full guide below

## Running

To run the code without deploying, from a termianl simply run:

````
python3 main.py
````

# Deployment
Using `build.cmd` you can build and clean up your directories from terminal

```
build.cmd
```

To not run full procefure Code will be built using the following command utilizing PyInstaller to make a single file executable app

Navigate to source code directory
````
cd <path to source code> 
````
````
pyinstaller --onefile --windowed --icon=icon.ico --name=DuckInSpace main.py 
````

To install PyInstaller use the following command:
````
pip install pyinstaller
````


# Testing/Running Tests

In order to run tests you must have `pytest` and `pytest-bdd` installed

To Install:
* pytest `pip install pytest`
* pytest bdd `pip install pytest-bdd`

To run all tests, simply run
```
$ pytest
``` 
To run one files tests, simply run
```
$ pytest tes\{filepath}
ex. $pytest test\test_SettingIO.py
``` 
which will output the test results

To run a single methods test, simply run
```
$ pytest tes\{filepath}::{defName}
ex. $pytest test\test_SettingIO.py::test_get_username
``` 
which will output the test results

The unit tests and behavioral are all in the test folder. They are labeled behavioral after test.

## Testing Technology

This uses PyTest, which can be installed using
```
$ pip install pytest
```

# Authors

Bradley Grose (bgrose@email.sc.edu) (@bgrose) <br>
David Keen (ddkeen@email.sc.edu) (@ddkeen) <br>
Colin Anderson (colinsa@email.sc.edu) (@cSwiggitySwooty) <br>
Owen Bond (obond@email.sc.edu) (@OTBond) <br>
Xzavian Slaughter (xzavian@email.sc.edu) (@xslau) <br>


# AutoPep8
````
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
````
